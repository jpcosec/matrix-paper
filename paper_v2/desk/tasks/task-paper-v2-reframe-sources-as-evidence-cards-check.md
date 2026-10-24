---
id: task-paper-v2-reframe-sources-as-evidence-cards-check
status: draft
summary: Review and close the acceptance evidence for render sources as scannable
  evidence cards inside the sldb inspector.
tags:
- workspace:desk
- artifact:task
- topic:closeout
task_type: closeout
resolver_role: supervisor
current_node: ritual-execution
depends_on:
- task-paper-v2-reframe-sources-as-evidence-cards-test
inherits_from:
- task-paper-v2-reframe-sources-as-evidence-cards
- task-paper-v2-reframe-sources-as-evidence-cards-test
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
subtasks: []
atoms: []
---

# paper_v2: reframe sources as evidence cards — check

## Rationale

_Explain why this task exists or the business driver behind it._

A parent task should not close only because implementation exists; a supervisor-level check must confirm that the acceptance evidence is strong enough.

## Goal

_Describe the concrete result this task must produce._

Review the parent implementation and test evidence, then decide whether the task can be considered truly closed.

## Scope

_State what is in scope and what is out of scope._

Closeout review only for `task-paper-v2-reframe-sources-as-evidence-cards`.

## Implementation Path

_Outline the expected implementation route or affected surface._

## Validation

_List the checks required before this task can close._

- inspect the implementation evidence from `task-paper-v2-reframe-sources-as-evidence-cards`
- inspect the acceptance evidence from `task-paper-v2-reframe-sources-as-evidence-cards-test`
- verify the parent task closure is justified by the editorial workloop contract
- reject closure when the evidence proves sync, layout, or status rendering but not usefulness

## Done When

_Name the observable condition that makes the task complete._

A supervisor can attest that `task-paper-v2-reframe-sources-as-evidence-cards` is either genuinely closable under the editorial workloop contract or must be reopened.

