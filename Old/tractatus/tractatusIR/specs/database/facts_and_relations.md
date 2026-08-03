# Facts, Relations & Wittgensteinian Format

## Summary
The DB doesn't just store "things" — it stores **projectable propositions**: facts as state assertions, relations as possible connections between objects, and rules as conditions under which connections make sense. Follows Wittgenstein's Sachverhalt: elementary propositions connecting names, with logical form shown through grammar (not asserted as ordinary facts).

## Concepts
- **Fact**: atomic typed proposition `D(c) = v` → `Fact = {subject, predicate, object, context, truth_status}`
- **RelationFact**: external factual relations `R(a,b)` → imports(module, library)
- **DimensionAssignment**: `D(c) = v` → compiles to bit assignment
- **DerivedRelation**: computed from matrices `M_D · M_Dᵀ` → `same_bucket(a,b,D)`
- **Rule**: logical form + constraints (grammar Γ) — NOT stored as ordinary world fact but as **authorizing condition**
- **Sachverhalt**: elementary proposition connecting names/objects
- **Logical form**: `f(x)`, `R(a,b)`, `D(x)=v` — shown by grammar, not asserted

## Three Levels of Relations

### 1. External Factual Relations
Ordinary relational facts:
```yaml
RelationFact:
  id: R_001
  relation: imports
  arguments:
    - from: MODULE_API
      to: LIB_FASTAPI
  context: K_SOFTWARE_ANALYSIS
  logical_form:
    kind: relation_application
    predicate: imports
    args: [a, b]
```

Wittgensteinian form: `imports(LIB_FASTAPI, LIB_PYDANTIC)` → `R(a,b)`

### 2. Dimensional Relations
Feed matrices and bits:
```yaml
DimensionAssignment:
  subject: MODULE_API
  dimension: D_LIBRARY_ROLE
  value: web_framework
  context: K_SOFTWARE_ANALYSIS
```

Compiles to: `D_LIBRARY_ROLE(MODULE_API) = web_framework` → bit assignment

### 3. Internal/Derived Relations
Not stored as primary facts — derived from matrices:
```yaml
DerivedRelation:
  relation: similar_to
  from: LIB_PYDANTIC
  to: LIB_MARSHMALLOW
  because:
    - D_LIBRARY_ROLE.validation_schema
```

Form: `similar_to(a,b) ⇔ ∃D,v: D(a)=v ∧ D(b)=v`

Computed from: `S = M_D · M_Dᵀ` (horizontal co-membership)

## Facts Storage (SQL)

```sql
CREATE TABLE facts (
  id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL REFERENCES concepts(id),
  predicate_id TEXT NOT NULL REFERENCES predicates(id),
  object_id TEXT NOT NULL,
  context_id TEXT NOT NULL REFERENCES contexts(id),
  logical_form JSONB NOT NULL,
  truth_status TEXT NOT NULL,  -- asserted_true | asserted_false | unknown
  source JSONB,
  confidence REAL DEFAULT 1.0,
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE relation_facts (
  id TEXT PRIMARY KEY,
  relation_id TEXT NOT NULL REFERENCES relations(id),
  context_id TEXT NOT NULL REFERENCES contexts(id),
  args JSONB NOT NULL,
  logical_form JSONB NOT NULL,
  truth_status TEXT NOT NULL,
  source JSONB,
  created_at TIMESTAMP DEFAULT now()
);
```

Fact form: `D_PARTE_COMESTIBLE(C_LECHUGA) = hoja`

## Wittgensteinian Format: Three Forms

### 1. Name (Name)
```
a = C_LECHUGA
b = C_ZANAHORIA
h = V_HOJA
r = V_RAIZ
```

Names aren't complete propositions. They're elements.

### 2. Elementary Proposition (Elementarsatz)
```
D(a) = h          D(b) = r
imports(m_api, lib_fastapi)
depends_on(m_service, m_repository)
```

Closest to: `f(x)`, `R(a,b)`, `D(x)=v`

From `tractatus_tree_de`: the elementary proposition affirms the existence of a state of affairs.

### 3. Logical Form / Rule (Gramar Γ)
This should NOT be stored as an ordinary fact about the world. It's the **condition for sense**:

```yaml
LogicalForm:
  id: LF_DIMENSION_ASSIGNMENT
  schema: "D(x) = v"
  constraints:
    - x ∈ domain(D)
    - v ∈ values(D)
    - D applies_to x
```

This is the Wittgensteinian insight: logical form **shows itself** in the correct use of signs. It's not another object in the world.

From `tractatus_tree_de`: certain relations are formal and show themselves, not represented as ordinary propositions.

## Query: "explain patterns and libraries this library has"

Decomposed into projection graph:

```yaml
QueryIR:
  raw: "explain patterns and libraries this library has"
  intent: explain
  target:
    type: software_artifact
    ref: THIS_LIBRARY
  requested_views:
    - architecture_patterns
    - dependencies
    - library_roles
    - relation_graph
  context: K_SOFTWARE_ANALYSIS
```

Compiles to plan:
```yaml
ProjectionPlan:
  root: THIS_LIBRARY
  dimensions:
    - D_ARCHITECTURAL_PATTERN
    - D_LIBRARY_ROLE
    - D_DEPENDENCY_TYPE
    - D_MODULE_ROLE
  relations:
    - imports
    - depends_on
    - uses_pattern
    - defines_module
    - calls
    - configures
```

## Query Graph Decomposition

