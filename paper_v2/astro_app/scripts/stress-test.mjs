import { spawn } from 'node:child_process';
import { writeFile, mkdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { chromium } from 'playwright';

const root = process.cwd();
const host = '127.0.0.1';
const port = 4321;
const baseUrl = `http://${host}:${port}`;
const reportPath = path.resolve(root, '../spec/stress-report.json');

const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function waitForHttp(url, timeoutMs = 30000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    try {
      const res = await fetch(url);
      if (res.ok) return true;
    } catch {}
    await wait(500);
  }
  throw new Error(`Timed out waiting for ${url}`);
}

async function fetchJsonWithRetry(url, attempts = 6) {
  let lastError;
  for (let i = 0; i < attempts; i++) {
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
      return await res.json();
    } catch (err) {
      lastError = err;
      await wait(400);
    }
  }
  throw lastError;
}

function resolveRepoPath(relativePath) {
  return path.resolve(root, '..', relativePath);
}

async function mutateValidationReport(relativePath, marker) {
  const filePath = resolveRepoPath('build/validation_report.json');
  const original = await readFile(filePath, 'utf8');
  const report = JSON.parse(original);
  const entry = (report.validation || []).find((item) => item.path === relativePath);
  if (!entry) {
    throw new Error(`Could not find ${relativePath} in validation_report.json`);
  }
  entry.input_data = entry.input_data || {};
  entry.input_data.title = `${entry.input_data.title || relativePath} ${marker}`;
  await writeFile(filePath, JSON.stringify(report, null, 2), 'utf8');
  return { filePath, original };
}

async function restoreFile(filePath, original) {
  await writeFile(filePath, original, 'utf8');
}

function countStatuses(graph) {
  const counts = {};
  const add = (status) => {
    counts[status] = (counts[status] || 0) + 1;
  };
  add(graph.manuscript?.derived?.support_status);
  for (const section of graph.sections || []) {
    add(section.derived?.support_status);
    for (const paragraph of section.paragraphs || []) {
      add(paragraph.derived?.support_status);
      for (const note of paragraph.notes || []) {
        add(note.derived?.support_status);
      }
    }
  }
  return counts;
}

