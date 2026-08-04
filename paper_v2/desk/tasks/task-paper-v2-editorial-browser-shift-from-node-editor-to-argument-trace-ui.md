---
id: task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
status: complete
summary: Document-left / SLDB-right decision captured; no duplicated prose.
tags:
- workspace:desk
- artifact:task
- topic:ui
- topic:editorial-browser
routine: routine-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
current_node: complete
history:
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
references:
- ../stitch_comment.md
- ../stitch_draft.md
depends_on: []
pills:
- desk/contexts/pill-pattern-document-left-sldb-right.md
files:
- astro_app/src/pages/index.astro
- astro_app/src/pages/api/graph.json.ts
- ../review/plans/paper-v2-current-state.md
- ../review/plans/paper-v2-constraints.md
- ../review/plans/paper-v2-execution-plan.md
checklists:
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-execution-ready
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-testing-ready
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-closeout-ready
---

# paper_v2 editorial browser: shift from node editor to argument trace UI

## Rationale

The original task split assumed a five-column trace browser and that assumption became wrong once the product direction was clarified.

## Goal

Record the governing product decision for the remaining work: the rendered document is the primary reading surface on the left, the SLDB structure is the inspector on the right, and the UI must not duplicate prose across panes.

## Scope

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
- Confirm the task references the two subagent evidence artifacts.
- Confirm the plan defines target UX, backend derivations, slices, and risks.
- Confirm the plan does **not** assume a richer backend than the current ref-derived graph.

## Done When

The board and downstream tasks use the corrected product model instead of the old multi-column record-browser assumption.
