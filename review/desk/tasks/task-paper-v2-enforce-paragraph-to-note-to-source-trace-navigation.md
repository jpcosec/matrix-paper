---
id: task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation
status: draft
summary: 'Make one active argumentative chain explicit across all columns.'
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation
current_node: checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-execution-ready
history: []
references:
- ../../plans/stitch-system-analysis.md
- ../../plans/paper-v2-current-state.md
- ../../plans/paper-v2-constraints.md
- ../../plans/paper-v2-execution-plan.md
- ../../stitch_comment.md
- ../../stitch_draft.md
depends_on:
- task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface
- task-paper-v2-make-the-paragraph-column-an-assertion-surface
- task-paper-v2-reframe-notes-as-warrant-and-reasoning
- task-paper-v2-reframe-sources-as-evidence-cards
pills: []
files:
- ../Neurips_peiper/paper_v2/astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-execution-ready
- checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-testing-ready
- checklist-task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation-closeout-ready
---

# paper_v2: enforce paragraph-to-note-to-source trace navigation

## Rationale

_Explain why this task exists or the business driver behind it._

The product meaning depends on following argumentative dependency, not just browsing adjacent lists.

## Goal

_Describe the concrete result this task must produce._

Tighten selection and drilldown behavior so the active trace is always explicit across manuscript, paragraph, note, and source surfaces.

## Scope

_State what is in scope and what is out of scope._

Selection logic and cross-column highlighting in /home/jp/proyectos/Matrix/Neurips_peiper/paper_v2/astro_app/src/pages/index.astro.

## Implementation Path

_Outline the expected implementation route or affected surface._

Ensure one visible active trace, stable manuscript anchor, and consistent rightward reveal of supporting layers.

## Validation

_List the checks required before this task can close._

- npm run build
- manual browser check

## Done When

_Name the observable condition that makes the task complete._

A user can follow one active argumentative chain across all columns without losing orientation.
