"""
Mermaid ↔ OWL Graph converter.

Formato esperado: graph TD con subgraph para zonas,
y labels de aristas en formato {dim: value}.
"""
import re
import uuid
from rdflib import Graph, Namespace, Literal, RDF, RDFS, URIRef

from .dims import ONTO, DIMS, SUBPROP_MAP, NODE_TYPE_MAP, parse_dim_label, dim_label

WS = Namespace("http://ontomap.io/instance#")

SPARQL_PREFIXES = """
PREFIX onto: <http://ontomap.io/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

# ─────────────────────────────────────────────
# LOADER: Mermaid → rdflib Graph
# ─────────────────────────────────────────────

def _slug(s: str) -> str:
    return re.sub(r'\W+', '_', s.strip().lower()).strip('_')


def _infer_node_class(node_id: str, subgraph_label: str | None) -> URIRef:
    """Infiere la clase OWL de un nodo según el contexto del subgraph."""
    if subgraph_label:
        sl = subgraph_label.lower()
        if "actor" in sl:
            return ONTO.Actor
        if "zone" in sl:
            return ONTO.Zone
    # Default: Artifact
    return ONTO.Artifact


def load_mermaid(text: str, base_ns: str = str(WS)) -> Graph:
    g = Graph()
    g.parse("ontology/core.ttl", format="turtle")

    NS = Namespace(base_ns)
    lines = text.splitlines()

    node_iris: dict[str, URIRef] = {}      # mermaid_id → IRI
    node_labels: dict[str, str] = {}       # mermaid_id → label
    current_subgraph: str | None = None    # label del subgraph activo
    subgraph_stack: list[str] = []
    zone_iris: dict[str, URIRef] = {}      # subgraph_id → IRI de zona
    node_zone: dict[str, str] = {}         # mermaid_id → subgraph_id

    edge_pattern = re.compile(
        r'^\s*(\w+)\s*(-\.->|-->|\.\.>|==>)\|?"?([^"|]*)\"?\|?\s*(\w+)'
    )
    node_pattern = re.compile(
        r'^\s*(\w+)\[([^\]]+)\]'           # ID[Label]
        r'|\s*(\w+)\(\[([^\]]+)\]\)'       # ID([Label])
    )
    subgraph_open = re.compile(
        r'^\s*subgraph\s+(\w+)\s*\[?"?([^"\]]*)"?\]?'
    )

    def ensure_node(mid: str, label: str | None = None, zone_id: str | None = None) -> URIRef:
        if mid not in node_iris:
            iri = NS[_slug(mid)]
            node_iris[mid] = iri
            lbl = label or mid
            node_labels[mid] = lbl
            cls = _infer_node_class(mid, subgraph_label=current_subgraph)
            g.add((iri, RDF.type, cls))
            g.add((iri, RDFS.label, Literal(lbl)))
        if zone_id and zone_id in zone_iris and mid not in node_zone:
            node_zone[mid] = zone_id
            _add_containment(zone_iris[zone_id], node_iris[mid])
        return node_iris[mid]

    def _add_containment(zone_iri: URIRef, node_iri: URIRef):
        edge_iri = NS[f"e_{uuid.uuid4().hex[:8]}"]
        g.add((edge_iri, RDF.type, ONTO.OntologyEdge))
        g.add((edge_iri, ONTO.source, zone_iri))
        g.add((edge_iri, ONTO.target, node_iri))
        g.add((edge_iri, ONTO.contains, node_iri))
        g.add((edge_iri, ONTO.where, node_iri))  # materializar padre

    def _add_edge(src_iri: URIRef, tgt_iri: URIRef, dims: dict):
        edge_iri = NS[f"e_{uuid.uuid4().hex[:8]}"]
        g.add((edge_iri, RDF.type, ONTO.OntologyEdge))
        g.add((edge_iri, ONTO.source, src_iri))
        g.add((edge_iri, ONTO.target, tgt_iri))
        for dim, val in dims.items():
            if dim not in DIMS:
                continue
            prop_iri, kind = DIMS[dim]
            if kind == "literal":
                g.add((edge_iri, prop_iri, Literal(val)))
            else:
                sub = SUBPROP_MAP.get(val.lower().replace("-", "_"))
                if sub:
                    g.add((edge_iri, sub, tgt_iri))
                # Materializar propiedad padre para SPARQL sin razonador
                g.add((edge_iri, prop_iri, tgt_iri))

    for line in lines:
        stripped = line.strip()

        # Ignorar comentarios y directivas
        if stripped.startswith('%%') or stripped in ('graph TD', 'graph LR', ''):
            continue

        # Apertura de subgraph
        m = subgraph_open.match(line)
        if m:
            sg_id = m.group(1)
            sg_label = (m.group(2) or sg_id).strip().strip('"')
            subgraph_stack.append(sg_id)
            current_subgraph = sg_label
            zone_iri = NS[_slug(sg_id)]
            zone_iris[sg_id] = zone_iri
            g.add((zone_iri, RDF.type, ONTO.Zone))
            g.add((zone_iri, RDFS.label, Literal(sg_label)))
            continue

        if stripped == 'end':
            if subgraph_stack:
                subgraph_stack.pop()
            current_subgraph = None
            continue

        # Declaración de nodo explícita
        m = node_pattern.match(line)
        if m:
            mid = m.group(1) or m.group(3)
            lbl = m.group(2) or m.group(4) or mid
            zone_id = subgraph_stack[-1] if subgraph_stack else None
            ensure_node(mid, lbl, zone_id)
            continue

        # Arista
        m = edge_pattern.match(line)
        if m:
            src_id, arrow, label_raw, tgt_id = m.group(1), m.group(2), m.group(3), m.group(4)
            zone_id = subgraph_stack[-1] if subgraph_stack else None
            src_iri = ensure_node(src_id, zone_id=zone_id)
            tgt_iri = ensure_node(tgt_id, zone_id=zone_id)
            dims = parse_dim_label(label_raw)
            if dims:
                _add_edge(src_iri, tgt_iri, dims)

    return g


# ─────────────────────────────────────────────
# DUMPER: rdflib Graph → Mermaid
# ─────────────────────────────────────────────

def dump_mermaid(g: Graph, direction: str = "TD") -> str:
    lines = [f"graph {direction}", ""]

    # 1. Zonas con sus nodos (subgraphs)
    zones_q = g.query(SPARQL_PREFIXES + """
        SELECT DISTINCT ?zone ?zone_label WHERE {
            ?zone a onto:Zone ;
                  rdfs:label ?zone_label .
        } ORDER BY ?zone_label
    """)

    zone_children_q = """
        SELECT DISTINCT ?child ?child_label ?child_type WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?zone ;
               onto:target ?child ;
               onto:contains ?child .
            ?child rdfs:label ?child_label .
            ?child a ?child_type .
        }
    """
    # Sub-zonas se renderizan como relaciones separadas (Mermaid no soporta subgraph anidado)
    zone_subzones_q = """
        SELECT DISTINCT ?subzone ?subzone_label WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?zone ;
               onto:target ?subzone ;
               onto:contains ?subzone .
            ?subzone a onto:Zone ;
                     rdfs:label ?subzone_label .
        }
    """

    seen_nodes = set()
    zone_subzone_edges = []  # (zone_id, subzone_id) para agregar al final

    for (zone, zone_label) in zones_q:
        zone_id = _mermaid_id(zone)
        lines.append(f'subgraph {zone_id} ["{zone_label}"]')
        children = g.query(SPARQL_PREFIXES + zone_children_q,
                           initBindings={"zone": zone})
        for (child, child_label, child_type) in children:
            child_id = _mermaid_id(child)
            if str(child_type) == str(ONTO.Zone):
                zone_subzone_edges.append((zone_id, child_id))
            else:
                lines.append(f"    {child_id}[{child_label}]")
                seen_nodes.add(str(child))
        lines.append("end")
        lines.append("")

    # Sub-zonas como flechas (Mermaid no soporta subgraph anidado)
    if zone_subzone_edges:
        lines.append("%% Jerarquía de zonas")
        for parent_id, child_id in zone_subzone_edges:
            lines.append(f'{parent_id} -->|"{{where: contains}}"| {child_id}')
        lines.append("")

    # 2. Nodos sin zona
    orphan_q = g.query(SPARQL_PREFIXES + """
        SELECT DISTINCT ?node ?label ?type WHERE {
            ?node a ?type ;
                  rdfs:label ?label .
            ?type rdfs:subClassOf* onto:Entity .
            FILTER NOT EXISTS {
                ?e a onto:OntologyEdge ;
                   onto:contains ?node .
            }
        } ORDER BY ?type ?label
    """)
    orphans = [(n, l, t) for n, l, t in orphan_q if str(n) not in seen_nodes]
    if orphans:
        lines.append("%% Nodos sin zona")
        for node, label, _ in orphans:
            lines.append(f"{_mermaid_id(node)}[{label}]")
        lines.append("")

    # 3. Aristas — excluye solo las de topología pura zona→nodo sin otras dims
    edges_q = g.query(SPARQL_PREFIXES + """
        SELECT DISTINCT ?e ?src ?tgt ?where_sub ?what_sub ?when ?how ?why WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?src ;
               onto:target ?tgt .
            FILTER NOT EXISTS {
                ?e onto:contains ?tgt .
                ?src a onto:Zone .
                ?tgt a onto:Zone .
                FILTER NOT EXISTS { ?e onto:when ?any_when }
                FILTER NOT EXISTS { ?e onto:how  ?any_how  }
                FILTER NOT EXISTS { ?e onto:why  ?any_why  }
            }
            FILTER NOT EXISTS {
                ?e onto:contains ?tgt .
                ?src a onto:Zone .
                ?tgt a ?tgt_type .
                FILTER(?tgt_type != onto:Zone)
                FILTER NOT EXISTS { ?e onto:when ?any_when }
                FILTER NOT EXISTS { ?e onto:how  ?any_how  }
                FILTER NOT EXISTS { ?e onto:why  ?any_why  }
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
        } ORDER BY ?src ?tgt
    """)

    lines.append("%% Relaciones")
    for row in edges_q:
        _, src, tgt, whr_sub, wht_sub, whn, how, why = row
        src_id = _mermaid_id(src)
        tgt_id = _mermaid_id(tgt)
        dims = {}
        if whr_sub: dims["where"] = _local(whr_sub)
        if wht_sub: dims["what"]  = _local(wht_sub)
        if whn:     dims["when"]  = str(whn)
        if how:     dims["how"]   = str(how)
        if why:     dims["why"]   = str(why)
        label = dim_label(dims)
        lines.append(f'{src_id} -->|"{label}"| {tgt_id}')

    return "\n".join(lines)


def _mermaid_id(iri) -> str:
    return _slug(str(iri).split("#")[-1].split("/")[-1])


def _local(iri) -> str:
    s = str(iri)
    return s.split("#")[-1].split("/")[-1]
