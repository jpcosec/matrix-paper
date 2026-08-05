---
id: task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
status: draft
summary: Document-left / SLDB-right decision captured; no duplicated prose.
tags:
- workspace:desk
- artifact:task
- topic:ui
- topic:editorial-browser
routine: routine-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
current_node: checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-execution-ready
history:
- 2026-08-04 - reopened for fresh-context readiness/test/check hardening after workflow acceptance changes.
references:
- ../spec/component/paper-v2-editorial-browser.yml
- ../spec/matrix/ui-components.yml
- ../spec/index.html
- ../spec/acceptance/editorial-workloop.md
- ../spec/workflow/editorial-repair-loop.yml
depends_on: []
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
- astro_app/src/pages/api/graph.json.ts
checklists:
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-execution-ready
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-testing-ready
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-closeout-ready
task_type: design
resolver_role: supervisor
inherits_from: []
inherit_acceptance_context: true
subtasks:
- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-readiness-check.md
- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-test.md
- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-check.md
atoms: []
---

# paper_v2 editorial browser: shift from node editor to argument trace UI

## Rationale

_Explain why this task exists or the business driver behind it._

The original task split assumed a five-column trace browser and that assumption became wrong once the product direction was clarified.

## Goal

_Describe the concrete result this task must produce._

Record the governing product decision for the remaining work: the rendered document is the primary reading surface on the left, the SLDB structure is the inspector on the right, and the UI must not duplicate prose across panes.

## Scope

_State what is in scope and what is out of scope._

Decision and workflow alignment only. This task exists to anchor the later implementation tasks to the corrected UI model.

## Implementation Path

_Outline the expected implementation route or affected surface._

### Target UX model

- Keep the manuscript as the fixed left anchor.
- Treat each paragraph as a **claim anchor**, not just a child record.
- Treat notes as **logical intent / warrant** for the selected claim.
- Treat sources as **evidence state** for the selected claim.
- Make the main user question: **what supports or leaves this paragraph unresolved?**

### Governing constraints

- Trace the relation, not the record.
- Use the current hierarchy as plumbing, not as the visible mental model.
- Promote editorial statuses over generic empty-field completeness.
- Do not let save/edit mechanics define the product surface.

### Planned slices

1. **Derived argument-status layer**
   - Extend `graph.json` with per-paragraph derived fields such as:
     - `note_count`
     - `source_count`
     - `has_note`
     - `has_source`
     - `support_status`
     - `status_reasons`
   - Keep derivations explicitly heuristic and based on the existing ref graph.

2. **Manuscript-as-trace surface**
   - Render the paper as continuous prose blocks.
   - Show paragraph-level status cues inline in the manuscript.
   - Make manuscript clicks open argumentative state, not just field panes.

3. **Paragraph-first right rail**
   - Make the paragraph column the dominant work surface.
   - Reframe the paragraph pane around:
     - assertion
     - support status
     - linked note intent
     - linked evidence summary
     - unresolved gaps

4. **Evidence-first notes and sources**
   - Demote generic field-editing chrome.
   - Render notes as support/warrant cards.
   - Render sources as evidence cards with excerpt, relevance, and origin up front.

5. **Validation and save-path hardening**
   - Preserve rebuild/refresh flow.
   - Separate argument-trace inspection work from save-path changes.
   - Only after the trace surface works, revisit the fragile string-replacement save flow.

## Validation

_List the checks required before this task can close._

- `deskops show task task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui --root .`
- Confirm the task references the governing workflow surfaces: `../spec/acceptance/editorial-workloop.md` and `../spec/workflow/editorial-repair-loop.yml`.
- Confirm the plan defines target UX, backend derivations, slices, and risks.
- Confirm the plan does **not** assume a richer backend than the current ref-derived graph.
- Confirm downstream implementation and test tasks inherit the editorial workloop acceptance context instead of defining only pane-local success.

## Done When

_Name the observable condition that makes the task complete._

The board and downstream tasks use the corrected product model instead of the old multi-column record-browser assumption, and they route closure through the full editorial repair loop rather than through pane presence, sync, or generic UI completeness alone.
