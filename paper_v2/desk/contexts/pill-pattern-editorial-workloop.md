---
# pill-xxx
id: pill-pattern-editorial-workloop
# e.g., language:python, library:pydantic
tags:
- workspace:desk
- topic:ui
- topic:editorial-workflow
- system:sldb
---

# Pattern: editorial work loop

## What

Define the minimum viable editorial loop for the paper_v2 UI.

## Why

A UI can satisfy layout, sync, and status contracts while still failing the actual editorial job.

## When

Apply to every paper_v2 task that changes UI behavior, acceptance, edit flow, rebuild flow, or evidence visibility.

## Where

- astro_app/src/pages/index.astro
- astro_app/src/pages/api/*.ts
- astro_app/scripts/*
- spec/*
- desk/tasks/task-paper-v2-*.md

## How

Every editorial UI slice must preserve this loop:

1. select a paragraph
2. read the linked note body in full or as a substantial visible excerpt
3. read the linked source excerpt/body in full or as a substantial visible excerpt
4. identify the next editorial action from the UI
5. reach the editable artifact directly
6. save or rebuild
7. verify the result in the UI

Minimum acceptance for any shipped UI path:

- the selected note exposes non-trivial reasoning text
- the selected source exposes non-trivial evidence text
- the UI reveals which artifact is the edit point
- the UI supports rebuild/refresh verification
- the user can tell what is missing without reading repo files outside the app

## How Not

Do not:

- treat pane presence as proof of usability
- treat sync correctness as proof of usefulness
- hide note/source content behind labels, counts, or status pills
- forbid all prose duplication when support content must be readable
- mark a task complete without proving the full editorial loop
