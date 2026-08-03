from pydantic import Field
from sldb import StructuredNLDoc

class CompositionSpecDoc(StructuredNLDoc):
    __semantics__ = {
        "type": ["knowledge", "composition-spec"],
        "workspace": ["desk", "atoms", "composiciones_spec"],
    }
    __template__ = """---
id: ⸢rev•id⸥
title: ⸢rev•title⸥
target_system: ⸢rev•target_system⸥
spec_type: ⸢rev•spec_type⸥
atom_count: ⸢rev•atom_count⸥
tags: ⸢rev•tags⸥
---

# ⸢render•title⸥

## Componente/Sistema Objetivo

⸢rev•target_system_detail⸥

## Tipo de Especificación

⸢rev•spec_type_detail⸥

## Cadena de Átomos Fundacionales

⸢rev•atom_chain⸥

## Detalle de la Especificación

⸢rev•spec_detail⸥
""".strip()

    title: str = Field(description="Título descriptivo de la especificación.")
    target_system: str = Field(description="Componente o sistema objetivo de la especificación.")
    target_system_detail: str = Field(default="", description="Descripción del sistema objetivo en Markdown.")
    spec_type: str = Field(description="Tipo de especificación (ej. API, Core, Hardware, Ingestion).")
    spec_type_detail: str = Field(default="", description="Explicación del tipo en Markdown.")
    atom_count: int = Field(description="Cantidad de átomos que la componen.")
    atom_chain: str = Field(description="Markdown con la cadena ordenada de átomos fundacionales.")
    spec_detail: str = Field(description="Markdown con el desarrollo de la especificación técnica.")
    tags: list[str] = Field(default_factory=list, description="Tags semánticos namespaced.")
