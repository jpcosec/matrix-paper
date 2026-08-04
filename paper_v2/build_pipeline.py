#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
MATRIX_ROOT = ROOT.parent
PROJECTS_ROOT = MATRIX_ROOT.parent
PAPER_SOURCE_ROOT = MATRIX_ROOT / "Neurips_peiper"
PAPER_CONFIG_ROOT = PAPER_SOURCE_ROOT / "paper"

KB_MAPPING_PATH = ROOT / "anchor" / "mapping.yaml"
ATOMS_INDEX_PATH = ROOT / "anchor" / "build" / "atoms_index.json"
KB_ATOMS_ROOT = MATRIX_ROOT / "TractatusKnowledgeMachine" / "atoms"
KB_SOURCES_DIR = ROOT / "sources" / "kb"
KB_EXCERPT_LIMIT = 1200
SLDB_SRC = PROJECTS_ROOT / "hum-ecosystem" / "tools" / "sldb" / "src"

if str(SLDB_SRC) not in sys.path:
    sys.path.insert(0, str(SLDB_SRC))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models import (  # noqa: E402
    PaperManuscriptDoc,
    PaperSectionDoc,
    PaperSourceDoc,
    SectionParagraphDoc,
    WritingNoteDoc,
)
from sldb.runtime.validation import (  # noqa: E402
    extract_model_data,
    render_model_markdown,
    validate_model_input_roundtrip,
)


def relpath(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, start=from_path.parent)


def sentence_claim(text: str, limit: int = 180) -> str:
    flat = re.sub(r"\s+", " ", text).strip()
    if not flat:
        return "Empty source block."
    match = re.search(r".*?[.!?](?:\s|$)", flat)
    claim = match.group(0).strip() if match else flat
    return claim[:limit].rstrip()


def split_heading_and_blocks(markdown: str, fallback_title: str) -> tuple[str, list[str]]:
    text = markdown.strip()
    title = fallback_title
    body = text
    if text.startswith("#"):
        lines = text.splitlines()
        first = lines[0].strip()
        if first.startswith("#"):
            title = first.lstrip("#").strip() or fallback_title
            body = "\n".join(lines[1:]).strip()
    blocks = [block.strip() for block in re.split(r"\n\s*\n", body) if block.strip()]
    return title, blocks


def ensure_dirs() -> None:
    for name in ("sources", "notes", "paragraphs", "sections", "manuscript", "build"):
        (ROOT / name).mkdir(parents=True, exist_ok=True)


def load_config() -> dict:
    config_path = PAPER_CONFIG_ROOT / "paper.yaml"
    return yaml.safe_load(config_path.read_text(encoding="utf-8"))


def resolve_source_path(path_str: str) -> Path:
    return (PAPER_CONFIG_ROOT / path_str).resolve()


def load_kb_mapping() -> dict[str, list[dict]]:
    """Anclas KB por parrafo desde anchor/mapping.yaml (automatico; {} si no existe)."""
    if not KB_MAPPING_PATH.exists():
        return {}
    data = yaml.safe_load(KB_MAPPING_PATH.read_text(encoding="utf-8")) or {}
    return data.get("paragraphs") or {}


def load_atom_titles() -> dict[str, str]:
    """atom_path -> title desde anchor/build/atoms_index.json (fallback: frontmatter)."""
    if not ATOMS_INDEX_PATH.exists():
        return {}
    index = json.loads(ATOMS_INDEX_PATH.read_text(encoding="utf-8"))
    return {atom["path"]: str(atom.get("title", "")) for atom in index.get("atoms", [])}


def atom_title(atom_path: str, atom_file: Path, titles: dict[str, str]) -> str:
    title = titles.get(atom_path, "")
    if title:
        return title
    match = re.search(r"^title:\s*(.+)$", atom_file.read_text(encoding="utf-8"), re.M)
    return match.group(1).strip() if match else Path(atom_path).stem.replace("_", " ")


