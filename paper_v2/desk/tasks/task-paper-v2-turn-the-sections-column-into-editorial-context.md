---
id: task-paper-v2-turn-the-sections-column-into-editorial-context
status: draft
summary: Make the sections pane a compact SLDB navigator with section health and counts.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-turn-the-sections-column-into-editorial-context
current_node: checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - Playwright confirmed the sections pane renders compact section navigation
  with status pills, counts, and one active section.
references:
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-testing-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-closeout-ready
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context-readiness-check.md
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context-test.md
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context-check.md
atoms: []
---

# paper_v2: turn the sections column into editorial context

## Rationale

_Explain why this task exists or the business driver behind it._

The sections pane should orient the user structurally without turning the right rail into another editor or manuscript clone.

## Goal

_Describe the concrete result this task must produce._

Make the sections column a compact editorial context surface: one active section, clear support status, paragraph counts, and enough context to guide paragraph selection.

## Scope

_State what is in scope and what is out of scope._

Only the sections pane behavior and markup in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

_Outline the expected implementation route or affected surface._

Render compact section rows with status pills, paragraph counts, and gap counts. Preserve one active section state and keep the pane lightweight relative to the manuscript and paragraph inspector.

## Validation

_List the checks required before this task can close._

- cd astro_app && npm run build
- cd astro_app && node scripts/stress-test.mjs
- manual browser check against `../spec/acceptance/editorial-workloop.md` step 1 (`select paragraph`) and step 4 (`identify next editorial action`)
- verify the sections pane exposes section health strongly enough to help choose where to work next
- verify the pane does not stop at counts and labels when a support gap must be escalated into paragraph-level action

## Done When

_Name the observable condition that makes the task complete._

The sections pane acts as compact editorial context: a user can scan section health, identify the active section, choose where to work next, and pivot into paragraph-level trace work without reading duplicated manuscript prose.
