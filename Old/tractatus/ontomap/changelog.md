# Changelog

## 2026-05-01

- resolved task `004-implement-canonical-projection`: 004-implement-canonical-projection

# Changelog - ontomap

## [0.1.2] - 2026-05-24

### Added
- Defined the projection contract in `ontomap/ontology/projection.py`.
- Implemented `ProjectionConfig`, `ProjectedGraph`, and `ProjectionFilter` Pydantic models.
- Added support for semantic `Lens` types (Who-What, Where-What, etc.) and multiple output formats (Mermaid, PlantUML, TTL, etc.).

## [0.1.1] - 2026-05-23

### Added
- Created `ontomap/desk/fixtures/ecosystem_6d_map.mmd` fixture representing the 6D ecosystem ontology relations.
- Mapped relations between `repopackage`, `kgdb`, and `ontology` using the 6D dimension model.

## [0.1.0] - 2026-05-22

### Added
- Defined `CanonicalEdge6D` Pydantic model in `ontomap/ontology/edge_model.py`.
- Implemented multidimensional (6D) edge reification pattern matching `core.ttl`.
- Added validation for `where` and `what` sub-properties.
- Added RDF/TTL export support using `rdflib`.
- Added `ontomap/ontology/__init__.py` to enable package structure.
