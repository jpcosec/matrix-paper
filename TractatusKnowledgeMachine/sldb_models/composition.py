from __future__ import annotations

from pydantic import Field

from sldb import StructuredNLDoc


class CompositionReviewDoc(StructuredNLDoc):
    __semantics__ = {
        "type": ["knowledge", "composition-review"],
        "workspace": ["desk", "atoms", "composiciones_review"],
    }
    __template__ = """---
title: ⸢rev•title⸥
folder: ⸢rev•folder⸥
question: ⸢rev•question⸥
atom_count: ⸢rev•atom_count⸥
tags: ⸢rev•tags⸥
---

# ⸢render•title⸥

## Carpeta Revisada

⸢rev•folder_path⸥

## Pregunta que responde esta composición

⸢rev•question_detail⸥

## Cadena argumentativa (átomos en orden de lectura)

⸢rev•chain⸥

## Síntesis

⸢rev•synthesis⸥

## Gaps detectados

⸢rev•gaps⸥
""".strip()

    title: str = Field(
        description="Título descriptivo de la composición."
    )
    folder: str = Field(
        description="Ruta relativa de la carpeta que esta composición revisa (desde atoms/)."
    )
    folder_path: str = Field(
        description="Ruta completa de la carpeta revisada, en formato Markdown con link."
    )
    question: str = Field(
        description="Pregunta clave que esta composición responde."
    )
    question_detail: str = Field(
        description="Markdown con la pregunta completa y contexto."
    )
    atom_count: int = Field(
        description="Número de átomos que componen la cadena argumentativa."
    )
    chain: str = Field(
        description="Markdown con la cadena argumentativa ordenada, cada átomo como wikilink."
    )
    synthesis: str = Field(
        description="Markdown con la síntesis argumentativa de la cadena."
    )
    gaps: str = Field(
        default="",
        description="Markdown con gaps o vacíos argumentativos detectados, si los hay."
    )
    tags: list[str] = Field(
        default_factory=list,
        description="Tags semánticos namespaced."
    )
