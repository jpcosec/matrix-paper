---
id: task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface-test
status: draft
summary: Prove the acceptance contract for make the left manuscript pane the primary
  trace entry surface.
tags:
- workspace:desk
- artifact:task
- topic:acceptance
task_type: test
resolver_role: tester
current_node: ritual-execution
depends_on:
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
inherits_from:
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
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

# paper_v2: rebuild manuscript pane as trace-first reading surface — test

## Rationale

_Explain why this task exists or the business driver behind it._

Prove that the parent task satisfies the editorial repair loop, not only local rendering or structural correctness.

## Goal

_Describe the concrete result this task must produce._

Produce test evidence that the parent task works for the editor-facing workflow contract.

## Scope

_State what is in scope and what is out of scope._

Acceptance validation only for `task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface`.

## Implementation Path

_Outline the expected implementation route or affected surface._

## Validation

_List the checks required before this task can close._

- run the smallest executable check relevant to the parent task
- validate the relevant step(s) in `../spec/acceptance/editorial-workloop.md`
- record whether the user can read support content, identify the next action, reach the edit target, or rebuild/verify, depending on the parent task scope
- reject pane-presence-only evidence

## Done When

_Name the observable condition that makes the task complete._

There is explicit test evidence that `task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface` satisfies its inherited editorial acceptance context.

