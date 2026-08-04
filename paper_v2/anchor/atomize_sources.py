#!/usr/bin/env python3
"""Atomize the 17 bib-cited sources missing from the KB.

Creates Source_PDF atoms in TractatusKnowledgeMachine/atoms/Fuentes/ from
references.bib metadata and registers them in comp_fuentes.md (bib-bridge
parseable format). Idempotent: skips existing atoms, inserts the comp section
only if absent. Run from Matrix repo root: python3 paper_v2/anchor/atomize_sources.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # Matrix/
BIB = ROOT / "Neurips_peiper" / "references.bib"
FUENTES = ROOT / "TractatusKnowledgeMachine" / "atoms" / "Fuentes"
COMP = FUENTES.parent / "composiciones_review" / "comp_fuentes.md"

KEYS = ["harnad1990symbolgrounding", "wittgenstein1922", "bender2020",
        "lyre2024understanding", "halueval2023", "semantic_entropy2024",
        "kommers2025slop", "dawid2024latent", "assran2023ijepa", "ibrahim2026",
        "ferrone2019", "liu2025code4logic", "lee2025entailment",
        "choi2025knowledge", "cheng2025empowering", "bian2025llm", "liang2025survey"]

# Deltas 1/2/3/6: bibkeys huérfanas (bib) + 7 related_papers (con PDF en repo)
KEYS += ["hornik1991approximation", "hanin2017universal", "wei2024measuring",
         "simhi2024distinguishing", "brachman1990", "lehmann1992", "sowa1991",
         "sansford2024grapheval", "mckenna2023", "yin2023", "marks2024",
         "chen2024", "gekhman2024", "kang2025", "chuang2024",
         "kruse2022causal"]

PDF_PATHS = {
    "mckenna2023": "review/related_papers/paper1_emnlp2023_182.pdf",
    "yin2023": "review/related_papers/paper2_acl2023_551.pdf",
    "marks2024": "review/related_papers/paper3_colm2024_2310_06824.pdf",
    "chen2024": "review/related_papers/paper4_iclr2024_2402_03744.pdf",
    "kang2025": "review/related_papers/paper5_naacl2025_2403_05612.pdf",
    "gekhman2024": "review/related_papers/paper6_emnlp2024_444.pdf",
    "chuang2024": "review/related_papers/paper7_iclr2024_2309_03883.pdf",
}

TEMPLATE = """---
id: atom-source-pdf-{slug}
title: Source PDF {key}
five_wh_one_plus: what
tags:
- system:matrix
---
# Source_PDF_{key}_pdf

**Tipo:** Registered Source (bib entry)
**Referencia Original:** `{key}` (`Neurips_peiper/references.bib`)
**Referencia Bibliográfica:** {surname} et al. ({year}). *{title}*.

Este nodo actúa como un ancla en el grafo de conocimiento para conectar conceptos abstractos con su origen externo o su implementación física en código, cumpliendo con la arquitectura de Provenance. Registrado desde `references.bib` ({pdf_note}).
"""


def bib_entries() -> dict:
    bib = BIB.read_text(encoding="utf-8")
    out = {}
    for k in KEYS:
        m = re.search(r'@(\w+)\{' + re.escape(k) + r',(.*?)\n\}', bib, re.S)
        if not m:
            raise SystemExit(f"bib key no encontrada: {k}")
        body = m.group(2)

        def field(name: str) -> str:
            f = re.search(name + r'\s*=\s*\{(.*?)\},?\s*(?:\n|$)', body, re.S) \
                or re.search(name + r'\s*=\s*"([^"]*)"', body)
            return re.sub(r'\s+', ' ', f.group(1)).strip() if f else ""

        author = field('author')
        surname = re.split(r'\s+and\s+', author)[0].split(',')[0].strip() or k
        out[k] = {"surname": surname, "year": field('year') or "s.f.",
                  "title": field('title')}
    return out


def main() -> None:
    entries = bib_entries()
    created, skipped = [], []
    for key, e in entries.items():
        path = FUENTES / f"Source_PDF_{key}_pdf.md"
        if path.exists():
            skipped.append(key)
            continue
        slug = key.replace("_", "-").lower()
        pdf_note = (f"PDF disponible en `{PDF_PATHS[key]}`" if key in PDF_PATHS
                    else "PDF no almacenado en el repositorio")
        path.write_text(TEMPLATE.format(slug=slug, key=key, pdf_note=pdf_note, **e),
                        encoding="utf-8")
        created.append(key)
    print(f"átomos creados={len(created)} ya_existían={len(skipped)}")

    # comp_fuentes.md: reconstruir la sección Source Bib completa (idempotente)
    comp = COMP.read_text(encoding="utf-8")
    total_bib = len(entries)
    bullets = [f"- **[[Source_PDF_{k}_pdf]]** — {e['surname']} ({e['year']}): {e['title']}."
               for k, e in entries.items()]
    section = f"### Source Bib ({total_bib} átomos — provenance bibliográfica)\n\n" + "\n".join(bullets)
    m = re.search(r"### Source Bib \(\d+ átomos[^)]*\)\n\n(?:- \*\*\[\[Source_PDF_.*\n?)+", comp)
    if m:
        comp = comp[:m.start()] + section + "\n" + comp[m.end():]
        print(f"comp_fuentes.md: sección Source Bib reconstruida ({total_bib} átomos)")
    else:
        comp = comp.replace("\n### Source Code", "\n" + section + "\n\n### Source Code", 1)
        print(f"comp_fuentes.md: sección Source Bib insertada ({total_bib} átomos)")
    comp = re.sub(r"atom_count: \d+", f"atom_count: {35 + total_bib}", comp, count=1)
    COMP.write_text(comp, encoding="utf-8")
    print(f"atom_count -> {35 + total_bib}")


if __name__ == "__main__":
    main()
