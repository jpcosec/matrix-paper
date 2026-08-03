# Stitch system analysis for paper_v2

## Core claim

Stitch is not proposing a prettier CRUD browser.
It proposes an editorial trace system where the paper stays visible while the user moves across a strict argumentative chain.

## System components

### 1. Manuscript anchor
- Fixed left pane.
- Full paper always visible.
- The manuscript is the main entry surface.
- Selection starts from prose, not from a record list.

### 2. Section context column
- Gives local context for the active part of the paper.
- Should summarize section purpose, paragraph count, and open gaps.
- Should not behave like a filesystem index.

### 3. Paragraph assertion surface
- Main working surface on the right.
- The paragraph is treated as an assertion/claim anchor.
- Must foreground claim text, support state, and unresolved issues.

### 4. Note / warrant surface
- Notes are not generic child docs.
- They express intent, reasoning, or warrant for the paragraph claim.
- They should answer why this paragraph exists and how it is logically framed.

### 5. Source / evidence surface
- Sources are evidence objects.
- They should foreground excerpt, relevance, anchor, and origin.
- They should answer what evidence supports the note/claim.

### 6. Derived editorial status layer
- The UI needs status derived from the current graph.
- Minimum statuses:
  - supported
  - missing-note
  - missing-source
  - evidence-pending
  - incomplete
- This is the minimum logic needed to make the UI feel like validation.

### 7. Cross-column trace navigation
- The real unit is the chain:
  - paragraph -> note -> source
- Selection should open the next trace layer without losing the manuscript.
- The UI should privilege trace-following over node browsing.

### 8. Validation language and visual interruptions
- Warnings should be editorial, not generic completeness badges.
- The interface needs visible interruptions like:
  - missing note
  - needs source
  - evidence pending
  - incomplete support
- These states are part of the product meaning, not decoration.

## Implementation order

1. Derived editorial status layer
2. Manuscript anchor as trace surface
3. Section context column
4. Paragraph assertion surface
5. Note / warrant surface
6. Source / evidence surface
7. Cross-column trace navigation polish
8. Validation language / visual interruption pass

## Why this decomposition works

- Each task changes one coherent surface.
- Each task is testable in browser.
- Graph derivation is separated from presentation.
- Validation semantics are separated from styling.
- We avoid another big-bang rewrite.
