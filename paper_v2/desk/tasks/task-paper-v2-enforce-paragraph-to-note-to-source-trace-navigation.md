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
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - Playwright confirmed one active section, paragraph, note, and source
  remain highlighted across the synchronized trace.
references:
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
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
task_type: test
resolver_role: tester
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
- task-paper-v2-reframe-sources-as-evidence-cards
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-readiness-check.md
- desk/tasks/task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-test.md
- desk/tasks/task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-check.md
atoms: []
---

# paper_v2: enforce paragraph-to-note-to-source trace navigation

## Rationale

_Explain why this task exists or the business driver behind it._

The whole UI only works if document selection and inspector selection stay synchronized.

## Goal

_Describe the concrete result this task must produce._

Tighten selection and drilldown behavior so one active trace stays explicit across the rendered document and the right-side SLDB inspector. The primary acceptance criterion is the synchronized active state: the selected paragraph, its section, its note, and its source must all be visibly highlighted at once, in both panes.

## Scope

_State what is in scope and what is out of scope._

Selection logic and cross-pane highlighting in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

_Outline the expected implementation route or affected surface._

Keep paragraph selection anchored in the manuscript, propagate that state through note and source selection, and preserve orientation while moving through the inspector.

## Validation

_List the checks required before this task can close._

- cd astro_app && npm run build
- run the structural stress test from `../spec/stress-test.md`
- validate navigation against `../spec/acceptance/editorial-workloop.md` steps 1-3 so sync is proven together with readable support visibility
- verify navigation preserves orientation while still exposing the next editorial action and edit target for the selected gap

## Done When

_Name the observable condition that makes the task complete._

A user can follow one active structural trace from manuscript paragraph to note to source without losing orientation between left and right panes, with the active node highlighted simultaneously in the document and in every inspector pane, and with the synced trace remaining useful for reading support and deciding the next repair action.
