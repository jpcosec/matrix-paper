---
id: task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
status: draft
summary: 'Plan the shift from hierarchical node editing toward manuscript-anchored argument traceability in paper_v2.'
tags:
- workspace:desk
- artifact:task
- topic:ui
- topic:editorial-browser
routine: routine-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui
current_node: checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-execution-ready
history:
- plans/paper-v2-current-state.md
- plans/paper-v2-constraints.md
- plans/paper-v2-execution-plan.md
references:
- ../stitch_comment.md
- ../stitch_draft.md
depends_on: []
pills: []
files:
- ../Neurips_peiper/paper_v2/astro_app/src/pages/index.astro
- ../Neurips_peiper/paper_v2/astro_app/src/pages/api/graph.json.ts
- plans/paper-v2-current-state.md
- plans/paper-v2-constraints.md
- plans/paper-v2-execution-plan.md
checklists:
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-execution-ready
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-testing-ready
- checklist-task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui-closeout-ready
---

# paper_v2 editorial browser: shift from node editor to argument trace UI

## Rationale

_Explain why this task exists or the business driver behind it._

Current Astro app improved layout but still feels like a node/field editor instead of an editorial traceability surface. We need a bounded execution plan before more UI implementation.

## Goal

_Describe the concrete result this task must produce._

Produce an execution plan that turns the current paper_v2 Astro UI into an argument-trace browser where manuscript, paragraph claim, note intent, and source evidence are visibly linked.

## Scope

_State what is in scope and what is out of scope._

Plan only. Cover /home/jp/proyectos/Matrix/Neurips_peiper/paper_v2/astro_app UI, graph payload derivations, interaction model, and validation approach. No implementation in this task.

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

## Risks / Unknowns

- `validation_report.json` may be too shallow for richer argumentative states without heuristics.
- The current save path is biased toward CRUD because it performs string replacement on source docs.
- Notes may mix logical intent and editorial scratchpad content, which could weaken clean trace rendering.

## Done When

_Name the observable condition that makes the task complete._

A desk task exists with a concrete argument-trace implementation plan, phased slices, validation contract, explicit risks, and subagent-backed evidence references in `plans/paper-v2-current-state.md`, `plans/paper-v2-constraints.md`, and `plans/paper-v2-execution-plan.md`.
