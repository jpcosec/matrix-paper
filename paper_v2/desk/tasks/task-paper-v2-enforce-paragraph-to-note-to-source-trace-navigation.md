---
id: task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation
status: draft
summary: Synchronize document and inspector selection across paragraph, note, and
  source nodes.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation
current_node: checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-execution-ready
history: []
references:
- ../review/plans/stitch-system-analysis.md
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
- ../stitch_comment.md
- ../stitch_draft.md
depends_on:
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
- task-paper-v2-reframe-sources-as-evidence-cards
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-execution-ready
- checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-testing-ready
- checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-closeout-ready
---

# paper_v2: enforce paragraph-to-note-to-source trace navigation

## Rationale

The whole UI only works if document selection and inspector selection stay synchronized.

## Goal

Tighten selection and drilldown behavior so one active trace stays explicit across the rendered document and the right-side SLDB inspector.

## Scope

Selection logic and cross-pane highlighting in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

Keep paragraph selection anchored in the manuscript, propagate that state through note and source selection, and preserve orientation while moving through the inspector.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

A user can follow one active structural trace from manuscript paragraph to note to source without losing orientation between left and right panes.
