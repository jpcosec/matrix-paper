# Fact Relation Rule

Source anchors:

- `specs/concepts/categorization.md`
- `specs/database/facts_and_relations.md`

## Early Structural Rule

The source corpus first establishes that the system should be modeled as a graph with typed relationships rather than a single hierarchy.

Examples preserved from the early corpus:

- `zanahoria -> es_un -> planta`
- `zanahoria -> puede_funcionar_como -> comida`

This preserves the rule:

`what it is` != `what it is used for` != `what state it is in`

## Later Fact Model

The later database layer distinguishes:

- `Fact`: typed proposition such as `D(c) = v`
- `RelationFact`: external relation such as `R(a, b)`
- `DimensionAssignment`: dimension-value assertion compiled to bits
- `DerivedRelation`: relation computed from signatures or matrices
- `Rule` or `LogicalForm`: authorizing condition for sense, not an ordinary world fact

## Canonical Role

This atom should hold the distinction between world assertions and grammar conditions.
