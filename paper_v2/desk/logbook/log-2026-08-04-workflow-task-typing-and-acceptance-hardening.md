# Workflow task typing and editorial acceptance hardening

Entry ID: workflow-log-2026-08-04-task-typing-acceptance-hardening
Date: 2026-08-04
Who: openai-api-agent
Role: supervisor
Action Kind: workflow-hardening

## Summary

Hardened the local `paper_v2` workflow so editorial UI work is routed and judged by an explicit editorial repair loop instead of by pane presence, sync, or generic UI completeness.

## 5W1H+

### What

Introduced local task typing, local inheritance policy, and editorial-workloop acceptance surfaces for `paper_v2`.

### Why

The `paper_v2` workflow was letting design, implementation, testing, and reflection collapse into the same task shape, and it was allowing UI work to close with evidence that proved structure but not editorial usability.

### When

After the workflow audit of the `paper_v2` editorial browser and before further local workflow reflections and task refactors.

### Where

`paper_v2/desk/contexts`, `paper_v2/desk/logbook`, `paper_v2/desk/tasks`, and workflow-facing acceptance/spec surfaces under `paper_v2/spec`.

### Who Detail

The change was written by the current API agent acting in a local workflow-supervision and repair role for `paper_v2`.

### How

Added local workflow policy documents, added local workflow-logbook surfaces, typed the `paper_v2` task set, wired inheritance metadata into those task docs, and tightened the local editorial acceptance artifacts.

## Workflow Artifacts Changed

### Files

- models.py
- desk/contexts/context-task-typing-and-inheritance.md
- desk/contexts/context-workflow-logbook-scope.md
- desk/contexts/pill-pattern-document-left-sldb-right.md
- desk/contexts/pill-pattern-editorial-workloop.md
- desk/logbook/README.md
- desk/logbook/log-2026-08-04-workflow-task-typing-and-acceptance-hardening.md
- desk/tasks/Board.md
- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui.md
- desk/tasks/task-paper-v2-derive-editorial-trace-status-in-graph-payload.md
- desk/tasks/task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface.md
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context.md
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface.md
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning.md
- desk/tasks/task-paper-v2-reframe-sources-as-evidence-cards.md
- desk/tasks/task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation.md
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues.md
- spec/acceptance/editorial-workloop.md
- spec/stress-test.md
- spec/workflow/editorial-repair-loop.yml

### Tasks

- desk/tasks/task-paper-v2-editorial-browser-shift-from-node-editor-to-argument-trace-ui.md
- desk/tasks/task-paper-v2-derive-editorial-trace-status-in-graph-payload.md
- desk/tasks/task-paper-v2-rebuild-manuscript-pane-as-trace-first-reading-surface.md
- desk/tasks/task-paper-v2-turn-the-sections-column-into-editorial-context.md
- desk/tasks/task-paper-v2-make-the-paragraph-column-an-assertion-surface.md
- desk/tasks/task-paper-v2-reframe-notes-as-warrant-and-reasoning.md
- desk/tasks/task-paper-v2-reframe-sources-as-evidence-cards.md
- desk/tasks/task-paper-v2-enforce-paragraph-to-note-to-source-trace-navigation.md
- desk/tasks/task-paper-v2-add-editorial-validation-language-and-interruption-cues.md

### Pills

- desk/contexts/pill-pattern-document-left-sldb-right.md
- desk/contexts/pill-pattern-editorial-workloop.md

### Rituals

- desk/rituals/execution.md
- desk/rituals/testing.md
- desk/rituals/closeout.md

### Specs

- spec/workflow/editorial-repair-loop.yml
- spec/acceptance/editorial-workloop.md
- spec/stress-test.md

## Workflow Reflection

### Observed Failure Mode

`paper_v2` tasks were too coarse and too polymorphic, so design/spec/testing/reflection concerns mixed together and weak validation still satisfied local closeout.

### Workflow Change Applied

The local workflow now distinguishes task intent explicitly and routes acceptance through an editorial repair loop that expects readable support context, visible next actions, edit-target discovery, and rebuild-and-verify behavior.

### Acceptance Gap

Structural stress evidence proved pane presence and sync but did not prove that an editor could actually read support material, identify the next repair target, perform the change, rebuild, and verify the result.

### Planning / Spec Reflection

The failure was not a simple absence of mockups. The visual direction already existed in `stitch_draft.md` and `spec/index.html`. The deeper problem was that planning and workflow specs stopped at layout, structure, and sync, while acceptance stopped at pane presence and manual inspection. In practice, the workflow let implementation optimize for graph-driven representability instead of the editor's repair loop.

### Task-Structure Reflection

The task split also amplified the drift. Notes, sources, sections, paragraph inspector, and navigation were sliced as local pane tasks, but no task owned the end-to-end editorial action: select paragraph, read note, read source, find edit target, rebuild, verify. That made it possible for every local slice to look complete while the full job remained unsupported.

### Spec Reflection

The corrective move is not "more spec" in the abstract. It is stronger spec in the right layer:

- workflow contract for the editorial repair loop
- acceptance spec with executable readability and edit-target checks
- typed tasks that separate design, implementation, testing, and reflection
- inheritance rules so local pane tasks cannot silently drop the global editorial contract

### Supervisor Reflection

The local workflow problem was not only missing tasks. It was missing workflow grammar specific to editorial work inside `paper_v2`. The new workflow surfaces help only if task docs now encode the stronger acceptance contract explicitly instead of keeping the old `npm run build` + manual check closure pattern.

## Tags

- workspace:desk
- topic:workflow
- topic:paper-v2-workflow
- topic:task-typing
- topic:acceptance-hardening

## Optional Workflow Details

Followup guardrails:

- add executable local acceptance checks for edit-target discovery and rebuild verification
- keep design, implementation, testing, and reflection separated in future `paper_v2` tasks unless a task explicitly justifies mixed purpose
- keep this logbook focused on `paper_v2` local workflow, not on deskops-central harness implementation details
