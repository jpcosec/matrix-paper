# Workflow task typing and inheritance

Policy Scope: paper_v2 workflow harness
Applies To: desk/tasks/*.md, desk/tasks/Board.md, desk/contexts/*.md, desk/rituals/*.md

## Summary

Tasks in this workspace were carrying design, implementation, testing, and reflection at the same time. This policy separates task intent through explicit task types and lets any task inherit workflow context from any other task without forcing a parent/child category.

## Task Types

- design
- plan
- spec
- implementation
- test
- reflection
- closeout
- workflow

## Inheritance Model

Use `inherits_from` as a workflow-context relation, not as a tree category. Any task may inherit from any other task when it needs the same pills, atoms, tags, references, or acceptance context. This is stronger than `depends_on`: `depends_on` blocks execution order, while `inherits_from` carries workflow context.

## Inheritable Fields

- pills
- tags
- references
- workflow constraints
- acceptance context
- relevant atoms

## Non Inheritable Fields

- status
- current_node
- history
- validation evidence
- done when text
- git commits

## Resolution Rules

A task keeps its own local state and local evidence. Inherited workflow context is additive by default. Local task fields may extend inherited pills, references, and constraints, but they must not silently erase them. When both `depends_on` and `inherits_from` are present, treat them as different semantics: order comes from `depends_on`, context comes from `inherits_from`.

## Validation Notes

Supervisors should reject large mixed-purpose tasks when they can be split into typed tasks. Executors should read inherited pills and acceptance context before acting. Testers should validate the local task outcome and also confirm that the inherited workflow contract was respected.