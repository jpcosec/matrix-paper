# paper_v2 stress test

## Source specs

Derived from:

- `spec/component/paper-v2-editorial-browser.yml`
- `spec/matrix/ui-components.yml`
- `spec/sequence/select-trace.yml`
- `spec/state/paragraph-support.yml`
- `spec/workflow/editorial-repair-loop.yml`
- `spec/acceptance/editorial-workloop.md`
- `spec/activity/build-and-serve.yml`
- `spec/deployment/dev-runtime.yml`

## What this stress test proves

### 1. Component contract

The app must expose these surfaces at the same time:

- document pane
- sections pane
- paragraph inspector
- notes pane
- sources pane
- `/api/graph.json`

### 2. Matrix coverage

The runtime must support the stages implied by the UI-components matrix:

- browse sections
- read/select paragraphs
- inspect paragraph detail
- inspect note support
- inspect source evidence
- consume graph payload derived by the API

### 3. Sequence integrity

Repeated paragraph, note, and source navigation must preserve one active trace:

- one active section
- one active paragraph
- zero-or-one active note
- zero-or-one active source

### 4. State integrity

Every observed `support_status` coming from `/api/graph.json` must map cleanly into the UI without client-side invention.

### 5. Editorial work-loop coverage

The runtime must support the minimum editorial loop, not just navigation:

- read non-trivial note reasoning text for the active paragraph
- read non-trivial source excerpt/body text for the active note
- identify what is missing from the current support state
- discover the next artifact to edit
- rebuild and verify the changed state

### 6. Endurance

The app must survive repeated cross-pane navigation without console errors or selection drift.

## Executable coverage status

The stress runner now proves more than structural stability.

It proves:

- pane presence
- active-trace invariants
- status mapping
- repeated navigation stability
- visible next-action guidance for exercised traces
- visible edit-target evidence for the active paragraph/note/source chain
- rebuild plus refresh verification after a controlled content mutation that is restored before exit

It still does not prove full closure-quality acceptance for everything a human editor might do end-to-end:

- arbitrary save/edit execution outside the controlled scripted mutation
- every possible repair path across all artifact types

Stress success is now stronger workflow evidence, but reviewer acceptance should still inspect whether any task claims broader behavior than the script actually exercises.

## Executable test

Run:

```bash
cd paper_v2/astro_app
node scripts/stress-test.mjs
```

The script will:

- start `astro dev`
- fetch `/api/graph.json`
- open the UI with Playwright
- walk sections, paragraphs, notes, and sources repeatedly
- assert active-trace invariants
- write `../spec/stress-report.json`

## Required next assertions for closure-quality acceptance

- selected note exposes substantial body text, not only labels or counts
- selected source exposes substantial excerpt/body text, not only metadata
- UI exposes the next editorial action for an unsupported paragraph
- UI exposes the edit target for the active gap
- rebuild/refresh verification is exercised after a controlled content change
- reviewer confirms any remaining uncovered repair paths are routed to the correct task instead of inferred from this script alone
