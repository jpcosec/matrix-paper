import { spawn } from 'node:child_process';
import { writeFile, mkdir } from 'node:fs/promises';
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

    const report = {
      generated_at: new Date().toISOString(),
      source_specs: [
        '../spec/component/paper-v2-editorial-browser.yml',
        '../spec/matrix/ui-components.yml',
        '../spec/sequence/select-trace.yml',
        '../spec/state/paragraph-support.yml',
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
      failures: {
        active_invariant_failures: activeInvariantFailures,
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
