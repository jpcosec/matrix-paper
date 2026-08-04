---
id: task-paper-v2-add-editorial-validation-language-and-interruption-cues
status: draft
summary: 'Replace generic completeness UI with editorial warning language.'
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-add-editorial-validation-language-and-interruption-cues
current_node: checklist-task-paper-v2-add-editorial-validation-language-and-interruption-cues-execution-ready
history: []
references:
- ../review/plans/stitch-system-analysis.md
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
- ../stitch_comment.md
- ../stitch_draft.md
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
- task-paper-v2-turn-the-sections-column-into-editorial-context
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
- task-paper-v2-reframe-sources-as-evidence-cards
pills: []
files:
- astro_app/src/pages/index.astro
- astro_app/src/pages/api/graph.json.ts
checklists:
- checklist-task-paper-v2-add-editorial-validation-language-and-interruption-cues-execution-ready
- checklist-task-paper-v2-add-editorial-validation-language-and-interruption-cues-testing-ready
- checklist-task-paper-v2-add-editorial-validation-language-and-interruption-cues-closeout-ready
---

# paper_v2: add editorial validation language and interruption cues

## Rationale

_Explain why this task exists or the business driver behind it._

The system still feels generic unless warnings use editorial language that interrupts the calm paper surface.

## Goal

_Describe the concrete result this task must produce._

Introduce a clear validation language and visual warning system for support gaps across manuscript and right-side columns.

## Scope

_State what is in scope and what is out of scope._

Validation labels, badges, and warning treatments in /home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro, driven by /api/graph.json status fields.

## Implementation Path

_Outline the expected implementation route or affected surface._

Replace generic completeness messaging with editorial states like missing note, missing source, evidence pending, and incomplete support.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

Validation cues visibly communicate logical weakness without collapsing the manuscript reading experience.
