from __future__ import annotations

from datetime import date

from pydantic import Field

from sldb import StructuredNLDoc


class PaperSourceDoc(StructuredNLDoc):
    __template__ = """
# ⸢rev•title⸥

Kind: ⸢rev•kind⸥
Origin: ⸢rev•origin⸥
Anchor: ⸢rev•anchor⸥

## Excerpt

⸢rev•excerpt⸥

## Relevance

⸢rev•relevance⸥
""".strip()

    title: str = Field(description="Human-readable title for the source atom.")
    kind: str = Field(description="Type of source atom or upstream input.")
    origin: str = Field(description="Original file or provenance pointer for the source atom.")
    anchor: str = Field(description="Stable local anchor for this source atom inside the paper pipeline.")
    excerpt: str = Field(description="Source text excerpt carried forward into writing.")
    relevance: str = Field(description="Why this source atom matters for the paper draft.")


class WritingNoteDoc(StructuredNLDoc):
    __compositions__ = {
        "source_digest": {
            "source_field": "sources",
            "model": "models:PaperSourceDoc",
            "template": "- {title} [{kind}] :: {anchor}",
        }
    }
    __template__ = """
# ⸢rev•title⸥

Stage: writing-note

## Sources

- ⸢rev,list•sources⸥

## Intent

⸢rev•intent⸥

## Claim

⸢rev•claim⸥

## Notes

⸢rev•notes⸥

## Source Digest

⸢render•source_digest⸥
""".strip()

    title: str = Field(description="Human-readable title for the writing note.")
    sources: list[str] = Field(default_factory=list, description="Relative paths to source atom documents that ground this note.")
    intent: str = Field(description="Writing intention for the note inside the section flow.")
    claim: str = Field(description="Main claim or move that the paragraph should express.")
    notes: str = Field(description="Drafting notes that bridge source material into paragraph prose.")


class SectionParagraphDoc(StructuredNLDoc):
    __compositions__ = {
        "note_digest": {
            "source_field": "notes_refs",
            "model": "models:WritingNoteDoc",
            "template": "- {title}: {claim}",
        }
    }
    __template__ = """
# ⸢rev•title⸥

Section: ⸢rev•section_id⸥
Paragraph Index: ⸢rev•paragraph_index⸥

## Notes

- ⸢rev,list•notes_refs⸥

## Paragraph Text

⸢rev•paragraph_text⸥

## Note Digest

⸢render•note_digest⸥
""".strip()

    title: str = Field(description="Human-readable title for the section paragraph document.")
    section_id: str = Field(description="Stable identifier of the parent section.")
    paragraph_index: int = Field(description="One-based paragraph index inside the section.")
    notes_refs: list[str] = Field(default_factory=list, description="Relative paths to writing-note documents used to draft the paragraph.")
    paragraph_text: str = Field(description="Final paragraph prose for the section block.")


class PaperSectionDoc(StructuredNLDoc):
    __compositions__ = {
        "paragraph_digest": {
            "source_field": "paragraph_refs",
            "model": "models:SectionParagraphDoc",
            "template": "- {title}",
        }
    }
    __template__ = """
# ⸢rev•title⸥

⸢rev•section_body⸥

Section ID: ⸢rev•section_id⸥
Source Section File: ⸢rev•source_section_file⸥

## Paragraph Refs

- ⸢rev,list•paragraph_refs⸥

## Paragraph Digest

⸢render•paragraph_digest⸥
""".strip()

    title: str = Field(description="Rendered section title in the manuscript.")
    section_body: str = Field(description="Clean section prose composed from paragraph_text fields.")
    section_id: str = Field(description="Stable identifier for the section document.")
    source_section_file: str = Field(description="Original current-paper section file used for bootstrap.")
    paragraph_refs: list[str] = Field(default_factory=list, description="Relative paths to paragraph documents that belong to this section.")


class PaperManuscriptDoc(StructuredNLDoc):
    __compositions__ = {
        "manuscript_body": {
            "source_field": "section_refs",
            "model": "models:PaperSectionDoc",
            "template": "# {title}\n\n{section_body}",
            "separator": "\n\n",
        },
        "section_digest": {
            "source_field": "section_refs",
            "model": "models:PaperSectionDoc",
            "template": "- {section_id}: {title}",
        }
    }
    __template__ = """
# ⸢rev•title⸥

## Abstract

⸢rev•abstract⸥

Bibliography: ⸢rev•bibliography⸥

## Section Refs

- ⸢rev,list•section_refs⸥

## Section Digest

⸢render•section_digest⸥

## Draft Body

⸢render•manuscript_body⸥
""".strip()

    title: str = Field(description="Paper title for the composed manuscript.")
    abstract: str = Field(description="Abstract text for the manuscript.")
    bibliography: str = Field(default="", description="Path to the bibliography file used by the paper.")
    section_refs: list[str] = Field(default_factory=list, description="Relative paths to section documents that make up the manuscript.")


