# paper_v2 stress test

## Source specs

Derived from:

- `spec/component/paper-v2-editorial-browser.yml`
- `spec/matrix/ui-components.yml`
- `spec/sequence/select-trace.yml`
- `spec/state/paragraph-support.yml`
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

### 5. Endurance

The app must survive repeated cross-pane navigation without console errors or selection drift.

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
