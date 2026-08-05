---
# pill-xxx
id: pill-pattern-document-left-sldb-right
# e.g., language:python, library:pydantic
tags:
- workspace:desk
- topic:ui
- system:sldb
---

# Pattern: document-left, sldb-right

## What

_Define the context or guardrail this pill carries._

Define the base interaction model for the editorial browser.

## Why

_Explain why this context matters for safe execution._

The old multi-column record browser repeated content and hid the actual reading flow.

## When

_Describe when an agent should apply this pill._

Apply to every paper_v2 UI task that changes layout, navigation, or validation cues.

## Where

_Name the files, surfaces, or scope this pill applies to._

astro_app/src/pages/index.astro and task routing under desk/tasks/Board.md.

## How

_Describe the correct way to apply this guidance._

Keep the rendered document on the left, keep the SLDB structure on the right, drive state from graph-derived metadata, and avoid duplicating the manuscript paragraph prose as a second reading surface in the inspector.

Readable support content is still allowed and required:

- note reasoning/body must be visible in the notes pane
- source excerpt/body must be visible in the sources pane
- the split must support the editorial work loop, not just structural inspection

## How Not

_Describe the shortcut or failure mode to avoid._

Do not reintroduce equal-weight CRUD columns, duplicate the manuscript as a second pane, hide note/source content behind labels or counts, or let mock labels override the SLDB structure.
