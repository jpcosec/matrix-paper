#!/usr/bin/env python3
"""Generate anchor/build/coverage.md (Fase 4). Run from paper_v2/."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ATOMS_ROOT = ROOT.parent / "TractatusKnowledgeMachine" / "atoms"

mapping = yaml.safe_load((ROOT / "anchor" / "mapping.yaml").read_text())
atoms_index = json.loads((ROOT / "anchor" / "build" / "atoms_index.json").read_text())["atoms"]
summary = (ROOT / "anchor" / "build" / "summary.md").read_text(encoding="utf-8")

paras = mapping["paragraphs"]
used = {a["atom_path"] for v in paras.values() for a in v}
bridges = Counter(a["bridge"] for v in paras.values() for a in v)

by_section: dict[str, list[int]] = {}
for anchor, v in paras.items():
    sec = anchor.rsplit("-p", 1)[0]
    by_section.setdefault(sec, [0, 0])
    by_section[sec][0 if v else 1] += 1

atom_paths = {a["path"] for a in atoms_index}
exclude_prefixes = ("composiciones_review/", "composiciones_spec/", "Fuentes/")
kb_atoms = {p for p in atom_paths if not p.startswith(exclude_prefixes) and p != "Propuesta_Indice.md"}
unused = sorted(kb_atoms - used)
unused_by_folder = Counter(p.split("/")[0] + "/" + (p.split("/")[1] if p.count("/") > 1 else "") for p in unused)

lines = [
    "# Cobertura del anclaje KB→paper (Fase 4)",
    "",
    f"- Párrafos anclados: **{sum(1 for v in paras.values() if v)}/{len(paras)}** (55 con átomos; 3 vacíos justificados: 2 encabezados de sección, 1 frase transicional).",
    f"- Entradas de anclaje: **{sum(len(v) for v in paras.values())}** (`kind: kb-atom` en `sources/kb/`).",
    f"- Átomos KB distintos usados: **{len(used & kb_atoms)}** de {len(kb_atoms)} (excluye Fuentes y composiciones).",
    "",
    "## Por sección",
    "",
    "| Sección | Anclados | Sin ancla |",
    "|---|---|---|",
]
for sec in sorted(by_section):
    a, b = by_section[sec]
    lines.append(f"| {sec} | {a} | {b} |")

lines += ["", "## Distribución por bridge", ""]
for b, n in bridges.most_common():
    lines.append(f"- `{b}`: {n}")

lines += [
    "",
    "## Gap inverso — átomos KB nunca usados por el paper",
    "",
    f"{len(unused)} de {len(kb_atoms)} átomos de contenido no aparecen en ningún anclaje.",
    "",
    "Top carpetas:",
]
for f, n in unused_by_folder.most_common(10):
    lines.append(f"- `{f}`: {n}")

lines += [
    "",
    "## Bibkeys citadas sin Source_PDF en la KB (17)",
    "",
    "Literature SotA no atomizada; candidatas a futura atomización:",
    "",
]
m = re.search(r"sin match[^\n]*\n\n?((?:`[^`]+`,?\s*)+)", summary, re.I)
bibkeys = re.findall(r"`([a-z0-9_]+)`", m.group(1), re.I) if m else []
lines.append(", ".join(f"`{b}`" for b in bibkeys) if bibkeys else "(ver summary.md)")

lines += [
    "",
    "## Apéndice — wikilinks rotos en la KB (11 distintos)",
    "",
    "Detectados en Fase 1 (ver `summary.md` para el top-20 con conteos):",
    "",
]
for w in ["[[BlockMatrix]] (×12)", "[[BooleanMatrix]] (×3)", "[[Dimension_Hipertensor]] (×2)",
          "[[Source_PDF_hornik1991approximation_pdf]]", "[[Source_PDF_arxiv2306_06085_pdf]]"]:
    lines.append(f"- {w}")

(ROOT / "anchor" / "build" / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("coverage.md written:", len(lines), "lines")
