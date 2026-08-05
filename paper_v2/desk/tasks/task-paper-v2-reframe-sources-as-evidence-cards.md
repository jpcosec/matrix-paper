---
id: task-paper-v2-reframe-sources-as-evidence-cards
status: draft
summary: Render sources as scannable evidence cards inside the SLDB inspector.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-reframe-sources-as-evidence-cards
current_node: checklist-task-paper-v2-reframe-sources-as-evidence-cards-execution-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - Playwright confirmed sources render as scannable evidence cards with
  excerpt, relevance, origin, and anchor metadata.
references:
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
depends_on:
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-execution-ready
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-testing-ready
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-closeout-ready
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-reframe-sources-as-evidence-cards-readiness-check.md
- desk/tasks/task-paper-v2-reframe-sources-as-evidence-cards-test.md
- desk/tasks/task-paper-v2-reframe-sources-as-evidence-cards-check.md
atoms: []
---

# paper_v2: reframe sources as evidence cards

## Rationale

_Explain why this task exists or the business driver behind it._

Sources are the evidence layer of the SLDB inspector and should be scannable without pretending to be a second reading surface.

## Goal

_Describe the concrete result this task must produce._

Render sources as usable evidence cards that foreground excerpt, relevance, origin, and anchor for the currently selected note and paragraph.

## Scope

_State what is in scope and what is out of scope._

Only the sources pane UI in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

_Outline the expected implementation route or affected surface._

Keep the surface read-only, make evidence easy to scan, and preserve the left-side document as the only full prose surface.

## Validation

_List the checks required before this task can close._

- cd astro_app && npm run build
- cd astro_app && node scripts/stress-test.mjs
- manual browser check against `../spec/acceptance/editorial-workloop.md` step 3 (`read source evidence`)
- verify the selected source exposes substantial visible excerpt/body text plus origin and anchor when available
- verify the evidence cards support deciding whether the current paragraph is actually supported, not only scanning metadata

## Done When

_Name the observable condition that makes the task complete._

The sources pane reads as an evidence rail inside the inspector and supports fast trace review with readable evidence substantial enough to judge support without leaving the app.
