# paper_v2 acceptance test — editorial work loop

## Source of truth

Derived from:

- `spec/workflow/editorial-repair-loop.yml`
- `spec/component/paper-v2-editorial-browser.yml`
- `spec/matrix/ui-components.yml`
- `spec/sequence/select-trace.yml`
- `spec/state/paragraph-support.yml`

## Purpose

Define the executable acceptance contract for the editorial browser.

This is stricter than the stress test.

The stress test proves structural stability.

This acceptance spec proves editorial usefulness.

## Required flow

### 1. Select paragraph

The user must be able to select a paragraph from the manuscript and see one active trace.

Must prove:

- exactly one active paragraph
- section context visible
- paragraph context visible

### 2. Read note body

The selected note must expose substantial reasoning text in the UI.

Must prove:

- selected note title visible
- note body visible
- note body is not only labels, pills, counts, or placeholders

Minimum executable heuristic:

- visible note body text length is greater than 120 characters

### 3. Read source evidence

The selected source must expose substantial evidence text in the UI.

Must prove:

- selected source title visible
- excerpt/body visible
- origin visible
- anchor visible when available

Minimum executable heuristic:

- visible source excerpt/body text length is greater than 120 characters

### 4. Identify next editorial action

The UI must help the user understand what is missing.

Must prove at least one of:

- support-gap explanation is visible
- next action text is visible
- missing evidence guidance is visible

### 5. Reveal edit target

The UI must expose which artifact should be edited next.

Must prove at least one of:

- paragraph file target visible
- note file target visible
- source file target visible
- explicit edit action targeting the relevant artifact

### 6. Rebuild and verify

The workflow must support rebuild/refresh verification.

Must prove:

- rebuild path exists
- refresh path exists
- changed state can be re-observed in the UI after rebuild

## Failure conditions

Acceptance fails when any of these are true:

- note pane shows only metadata or tiny fragments
- source pane shows only metadata or tiny fragments
- sync works but the user cannot tell what to do next
- UI hides the edit target for the active support gap
- rebuild exists but is not tied to verification

## Evidence format

The acceptance runner should write a report containing:

- note readability metrics
- source readability metrics
- active trace integrity
- visible support-gap guidance
- visible edit-target evidence
- rebuild/refresh verification evidence

## Current status

As of now, the repository has:

- a structural stress test
- a workflow contract

But acceptance is not complete until the executable test proves this document.