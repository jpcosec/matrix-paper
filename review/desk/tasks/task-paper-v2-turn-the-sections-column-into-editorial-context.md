---
id: task-paper-v2-turn-the-sections-column-into-editorial-context
status: draft
summary: 'Refactor the sections column from index to editorial context.'
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-turn-the-sections-column-into-editorial-context
current_node: checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
history: []
references:
- ../../plans/stitch-system-analysis.md
- ../../plans/paper-v2-current-state.md
- ../../plans/paper-v2-constraints.md
- ../../plans/paper-v2-execution-plan.md
- ../../stitch_comment.md
- ../../stitch_draft.md
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
pills: []
files:
- ../Neurips_peiper/paper_v2/astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-testing-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-closeout-ready
---

# paper_v2: turn the sections column into editorial context

## Rationale

_Explain why this task exists or the business driver behind it._

The section column currently behaves like an index; it should instead summarize context and open issues for the active section.

## Goal

_Describe the concrete result this task must produce._

Refactor the sections column so it communicates section purpose, paragraph counts, and trace gaps instead of acting as a simple list.

## Scope

_State what is in scope and what is out of scope._

Only the section column UI in /home/jp/proyectos/Matrix/Neurips_peiper/paper_v2/astro_app/src/pages/index.astro.

## Implementation Path

_Outline the expected implementation route or affected surface._

Use graph-derived counts to show section health and paragraph distribution. Keep the column lightweight and contextual.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The section column reads as editorial context, not as filesystem navigation.
