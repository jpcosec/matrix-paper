---
id: task-paper-v2-make-the-paragraph-column-an-assertion-surface
status: draft
summary: 'Turn the paragraph pane into an assertion-first editorial surface.'
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
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
pills: []
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-execution-ready
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-testing-ready
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-closeout-ready
---

# paper_v2: make the paragraph column an assertion surface

## Rationale

_Explain why this task exists or the business driver behind it._

The paragraph pane is the narrative core of the system and must foreground the claim rather than metadata fields.

## Goal

_Describe the concrete result this task must produce._

Redesign the paragraph pane so the selected paragraph reads as an assertion dossier with support state, gaps, and trace summary.

## Scope

_State what is in scope and what is out of scope._

Only the paragraph/detail pane in /home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro.

## Implementation Path

_Outline the expected implementation route or affected surface._

Prioritize assertion text, status, reasons, note/source counts, and section context. Do not reintroduce save fields in this task.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The paragraph column clearly feels like the claim anchor of the editorial system.
