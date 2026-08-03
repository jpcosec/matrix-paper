---
id: task-paper-v2-reframe-sources-as-evidence-cards
status: draft
summary: 'Reframe sources as evidence cards for the active trace.'
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-reframe-sources-as-evidence-cards
current_node: checklist-task-paper-v2-reframe-sources-as-evidence-cards-execution-ready
history: []
references:
- ../../plans/stitch-system-analysis.md
- ../../plans/paper-v2-current-state.md
- ../../plans/paper-v2-constraints.md
- ../../plans/paper-v2-execution-plan.md
- ../../stitch_comment.md
- ../../stitch_draft.md
depends_on:
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
pills: []
files:
- ../Neurips_peiper/paper_v2/astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-execution-ready
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-testing-ready
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-closeout-ready
---

# paper_v2: reframe sources as evidence cards

## Rationale

_Explain why this task exists or the business driver behind it._

Sources are the proof layer of the system and must read as evidence, not as attached records.

## Goal

_Describe the concrete result this task must produce._

Refactor the sources column so linked sources foreground excerpt, relevance, origin, and anchor as support for the selected note and paragraph.

## Scope

_State what is in scope and what is out of scope._

Only the sources column UI in /home/jp/proyectos/Matrix/Neurips_peiper/paper_v2/astro_app/src/pages/index.astro.

## Implementation Path

_Outline the expected implementation route or affected surface._

Make evidence easy to scan and compare. Keep the surface read-only in this task.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The sources column reads as an evidence rail for the active argumentative trace.
