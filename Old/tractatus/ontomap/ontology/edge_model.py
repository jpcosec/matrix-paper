from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field, field_validator, model_validator
from rdflib import Graph, Namespace, RDF, URIRef, Literal
import uuid

# Semantic Namespace
ONTO = Namespace("http://ontomap.io/ontology#")

# Dimension sub-properties extracted from ontomap/converters/dims.py
WHERE_PROPS = {
    "contains": ONTO.contains,
    "is_located_in": ONTO.isLocatedIn,
    "persists_at": ONTO.persistsAt,
    "belongs_to": ONTO.belongsTo,
}

WHAT_PROPS = {
    "informs": ONTO.informs,
    "organizes": ONTO.organizes,
    "validates": ONTO.validates,
    "depends_on": ONTO.dependsOn,
    "inherits": ONTO.inherits,
    "implements": ONTO.implements,
    "composes": ONTO.composes,
    "refs_by_id": ONTO.refsById,
    "transitions_to": ONTO.transitionsTo,
    "state_update": ONTO.stateUpdate,
}

ALL_SUBPROPS = {**WHERE_PROPS, **WHAT_PROPS}

class CanonicalEdge6D(BaseModel):
    """
    Canonical multidimensional edge model (6D) for OntoMap.
    This model acts as the source of semantic relation truth.
    """
    source: str = Field(..., description="IRI of the source node")
    target: str = Field(..., description="IRI of the target node")
    
    # 6 Dimensions of the edge
    who: Optional[str] = Field(None, description="Who: Context actor or responsible entity (ObjectProperty)")
    what: Optional[str] = Field(None, description="What: The object of the semantic relation (ObjectProperty)")
    where: Optional[str] = Field(None, description="Where: Topology or persistence context (ObjectProperty)")
    when: Optional[str] = Field(None, description="When: Temporal or phase context (DatatypeProperty)")
    how: Optional[str] = Field(None, description="How: Mechanical or technical context (DatatypeProperty)")
    why: Optional[str] = Field(None, description="Why: Rationale or business rule (DatatypeProperty)")
    
    # Semantic specialization
    what_rel: str = Field("what", description="Specific sub-property for 'what' (e.g., 'informs')")
    where_rel: str = Field("where", description="Specific sub-property for 'where' (e.g., 'contains')")
    
    edge_id: Optional[str] = Field(None, description="Optional IRI for the reified edge instance")

    @field_validator("where_rel")
    @classmethod
    def validate_where_rel(cls, v: str) -> str:
        if v != "where" and v not in WHERE_PROPS:
            raise ValueError(f"'{v}' is not a valid 'where' sub-property. Valid: {list(WHERE_PROPS.keys())}")
        return v

    @field_validator("what_rel")
    @classmethod
    def validate_what_rel(cls, v: str) -> str:
        if v != "what" and v not in WHAT_PROPS:
            raise ValueError(f"'{v}' is not a valid 'what' sub-property. Valid: {list(WHAT_PROPS.keys())}")
        return v

    @model_validator(mode="after")
    def check_dimension_consistency(self) -> 'CanonicalEdge6D':
        # If a specific sub-relation is used, the dimension value should ideally be present.
        # However, for 'what' and 'where', if no specific value is given, it might imply the target.
        # But per OntoMap convention in example.ttl, they are often different.
        return self

    def to_rdf(self, graph: Optional[Graph] = None, base_ns: Optional[Namespace] = None) -> Graph:
        """
        Exports the edge to an RDF Graph using the OntoMap reification pattern.
        """
        if graph is None:
            graph = Graph()
            graph.bind("onto", ONTO)
            if base_ns:
                graph.bind("ex", base_ns)
        
        # Determine Edge URI
        if self.edge_id:
            edge_uri = URIRef(self.edge_id)
        else:
            # Fallback to a URN if no ID provided
            edge_uri = URIRef(f"urn:uuid:{uuid.uuid4()}")

        # Base reification
        graph.add((edge_uri, RDF.type, ONTO.OntologyEdge))
        graph.add((edge_uri, ONTO.source, URIRef(self.source)))
        graph.add((edge_uri, ONTO.target, URIRef(self.target)))

        # 6D Dimensions mapping
        if self.who:
            graph.add((edge_uri, ONTO.who, URIRef(self.who)))
        
        if self.what:
            prop = WHAT_PROPS.get(self.what_rel, ONTO.what)
            graph.add((edge_uri, prop, URIRef(self.what)))
            
        if self.where:
            prop = WHERE_PROPS.get(self.where_rel, ONTO.where)
            graph.add((edge_uri, prop, URIRef(self.where)))
            
        if self.when:
            graph.add((edge_uri, ONTO.when, Literal(self.when)))
            
        if self.how:
            graph.add((edge_uri, ONTO.how, Literal(self.how)))
            
        if self.why:
            graph.add((edge_uri, ONTO.why, Literal(self.why)))
            
        return graph

    def to_ttl(self, base_ns: Optional[Namespace] = None) -> str:
        """
        Returns the RDF representation in Turtle format.
        """
        g = self.to_rdf(base_ns=base_ns)
        return g.serialize(format="longturtle")