class WorkflowTaskPolicyDoc(StructuredNLDoc):
    __template__ = """
# ⸢rev•title⸥

Policy Scope: ⸢rev•policy_scope⸥
Applies To: ⸢rev•applies_to⸥

## Summary

⸢rev•summary⸥

## Task Types

- ⸢rev,list•task_types⸥

## Inheritance Model

⸢rev•inheritance_model⸥

## Inheritable Fields

- ⸢rev,list•inheritable_fields⸥

## Non Inheritable Fields

- ⸢rev,list•non_inheritable_fields⸥

## Resolution Rules

⸢rev•resolution_rules⸥

## Validation Notes

⸢rev•validation_notes⸥
""".strip()

    title: str = Field(description="Human-readable title for the workflow task policy.")
    policy_scope: str = Field(description="Workflow scope governed by this policy document.")
    applies_to: str = Field(description="Task surfaces or directories where the policy applies.")
    summary: str = Field(description="Short explanation of the workflow problem this policy solves.")
    task_types: list[str] = Field(default_factory=list, description="Allowed task types for the local workflow.")
    inheritance_model: str = Field(description="How tasks inherit workflow context from other tasks.")
    inheritable_fields: list[str] = Field(default_factory=list, description="Task fields that may be inherited through workflow resolution.")
    non_inheritable_fields: list[str] = Field(default_factory=list, description="Task fields that must remain local to each task.")
    resolution_rules: str = Field(description="Operational rules for combining inherited and local task context.")
    validation_notes: str = Field(description="How supervisors, executors, and testers should validate the policy in practice.")


class WorkflowLogEntryDoc(StructuredNLDoc):
    __template__ = """
# ⸢rev•title⸥

Entry ID: ⸢rev•entry_id⸥
Date: ⸢rev•date⸥
Who: ⸢rev•who⸥
Role: ⸢rev•role⸥
Action Kind: ⸢rev•action_kind⸥

## Summary

⸢rev•summary⸥

## 5W1H+

### What

⸢rev•what⸥

### Why

⸢rev•why⸥

### When

⸢rev•when_detail⸥

### Where

⸢rev•where⸥

### Who Detail

⸢rev•who_detail⸥

### How

⸢rev•how⸥

## Workflow Artifacts Changed

### Files

- ⸢rev,list•workflow_files⸥

### Tasks

- ⸢rev,list•workflow_tasks⸥

### Pills

- ⸢rev,list•workflow_pills⸥

### Rituals

- ⸢rev,list•workflow_rituals⸥

### Specs

- ⸢rev,list•workflow_specs⸥

## Workflow Reflection

### Observed Failure Mode

⸢rev•observed_failure_mode⸥

### Workflow Change Applied

⸢rev•workflow_change_applied⸥

### Acceptance Gap

⸢rev•acceptance_gap⸥

### Supervisor Reflection

⸢rev•supervisor_reflection⸥

## Tags

- ⸢rev,list•tags⸥

## Optional Workflow Details

⸢rev•optional_workflow_details⸥
""".strip()

    title: str = Field(description="Human-readable title for the workflow log entry.")
    entry_id: str = Field(description="Stable identifier for the workflow log entry.")
    date: str = Field(default_factory=lambda: date.today().isoformat(), description="Date or timestamp associated with the workflow action.")
    who: str = Field(description="Agent or actor that authored the workflow log entry.")
    role: str = Field(description="Workflow role of the author, such as supervisor or executor.")
    action_kind: str = Field(description="Kind of workflow action captured by the entry.")
    summary: str = Field(description="Short summary of the workflow action or reflection.")
    what: str = Field(description="What workflow action was taken.")
    why: str = Field(description="Why the workflow action was necessary.")
    when_detail: str = Field(description="When the workflow action took place in local process terms.")
    where: str = Field(description="Where in the workflow surfaces or repo the action applied.")
    who_detail: str = Field(description="More detailed description of the actor that took the workflow action.")
    how: str = Field(description="How the workflow action was carried out.")
    workflow_files: list[str] = Field(default_factory=list, description="Workflow-facing files changed or reviewed by the action.")
    workflow_tasks: list[str] = Field(default_factory=list, description="Task documents introduced, executed, inherited, or questioned.")
    workflow_pills: list[str] = Field(default_factory=list, description="Pills introduced, applied, or questioned.")
    workflow_rituals: list[str] = Field(default_factory=list, description="Workflow rituals touched by the action.")
    workflow_specs: list[str] = Field(default_factory=list, description="Spec artifacts changed from a workflow-governance perspective.")
    optional_workflow_details: str = Field(default="", description="Optional freeform workflow details such as primitives, commits, runs, atoms, or followup guardrails.")
    observed_failure_mode: str = Field(description="Workflow failure mode observed during the action.")
    workflow_change_applied: str = Field(description="Concrete workflow change applied by the action.")
    acceptance_gap: str = Field(default="", description="Acceptance or closeout weakness exposed by the action.")
    supervisor_reflection: str = Field(default="", description="Supervisor-facing reflection about routing, gating, or closeout.")
    tags: list[str] = Field(default_factory=list, description="Workflow-oriented tags for later retrieval.")
