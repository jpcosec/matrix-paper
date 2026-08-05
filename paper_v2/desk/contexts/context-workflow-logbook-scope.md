# Workflow logbook scope

Policy Scope: paper_v2 workflow logbook
Applies To: desk/logbook/*.md

## Summary

The logbook is a workflow-harness surface. It records how work was routed, validated, corrected, or reflected upon. It must not become a second surface for project-domain design, product decisions, or paper content.

## Task Types

- workflow
- reflection
- closeout

## Inheritance Model

Logbook entries may reference workflow tasks, pills, rituals, specs, commits, and runs, but they do not inherit project-domain truth. Stable workflow knowledge should be promoted to workflow-facing atoms or policy contexts and then referenced from the logbook.

## Inheritable Fields

- workflow task references
- workflow pill references
- workflow ritual references
- workflow spec references
- workflow acceptance reflections

## Non Inheritable Fields

- project-domain design content
- manuscript content
- scientific rationale
- UI/product justification as domain truth
- implementation details that belong in the task itself

## Resolution Rules

A logbook entry should answer what changed in the workflow, why it changed, what workflow artifacts were touched, and what guardrail or acceptance consequence followed. If an entry mainly explains the product or the paper, it belongs elsewhere in deskops.

## Validation Notes

Supervisors should reject logbook entries that drift into project-domain narrative. Executors and testers may write entries only when the content is about workflow execution, acceptance, routing, or closeout.