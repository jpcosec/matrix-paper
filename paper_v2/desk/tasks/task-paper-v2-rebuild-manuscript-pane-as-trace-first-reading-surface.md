---
id: task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
status: ready_for_testing
summary: Make the left manuscript pane the primary trace entry surface.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
current_node: checklist-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-testing-ready
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
- checklist-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-execution-ready
- checklist-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-testing-ready
- checklist-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-closeout-ready
---

# paper_v2: rebuild manuscript pane as trace-first reading surface

## Rationale

_Explain why this task exists or the business driver behind it._

The left pane must become the main argumentative entry point, not just a long rendered document.

## Goal

_Describe the concrete result this task must produce._

Turn the manuscript pane into a readable trace surface where paragraph-level support state is visible inline and selection starts from prose.

## Scope

_State what is in scope and what is out of scope._

Only the manuscript pane behavior and markup in /home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro.

## Implementation Path

_Outline the expected implementation route or affected surface._

Keep the full paper visible, preserve markdown rendering, and add paragraph-level trace cues without turning the pane into a record list.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

A user can understand paragraph support state directly inside the manuscript and drill rightward from the selected prose block.
