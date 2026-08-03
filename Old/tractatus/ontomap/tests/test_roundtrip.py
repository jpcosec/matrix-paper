import pytest
from rdflib import Graph, Namespace, RDF, URIRef
from ontology.edge_model import CanonicalEdge6D, ONTO

def test_rdf_roundtrip_validation():
    """Verify that 6D edge semantics are preserved when moving through RDF."""
    # 1. Source (using full IRIs for stable roundtrip)
    EX = Namespace("http://example.org/")
    original = CanonicalEdge6D(
        source=str(EX.S),
        target=str(EX.T),
        who=str(EX.A),
        what=str(EX.F),
        what_rel="depends_on",
        why="Rationale"
    )
    
    # 2. To RDF
    g = original.to_rdf(base_ns=EX)
    
    # 3. From RDF (Structural validation)
    # Find the edge reification
    edge_uri = g.value(predicate=RDF.type, object=ONTO.OntologyEdge)
    assert edge_uri is not None
    
    # Verify dimensions in RDF
    assert g.value(edge_uri, ONTO.source) == EX.S
    assert g.value(edge_uri, ONTO.target) == EX.T
    assert g.value(edge_uri, ONTO.who) == EX.A
    # Check specific 'what' sub-property
    assert g.value(edge_uri, ONTO.dependsOn) == EX.F
    assert str(g.value(edge_uri, ONTO.why)) == "Rationale"
    
    print("RDF Structural Roundtrip: VALID")

def test_format_preservation():
    """Verify that Turtle serialization preserves the 6D structure."""
    edge = CanonicalEdge6D(source="ex:S", target="ex:T", what="ex:F", what_rel="implements")
    ttl = edge.to_ttl(base_ns=Namespace("http://example.org/"))
    
    assert "implements" in ttl
    assert "OntologyEdge" in ttl
