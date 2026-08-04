#!/usr/bin/env python3
"""Fase 5 merge: aplica revisiones léxicas + añade anclas bib de los 17 nuevos átomos.

Run from Matrix repo root: python3 paper_v2/anchor/apply_phase5.py
Inputs:
- anchor/mapping.yaml (se reescribe)
- anchor/build/fase5_lexical_reviews.json (reviews mergeados de los 3 shards)
- anchor/build/candidates.json (bibkeys por párrafo, extracción completa Fase 1)
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]          # paper_v2/
ATOMS_ROOT = ROOT.parent / "TractatusKnowledgeMachine" / "atoms"
MAPPING = ROOT / "anchor" / "mapping.yaml"
REVIEWS = ROOT / "anchor" / "build" / "fase5_lexical_reviews.json"
CANDIDATES = ROOT / "anchor" / "build" / "candidates.json"

NEW_BIB_KEYS = ["harnad1990symbolgrounding", "wittgenstein1922", "bender2020",
                "lyre2024understanding", "halueval2023", "semantic_entropy2024",
                "kommers2025slop", "dawid2024latent", "assran2023ijepa", "ibrahim2026",
                "ferrone2019", "liu2025code4logic", "lee2025entailment",
                "choi2025knowledge", "cheng2025empowering", "bian2025llm", "liang2025survey"]


def main() -> None:
    mapping = yaml.safe_load(MAPPING.read_text(encoding="utf-8"))
    paras = mapping["paragraphs"]

    dropped = replaced = kept = errors = 0
    if REVIEWS.is_file():
        reviews = json.loads(REVIEWS.read_text(encoding="utf-8"))["reviews"]
        for rev in reviews:
            anchor = rev["anchor"]
            entries = paras.get(anchor, [])
            for e in rev["entries"]:
                idx = next((i for i, x in enumerate(entries)
                            if x["atom_path"] == e["atom_path"] and x["bridge"] == "lexical"), None)
                if idx is None:
                    print(f"WARN no match: {anchor} {e['atom_path']}")
                    errors += 1
                    continue
                if e["verdict"] == "drop":
                    entries.pop(idx)
                    dropped += 1
                elif e["verdict"] == "replace" and e.get("replacement_atom_path"):
                    newp = e["replacement_atom_path"]
                    if not (ATOMS_ROOT / newp).is_file():
                        print(f"WARN replacement inexistente: {newp}")
                        errors += 1
                        continue
                    entries[idx]["atom_path"] = newp
                    entries[idx]["atom_id"] = Path(newp).stem
                    entries[idx]["detail"] = f"reemplazado en revisión Fase 5: {e.get('reason', '')}"
                    replaced += 1
                else:
                    kept += 1
    else:
        print("WARN: sin fase5_lexical_reviews.json; solo bib-add")

    added_bib = 0
    cand = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    cand_paras = cand["paragraphs"] if "paragraphs" in cand else cand
    for cp in cand_paras:
        anchor = cp["anchor"]
        entries = paras.setdefault(anchor, [])
        have = {x["atom_path"] for x in entries}
        for key in cp.get("bibkeys") or []:
            if key not in NEW_BIB_KEYS:
                continue
            atom_path = f"Fuentes/Source_PDF_{key}_pdf.md"
            if atom_path in have:
                continue
            if not (ATOMS_ROOT / atom_path).is_file():
                print(f"WARN átomo bib inexistente: {atom_path}")
                errors += 1
                continue
            entries.append({
                "atom_id": f"atom-source-pdf-{key.replace('_', '-').lower()}",
                "atom_path": atom_path,
                "bridge": "bib",
                "score": 1.0,
                "detail": f"[@{key}] → Source_PDF atomizado (Fase 5)",
            })
            added_bib += 1

    MAPPING.write_text(yaml.safe_dump(mapping, allow_unicode=True, sort_keys=False),
                       encoding="utf-8")
    total = sum(len(v) for v in paras.values())
    anchored = sum(1 for v in paras.values() if v)
    print(f"lexical: kept={kept} dropped={dropped} replaced={replaced} | "
          f"bib nuevas={added_bib} | errores={errors}")
    print(f"mapping final: párrafos_anclados={anchored}/{len(paras)} entradas={total}")


if __name__ == "__main__":
    main()
