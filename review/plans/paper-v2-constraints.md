Inherited decisions:
- paper_v2 is supposed to be an editorial column browser for argument validation, not a generic text editor or CRUD admin. The visual paper aesthetic is already part of that contract, but it is only valid if it serves traceability rather than record management.
- The core semantic chain already defined in the project is strict traceability from paragraph/claim -> note/logical intent -> source/evidence. That relation, not the filesystem-style tree by itself, is the product's conceptual center.
- The current implementation contract is still path-driven and hierarchical: manuscript -> sections -> paragraphs -> notes -> sources, with one selected item per level and downward auto-selection. Any plan has to acknowledge that this is the current source of truth rather than pretending richer graph semantics already exist.
- Validation cues are supposed to interrupt the calm paper surface when rigor breaks down. "Missing" and "Needs Citation" are not decorative badges; they are the beginning of an argumentative status system.
- Scope for this task is an implementation-plan audit only. No code changes, no silent backend reinvention, and no widening into a general editor redesign.

Diagnosis:
- The redesign is most at risk of drifting by treating the multi-column layout and editorial styling as the product change, when the actual mismatch is behavioral: users still traverse records and edit fields instead of following an argument trace.
- The strongest hidden contradiction is that the stated product language centers traceability, but the current UI contract centers per-node selection and per-node save operations. If a new plan preserves that interaction model and merely restyles panes, it will still ship another node editor.
- The 4 constraints that must govern the implementation plan are:
  1. Trace the relation, not the record. Every primary interaction should answer "what supports, qualifies, or leaves this claim unresolved?" rather than "which child node is selected?" If a plan's main unit of navigation is still section/paragraph/note/source cards in sequence, it is drifting.
  2. Keep the manuscript as the anchor, but make prose entry points open argumentative state. The left paper surface can remain the user's anchor, yet selecting prose must reveal support gaps, linked intent, and evidence status inline or in adjacent trace views, not just CRUD forms for descendants.
  3. Do not assume backend semantics that do not exist. The present graph contract is still a hierarchical reconstruction from validation-report refs. The next plan may derive claim-status lenses from that data, but it must clearly separate derived UI semantics from any truly new backend model.
  4. Promote argumentative status over empty-field completeness. "Missing" only matters if it maps to editorial meaning such as unsupported claim, absent note, unresolved warrant, or citation debt. A plan that keeps generic field-completeness badges as the main status system is drifting back toward data hygiene instead of reasoning hygiene.
- A fifth constraint is implied by the current save architecture: do not let editing workflows define the product. Because saving is currently text replacement plus reload, the redesign plan should prioritize inspection, tracing, filtering, and issue surfacing first. Otherwise implementation gravity will pull the UI back into form-editing.

Drift / contradiction check:
- Drift: "columns" are being treated as evidence of success, but the inherited intent is "argument traceability." The current-state review explicitly shows the existing columns already behave like a hierarchy browser, so more columns or prettier cards do not satisfy the brief.
- Drift: the current model navigates by parent-child containment, while the intended model navigates by argumentative dependency. If the plan still starts with "pick a section, then a paragraph, then a note," it preserves the wrong mental model.
- Drift: validation currently means empty/null checks, while the intended product language implies epistemic/editorial states. Quietly keeping the former while speaking in the language of the latter would be a hidden contract break.
- Contradiction: the project says the paragraph column is the narrative core, but the current implementation makes downstream note/source forms the real work surface. A consistent plan has to reverse that priority so the paragraph becomes the visible claim anchor and notes/sources become trace evidence, not sibling records to edit.
- Contradiction: the commentary claims the interface lets users see complete traceability without losing focus on text, but the current-state report shows focus is still lost into drill-down panes and save buttons. The plan must close that gap explicitly.

