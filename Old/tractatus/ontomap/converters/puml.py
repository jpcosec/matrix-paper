"""
PlantUML ↔ OWL Graph converter.

Formato: diagrama de componentes (@startuml/@enduml)
con packages para zonas y flechas anotadas con {dim: value}.
"""
import re
import uuid
from rdflib import Graph, Namespace, Literal, RDF, RDFS, URIRef

from .dims import ONTO, DIMS, SUBPROP_MAP, parse_dim_label, dim_label

WS = Namespace("http://ontomap.io/instance#")

SPARQL_PREFIXES = """
PREFIX onto: <http://ontomap.io/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

# Símbolo UML por tipo de nodo
TYPE_SYMBOLS = {
    str(ONTO.Actor):    "[Actor]",
    str(ONTO.Zone):     "[Zone]",
    str(ONTO.Artifact): "[Artifact]",
    str(ONTO.Process):  "[Process]",
    str(ONTO.LLMAgent): "[LLMAgent]",
    str(ONTO.CLI):      "[CLI]",
    str(ONTO.Document): "[Document]",
    str(ONTO.DataModel):"[DataModel]",
    str(ONTO.CodeModule):"[CodeModule]",
}


# ─────────────────────────────────────────────
# LOADER: PlantUML → rdflib Graph
# ─────────────────────────────────────────────

def _slug(s: str) -> str:
    return re.sub(r'\W+', '_', s.strip().lower()).strip('_')


def load_puml(text: str, base_ns: str = str(WS)) -> Graph:
    g = Graph()
    g.parse("ontology/core.ttl", format="turtle")

    NS = Namespace(base_ns)
    lines = text.splitlines()

    node_iris: dict[str, URIRef] = {}
    zone_iris: dict[str, URIRef] = {}
    pkg_stack: list[str] = []

    pkg_open   = re.compile(r'^\s*(?:package|frame|node)\s+"([^"]+)"\s*(?:as\s+(\w+))?\s*\{?')
    node_decl  = re.compile(r'^\s*\[([^\]]+)\](?:\s+as\s+(\w+))?\s*$')
    edge_pat   = re.compile(r'^\s*\[([^\]]+)\]\s*(-->|\.\.>|--)\s*\[([^\]]+)\]\s*(?::\s*(.+))?')
    alias_edge = re.compile(r'^\s*(\w+)\s*(-->|\.\.>|--)\s*(\w+)\s*(?::\s*(.+))?')  # flechas entre aliases

    def ensure_node(label: str, alias: str | None = None) -> URIRef:
        key = alias or _slug(label)
        if key not in node_iris:
            iri = NS[key]
            node_iris[key] = iri
            # Infiere tipo desde contexto de package
            cls = ONTO.Actor if "actor" in (pkg_stack[-1] if pkg_stack else "").lower() else ONTO.Artifact
            g.add((iri, RDF.type, cls))
            g.add((iri, RDFS.label, Literal(label)))
            if pkg_stack:
                zone_id = pkg_stack[-1]
                if zone_id in zone_iris:
                    _add_containment(g, NS, zone_iris[zone_id], iri)
        return node_iris[key]

    for line in lines:
        stripped = line.strip()
        if stripped in ("@startuml", "@enduml", ""):
            continue
        if stripped.startswith("'") or stripped.startswith("title"):
            continue

        # Package/zone
        m = pkg_open.match(line)
        if m:
            label = m.group(1)
            alias = m.group(2) or _slug(label)
            pkg_stack.append(alias)
            iri = NS[alias]
            zone_iris[alias] = iri
            g.add((iri, RDF.type, ONTO.Zone))
            g.add((iri, RDFS.label, Literal(label)))
            continue

        if stripped == '}':
            if pkg_stack:
                pkg_stack.pop()
            continue

        # Nodo
        m = node_decl.match(line)
        if m:
            ensure_node(m.group(1), m.group(2))
            continue

        # Arista con labels [Src] --> [Tgt]
        m = edge_pat.match(line)
        if m:
            src_iri = ensure_node(m.group(1))
            tgt_iri = ensure_node(m.group(3))
            label_raw = m.group(4) or ""
            dims = parse_dim_label(label_raw)
            if dims:
                _add_semantic_edge(g, NS, src_iri, tgt_iri, dims, tgt_iri)
            continue

        # Arista entre aliases (packages): alias --> alias
        m = alias_edge.match(line)
        if m:
            src_alias, _, tgt_alias, label_raw = m.group(1), m.group(2), m.group(3), m.group(4) or ""
            src_iri = zone_iris.get(src_alias) or node_iris.get(src_alias)
            tgt_iri = zone_iris.get(tgt_alias) or node_iris.get(tgt_alias)
            if src_iri and tgt_iri:
                dims = parse_dim_label(label_raw)
                if dims:
                    _add_semantic_edge(g, NS, src_iri, tgt_iri, dims, tgt_iri)

    return g


def _add_containment(g: Graph, NS: Namespace, zone_iri: URIRef, node_iri: URIRef):
    eid = NS[f"e_{uuid.uuid4().hex[:8]}"]
    g.add((eid, RDF.type, ONTO.OntologyEdge))
    g.add((eid, ONTO.source, zone_iri))
    g.add((eid, ONTO.target, node_iri))
    g.add((eid, ONTO.contains, node_iri))
    g.add((eid, ONTO.where, node_iri))  # materializar padre


def _add_semantic_edge(g: Graph, NS: Namespace, src: URIRef, tgt: URIRef,
                       dims: dict, tgt_iri: URIRef):
    eid = NS[f"e_{uuid.uuid4().hex[:8]}"]
    g.add((eid, RDF.type, ONTO.OntologyEdge))
    g.add((eid, ONTO.source, src))
    g.add((eid, ONTO.target, tgt))
    for dim, val in dims.items():
        if dim not in DIMS:
            continue
        prop_iri, kind = DIMS[dim]
        if kind == "literal":
            g.add((eid, prop_iri, Literal(val)))
        else:
            sub = SUBPROP_MAP.get(val.lower().replace("-", "_"))
            if sub:
                g.add((eid, sub, tgt_iri))
            g.add((eid, prop_iri, tgt_iri))  # materializar padre


# ─────────────────────────────────────────────
# DUMPER: rdflib Graph → PlantUML
# ─────────────────────────────────────────────

def dump_puml(g: Graph, title: str = "Ontological Graph") -> str:
    lines = ["@startuml", f"title {title}", ""]

    # 1. Packages (zonas)
    zones_q = g.query(SPARQL_PREFIXES + """
        SELECT DISTINCT ?zone ?zone_label WHERE {
            ?zone a onto:Zone ; rdfs:label ?zone_label .
        } ORDER BY ?zone_label
    """)

    child_q = """
        SELECT DISTINCT ?child ?child_label ?ct WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?zone ;
               onto:target ?child ;
               onto:contains ?child .
            ?child rdfs:label ?child_label .
            ?child a ?ct .
        }
    """

    seen_nodes = set()
    zone_subzone_edges = []

    for (zone, zone_label) in zones_q:
        alias = _slug(str(zone).split("#")[-1].split("/")[-1])
        lines.append(f'package "{zone_label}" as {alias} {{')
        seen_nodes.add(str(zone))  # evitar re-declaración en huérfanos
        children = g.query(SPARQL_PREFIXES + child_q, initBindings={"zone": zone})
        for (child, child_label, ct) in children:
            if str(ct) == str(ONTO.Zone):
                child_alias = _slug(str(child).split("#")[-1].split("/")[-1])
                zone_subzone_edges.append((alias, child_alias))
            else:
                child_alias = _slug(str(child).split("#")[-1].split("/")[-1])
                lines.append(f"  [{child_label}] as {child_alias}")
                seen_nodes.add(str(child))
        lines.append("}")
        lines.append("")

    if zone_subzone_edges:
        lines.append("' Jerarquía de zonas")
        for parent_a, child_a in zone_subzone_edges:
            # Usar alias directamente (sin []), PlantUML soporta flechas entre packages
            lines.append(f"{parent_a} --> {child_a} : {{where: contains}}")
        lines.append("")

    # 2. Nodos sin zona (excluye zonas ya declaradas como packages)
    orphan_q = g.query(SPARQL_PREFIXES + """
        SELECT DISTINCT ?node ?label WHERE {
            ?node a ?t ; rdfs:label ?label .
            ?t rdfs:subClassOf* onto:Entity .
            FILTER NOT EXISTS { ?e a onto:OntologyEdge ; onto:contains ?node }
            FILTER NOT EXISTS { ?node a onto:Zone }
        }
    """)
    for node, label in orphan_q:
        if str(node) not in seen_nodes:
            alias = _slug(str(node).split("#")[-1].split("/")[-1])
            lines.append(f"[{label}] as {alias}")
    lines.append("")

    # 3. Relaciones — sub-propiedades para recuperar valores semánticos
    edges_q = g.query(SPARQL_PREFIXES + """
        SELECT DISTINCT ?src_label ?tgt_label ?where_sub ?what_sub ?when ?how ?why WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?src ;
               onto:target ?tgt .
            ?src rdfs:label ?src_label .
            ?tgt rdfs:label ?tgt_label .
            FILTER NOT EXISTS {
                ?e onto:contains ?tgt .
                ?src a onto:Zone .
                FILTER NOT EXISTS { ?e onto:when ?any_w }
                FILTER NOT EXISTS { ?e onto:how  ?any_h }
                FILTER NOT EXISTS { ?e onto:why  ?any_y }
            }
            OPTIONAL {
                ?e ?where_sub ?tgt .
                ?where_sub rdfs:subPropertyOf onto:where .
                FILTER(?where_sub != onto:where)
            }
            OPTIONAL {
                ?e ?what_sub ?tgt .
                ?what_sub rdfs:subPropertyOf onto:what .
                FILTER(?what_sub != onto:what)
            }
            OPTIONAL { ?e onto:when ?when }
            OPTIONAL { ?e onto:how  ?how  }
            OPTIONAL { ?e onto:why  ?why  }
        } ORDER BY ?src_label ?tgt_label
    """)

    for row in edges_q:
        src_lbl, tgt_lbl, whr_sub, wht_sub, whn, how, why = row
        dims = {}
        if whr_sub: dims["where"] = _local(whr_sub)
        if wht_sub: dims["what"]  = _local(wht_sub)
        if whn:     dims["when"]  = str(whn)
        if how:     dims["how"]   = str(how)
        if why:     dims["why"]   = str(why)
        label = dim_label(dims)
        lines.append(f"[{src_lbl}] --> [{tgt_lbl}] : {label}")

    lines.append("")
    lines.append("@enduml")
    return "\n".join(lines)


def _slug(s: str) -> str:
    return re.sub(r'\W+', '_', s.strip().lower()).strip('_')


def _local(iri) -> str:
    s = str(iri)
    return s.split("#")[-1].split("/")[-1]