async function main() {
  const server = spawn('npm', ['run', 'dev', '--', '--host', host, '--port', String(port)], {
    cwd: root,
    stdio: ['ignore', 'pipe', 'pipe'],
    env: { ...process.env },
    detached: true,
  });

  let serverLog = '';
  server.stdout.on('data', (buf) => { serverLog += buf.toString(); });
  server.stderr.on('data', (buf) => { serverLog += buf.toString(); });

  const cleanup = async () => {
    if (server.exitCode != null) return;
    try { process.kill(-server.pid, 'SIGTERM'); } catch {}
    await wait(1000);
    if (server.exitCode == null) {
      try { process.kill(-server.pid, 'SIGKILL'); } catch {}
      await wait(300);
    }
  };

  try {
    await waitForHttp(`${baseUrl}/api/graph.json`);
    const graph = await fetchJsonWithRetry(`${baseUrl}/api/graph.json`);
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 1200 } });

    const consoleErrors = [];
    const pageErrors = [];
    const http404s = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('pageerror', (err) => pageErrors.push(String(err)));
    page.on('response', (res) => {
      if (res.status() === 404) http404s.push(res.url());
    });

    await page.goto(`${baseUrl}/`, { waitUntil: 'networkidle' });
    await page.waitForSelector('.paper-title');

    const selectorsPresent = {
      paperTitle: await page.locator('.paper-title').count(),
      sectionsPane: await page.locator('#sections-list').count(),
      paragraphPane: await page.locator('#paragraph-pane').count(),
      notesPane: await page.locator('#notes-pane').count(),
      sourcesPane: await page.locator('#sources-pane').count(),
      paragraphTraces: await page.locator('.paragraph-trace').count(),
      sectionRows: await page.locator('.section-row').count(),
    };

    const expectedStatuses = Object.keys(countStatuses(graph)).filter(Boolean).sort();
    const seenStatusLabels = new Set();
    for (const locator of [
      page.locator('.paper-summary-strip .status-pill'),
      page.locator('.section-row .status-pill'),
      page.locator('#paragraph-pane .status-pill'),
      page.locator('#notes-pane .status-pill'),
    ]) {
      const texts = await locator.allTextContents();
      texts.forEach((t) => seenStatusLabels.add(t.trim()));
    }

    const navigationRuns = [];
    const readabilityChecks = [];
    const sectionCount = Math.min(await page.locator('.section-row').count(), 5);
    for (let s = 0; s < sectionCount; s++) {
      await page.locator('.section-row').nth(s).click();
      await page.waitForTimeout(100);
      const activeSectionTitle = (await page.locator('#selected-section-label').textContent())?.trim();
      const activeSectionBlock = page.locator('.section-block[data-active="true"]');
      const paragraphCount = await activeSectionBlock.locator('.paragraph-trace').count();
      const localRuns = Math.min(paragraphCount, 4);
      for (let p = 0; p < localRuns; p++) {
        await activeSectionBlock.locator('.paragraph-trace').nth(p).click();
        await page.waitForTimeout(40);
        const noteCount = await page.locator('.note-card').count();
        if (noteCount > 1) {
          await page.locator('.note-card').nth(Math.min(1, noteCount - 1)).click();
          await page.waitForTimeout(40);
        }
        const sourceCount = await page.locator('.source-card').count();
        if (sourceCount > 1) {
          await page.locator('.source-card').nth(Math.min(1, sourceCount - 1)).click();
          await page.waitForTimeout(40);
        }
        const noteBodyText = ((await page.locator('.note-card.active .note-body').first().textContent()) || '').trim();
        const sourceExcerptText = ((await page.locator('.source-card.active .note-body').first().textContent()) || '').trim();
        const traceDiagnosisText = ((await page.locator('#paragraph-pane .card-reasons').textContent()) || '').trim();
        const sourceMetaText = ((await page.locator('.source-card.active .row-meta').first().textContent()) || '').trim();

        const nextActionText = ((await page.locator('#paragraph-pane .next-action-box').textContent()) || '').trim();
        const editTargetText = ((await page.locator('#paragraph-pane .edit-target-box').textContent()) || '').trim();
        const noteEditTargetText = ((await page.locator('.note-card.active .edit-target-box').first().textContent()) || '').trim();
        const sourceEditTargetText = ((await page.locator('.source-card.active .edit-target-box').first().textContent()) || '').trim();
        const verifyText = ((await page.locator('#paragraph-pane .verify-workloop').textContent()) || '').trim();

        readabilityChecks.push({
          sectionIndex: s,
          paragraphIndex: p,
          note_body_length: noteBodyText.length,
          source_excerpt_length: sourceExcerptText.length,
          has_trace_guidance: traceDiagnosisText.length > 0,
          has_source_meta: sourceMetaText.length > 0,
          has_next_action_text: nextActionText.length > 0,
          has_edit_target_text: [editTargetText, noteEditTargetText, sourceEditTargetText].some((value) => value.length > 0),
          has_verify_text: verifyText.length > 0,
          next_action_text: nextActionText,
          edit_target_text: editTargetText,
          note_edit_target_text: noteEditTargetText,
          source_edit_target_text: sourceEditTargetText,
          verify_text: verifyText,
        });

        navigationRuns.push({
          sectionIndex: s,
          activeSectionTitle,
          paragraphIndex: p,
          activeSection: await page.locator('.section-row[data-active="true"]').count(),
          activeParagraph: await page.locator('.paragraph-trace[data-active="true"]').count(),
          activeNote: await page.locator('.note-card.active').count(),
          activeSource: await page.locator('.source-card.active').count(),
          paragraphPaneTitle: (await page.locator('#selected-paragraph-label').textContent())?.trim(),
          notePaneTitle: (await page.locator('#selected-note-label').textContent())?.trim(),
          sourcePaneTitle: (await page.locator('#selected-source-label').textContent())?.trim(),
        });
      }
    }

    const activeInvariantFailures = navigationRuns.filter((run) => (
      run.activeSection !== 1 || run.activeParagraph !== 1 || run.activeNote > 1 || run.activeSource > 1
    ));
    const weakNoteReadability = readabilityChecks.filter((run) => run.note_body_length <= 120);
    const weakSourceReadability = readabilityChecks.filter((run) => run.source_excerpt_length <= 120);
    const missingTraceGuidance = readabilityChecks.filter((run) => !run.has_trace_guidance);
    const missingNextActionEvidence = readabilityChecks.filter((run) => !run.has_next_action_text);
    const missingEditTargetEvidence = readabilityChecks.filter((run) => !run.has_edit_target_text);
    const missingVerifyGuidance = readabilityChecks.filter((run) => !run.has_verify_text);

    const rebuildVerification = {
      target_path: graph.sections?.[0]?.paragraphs?.[0]?.notes?.[0]?.path || '',
      marker: `stress-marker-${Date.now()}`,
      rebuild_button_present: await page.locator('#rebuild').count(),
      refresh_button_present: await page.locator('#refresh-graph').count(),
      pre_mutation_note_label: (await page.locator('#selected-note-label').textContent())?.trim() || '',
      after_refresh_mutation_note_label: '',
      after_rebuild_note_label: '',
      after_final_refresh_note_label: '',
      changed_state_visible_after_refresh: false,
      rebuild_cleared_changed_state: false,
      final_refresh_preserved_rebuild_state: false,
      cleanup_restored: false,
      cleanup_error: '',
    };

    let mutationSnapshot = null;
    if (rebuildVerification.target_path) {
      try {
        await page.locator('.section-row').first().click();
        await page.waitForTimeout(100);
        await page.locator('.section-block[data-active="true"] .paragraph-trace').first().click();
        await page.waitForTimeout(60);
        mutationSnapshot = await mutateValidationReport(rebuildVerification.target_path, rebuildVerification.marker);

        await page.locator('#refresh-graph').click();
        await page.waitForFunction((marker) => {
          const label = document.querySelector('#selected-note-label')?.textContent || '';
          return label.includes(marker);
        }, rebuildVerification.marker);
        rebuildVerification.after_refresh_mutation_note_label = (await page.locator('#selected-note-label').textContent())?.trim() || '';
        rebuildVerification.changed_state_visible_after_refresh = rebuildVerification.after_refresh_mutation_note_label.includes(rebuildVerification.marker);

        await page.locator('#rebuild').click();
        await page.waitForFunction((marker) => {
          const label = document.querySelector('#selected-note-label')?.textContent || '';
          return !label.includes(marker);
        }, rebuildVerification.marker);
        rebuildVerification.after_rebuild_note_label = (await page.locator('#selected-note-label').textContent())?.trim() || '';
        rebuildVerification.rebuild_cleared_changed_state = !rebuildVerification.after_rebuild_note_label.includes(rebuildVerification.marker);

        await page.locator('#refresh-graph').click();
        await page.waitForFunction((marker) => {
          const label = document.querySelector('#selected-note-label')?.textContent || '';
          return !label.includes(marker);
        }, rebuildVerification.marker);
        rebuildVerification.after_final_refresh_note_label = (await page.locator('#selected-note-label').textContent())?.trim() || '';
        rebuildVerification.final_refresh_preserved_rebuild_state = !rebuildVerification.after_final_refresh_note_label.includes(rebuildVerification.marker);
      } finally {
        if (mutationSnapshot) {
          try {
            if (!(rebuildVerification.rebuild_cleared_changed_state && rebuildVerification.final_refresh_preserved_rebuild_state)) {
              await restoreFile(mutationSnapshot.filePath, mutationSnapshot.original);
              await page.locator('#refresh-graph').click();
              await page.waitForFunction((marker) => {
                const label = document.querySelector('#selected-note-label')?.textContent || '';
                return !label.includes(marker);
              }, rebuildVerification.marker);
            }
            rebuildVerification.cleanup_restored = true;
          } catch (cleanupError) {
            rebuildVerification.cleanup_error = String(cleanupError);
          }
        }
      }
    }

    const report = {
      generated_at: new Date().toISOString(),
      source_specs: [
        '../spec/component/paper-v2-editorial-browser.yml',
        '../spec/matrix/ui-components.yml',
        '../spec/sequence/select-trace.yml',
        '../spec/state/paragraph-support.yml',
        '../spec/workflow/editorial-repair-loop.yml',
        '../spec/acceptance/editorial-workloop.md',
        '../spec/activity/build-and-serve.yml',
        '../spec/deployment/dev-runtime.yml',
      ],
      graph_summary: {
        manuscript_status: graph.manuscript?.derived?.support_status,
        section_count: graph.sections?.length || 0,
        paragraph_count: (graph.sections || []).reduce((n, s) => n + (s.paragraphs?.length || 0), 0),
        observed_status_counts: countStatuses(graph),
      },
      component_contract: selectorsPresent,
      status_mapping: {
        expected_statuses: expectedStatuses,
        seen_ui_labels: Array.from(seenStatusLabels).sort(),
      },
      navigation_runs: navigationRuns,
      editorial_readability: {
        note_body_threshold: 120,
        source_excerpt_threshold: 120,
        checks: readabilityChecks,
        weak_note_readability: weakNoteReadability,
        weak_source_readability: weakSourceReadability,
        missing_trace_guidance: missingTraceGuidance,
        missing_next_action_evidence: missingNextActionEvidence,
        missing_edit_target_evidence: missingEditTargetEvidence,
        missing_verify_guidance: missingVerifyGuidance,
      },
      rebuild_refresh_verification: rebuildVerification,
      failures: {
        active_invariant_failures: activeInvariantFailures,
        weak_note_readability: weakNoteReadability,
        weak_source_readability: weakSourceReadability,
        missing_trace_guidance: missingTraceGuidance,
        missing_next_action_evidence: missingNextActionEvidence,
        missing_edit_target_evidence: missingEditTargetEvidence,
        missing_verify_guidance: missingVerifyGuidance,
        rebuild_refresh_verification: rebuildVerification.changed_state_visible_after_refresh && rebuildVerification.rebuild_cleared_changed_state && rebuildVerification.final_refresh_preserved_rebuild_state ? [] : [rebuildVerification],
        console_errors: consoleErrors,
        page_errors: pageErrors,
        http_404s: Array.from(new Set(http404s)).sort(),
      },
      pass: (
        selectorsPresent.paperTitle === 1 &&
        selectorsPresent.sectionsPane === 1 &&
        selectorsPresent.paragraphPane === 1 &&
        selectorsPresent.notesPane === 1 &&
        selectorsPresent.sourcesPane === 1 &&
        selectorsPresent.paragraphTraces > 0 &&
        selectorsPresent.sectionRows > 0 &&
        activeInvariantFailures.length === 0 &&
        weakNoteReadability.length === 0 &&
        weakSourceReadability.length === 0 &&
        missingTraceGuidance.length === 0 &&
        missingNextActionEvidence.length === 0 &&
        missingEditTargetEvidence.length === 0 &&
        missingVerifyGuidance.length === 0 &&
        rebuildVerification.changed_state_visible_after_refresh &&
        rebuildVerification.rebuild_cleared_changed_state &&
        rebuildVerification.final_refresh_preserved_rebuild_state &&
        rebuildVerification.cleanup_restored &&
        pageErrors.length === 0 &&
        Array.from(new Set(http404s)).filter((url) => !url.endsWith('/favicon.ico')).length === 0
      ),
    };

    await mkdir(path.dirname(reportPath), { recursive: true });
    await writeFile(reportPath, JSON.stringify(report, null, 2));
    await browser.close();

    if (!report.pass) {
      console.error(JSON.stringify(report, null, 2));
      throw new Error(`Stress test failed. See ${reportPath}`);
    }

    console.log(`Stress test passed. Report: ${reportPath}`);
  } finally {
    await cleanup();
  }
}

main()
  .then(() => process.exit(0))
  .catch((err) => {
    console.error(err.stack || String(err));
    process.exit(1);
  });
