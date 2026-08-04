---
id: task-paper-v2-derive-editorial-trace-status-in-graph-payload
status: complete
summary: Derive editorial support status in the graph payload for downstream trace
  UI.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-derive-editorial-trace-status-in-graph-payload
current_node: complete
history:
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB inspector UI.
- 2026-08-04 - fetched /api/graph.json and confirmed manuscript, section, paragraph, and note derived support fields are present.
references:
- ../review/plans/stitch-system-analysis.md
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
- ../stitch_comment.md
- ../stitch_draft.md
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

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

/api/graph.json exposes stable derived editorial status fields that are consumed by the UI.
