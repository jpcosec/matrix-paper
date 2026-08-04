---
# board-xxx
id: board-001
# Affected workspace or domain
scope: desk
# List of task-xxx paths
tasks:
- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui.md
- desk/tasks/task-paper-v2-derive-editorial-trace-status-in-graph-payload.md
- desk/tasks/task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface.md
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context.md
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface.md
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning.md
- desk/tasks/task-paper-v2-reframe-sources-as-evidence-cards.md
- desk/tasks/task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation.md
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues.md
# List of pill-xxx paths
pills:
- desk/contexts/pills.md
- desk/contexts/pill-pattern-document-left-sldb-right.md
# List of ritual-xxx paths
rituals:
- desk/rituals/execution.md
- desk/rituals/testing.md
- desk/rituals/closeout.md
# e.g., system:sldb, workspace:desk
tags:
- workspace:desk
---

# review Board

## Purpose

_Explain what this board routes and why it exists._

Route the paper_v2 editorial browser work as a rendered-document + SLDB-inspector UI, not as a multi-column record form.

## Notes

- The old five-column record-browser framing is obsolete.
- `pill-pattern-document-left-sldb-right` is the governing pill for every remaining UI task.
- The rendered document is the only full prose surface.
- The right rail may show structure, counts, status, and linked support, but it must not duplicate manuscript text.
- `paper_v2/spec/` (spec2viz diagrams + UI mocks) is the visual source of truth: any task that changes layout or selection behavior must update the component spec, the UI-component matrix, or the HTML mocks.
- Synchronized active state (paragraph ↔ section ↔ note ↔ source) is the core acceptance criterion, not a detail.

## Task Details

- paper_v2 editorial browser: shift from node editor to argument trace UI [complete] - Captures the corrected product direction for the remaining work.
- paper_v2: derive editorial trace status in graph payload [complete] - Expose note, section, and manuscript support state so the inspector does not invent it client-side.
- paper_v2: rebuild manuscript pane as trace-first reading surface [complete] - Keep the rendered document as the primary selection surface.
- paper_v2: turn the sections column into editorial context [complete] - Make the sections pane a compact SLDB navigator with status and counts.
- paper_v2: make the paragraph column an assertion surface [complete] - Make the paragraph inspector structural and status-first without duplicating prose.
- paper_v2: reframe notes as warrant and reasoning [complete] - Render notes as support cards inside the inspector.
- paper_v2: reframe sources as evidence cards [complete] - Render sources as scannable evidence cards inside the inspector.
- paper_v2: enforce paragraph-to-note-to-source trace navigation [complete] - Keep document and inspector selection synchronized.
- paper_v2: add editorial validation language and interruption cues [complete] - Add readable support-state cues across both panes.
