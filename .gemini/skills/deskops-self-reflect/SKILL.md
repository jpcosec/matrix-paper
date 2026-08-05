---
name: deskops-self-reflect
description: Audit workflow drift in repos that use deskops. Use when implementation, spec, and task closeout appear aligned on paper but the shipped artifact is still weak in practice.
---

# deskops self-reflect

Use this skill to inspect how a repo-local workflow produced a bad result.

Focus on artifact truth, not chat memory.

## Purpose

Detect workflow drift between:

- product model
- spec artifacts
- deskops tasks and pills
- validation and closeout evidence
- shipped behavior

## When to use

Activate when one or more of these are true:

- the UI or feature feels wrong even though tasks are marked `complete`
- spec mocks look better than the shipped artifact
- validation passed but the work is not actually useful
- the team is asking whether the failure came from methodology, planning, spec, or acceptance

## Mandatory read route

Read in this order:

1. repo `README.md`
2. `desk/tasks/Board.md`
3. relevant `desk/contexts/*.md` pills
4. `desk/rituals/execution.md`
5. `desk/rituals/testing.md`
6. `desk/rituals/closeout.md`
7. relevant `desk/tasks/task-*.md`
8. visual/spec artifacts that governed the work
9. validation artifacts (`stress-test.md`, reports, screenshots, logs)
10. shipped implementation surface
11. `git log` for the affected paths
12. `.deskops.log`

## Audit steps

### 1. Recover the declared model

Extract the intended workflow from:

- board purpose and notes
- pills
- task goals and done-when clauses
- spec mocks and diagrams

Write down the intended user job in one sentence.

### 2. Recover the shipped contract

Inspect the implementation and list what the product actually optimizes for.

Prefer statements like:

- "optimizes for graph traversal"
- "optimizes for pane presence"
- "optimizes for status rendering"
- "does not provide direct edit loop"

### 3. Compare model vs artifact

Build a mismatch table with these columns:

- intended behavior
- artifact evidence
- shipped behavior
- impact on the user task

### 4. Inspect validation quality

For every relevant task, extract:

- validation commands
- manual checks
- closeout wording
- stress/smoke coverage

Then ask:

- did validation prove usefulness or only structure?
- did validation prove the core task or only local slices?
- could the task be marked complete while still being bad?

### 5. Classify the failure

Classify each finding as one or more of:

- planning failure
- spec failure
- acceptance failure
- task slicing failure
- test contract failure
- implementation drift

### 6. State the root cause precisely

Use this template:

- "The repo declared X."
- "The tasks and tests enforced Y."
- "So the shipped artifact optimized for Y instead of X."

## Output format

Return:

- declared methodology traces
- strongest mismatch evidence
- validation blind spots
- root-cause classification
- concrete spec/test gaps

## Anti-patterns

Do not:

- invent process history that is not present in artifacts
- say "the methodology is wrong" without naming the failing artifact
- treat `complete` task status as proof of product quality
- confuse architecture correctness with user-task success
- audit from chat memory while ignoring `desk/`, spec, logs, and git history
- stop at "implementation drift" without asking why closeout allowed it

## Short audit checklist

- Board reviewed
- Governing pill reviewed
- Relevant tasks reviewed
- Spec/mock reviewed
- Validation artifact reviewed
- Shipped surface inspected
- Mismatch table written
- Root cause classified
