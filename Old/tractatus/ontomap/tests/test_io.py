import pytest
from pathlib import Path
from rdflib import Graph
from cli import LOADERS, DUMPERS

def test_ttl_to_mermaid_io(tmp_path):
    """Verify that we can load TTL and dump Mermaid."""
    ttl_content = """
    @prefix onto: <http://ontomap.io/ontology#> .
    @prefix ex: <http://example.org/> .
    
    ex:Edge1 a onto:OntologyEdge ;
        onto:source ex:Node1 ;
        onto:target ex:Node2 ;
        onto:why "Test" .
    """
    ttl_file = tmp_path / "test.ttl"
    ttl_file.write_text(ttl_content)
    
    g = LOADERS[".ttl"](str(ttl_file))
    assert len(g) > 0
    
    mmd_file = tmp_path / "test.mmd"
    DUMPERS[".mmd"](g, str(mmd_file))
    
    assert mmd_file.exists()
    assert "node1" in mmd_file.read_text().lower()
