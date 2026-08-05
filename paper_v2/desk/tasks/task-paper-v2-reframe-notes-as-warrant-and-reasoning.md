---
id: task-paper-v2-reframe-notes-as-warrant-and-reasoning
status: draft
summary: Fix and preserve readable notes-pane support cards for the selected paragraph,
  with fresh-context acceptance evidence.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-reframe-notes-as-warrant-and-reasoning
current_node: checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-testing-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB
  inspector UI.
- 2026-08-04 - Playwright confirmed notes render as support cards exposing intent,
  claim, and reasoning for the active paragraph.
references:
- spec/component/paper-v2-editorial-browser.yml
- spec/matrix/ui-components.yml
- spec/index.html
- spec/acceptance/editorial-workloop.md
- spec/workflow/editorial-repair-loop.yml
depends_on:
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
- astro_app/scripts/stress-test.mjs
- spec/acceptance/editorial-workloop.md
- spec/workflow/editorial-repair-loop.yml
checklists:
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-execution-ready
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-testing-ready
- checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-closeout-ready
task_type: implementation
resolver_role: executor
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning-readiness-check.md
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning-test.md
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning-check.md
atoms: []
---

# paper_v2: reframe notes as warrant and reasoning

## Rationale

_Explain why this task exists or the business driver behind it._

Notes belong to the SLDB inspector as support artifacts for the selected paragraph, not as generic child rows.

## Goal

_Describe the concrete result this task must produce._

Ensure the notes pane renders readable support cards that explain intent, claim, and reasoning for the selected paragraph inside the right-side inspector, and fix any failing note-readability traces surfaced by the executable evidence.

## Scope

_State what is in scope and what is out of scope._

Own the notes-pane part of the editorial workloop in `/home/jp/proyectos/Matrix/paper_v2/astro_app/src/pages/index.astro`.

In scope:

- readable note intent
- readable note claim
- readable note reasoning body
- note-level support state presentation
- explicit evidence that the note-body step of the editorial workloop passes

Out of scope for this task:

- adding the global rebuild/refresh controls
- defining the global edit-target cues outside the notes pane
- changing unrelated inspector panes except where needed to preserve the notes-pane contract

## Implementation Path

_Outline the expected implementation route or affected surface._

Expose intent, claim, reasoning, and note-level support state. Keep the pane structural and do not repeat the left-side manuscript prose.

Implementation exists as a baseline, but the current executable evidence may still fail. A fresh executor should first run the task-local acceptance path below. If the evidence fails, the executor must treat that as reopen-and-fix work for this notes-pane slice; if it passes, the executor's job is to preserve the acceptance trail.

For the broader editorial workloop, this task relies on inherited acceptance context from `task-paper-v2-make-the-paragraph-column-an-assertion-surface` and `task-paper-v2-add-editorial-validation-language-and-interruption-cues` for next-action, edit-target, and rebuild/refresh cues.

## Validation

_List the checks required before this task can close._

Executor-scoped validation for this parent task:

- `cd astro_app && npm run build`
- `cd astro_app && node scripts/stress-test.mjs`
- inspect the generated stress report JSON and confirm the notes-pane slice records note-body readability metrics for the exercised traces
- treat any non-empty `editorial_readability.weak_note_readability` entries in the generated stress report JSON as reopen-and-fix conditions for this parent task
- record the evidence path left for the tester instead of relying on an unstructured manual browser impression

Broader inherited editorial acceptance is judged by the `-test` and `-check` subtasks, not by the executor alone.

## Done When

_Name the observable condition that makes the task complete._

The notes pane explains why the selected paragraph exists and what support logic is attached to it, and the executor has left explicit repo-artifact evidence for the tester to evaluate the inherited editorial workloop contract.
