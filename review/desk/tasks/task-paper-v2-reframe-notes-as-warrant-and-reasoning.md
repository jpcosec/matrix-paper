---
id: task-paper-v2-reframe-notes-as-warrant-and-reasoning
status: draft
summary: 'Reframe notes as warrant and reasoning for the active paragraph.'
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-reframe-notes-as-warrant-and-reasoning
current_node: checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-execution-ready
history: []
references:
- ../../plans/stitch-system-analysis.md
- ../../plans/paper-v2-current-state.md
- ../../plans/paper-v2-constraints.md
- ../../plans/paper-v2-execution-plan.md
- ../../stitch_comment.md
- ../../stitch_draft.md
depends_on:
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
pills: []
files:
- ../Neurips_peiper/paper_v2/astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-execution-ready
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-testing-ready
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-closeout-ready
---

# paper_v2: reframe notes as warrant and reasoning

## Rationale

_Explain why this task exists or the business driver behind it._

Notes currently risk reading like generic child records. Stitch treats them as logical intent and warrant surfaces.

## Goal

_Describe the concrete result this task must produce._

Refactor the notes column so linked notes read as warrant/intention artifacts attached to the active paragraph claim.

## Scope

_State what is in scope and what is out of scope._

Only the notes column UI in /home/jp/proyectos/Matrix/Neurips_peiper/paper_v2/astro_app/src/pages/index.astro.

## Implementation Path

_Outline the expected implementation route or affected surface._

Expose intent, claim, and reasoning in reading-first cards. Make evidence gaps visible per note.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The notes column answers why the paragraph exists and how its claim is framed.
