---
id: task-paper-v2-reframe-notes-as-warrant-and-reasoning
status: draft
summary: Render notes as structural support cards for the selected paragraph inside
  the SLDB inspector.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-reframe-notes-as-warrant-and-reasoning
current_node: checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-execution-ready
history: []
references:
- ../review/plans/stitch-system-analysis.md
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
- ../stitch_comment.md
- ../stitch_draft.md
depends_on:
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-execution-ready
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-testing-ready
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-closeout-ready
---

# paper_v2: reframe notes as warrant and reasoning

## Rationale

Notes belong to the SLDB inspector as support artifacts for the selected paragraph, not as generic child rows.

## Goal

Render notes as readable support cards that explain intent, claim, and reasoning for the selected paragraph inside the right-side inspector.

## Scope

Only the notes pane UI in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

Expose intent, claim, reasoning, and note-level support state. Keep the pane structural and do not repeat the left-side manuscript prose.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The notes pane explains why the selected paragraph exists and what support logic is attached to it.
