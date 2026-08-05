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
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - live UI check confirmed aggregate manuscript status, paragraph rails,
  status pills, and guided empty-state copy are present.
references:
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
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues-readiness-check.md
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues-test.md
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues-check.md
atoms: []
---

# paper_v2: add editorial validation language and interruption cues

## Rationale

_Explain why this task exists or the business driver behind it._

The split document/inspector UI needs clear support-state language so gaps are visible without turning the app into a form.

## Goal

_Describe the concrete result this task must produce._

Introduce readable validation language and visual interruption cues for support gaps across the rendered document and the right-side SLDB inspector.

## Scope

_State what is in scope and what is out of scope._

Validation labels, badges, and warning treatments in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`, driven by `/api/graph.json` status fields. Includes the aggregate status strip over the manuscript title (support counts for the whole document) and per-paragraph status rails inside the rendered document.

## Implementation Path

_Outline the expected implementation route or affected surface._

Use graph-derived states like missing note, missing source, evidence pending, and incomplete support. Keep the cues concise and avoid generic CRUD completeness language.

## Validation

_List the checks required before this task can close._

- cd astro_app && npm run build
- cd astro_app && node scripts/stress-test.mjs
- inspect the generated stress report JSON
- manual browser check against `spec/acceptance/editorial-workloop.md` step 4 (`identify next editorial action`)
- verify validation cues communicate what is missing or blocked, not only that a status exists
- verify interruption cues guide the editor toward the next repair action and the relevant artifact without collapsing the manuscript reading experience

## Done When

_Name the observable condition that makes the task complete._

Validation cues visibly communicate support weakness without collapsing the manuscript reading experience or duplicating content. Done means: aggregate status strip over the title, per-paragraph status rail in the document, status pills in every inspector pane, empty states that read as guidance, and support-gap language that helps the editor decide what to do next.