Recommendation:
- The best next move is a narrow planning pivot: define the next implementation around an argument-trace lens layered on top of the current hierarchy, not around further refinement of the hierarchy itself.
- Concretely, the implementation plan should commit to four governing rules:
  1. Paragraphs are treated as claim anchors in the UI.
  2. Notes and sources are rendered primarily as trace evidence/status attached to those anchors, not as independent editable destination panes.
  3. Validation states are redefined in editorial terms derived from current data: missing note, missing source, evidence pending, citation debt, unresolved support.
  4. Any new navigation affordance must let users move along support/justification gaps before moving along content-type levels.
- This is a pivot in interaction semantics, not a pivot in data architecture. It revises one inherited assumption only: that the existing hierarchical selection model is an acceptable foundation for the redesign. The evidence says it is not; at most, it can remain as implementation plumbing behind a claim-first surface.
- No executor handoff is warranted from this review alone. The main agent should use these constraints to tighten the implementation plan before any coding begins.

Risks:
- The current graph contract may be too shallow to express richer argumentative states without derived heuristics, so the plan must distinguish "available now from existing refs" from "requires backend extension."
- The existing save path is structurally biased toward field editing; if the implementation plan does not explicitly demote CRUD interactions, they may dominate again during execution.
- There is still some ambiguity around whether notes always correspond cleanly to a single logical intent versus mixed editorial annotations. If that assumption is false, trace views may need extra normalization.
- Because the commentary is aspirational and the current state is operational, teams may overread the aspiration and underbudget the semantic/UI work needed to bridge the gap.

Need from main agent:
- No blocking decision required for this audit.

Suggested execution prompt:
- No handoff warranted.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Produced a scope-limited audit with 4 primary implementation constraints and drift checks, based only on paper-v2-current-state.md and stitch_comment.md, without proposing code changes."
    }
  ],
  "changedFiles": [
    "/home/jp/proyectos/Matrix/review/plans/paper-v2-constraints.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read /tmp/pi-subagents-uid-1000/chain-runs/52e7a85a/parallel-0/0-context-builder/plans/paper-v2-current-state.md",
      "result": "passed",
      "summary": "Reviewed the current interaction model, data flow, rendering model, and known node-editor drift."
    },
    {
      "command": "read /home/jp/proyectos/Matrix/stitch_comment.md",
      "result": "passed",
      "summary": "Reviewed the stated editorial-browser intent and traceability contract."
    },
    {
      "command": "git -C /home/jp/proyectos/Matrix/Matrix status --short",
      "result": "passed",
      "summary": "Verified there are existing unstaged and untracked changes in the nearby repo, but no staged files."
    },
    {
      "command": "mkdir -p /home/jp/proyectos/Matrix/review/plans && write /home/jp/proyectos/Matrix/review/plans/paper-v2-constraints.md",
      "result": "passed",
      "summary": "Created the required output directory and wrote the audit report to the authoritative path."
    }
  ],
  "validationOutput": [
    "Output file written to /home/jp/proyectos/Matrix/review/plans/paper-v2-constraints.md.",
    "No code or test changes were made, per task scope.",
    "git status in /home/jp/proyectos/Matrix/Matrix showed no staged files."
  ],
  "residualRisks": [
    "The current hierarchy-backed graph may require derived heuristics before argumentative status can be surfaced convincingly.",
    "The existing save architecture still biases future implementation toward CRUD unless the plan explicitly deprioritizes form-first editing."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added a constraints audit report that defines the non-negotiable planning rules needed to keep paper_v2 focused on argument traceability instead of hierarchical node editing.",
  "reviewFindings": [
    "high: The implementation plan must make claim/evidence relations the primary interaction unit; otherwise the redesign remains a styled node browser.",
    "high: Validation states must be reinterpreted as editorial argument status, not generic field emptiness.",
    "medium: The current path-driven hierarchy can remain as plumbing, but not as the visible navigation model."
  ],
  "manualNotes": "This run performed a read-only audit plus required report-file write; no product source files were edited."
}
```
