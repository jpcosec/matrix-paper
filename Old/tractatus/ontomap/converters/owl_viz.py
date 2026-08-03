"""
OWL Ontology → Mermaid visualizer.
Renderiza la estructura de la ontología (clases, propiedades, axiomas),
no las instancias.
"""
from rdflib import Graph, RDF, RDFS, OWL, Namespace

ONTO = Namespace("http://ontomap.io/ontology#")

AXIOM_LABELS = {
    str(OWL.TransitiveProperty):  "transitive",
    str(OWL.IrreflexiveProperty): "irreflexive",
    str(OWL.AsymmetricProperty):  "asymmetric",
}


def local(iri) -> str:
    return str(iri).split("#")[-1].split("/")[-1]


def dump_owl_mermaid(g: Graph) -> str:
    lines = ["graph TD", ""]

    classes = set()
    properties = set()

    # ── Jerarquía de clases (subClassOf) ─────────────────
    lines.append("  %% Clases")
    for s, _, o in g.triples((None, RDFS.subClassOf, None)):
        sc, oc = local(s), local(o)
        classes.update([sc, oc])
        lines.append(f"  {sc}[{sc}] -->|subClassOf| {oc}[{oc}]")
    lines.append("")

    # ── Jerarquía de propiedades (subPropertyOf) ──────────
    lines.append("  %% Propiedades")
    for s, _, o in g.triples((None, RDFS.subPropertyOf, None)):
        sp, op = local(s), local(o)
        properties.update([sp, op])
        lines.append(f"  {sp}([{sp}]) -->|subPropertyOf| {op}([{op}])")
    lines.append("")

    # ── Domain / Range ────────────────────────────────────
    lines.append("  %% Domain y Range")
    for s, _, o in g.triples((None, RDFS.domain, None)):
        sp, oc = local(s), local(o)
        lines.append(f"  {sp}([{sp}]) -.->|domain| {oc}[{oc}]")
    for s, _, o in g.triples((None, RDFS.range, None)):
        sp, oc = local(s), local(o)
        lines.append(f"  {sp}([{sp}]) -.->|range| {oc}[{oc}]")
    lines.append("")

    # ── Axiomas OWL ───────────────────────────────────────
    lines.append("  %% Axiomas OWL")
    seen_axioms: dict[str, list[str]] = {}
    for axiom_type, label in AXIOM_LABELS.items():
        for s, _, _ in g.triples((None, RDF.type, g.store._IOMemory__spo if False else None)):
            pass
        for s in g.subjects(RDF.type, g.resource(axiom_type) if False else None):
            pass

    # Forma directa: iterar por tipo de axioma
    for s, p, o in g:
        if str(p) == str(RDF.type) and str(o) in AXIOM_LABELS:
            prop = local(s)
            label = AXIOM_LABELS[str(o)]
            key = prop
            seen_axioms.setdefault(key, []).append(label)

    for prop, axioms in seen_axioms.items():
        label = " + ".join(axioms)
        lines.append(f"  axiom_{prop}{{\"⚡ {label}\"}} --- {prop}([{prop}])")
    lines.append("")

    return "\n".join(lines)
