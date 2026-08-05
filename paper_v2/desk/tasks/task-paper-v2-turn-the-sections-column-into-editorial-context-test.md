---
id: task-paper-v2-turn-the-sections-column-into-editorial-context-test
status: draft
summary: Prove the acceptance contract for make the sections pane a compact sldb navigator with section health and counts.
tags:
- workspace:desk
- artifact:task
- topic:acceptance
task_type: test
resolver_role: tester
current_node: checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-test-execution-ready
depends_on:
- task-paper-v2-turn-the-sections-column-into-editorial-context
inherits_from:
- task-paper-v2-turn-the-sections-column-into-editorial-context
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

# paper_v2: turn the sections column into editorial context — test

## Rationale

Prove that the parent task satisfies the editorial repair loop, not only local rendering or structural correctness.

## Goal

Produce test evidence that the parent task works for the editor-facing workflow contract.

## Scope

Acceptance validation only for `task-paper-v2-turn-the-sections-column-into-editorial-context`.

## Validation

- run the smallest executable check relevant to the parent task
- validate the relevant step(s) in `../spec/acceptance/editorial-workloop.md`
- record whether the user can read support content, identify the next action, reach the edit target, or rebuild/verify, depending on the parent task scope
- reject pane-presence-only evidence

## Done When

There is explicit test evidence that `task-paper-v2-turn-the-sections-column-into-editorial-context` satisfies its inherited editorial acceptance context.
