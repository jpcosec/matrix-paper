---
id: task-paper-v2-reframe-sources-as-evidence-cards
status: draft
summary: Render sources as scannable evidence cards inside the SLDB inspector.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-reframe-sources-as-evidence-cards
current_node: checklist-task-paper-v2-reframe-sources-as-evidence-cards-execution-ready
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
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-execution-ready
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-testing-ready
- checklist-task-paper-v2-reframe-sources-as-evidence-cards-closeout-ready
---

# paper_v2: reframe sources as evidence cards

## Rationale

Sources are the evidence layer of the SLDB inspector and should be scannable without pretending to be a second reading surface.

## Goal

Render sources as usable evidence cards that foreground excerpt, relevance, origin, and anchor for the currently selected note and paragraph.

## Scope

Only the sources pane UI in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

Keep the surface read-only, make evidence easy to scan, and preserve the left-side document as the only full prose surface.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

The sources pane reads as an evidence rail inside the inspector and supports fast trace review.
