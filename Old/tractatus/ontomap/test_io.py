"""
Test de round-trip:
  workspace.ttl → Mermaid → nuevo grafo → PlantUML
  + carga directa desde el Mermaid original del spec
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from rdflib import Graph
from converters.mermaid import load_mermaid, dump_mermaid
from converters.puml import load_puml, dump_puml

SPARQL = """
PREFIX onto: <http://ontomap.io/ontology#>
SELECT (COUNT(*) as ?n) WHERE { ?e a onto:OntologyEdge }
"""

# ── 1. Cargar el grafo base y materializar subPropertyOf ─
from converters.dims import ONTO, SUBPROP_MAP
from rdflib import URIRef

g_base = Graph()
g_base.parse("ontology/core.ttl",      format="turtle")
g_base.parse("ontology/workspace.ttl", format="turtle")

# Inverso de SUBPROP_MAP: sub_iri → parent_iri
PARENT_OF = {str(v): None for v in SUBPROP_MAP.values()}
PARENT_OF.update({
    str(ONTO.contains):    ONTO.where,
    str(ONTO.isLocatedIn): ONTO.where,
    str(ONTO.persistsAt):  ONTO.where,
    str(ONTO.belongsTo):   ONTO.where,
    str(ONTO.informs):     ONTO.what,
    str(ONTO.organizes):   ONTO.what,
    str(ONTO.validates):   ONTO.what,
    str(ONTO.dependsOn):   ONTO.what,
    str(ONTO.inherits):    ONTO.what,
    str(ONTO.implements):  ONTO.what,
    str(ONTO.composes):    ONTO.what,
    str(ONTO.refsById):    ONTO.what,
    str(ONTO.transitionsTo): ONTO.what,
    str(ONTO.stateUpdate): ONTO.what,
})
from rdflib import RDF
new_triples = []
for s, p, o in g_base:
    parent = PARENT_OF.get(str(p))
    if parent:
        new_triples.append((s, parent, o))
for t in new_triples:
    g_base.add(t)
base_edges = list(g_base.query(SPARQL))[0][0]
print(f"[base]     {len(g_base)} tripletas, {base_edges} aristas\n")

# ── 2. Dump → Mermaid ────────────────────────
mermaid_out = dump_mermaid(g_base)
print("── Mermaid generado ──")
print(mermaid_out[:600], "...\n" if len(mermaid_out) > 600 else "\n")

with open("out.mmd", "w") as f:
    f.write(mermaid_out)
print("  → out.mmd guardado\n")

# ── 3. Reload Mermaid → nuevo grafo ──────────
g_reload = load_mermaid(mermaid_out)
reload_edges = list(g_reload.query(SPARQL))[0][0]
print(f"[reload]   {len(g_reload)} tripletas, {reload_edges} aristas\n")

# ── 4. Dump → PlantUML ───────────────────────
puml_out = dump_puml(g_base)
print("── PlantUML generado ──")
print(puml_out[:600], "...\n" if len(puml_out) > 600 else "\n")

with open("out.puml", "w") as f:
    f.write(puml_out)
print("  → out.puml guardado\n")

# ── 5. Reload PlantUML → grafo ───────────────
g_puml = load_puml(puml_out)
puml_edges = list(g_puml.query(SPARQL))[0][0]
print(f"[puml]     {len(g_puml)} tripletas, {puml_edges} aristas\n")

# ── 6. Cargar el Mermaid original del usuario ─
original_mermaid = open("spec_diagram.mmd").read() if os.path.exists("spec_diagram.mmd") else None
if original_mermaid:
    g_orig = load_mermaid(original_mermaid)
    orig_edges = list(g_orig.query(SPARQL))[0][0]
    print(f"[original] {len(g_orig)} tripletas, {orig_edges} aristas")
