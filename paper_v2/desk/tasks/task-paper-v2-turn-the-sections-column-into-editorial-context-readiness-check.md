---
id: task-paper-v2-turn-the-sections-column-into-editorial-context-readiness-check
status: draft
summary: Verify that a fresh-context subagent can execute make the sections pane a compact sldb navigator with section health and counts from deskops artifacts alone.
tags:
- workspace:desk
- artifact:task
- topic:workflow
- topic:readiness
task_type: workflow
resolver_role: supervisor
current_node: checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-readiness-check-execution-ready
depends_on: []
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
- desk/contexts/pill-pattern-document-left-sldb-right.md
- desk/contexts/pill-pattern-editorial-workloop.md
files:
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context.md
checklists: []
subtasks: []
atoms: []
---

# paper_v2: turn the sections column into editorial context — readiness check

## Rationale

Before any fresh-context subagent executes the parent task, the workflow artifacts must be sufficient on their own.

## Goal

Prove that a new subagent can reconstruct the parent task from deskops evidence without human briefing.

## Scope

Readiness audit only for `task-paper-v2-turn-the-sections-column-into-editorial-context`.

## Validation

- inspect the parent task, inherited pills, board notes, and referenced acceptance/spec artifacts
- verify a fresh-context subagent could identify goal, scope, governing pills, inherited acceptance, expected evidence, and completion criteria from repo artifacts alone
- record any ambiguity that would force a chat-based clarification
- fail when the task still depends on implicit human context

## Done When

There is an explicit readiness verdict for `task-paper-v2-turn-the-sections-column-into-editorial-context`: either `ready-for-fresh-execution` or `needs-context-hardening`.
