---
id: task-paper-v2-derive-editorial-trace-status-in-graph-payload
status: draft
summary: Derive editorial support status in the graph payload for downstream trace
  UI.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-derive-editorial-trace-status-in-graph-payload
current_node: checklist-task-paper-v2-derive-editorial-trace-status-in-graph-payload-execution-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - fetched /api/graph.json and confirmed manuscript, section, paragraph,
  and note derived support fields are present.
references:
- spec/acceptance/editorial-workloop.md
- spec/workflow/editorial-repair-loop.yml
- spec/index.html
depends_on:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/api/graph.json.ts
checklists:
- checklist-task-paper-v2-derive-editorial-trace-status-in-graph-payload-execution-ready
- checklist-task-paper-v2-derive-editorial-trace-status-in-graph-payload-testing-ready
- checklist-task-paper-v2-derive-editorial-trace-status-in-graph-payload-closeout-ready
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-derive-editorial-trace-status-in-graph-payload-readiness-check.md
- desk/tasks/task-paper-v2-derive-editorial-trace-status-in-graph-payload-test.md
- desk/tasks/task-paper-v2-derive-editorial-trace-status-in-graph-payload-check.md
atoms: []
---

# paper_v2: derive editorial trace status in graph payload

## Rationale

_Explain why this task exists or the business driver behind it._

The UI cannot feel like traceability without explicit editorial states derived from the current SLDB graph.

## Goal

_Describe the concrete result this task must produce._

Add derived paragraph, note, section, and manuscript status fields to /api/graph.json so the frontend can render support state without inventing data in the browser.

## Scope

_State what is in scope and what is out of scope._

Only /home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/api/graph.json.ts and its returned payload contract.

## Implementation Path

_Outline the expected implementation route or affected surface._

Derive support_status, status_reasons, counts, and section/manuscript aggregates from the existing refs. Keep the derivation heuristic and grounded in current graph data.

## Validation

_List the checks required before this task can close._

- cd astro_app && npm run build
- verify `/api/graph.json` exposes stable derived editorial status fields for manuscript, section, paragraph, note, and source-linked context
- verify the payload supports the editorial workloop acceptance surfaces from `../spec/acceptance/editorial-workloop.md`
- cd astro_app && node scripts/stress-test.mjs
- manual browser check focused on whether the derived status helps identify the next editorial action, not only whether labels render

## Done When

_Name the observable condition that makes the task complete._

`/api/graph.json` exposes stable derived editorial status fields that are consumed by the UI and are sufficient to explain support gaps, next-action cues, and rebuild-verifiable state without inventing client-side editorial meaning.