def kb_excerpt(atom_file: Path, limit: int = KB_EXCERPT_LIMIT) -> str:
    """Seccion '## Que es' del atomo (fallback: primer parrafo tras el H1), <= limit chars."""
    text = atom_file.read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    body = text[frontmatter.end():] if frontmatter else text
    match = re.search(r"^## Qué es[ \t]*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if match:
        excerpt = match.group(1)
    else:
        heading = re.search(r"^# .*$", body, re.M)
        rest = body[heading.end():] if heading else body
        rest = "\n".join(
            line for line in rest.splitlines() if not line.lstrip().startswith("#")
        )
        blocks = [block.strip() for block in re.split(r"\n\s*\n", rest) if block.strip()]
        excerpt = blocks[0] if blocks else ""
    lines = [line for line in excerpt.splitlines() if line.strip() != "---"]
    return "\n".join(lines).strip()[:limit]


def write_doc(model_type, path: Path, payload: dict) -> dict:
    markdown = render_model_markdown(model_type, payload)
    path.write_text(markdown + "\n", encoding="utf-8")
    valid, details = validate_model_input_roundtrip(model_type, markdown)
    return {
        "path": str(path.relative_to(ROOT)),
        "model": model_type.__name__,
        "valid": valid,
        "input_data": details["input_data"],
    }


def build_sources_notes_paragraphs(
    config: dict,
    kb_paragraphs: dict[str, list[dict]],
    atom_titles: dict[str, str],
) -> tuple[list[str], list[dict]]:
    validations: list[dict] = []
    section_doc_refs: list[str] = []

    for section_rel in config["sections"]:
        source_path = resolve_source_path(section_rel)
        section_id = source_path.stem
        fallback_title = section_id.replace("_", " ").title()
        title, blocks = split_heading_and_blocks(
            source_path.read_text(encoding="utf-8"), fallback_title
        )

        paragraph_refs: list[str] = []
        paragraph_doc_paths: list[Path] = []
        for index, block in enumerate(blocks, start=1):
            stem = f"{section_id}-p{index:02d}"
            source_doc_path = ROOT / "sources" / f"{stem}.md"
            note_doc_path = ROOT / "notes" / f"{stem}.md"
            paragraph_doc_path = ROOT / "paragraphs" / f"{stem}.md"

            validations.append(
                write_doc(
                    PaperSourceDoc,
                    source_doc_path,
                    {
                        "title": f"{title} source {index:02d}",
                        "kind": "current-paper-block",
                        "origin": str(source_path.relative_to(PAPER_SOURCE_ROOT)),
                        "anchor": stem,
                        "excerpt": block,
                        "relevance": f"Bootstrap source block {index:02d} extracted from the current {title} draft.",
                    },
                )
            )

            kb_refs: list[str] = []
            for kb_entry in kb_paragraphs.get(stem, []):
                atom_path = kb_entry["atom_path"]
                atom_file = (KB_ATOMS_ROOT / atom_path).resolve()
                kb_source_path = KB_SOURCES_DIR / f"{stem}__{kb_entry['atom_id']}.md"
                validations.append(
                    write_doc(
                        PaperSourceDoc,
                        kb_source_path,
                        {
                            "title": atom_title(atom_path, atom_file, atom_titles),
                            "kind": "kb-atom",
                            "origin": os.path.relpath(atom_file, ROOT),
                            "anchor": kb_entry["atom_id"],
                            "excerpt": kb_excerpt(atom_file),
                            "relevance": (
                                f"bridge={kb_entry['bridge']} score={kb_entry['score']}"
                                f" — {kb_entry['detail']}"
                            ),
                        },
                    )
                )
                kb_refs.append(relpath(note_doc_path, kb_source_path))

            source_ref = relpath(note_doc_path, source_doc_path)
            validations.append(
                write_doc(
                    WritingNoteDoc,
                    note_doc_path,
                    {
                        "title": f"{title} note {index:02d}",
                        "sources": [source_ref, *kb_refs],
                        "intent": f"Bridge source block {index:02d} into section-ready prose for {title}.",
                        "claim": sentence_claim(block),
                        "notes": block,
                    },
                )
            )

            note_ref = relpath(paragraph_doc_path, note_doc_path)
            validations.append(
                write_doc(
                    SectionParagraphDoc,
                    paragraph_doc_path,
                    {
                        "title": f"{title} paragraph {index:02d}",
                        "section_id": section_id,
                        "paragraph_index": index,
                        "notes_refs": [note_ref],
                        "paragraph_text": block,
                    },
                )
            )
            paragraph_refs.append(relpath(ROOT / "sections" / f"{section_id}.md", paragraph_doc_path))
            paragraph_doc_paths.append(paragraph_doc_path)

        section_doc_path = ROOT / "sections" / f"{section_id}.md"
        section_body = "\n\n".join(
            extract_model_data(
                SectionParagraphDoc, path.read_text(encoding="utf-8")
            )["paragraph_text"]
            for path in paragraph_doc_paths
        )
        validations.append(
            write_doc(
                PaperSectionDoc,
                section_doc_path,
                {
                    "title": title,
                    "section_body": section_body,
                    "section_id": section_id,
                    "source_section_file": str(source_path.relative_to(PAPER_SOURCE_ROOT)),
                    "paragraph_refs": paragraph_refs,
                },
            )
        )
        section_doc_refs.append(relpath(ROOT / "manuscript" / "paper.md", section_doc_path))

    return section_doc_refs, validations


def build_manuscript(config: dict, section_doc_refs: list[str]) -> dict:
    abstract_path = resolve_source_path(config["abstract_file"])
    manuscript_path = ROOT / "manuscript" / "paper.md"
    bibliography_path = (PAPER_CONFIG_ROOT / config["bibliography"]).resolve()
    payload = {
        "title": config["title"],
        "abstract": abstract_path.read_text(encoding="utf-8").strip(),
        "bibliography": os.path.relpath(bibliography_path, start=manuscript_path.parent),
        "section_refs": section_doc_refs,
    }
    return write_doc(PaperManuscriptDoc, manuscript_path, payload)


def compose_manuscript() -> dict:
    manuscript_path = ROOT / "manuscript" / "paper.md"
    payload = extract_model_data(
        PaperManuscriptDoc, manuscript_path.read_text(encoding="utf-8")
    )
    section_chunks: list[str] = []
    for ref in payload.get("section_refs", []):
        section_path = (manuscript_path.parent / ref).resolve()
        section_payload = extract_model_data(
            PaperSectionDoc, section_path.read_text(encoding="utf-8")
        )
        section_chunks.append(
            f"# {section_payload['title']}\n\n{section_payload['section_body']}"
        )

    rendered = (
        f"# {payload['title']}\n\n"
        f"## Abstract\n\n{payload['abstract'].strip()}\n\n"
        + "\n\n".join(section_chunks).strip()
        + "\n"
    )
    (ROOT / "build" / "paper.composed.md").write_text(rendered, encoding="utf-8")
    report = {
        "path": "build/paper.composed.md",
        "mode": "field-composed-render",
        "section_count": len(payload.get("section_refs", [])),
        "sources": payload.get("section_refs", []),
    }
    (ROOT / "build" / "compose_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return report


def main() -> int:
    ensure_dirs()
    config = load_config()
    kb_paragraphs = load_kb_mapping()
    atom_titles = load_atom_titles() if kb_paragraphs else {}
    # Idempotente: sources/kb/ se borra siempre y se regenera desde mapping.yaml.
    shutil.rmtree(KB_SOURCES_DIR, ignore_errors=True)
    if kb_paragraphs:
        KB_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    section_doc_refs, validations = build_sources_notes_paragraphs(
        config, kb_paragraphs, atom_titles
    )
    validations.append(build_manuscript(config, section_doc_refs))
    compose_report = compose_manuscript()

    summary = {
        "validation": validations,
        "compose": compose_report,
    }
    (ROOT / "build" / "validation_report.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(ROOT / "build" / "paper.composed.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
