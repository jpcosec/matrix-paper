import pytest
from pathlib import Path
from rdflib import Graph, Namespace, RDF
from ontology.edge_model import CanonicalEdge6D, ONTO
from cli import DUMPERS

def test_canonical_to_mermaid_projection(tmp_path):
    """Verify that a CanonicalEdge6D can be projected to Mermaid via CLI logic."""
    # 1. Create a 6D edge
    edge = CanonicalEdge6D(
        source="ex:ActorA",
        target="ex:ArtifactB",
        who="ex:AgentX",
        what="ex:FeatureY",
        what_rel="depends_on",
        where="ex:ZoneZ",
        where_rel="contains",
        why="Because it's required"
    )
    
    # 2. Export to RDF Graph
    EX = Namespace("http://example.org/")
    g = edge.to_rdf(base_ns=EX)
    
    # 3. Project to Mermaid using the dumper
    output_file = tmp_path / "projection.mmd"
    dumper = DUMPERS[".mmd"]
    dumper(g, str(output_file))
    
    assert output_file.exists()
    content = output_file.read_text().lower()
    
    # Verify Mermaid content contains semantic links (normalized to lowercase by dump_mermaid)
    assert "actora" in content
    assert "artifactb" in content
    # Note: the current dump_mermaid might only show 'why' or generic labels 
    # based on the reification pattern.
