---
id: task-paper-v2-reframe-notes-as-warrant-and-reasoning-test
status: draft
summary: Prove the acceptance contract for render notes as structural support cards for the selected paragraph inside.
tags:
- workspace:desk
- artifact:task
- topic:acceptance
task_type: test
resolver_role: tester
current_node: checklist-task-paper-v2-reframe-notes-as-warrant-and-reasoning-test-execution-ready
depends_on:
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
inherits_from:
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
inherit_acceptance_context: true
references:
- spec/component/paper-v2-editorial-browser.yml
- spec/matrix/ui-components.yml
- spec/index.html
- spec/acceptance/editorial-workloop.md
- spec/workflow/editorial-repair-loop.yml
pills:
- desk/contexts/pill-pattern-editorial-workloop.md
files:
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning.md
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface.md
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues.md
- astro_app/src/pages/index.astro
- astro_app/scripts/stress-test.mjs
checklists: []
subtasks: []
atoms: []
---

# paper_v2: reframe notes as warrant and reasoning — test

## Rationale

Prove that the parent task satisfies the editorial repair loop, not only local rendering or structural correctness.

## Goal

Produce test evidence that the parent task works for the editor-facing workflow contract.

## Scope

Acceptance validation only for `task-paper-v2-reframe-notes-as-warrant-and-reasoning`.

## Validation

- run `cd astro_app && node scripts/stress-test.mjs`
- inspect the generated stress report JSON and verify the note-readability metrics satisfy `spec/acceptance/editorial-workloop.md` step 2 (`read note body`)
- verify the inherited next-action, edit-target, and rebuild/refresh cues required by the broader editorial workloop are covered by the parent/inherited task surfaces named above
- record pass/fail evidence explicitly and reject pane-presence-only evidence

## Done When

There is explicit test evidence that `task-paper-v2-reframe-notes-as-warrant-and-reasoning` satisfies the note-body slice directly and preserves the inherited broader editorial acceptance context.
