---
id: task-paper-v2-make-the-paragraph-column-an-assertion-surface
status: draft
summary: Make the paragraph inspector structural and status-first without duplicating
  the left-side prose.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-make-the-paragraph-column-an-assertion-surface
current_node: checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-execution-ready
history: []
references:
- ../review/plans/stitch-system-analysis.md
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
- ../stitch_comment.md
- ../stitch_draft.md
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
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-execution-ready
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-testing-ready
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-closeout-ready
---

# paper_v2: make the paragraph column an assertion surface

## Rationale

The paragraph inspector should explain the selected node structurally, but the paragraph prose itself already lives on the left in the rendered document.

## Goal

Make the paragraph inspector status-first and structural: show support state, counts, and section context without duplicating the paragraph text.

## Scope

Only the paragraph inspector in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

Use graph-derived status, reasons, note/source counts, and section context. Keep the pane read-oriented and do not repeat the rendered paragraph body.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The paragraph inspector makes the selected node understandable without turning the right rail into a second manuscript view.
