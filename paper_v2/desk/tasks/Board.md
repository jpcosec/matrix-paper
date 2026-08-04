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



## Notes

_Add short operational notes about the current routed set._

- paper_v2 editorial browser: shift from node editor to argument trace UI [draft] - Produce an execution plan that turns the current paper_v2 Astro UI into an argument-trace browser where manuscript, paragraph claim, note intent, and source evidence are visibly linked.
- paper_v2: derive editorial trace status in graph payload [draft] - Add derived paragraph, note, section, and manuscript status fields to /api/graph.json so the frontend can render support state without inventing data in the browser.
- paper_v2: rebuild manuscript pane as trace-first reading surface [draft] - Turn the manuscript pane into a readable trace surface where paragraph-level support state is visible inline and selection starts from prose.
- paper_v2: turn the sections column into editorial context [draft] - Refactor the sections column so it communicates section purpose, paragraph counts, and trace gaps instead of acting as a simple list.
- paper_v2: make the paragraph column an assertion surface [draft] - Redesign the paragraph pane so the selected paragraph reads as an assertion dossier with support state, gaps, and trace summary.
- paper_v2: reframe notes as warrant and reasoning [draft] - Refactor the notes column so linked notes read as warrant/intention artifacts attached to the active paragraph claim.
- paper_v2: reframe sources as evidence cards [draft] - Refactor the sources column so linked sources foreground excerpt, relevance, origin, and anchor as support for the selected note and paragraph.
- paper_v2: enforce paragraph-to-note-to-source trace navigation [draft] - Tighten selection and drilldown behavior so the active trace is always explicit across manuscript, paragraph, note, and source surfaces.

## Task Details

_Generated from the task references above._

- paper_v2 editorial browser: shift from node editor to argument trace UI [draft] - Produce an execution plan that turns the current paper_v2 Astro UI into an argument-trace browser where manuscript, paragraph claim, note intent, and source evidence are visibly linked.
- paper_v2: derive editorial trace status in graph payload [draft] - Add derived paragraph, note, section, and manuscript status fields to /api/graph.json so the frontend can render support state without inventing data in the browser.
- paper_v2: rebuild manuscript pane as trace-first reading surface [draft] - Turn the manuscript pane into a readable trace surface where paragraph-level support state is visible inline and selection starts from prose.
- paper_v2: turn the sections column into editorial context [draft] - Refactor the sections column so it communicates section purpose, paragraph counts, and trace gaps instead of acting as a simple list.
- paper_v2: make the paragraph column an assertion surface [draft] - Redesign the paragraph pane so the selected paragraph reads as an assertion dossier with support state, gaps, and trace summary.
- paper_v2: reframe notes as warrant and reasoning [draft] - Refactor the notes column so linked notes read as warrant/intention artifacts attached to the active paragraph claim.
- paper_v2: reframe sources as evidence cards [draft] - Refactor the sources column so linked sources foreground excerpt, relevance, origin, and anchor as support for the selected note and paragraph.
- paper_v2: enforce paragraph-to-note-to-source trace navigation [draft] - Tighten selection and drilldown behavior so the active trace is always explicit across manuscript, paragraph, note, and source surfaces.
- paper_v2: add editorial validation language and interruption cues [draft] - Introduce a clear validation language and visual warning system for support gaps across manuscript and right-side columns.
