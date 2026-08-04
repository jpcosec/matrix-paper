from __future__ import annotations

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
