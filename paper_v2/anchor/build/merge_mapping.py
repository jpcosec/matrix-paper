#!/usr/bin/env python3
"""Fase 3 - Paso 1: merge mapping_draft.yaml + fase2_verdicts.json -> anchor/mapping.yaml.

Reglas (segun anchor/build/fase3_spec.md):
1. De mapping_draft: TODOS los candidatos bib y bib_transitive; lexical con score >= 0.5.
2. De fase2_verdicts: aceptados con confidence >= 0.6 -> bridge=fase2_review (score=confidence).
3. Dedupe por atom_path (gana mayor score; empate: bib > bib_transitive > fase2_review > lexical).
4. Cap final de 6 atomos por parrafo (se descarta el excedente de menor score).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

BUILD_DIR = Path(__file__).resolve().parent
ANCHOR_DIR = BUILD_DIR.parent
DRAFT_PATH = BUILD_DIR / "mapping_draft.yaml"
VERDICTS_PATH = BUILD_DIR / "fase2_verdicts.json"
OUT_PATH = ANCHOR_DIR / "mapping.yaml"

LEXICAL_MIN = 0.5
FASE2_MIN = 0.6
CAP = 6
# Prioridad de desempate: bib > bib_transitive > fase2_review > lexical.
# La spec nombra "bib > fase2_review > lexical"; bib_transitive (derivado de bib,
# deterministico) se ubica inmediatamente despues de bib.
BRIDGE_PRIORITY = {"bib": 0, "bib_transitive": 1, "fase2_review": 2, "lexical": 3}


def main() -> int:
    draft = yaml.safe_load(DRAFT_PATH.read_text(encoding="utf-8"))
    verdicts = json.loads(VERDICTS_PATH.read_text(encoding="utf-8"))["verdicts"]

    merged: dict[str, dict[str, dict]] = {}

    def add(anchor: str, atom_id: str, atom_path: str, bridge: str, score: float, detail: str) -> None:
        entries = merged.setdefault(anchor, {})
        prev = entries.get(atom_path)
        cand = {
            "atom_id": atom_id,
            "atom_path": atom_path,
            "bridge": bridge,
            "score": round(float(score), 4),
            "detail": str(detail),
        }
        if prev is None:
            entries[atom_path] = cand
            return
        key = lambda e: (e["score"], -BRIDGE_PRIORITY[e["bridge"]])
        if key(cand) > key(prev):
            entries[atom_path] = cand

    # 1. mapping_draft
    for para in draft["paragraphs"]:
        anchor = para["anchor"]
        merged.setdefault(anchor, {})
        for cand in para["candidates"]:
            bridge = cand["bridge"]
            if bridge in ("bib", "bib_transitive"):
                add(anchor, cand["atom_id"], cand["atom_path"], bridge, cand["score"], cand["detail"])
            elif bridge == "lexical" and float(cand["score"]) >= LEXICAL_MIN:
                add(anchor, cand["atom_id"], cand["atom_path"], bridge, cand["score"], cand["detail"])

    # 2. fase2 verdicts
    n_fase2 = 0
    for verdict in verdicts:
        anchor = verdict["anchor"]
        merged.setdefault(anchor, {})
        for acc in verdict["accepted"]:
            conf = float(acc["confidence"])
            if conf >= FASE2_MIN:
                add(anchor, acc["atom_id"], acc["atom_path"], "fase2_review", conf, acc["reason"])
                n_fase2 += 1

    # 3+4. orden determinista y cap 6
    paragraphs: dict[str, list] = {}
    stats = {"anchors": 0, "anchored": 0, "entries": 0, "dropped_cap": 0, "fase2_added": n_fase2}
    for anchor, entries in merged.items():
        ordered = sorted(
            entries.values(),
            key=lambda e: (-e["score"], BRIDGE_PRIORITY[e["bridge"]], e["atom_id"]),
        )
        stats["dropped_cap"] += max(0, len(ordered) - CAP)
        kept = ordered[:CAP]
        paragraphs[anchor] = kept
        stats["anchors"] += 1
        stats["entries"] += len(kept)
        if kept:
            stats["anchored"] += 1

    mapping = {
        "version": 1,
        "generated_by": "anchor merge (fases 1+2)",
        "paragraphs": paragraphs,
        # section_compositions bendecido por el orquestador: copia verbatim.
        "sections": draft["section_compositions"],
    }
    OUT_PATH.write_text(
        yaml.safe_dump(mapping, allow_unicode=True, sort_keys=False, width=140),
        encoding="utf-8",
    )
    print(f"[OK] {OUT_PATH}")
    print(f"[OK] parrafos: {stats['anchors']} (con ancla: {stats['anchored']}, sin ancla: {stats['anchors'] - stats['anchored']})")
    print(f"[OK] entradas totales: {stats['entries']} | fase2 agregadas: {stats['fase2_added']} | descartadas por cap: {stats['dropped_cap']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
