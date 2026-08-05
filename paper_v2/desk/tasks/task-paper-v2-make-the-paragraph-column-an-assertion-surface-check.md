---
id: task-paper-v2-make-the-paragraph-column-an-assertion-surface-check
status: draft
summary: Review and close the acceptance evidence for make the paragraph inspector structural and status-first without duplicating.
tags:
- workspace:desk
- artifact:task
- topic:closeout
task_type: closeout
resolver_role: supervisor
current_node: checklist-task-paper-v2-make-the-paragraph-column-an-assertion-surface-check-execution-ready
depends_on:
- task-paper-v2-make-the-paragraph-column-an-assertion-surface-test
inherits_from:
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
- task-paper-v2-make-the-paragraph-column-an-assertion-surface-test
inherit_acceptance_context: true
references:
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
- ../spec/acceptance/editorial-workloop.md
- ../spec/workflow/editorial-repair-loop.yml
pills:
- desk/contexts/pill-pattern-editorial-workloop.md
files:
- astro_app/src/pages/index.astro
- astro_app/src/pages/api/graph.json.ts
checklists: []
subtasks: []
atoms: []
---

# paper_v2: make the paragraph column an assertion surface — check

## Rationale

A parent task should not close only because implementation exists; a supervisor-level check must confirm that the acceptance evidence is strong enough.

## Goal

Review the parent implementation and test evidence, then decide whether the task can be considered truly closed.

## Scope

Closeout review only for `task-paper-v2-make-the-paragraph-column-an-assertion-surface`.

## Validation

- inspect the implementation evidence from `task-paper-v2-make-the-paragraph-column-an-assertion-surface`
- inspect the acceptance evidence from `task-paper-v2-make-the-paragraph-column-an-assertion-surface-test`
- verify the parent task closure is justified by the editorial workloop contract
- reject closure when the evidence proves sync, layout, or status rendering but not usefulness

## Done When

A supervisor can attest that `task-paper-v2-make-the-paragraph-column-an-assertion-surface` is either genuinely closable under the editorial workloop contract or must be reopened.
