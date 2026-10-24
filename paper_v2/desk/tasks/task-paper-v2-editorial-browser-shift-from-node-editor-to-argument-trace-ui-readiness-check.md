---
id: task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-readiness-check
status: draft
summary: Verify that a fresh-context subagent can execute document-left / sldb-right
  decision captured; no duplicated prose from deskops artifacts alone.
tags:
- workspace:desk
- artifact:task
- topic:workflow
- topic:readiness
task_type: workflow
resolver_role: supervisor
current_node: ritual-execution
depends_on: []
inherits_from:
- task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
inherit_acceptance_context: true
references:
- ../spec/acceptance/editorial-workloop.md
- ../spec/workflow/editorial-repair-loop.yml
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
- desk/contexts/pill-pattern-editorial-workloop.md
files:
- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui.md
subtasks: []
atoms: []
---

# paper_v2 editorial browser: shift from node editor to argument trace UI — readiness check

## Rationale

_Explain why this task exists or the business driver behind it._

Before any fresh-context subagent executes the parent task, the workflow artifacts must be sufficient on their own.

## Goal

_Describe the concrete result this task must produce._

Prove that a new subagent can reconstruct the parent task from deskops evidence without human briefing.

## Scope

_State what is in scope and what is out of scope._

Readiness audit only for `task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui`.

## Implementation Path

_Outline the expected implementation route or affected surface._

## Validation

_List the checks required before this task can close._

- inspect the parent task, inherited pills, board notes, and referenced acceptance/spec artifacts
- verify a fresh-context subagent could identify goal, scope, governing pills, inherited acceptance, expected evidence, and completion criteria from repo artifacts alone
- record any ambiguity that would force a chat-based clarification
- fail when the task still depends on implicit human context

## Done When

_Name the observable condition that makes the task complete._

There is an explicit readiness verdict for `task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui`: either `ready-for-fresh-execution` or `needs-context-hardening`.

