---
id: task-paper-v2-make-the-paragraph-column-an-assertion-surface
status: draft
summary: Make the paragraph inspector structural and status-first without duplicating
  the left-side prose.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-make-the-paragraph-column-an-assertion-surface
current_node: checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-execution-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - Playwright confirmed the paragraph inspector stays status-first and
  does not duplicate left-side paragraph prose.
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
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-execution-ready
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-testing-ready
- checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-closeout-ready
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface-readiness-check.md
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface-test.md
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface-check.md
atoms: []
---

# paper_v2: make the paragraph column an assertion surface

## Rationale

_Explain why this task exists or the business driver behind it._

The paragraph inspector should explain the selected node structurally, but the paragraph prose itself already lives on the left in the rendered document.

## Goal

_Describe the concrete result this task must produce._

Make the paragraph inspector status-first and structural: show support state, counts, and section context without duplicating the paragraph text.

## Scope

_State what is in scope and what is out of scope._

Only the paragraph inspector in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

## Implementation Path

_Outline the expected implementation route or affected surface._

Use graph-derived status, reasons, note/source counts, and section context. Keep the pane read-oriented and do not repeat the rendered paragraph body.

## Validation

_List the checks required before this task can close._

- cd astro_app && npm run build
- cd astro_app && node scripts/stress-test.mjs
- inspect the generated stress report JSON
- manual browser check against `spec/acceptance/editorial-workloop.md` step 4 (`identify next editorial action`) and step 5 (`reveal edit target`)
- verify the paragraph inspector exposes support state, section context, and support-gap guidance strongly enough to decide what to fix next
- verify the paragraph inspector helps reveal the relevant edit target instead of functioning only as a status summary

## Done When

_Name the observable condition that makes the task complete._

The paragraph inspector makes the selected node understandable without turning the right rail into a second manuscript view, and it helps the editor understand what is missing and which linked artifact should be touched next.
