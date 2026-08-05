---
id: task-paper-v2-derive-editorial-trace-status-in-graph-payload-check
status: draft
summary: Review and close the acceptance evidence for derive editorial support status in the graph payload for downstream trace.
tags:
- workspace:desk
- artifact:task
- topic:closeout
task_type: closeout
resolver_role: supervisor
current_node: checklist-task-paper-v2-derive-editorial-trace-status-in-graph-payload-check-execution-ready
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload-test
inherits_from:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
- task-paper-v2-derive-editorial-trace-status-in-graph-payload-test
inherit_acceptance_context: true
references:
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

# paper_v2: derive editorial trace status in graph payload — check

## Rationale

A parent task should not close only because implementation exists; a supervisor-level check must confirm that the acceptance evidence is strong enough.

## Goal

Review the parent implementation and test evidence, then decide whether the task can be considered truly closed.

## Scope

Closeout review only for `task-paper-v2-derive-editorial-trace-status-in-graph-payload`.

## Validation

- inspect the implementation evidence from `task-paper-v2-derive-editorial-trace-status-in-graph-payload`
- inspect the acceptance evidence from `task-paper-v2-derive-editorial-trace-status-in-graph-payload-test`
- verify the parent task closure is justified by the editorial workloop contract
- reject closure when the evidence proves sync, layout, or status rendering but not usefulness

## Done When

A supervisor can attest that `task-paper-v2-derive-editorial-trace-status-in-graph-payload` is either genuinely closable under the editorial workloop contract or must be reopened.
