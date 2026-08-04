---
id: task-paper-v2-turn-the-sections-column-into-editorial-context
status: complete
summary: Make the sections pane a compact SLDB navigator with section health and counts.
tags:
- workspace:desk
- artifact:task
routine: routine-task-paper-v2-turn-the-sections-column-into-editorial-context
current_node: complete
history:
- 2026-08-04 - validated npm run build in astro_app after UI/spec workflow alignment.
- 2026-08-04 - validated python3 build_pipeline.py from paper_v2 root.
- 2026-08-04 - validated the live app with Playwright smoke checks on the split document/SLDB inspector UI.
- 2026-08-04 - Playwright confirmed the sections pane renders compact section navigation with status pills, counts, and one active section.
references:
- ../review/plans/stitch-system-analysis.md
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
- ../stitch_comment.md
- ../stitch_draft.md
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
depends_on:
- task-paper-v2-derive-editorial-trace-status-in-graph-payload
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
checklists:
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-execution-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-testing-ready
- checklist-task-paper-v2-turn-the-sections-column-into-editorial-context-closeout-ready
---

# paper_v2: turn the sections column into editorial context

## Rationale

_Explain why this task exists or the business driver behind it._



## Goal

_Describe the concrete result this task must produce._



## Scope

_State what is in scope and what is out of scope._

- npm run build
- manual browser check

## Implementation Path

_Outline the expected implementation route or affected surface._



## Validation

_List the checks required before this task can close._

- 

## Done When

_Name the observable condition that makes the task complete._
