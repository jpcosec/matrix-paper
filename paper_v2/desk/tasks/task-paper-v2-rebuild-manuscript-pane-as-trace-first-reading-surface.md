---
id: task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
status: draft
summary: Make the left manuscript pane the primary trace entry surface.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
current_node: checklist-task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-execution-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - Playwright confirmed the rendered manuscript loads as the primary left
  reading surface with selectable paragraph traces.
references:
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
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
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-readiness-check.md
- desk/tasks/task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-test.md
- desk/tasks/task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-check.md
atoms: []
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

- cd astro_app && npm run build
- cd astro_app && node scripts/stress-test.mjs
- manual browser check against `../spec/acceptance/editorial-workloop.md` step 1 (`select paragraph`)
- verify a paragraph can be selected from the manuscript and the active trace remains visually obvious across panes
- verify the manuscript pane reveals support state without becoming the only place where the next editorial action is understandable

## Done When

_Name the observable condition that makes the task complete._

A user can understand paragraph support state directly inside the manuscript, select a concrete paragraph as the active repair target, and drill rightward into readable support context without losing the paragraph as the governing anchor.
