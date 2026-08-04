---
id: task-paper-v2-turn-the-sections-column-into-editorial-context
status: draft
summary: Make the sections pane a compact SLDB navigator with section health and counts.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-turn-the-sections-column-into-editorial-context
current_node: checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
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
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-testing-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-closeout-ready
---

# paper_v2: turn the sections column into editorial context

## Rationale

The sections pane is now part of the right-side SLDB inspector, so it must behave like a compact structural navigator rather than a decorative extra column.

## Goal

Make the sections pane readable and useful as the top-level SLDB navigator for the active document, with section status, counts, and fast reorientation.

## Scope

Only the sections pane inside `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

Use graph-derived section status and counts, keep labels short, and make the pane help the reader jump through the document without repeating manuscript prose.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The sections pane reads as structural navigation for the rendered document, not as filesystem navigation or a duplicate reading surface.