```
QUERY
├── target: THIS_LIBRARY
├── ask: explain
├── view: patterns
│   ├── dimension: D_ARCHITECTURAL_PATTERN
│   └── relation: uses_pattern
│       └── evidence: files/classes/modules
└── view: libraries
    ├── relation: imports / depends_on
    ├── dimension: D_LIBRARY_ROLE
    └── evidence: pyproject/package.json/import graph
```

In Wittgensteinian terms: the query projects the target onto multiple dimensions/relations to build a picture (Bild) of the library.

## Iterative Projection Recovery

```pseudo
answer_query(query_text, db):
  ir = parse_nl_to_query_ir(query_text)
  K = resolve_context(ir)
  validate_query_ir(ir, K)

  projections = []
  for requested_view in graph.requested_views:
    projection_schema = resolve_projection_schema(requested_view, K)
    facts = retrieve_relevant_facts(
      target=ir.target,
      dimensions=projection_schema.dimensions,
      relations=projection_schema.relations
    )
    compiled = compile_facts_to_signatures(facts, K)
    validated = validate_signatures(compiled, K)
    projection = build_projection(validated, projection_schema)
    projections.append(projection)

  relations = derive_horizontal_and_structural_relations(projections)
  explanation = verbalize(projections, relations)
  return explanation
```

Concrete example:
```pseudo
explain_library(target, K_SOFTWARE_ANALYSIS):
  deps = traverse_relation(target, relation=depends_on/imports)
  dep_roles = project_all(
    concepts=deps,
    dimensions=[D_LIBRARY_ROLE, D_DEPENDENCY_TYPE]
  )

  patterns = project(
    concept=target,
    dimensions=[D_ARCHITECTURAL_PATTERN, D_MODULE_ORGANIZATION]
  )

  modules = traverse_relation(target, relation=defines_module)
  module_roles = project_all(
    concepts=modules,
    dimensions=[D_MODULE_ROLE, D_LAYER]
  )

  evidence = collect_evidence(facts used)
  return compose_explanation(patterns, deps, dep_roles, modules, evidence)
```

## Derived Relations Storage (Optional Materialization)

```sql
CREATE TABLE derived_relations (
  id TEXT PRIMARY KEY,
  relation_type TEXT,  -- same_bucket | similar_to | contrasts_with
  from_id TEXT REFERENCES concepts(id),
  to_id TEXT REFERENCES concepts(id),
  context_id TEXT REFERENCES contexts(id),
  basis JSONB NOT NULL,  -- {"dimension": "D_LIBRARY_ROLE", "value": "web_framework"}
  score REAL,
  generated_at TIMESTAMP DEFAULT now()
);
```

Example:
```yaml
derived_relations:
  - relation_type: same_role_as
    from: LIB_PYDANTIC
    to: LIB_MARSHMALLOW
    context: K_SOFTWARE_ANALYSIS
    basis:
      dimension: D_LIBRARY_ROLE
      value: validation_schema
```

## Key Wittgensteinian Distinction

| Type | Stored As | Example | Logical Status |
|------|----------|---------|---------------|
| **Fact** | Ordinary assertion | `D_PARTE(lechuga)=hoja` | Makes sense, can be true/false |
| **RelationFact** | Ordinary assertion | `imports(api, fastapi)` | Makes sense, can be true/false |
| **DimensionAssignment** | Fact with typed predicate | `D_LIBRARY_ROLE(fastapi)=web_framework` | Makes sense under grammar |
| **DerivedRelation** | Computed on-demand | `similar_to(pydantic, marshmallow)` | Shown by matrix co-membership |
| **Rule/LogicalForm** | Grammar Γ, NOT fact | `D(x)=v requires x∈domain(D), v∈values(D)` | **Shows itself**, not asserted |

The crucial Wittgensteinian point: **rules of sense are not facts in the world**. They're the scaffolding that makes facts possible.

From `tractatus_tree_de`: the logical form of a proposition cannot be represented within the system — it shows itself.

## Example: "explain patterns and libraries"

Input: `"explain patterns and libraries this library has"`

Parser:
```yaml
ProjectionIR:
  intent: explain
  context: K_SOFTWARE_ANALYSIS
  constraints:
    - dimension: D_ARCHITECTURAL_PATTERN
    - relation: imports / depends_on
    - dimension: D_LIBRARY_ROLE
  signature_type: explain
```

Compiler:
```yaml
bits: [for D_ARCH_PATTERN, D_LIB_ROLE, D_DEP_TYPE...]
valid_mask: [1,1,1,...]
```

Validator:
```yaml
status: SINNVOLL
denotation: {patterns, deps, roles}
```

Executor:
```yaml
explanation:
  "The library uses Repository pattern and Service Layer.
   Uses FastAPI as web framework, Pydantic for validation/schemas,
   SQLAlchemy as ORM and pytest for testing."
```

## How Relations Are Stored: Summary

```
Facts = states of things affirmed
  ↓
RelationFacts = possible forms of connection between objects
  ↓
DimensionAssignments = feed matrices/bits
  ↓
DerivedRelations = computed from signatures/matrices
  ↓
Rules (Γ) = authorize what connections make sense
  (NOT stored as facts — they're the enabling conditions)
```

Compact Wittgensteinian formulation:
> Facts store what states of things are affirmed.
> Relations store the possible forms of connection.
> Rules (grammar Γ) decide what connections make sense.
> Projection recovers, filters, and reorganizes those facts according to the query's context.

## References
- turn-42.md (facts as Sachverhalt, 3 relation levels, Wittgensteinian format: Name/ElementaryProposition/LogicalForm, query graph decomposition)

## Version Notes
- Turn 42: facts stored as elementary propositions D(c)=v; 3 relation types (external/dimensional/derived); Wittgensteinian distinction: rules Γ show themselves, aren't ordinary facts
