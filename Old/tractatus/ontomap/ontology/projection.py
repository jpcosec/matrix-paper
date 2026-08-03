from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
from enum import Enum

class ProjectionFormat(str, Enum):
    """Supported output formats for graph projections."""
    MERMAID = "mermaid"
    PLANTUML = "plantuml"
    TTL = "ttl"
    JSON = "json"
    DOT = "dot"

class LensType(str, Enum):
    """Predefined semantic lenses for viewing the 6D edge model."""
    WHO_WHAT = "who-what"
    WHERE_WHAT = "where-what"
    DEPENDENCY = "dependency"
    STATE_MACHINE = "state-machine"
    AST = "ast"
    UML_CLASS = "uml-class"
    UML_SEQUENCE = "uml-sequence"
    CUSTOM = "custom"

class ProjectionFilter(BaseModel):
    """
    Criteria for filtering nodes and edges during projection.
    Used to extract subgraphs from the global knowledge base.
    """
    node_types: Optional[List[str]] = Field(
        None, description="Filter nodes by type (e.g., actor, zone, artifact, process)"
    )
    edge_dimensions: Optional[Dict[str, List[str]]] = Field(
        None, description="Filter edges by dimension values (e.g., {'what': ['depends_on']})"
    )
    source_ids: Optional[List[str]] = Field(
        None, description="Whitelist of source node IDs"
    )
    target_ids: Optional[List[str]] = Field(
        None, description="Whitelist of target node IDs"
    )

class ProjectionConfig(BaseModel):
    """
    Configuration for a projection operation.
    Defines how the multidimensional graph should be filtered and styled.
    """
    format: ProjectionFormat = Field(
        default=ProjectionFormat.MERMAID, description="Target serialization format"
    )
    lens: LensType = Field(
        default=LensType.CUSTOM, description="Predefined semantic lens to apply"
    )
    filters: Optional[ProjectionFilter] = Field(
        None, description="Specific filters to refine the projection"
    )
    style_map: Dict[str, Any] = Field(
        default_factory=dict, description="Visual style configuration for nodes and edges"
    )

class ProjectedGraph(BaseModel):
    """
    The result of a projection operation.
    Contains the filtered graph data and the resulting serialized output.
    """
    nodes: List[Dict[str, Any]] = Field(..., description="The set of nodes in the projection")
    edges: List[Dict[str, Any]] = Field(..., description="The set of edges in the projection")
    config: ProjectionConfig = Field(..., description="The configuration that produced this projection")
    output: Optional[str] = Field(
        None, description="The serialized graph string (e.g., Mermaid code)"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Execution metadata (timing, stats, etc.)"
    )
