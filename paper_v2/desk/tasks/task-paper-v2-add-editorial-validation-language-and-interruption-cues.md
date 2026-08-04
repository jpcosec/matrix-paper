---
id: task-paper-v2-add-editorial-validation-language-and-interruption-cues
status: draft
summary: Add readable support-state cues across the rendered document and the SLDB
  inspector.
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
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
- task-paper-v2-turn-the-sections-column-into-editorial-context
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
- task-paper-v2-reframe-sources-as-evidence-cards
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
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

The split document/inspector UI needs clear support-state language so gaps are visible without turning the app into a form.

## Goal

Introduce readable validation language and visual interruption cues for support gaps across the rendered document and the right-side SLDB inspector.

## Scope

Validation labels, badges, and warning treatments in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`, driven by `/api/graph.json` status fields. Includes the aggregate status strip over the manuscript title (support counts for the whole document) and per-paragraph status rails inside the rendered document.

## Implementation Path

Use graph-derived states like missing note, missing source, evidence pending, and incomplete support. Keep the cues concise and avoid generic CRUD completeness language.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

Validation cues visibly communicate support weakness without collapsing the manuscript reading experience or duplicating content. Done means: aggregate status strip over the title, per-paragraph status rail in the document, status pills in every inspector pane, and empty states that read as guidance (e.g. "Select a paragraph first") rather than as blank chrome.
