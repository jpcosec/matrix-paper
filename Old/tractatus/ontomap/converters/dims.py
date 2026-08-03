"""
Mapping entre labels de texto {dim: value} y propiedades OWL.
Compartido por los parsers de Mermaid y PlantUML.
"""
import re
from rdflib import Namespace

ONTO = Namespace("http://ontomap.io/ontology#")

# Dimensiones y si su valor es un IRI (ObjectProperty) o string (DatatypeProperty)
DIMS: dict[str, tuple] = {
    "where": (ONTO.where, "object"),
    "what":  (ONTO.what,  "object"),
    "when":  (ONTO.when,  "literal"),
    "how":   (ONTO.how,   "literal"),
    "why":   (ONTO.why,   "literal"),
    "who":   (ONTO.who,   "object"),
}

# Sub-propiedades conocidas de where/what → su IRI
SUBPROP_MAP: dict[str, object] = {
    # where
    "contains":    ONTO.contains,
    "is_located_in": ONTO.isLocatedIn,
    "persists_at": ONTO.persistsAt,
    "belongs_to":  ONTO.belongsTo,
    # what
    "informs":       ONTO.informs,
    "organizes":     ONTO.organizes,
    "validates":     ONTO.validates,
    "depends_on":    ONTO.dependsOn,
    "inherits":      ONTO.inherits,
    "implements":    ONTO.implements,
    "composes":      ONTO.composes,
    "refs_by_id":    ONTO.refsById,
    "transitions_to": ONTO.transitionsTo,
    "state_update":  ONTO.stateUpdate,
}

# Node types: label en diagramas → IRI de clase OWL
NODE_TYPE_MAP: dict[str, object] = {
    "actor":    ONTO.Actor,
    "zone":     ONTO.Zone,
    "artifact": ONTO.Artifact,
    "process":  ONTO.Process,
    # subclases concretas
    "llmagent":   ONTO.LLMAgent,
    "humanagent": ONTO.HumanAgent,
    "cli":        ONTO.CLI,
    "filesystem": ONTO.FileSystem,
    "database":   ONTO.Database,
    "document":   ONTO.Document,
    "codemodule": ONTO.CodeModule,
    "datamodel":  ONTO.DataModel,
    "algorithm":  ONTO.Algorithm,
}


def parse_dim_label(label: str) -> dict:
    """
    Parsea un label como '{what: informs}, {why: rationale}'
    y retorna un dict {dim_name: value}.
    """
    result = {}
    for m in re.finditer(r'\{(\w+)\s*:\s*([^}]+)\}', label):
        key = m.group(1).strip().lower()
        val = m.group(2).strip()
        if key in DIMS:
            result[key] = val
    return result


def dim_label(dims: dict) -> str:
    """
    Serializa un dict de dimensiones a label de diagrama.
    Solo incluye dims con valor no-None.
    """
    parts = [f"{{{k}: {v}}}" for k, v in dims.items() if v]
    return ", ".join(parts)
