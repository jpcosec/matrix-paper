# paper_v2 execution plan

## Goal

Shift the current Astro app from a hierarchical node editor toward a manuscript-anchored argument-trace browser.

## Evidence base

- `plans/paper-v2-current-state.md`
- `plans/paper-v2-constraints.md`
- `../stitch_comment.md`
- `../stitch_draft.md`

## Target UX model

- Left pane stays as the stable manuscript reader.
- Paragraphs are treated as claim anchors.
- Right-side columns answer:
  - what this paragraph claims
  - what note gives it intent/warrant
  - what source evidence supports it
  - what is still missing
- Notes and sources are support surfaces first, edit forms second.

## Required graph derivations

Derive these in `src/pages/api/graph.json.ts` from the current refs without inventing a new backend model:

- `note_count`
- `source_count`
- `has_note`
- `has_source`
- `support_status`
- `status_reasons`
- optional per-section aggregates:
  - `paragraph_count`
  - `supported_count`
  - `unsupported_count`

Proposed `support_status` values:

- `supported`
- `missing-note`
- `missing-source`
- `evidence-pending`
- `incomplete`

## Planned slices

### Slice 1 — Add editorial status derivations

Scope:
- extend graph payload only
- no layout rewrite yet

Output:
- paragraph and section status metadata available to the UI

Validation:
- inspect `/api/graph.json`
- confirm derived fields exist for all paragraphs

Stop point:
- payload is stable and can drive a trace UI

### Slice 2 — Rebuild manuscript pane as trace surface

Scope:
- keep paper visible at all times
- render continuous section/paragraph prose
- add inline status cues per paragraph

Output:
- manuscript shows support state directly in the paper
- click on paragraph opens trace context to the right

Validation:
- browser check: left pane remains stable while drilling down
- paragraph selection visibly syncs with right panes

Stop point:
- manuscript works as the primary navigation surface

### Slice 3 — Make paragraph pane the main argument surface

Scope:
- paragraph pane becomes claim-first
- prioritize assertion text, support summary, gaps, linked note/source counts
- demote raw field editing

Output:
- selected paragraph reads like a claim dossier, not a node form

Validation:
- browser check: selected paragraph clearly shows assertion + support state + gaps

Stop point:
- paragraph column no longer feels like generic CRUD

### Slice 4 — Reframe notes and sources as warrant/evidence

Scope:
- notes render as intent/claim/warrant cards
- sources render as evidence cards with excerpt, relevance, origin first
- preserve edit controls but move them behind the trace reading order

Output:
- right rail reads as note -> evidence trace

Validation:
- browser check: notes and sources visually read as support artifacts

Stop point:
- user can follow paragraph -> note -> source without thinking in document types

### Slice 5 — Harden save semantics separately

Scope:
- isolate save-path work from trace-UI work
- replace naive string replacement only after the new trace UI is proven

Output:
- separate implementation task for safer writes

Validation:
- edit/save/rebuild smoke test after any write-path changes

Stop point:
- no save refactor is bundled into the trace UI rewrite unless required

## Validation contract

For execution later, require:

- `npm run build` in `Neurips_peiper/paper_v2/astro_app`
- browser verification that manuscript remains fixed while tracing rightward
- browser verification that paragraph status is visible without opening forms
- browser verification that note/source panes read as support/evidence, not admin fields
- rebuild smoke test after UI changes

## Risks

- current graph semantics may be too shallow for strong argumentative states
- note content may be inconsistent across docs
- save architecture may keep pulling the UI back toward field editing

## Non-goals

- no backend redesign beyond derived graph fields
- no general-purpose editor rewrite
- no save-system rewrite in the same first implementation slice
