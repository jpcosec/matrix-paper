# Mathematical Formalization

## Summary
The system admits mathematical formalization: the core is a contextualized boolean algebra containing an abelian group under XOR, a boolean semiring for matrices, and a lattice of partitions induced by dimensions. The system is NOT just computations on bits — it requires a **grammar of sense** that authorizes which bits are meaningful. **15 additional formalizations are still needed** (Turn 44).

## Concepts
- 𝔹ⁿ = {0,1}ⁿ — space of binary signatures`
- `(𝔹ⁿ, XOR)` — abelian group of bit differences/contrasts`
- `(𝔹ⁿ, AND, OR, NOT)` — boolean algebra`
- `WF_K ⊆ 𝔹ⁿ` — well-formed signatures (not necessarily a subgroup)`
- `(𝒫(U), ∩, ∪, complement)` — set algebra of denotations`
- `({0,1}, OR, AND)` — boolean semiring for matrix multiplication`
- `Partitions(U)` — lattice of partitions induced by dimensions`
- `𝓒 = (U, 𝔹ⁿ, K, WF_K, ⟦·⟧_K)` — full system tuple`
- **𝓓 = (C, K, D, V, B, Γ, Σ, Ω, I)** — complete system with sense grammar Γ, typed signatures Σ, operations Ω, indices I`
- **Three signature types**: ConceptSignature, QuerySignature, ContrastSignature`
- **Typed operations**: `contrast: Concept × Concept → Contrast`, `filter_and: Query × Query → Query`

## The Group: (𝔹ⁿ, XOR)

The full bit space under XOR **does form an abelian group**:

### Properties
```
Closure:       x XOR y ∈ 𝔹ⁿ
Associativity:  (x XOR y) XOR z = x XOR (y XOR z)
Identity:       x XOR 0 = x
Inverse:        x XOR x = 0
Commutativity:  x XOR y = y XOR x
```

### Semantic Interpretation
```
x XOR y = contrast/difference between x and y
diff(a, b) = a XOR b  → bits where they differ
```

### Moving Between Concepts
```
a XOR (a XOR b) = b
```
Read as: "concept_a + contrast = concept_b"

### Important Limitation
While `(𝔹ⁿ, XOR)` is a group, **WF_K** (well-formed signatures) is **not necessarily a subgroup**:
```
One-hot dimension D = {hoja, raiz, tallo}
Valid: [1,0,0], [0,1,0], [0,0,1]
[1,0,0] XOR [0,1,0] = [1,1,0] ∉ WF_K  (violates one-hot!)
```
The group exists on the full space, but doesn't preserve semantic restrictions.

## Boolean Algebra: (𝔹ⁿ, AND, OR, NOT, 0, 1)

The full signature space forms a **boolean algebra**:

```
x AND y   = shared features / intersection
x OR y    = union of possibilities
NOT x     = complement within local space
x XOR y   = symmetric difference / contrast
```

Operations correspond to set operations on denotations:
```
⟦x AND y⟧_K = ⟦x⟧_K ∩ ⟦y⟧_K
⟦x OR y⟧_K  = ⟦x⟧_K ∪ ⟦y⟧_K
⟦NOT x⟧_K   = U \ ⟦x⟧_K
```

## Well-Formed Signatures: WF_K ⊆ 𝔹ⁿ

Defined by context K's grammatical rules:
```
WF_K = {x ∈ 𝔹ⁿ | each one-hot dimension has exactly one 1,
                      each boolean dimension has value in {0,1},
                      applicable bits respect valid_mask}
```

Example (one-hot D_PARTE with 3 values):
```
WF_K = {[1,0,0], [0,1,0], [0,0,1]}
```
Note: WF_K is a **language of valid signatures**, not closed under XOR.

## Set Algebra: (𝒫(U), ∩, ∪, \)

Each signature denotes a subset of local universe:
```
⟦x⟧_K ⊆ U
```

This is a **boolean algebra of sets**:
```
⟦x AND y⟧ = ⟦x⟧ ∩ ⟦y⟧
⟦x OR y⟧  = ⟦x⟧ ∪ ⟦y⟧
⟦NOT x⟧   = U \ ⟦x⟧
```

Sense conditions:
```
sinnvoll(x,K)  ⇔ 0 < |⟦x⟧_K| < |U|
sinnlos_taut(x,K) ⇔ ⟦x⟧_K = U
sinnlos_contra(x,K) ⇔ ⟦x⟧_K = ∅
unsinnig(x,K) ⇔ x ∉ WF_K
```

## Boolean Semiring: ({0,1}, OR, AND)

Matrices live in the **boolean semiring**:
```
Sum (⊕) = OR
Product (⊗) = AND
```

Matrix multiplication:
```
S = M_D · M_Dᵀ
S[i,j] = OR_k(M_D[i,k] AND M_D[j,k])
```
Interpretation: `S[i,j] = 1` iff concepts i and j share a value in dimension D.

## Lattice of Partitions: Partitions(U)

Each dimension D induces a partition π_D of U:
```
π_D = {{c | D(c) = v₁}, {c | D(c) = v₂}, ...}
```

Refinement order: π₁ ≤ π₂ if π₂ refines π₁ (smaller buckets).

The set of all partitions **Partitions(U)** forms a **lattice**:
- Meet (∧): coarsest common refinement
- Join (∨): finest common coarsening

The search tree is a **trajectory in the partition lattice**:
```
{lechuga, zanahoria, apio, espinaca}
  → {lechuga, espinaca} | {zanahoria} | {apio}    (by D_PARTE)
    → {lechuga} | {espinaca}                          (by D_ESTRUCTURA)
```

## Full System Tuple: 𝓒 = (U, 𝔹ⁿ, K, WF_K, M_K, ⟦·⟧_K)

Complete formal definition:
```
𝓒 = (U, B, K, WF, ⟦·⟧)
where:
  U        = finite set of concepts
  B = 𝔹ⁿ      = space of binary signatures
  K        = context (universe, dimensions, values, applicability, sense_mask)
  WF ⊆ B        = well-formed signatures
  ⟦·⟧ : WF → 𝒫(U)  = denotation function
```

### Context K Components
```
K = (U, D, V, A, S, R)
  U = local universe
  D = sequence/tree of dimensions
  V = possible values per dimension
  A = applicability conditions per dimension
  S = sense_mask (what's meaningful in this context)
  R = well-formedness rules
```

### Projection
```
P_K : Expression → 𝔹ⁿ
sinnvoll(e,K) ⇔ P_K(e) ∈ WF ∧ 0 < |⟦P_K(e)⟧| < |U|
```

## Homomorphism

Ideally, denotation preserves operations:
```
⟦x AND y⟧_K = ⟦x⟧_K ∩ ⟦y⟧_K
⟦x OR y⟧_K  = ⟦x⟧_K ∪ ⟦y⟧_K
⟦NOT x⟧_K   = U \ ⟦x⟧_K
```

When this holds, `⟦·⟧_K` is a **homomorphism of boolean algebras** from expressions to subsets of U.

## Masks as Additional Structure

The system has 4 masks, all in 𝔹ⁿ:
```
valid_mask        → what applies to concept (ontological)
sense_mask        → what has sense in context/task
discriminative_mask → what separates candidates now
observed_mask     → what has been measured
```

Effective mask: `m = valid AND sense AND discriminative AND observed`

Effective signature: `eff(x) = x AND m`

## Summary: What Mathematical Structure Is This?

| Component | Structure |
|-----------|-----------|
| Full bit space 𝔹ⁿ under XOR | **Abelian group** |
| Full bit space under AND, OR, NOT | **Boolean algebra** |
| Well-formed WF_K | **Typed language** (not closed under XOR) |
| Denotations 𝒫(U) | **Boolean algebra of sets** |
| Matrices over {0,1} | **Boolean semiring** |
| Partitions(U) | **Lattice** (retículo) |
| Full system 𝓒 | **Contextualized boolean algebra + masks + denotation homomorphism** |

## Key Formal Statement

> The system is not primarily a group. It is a **contextualized boolean algebra** containing an abelian group of contrasts under XOR, a boolean semiring for projection matrices, and a lattice of partitions induced by discriminative dimensions.

---

## 15 Missing Formalizations (Turn 44)

### 1. Identity and Equivalence

Formalize when two things are "the same" within the system.

```
same_concept(a, b)    ⇔  core identity (same C_ID)
alias_of(a, b)         ⇔  surface forms mapping to same concept
translation_of(a, b)  ⇔  cross-linguistic equivalents
subconcept_of(a, b)    ⇔  hierarchical subtype relation
projection_equivalent(a, b, K) ⇔  same signature under context K
```

Example:
```
C_LECHUGA:
  aliases: ["lechuga", "lettuce"]
  scientific_name: "Lactuca sativa"
  same_as: [WIKIDATA_Q83193]
```

Without this, the parser may duplicate concepts.

### 2. Minimal Type System

Ontological types for system entities and domain entities.

**System types:**
```
Concept, Dimension, Value, Context, Fact, Relation, Rule, Signature, Query, Source, Evidence
```

**Domain types (example: software):**
```
library, module, function, class, file, pattern, dependency
```

**Type hierarchy:**
```
T_LIBRARY → T_SOFTWARE_ARTIFACT → T_ENTITY
```

Type constraints enable sense validation:
```
imports(x, y) is sinnvoll ⇔ x ∈ {module, package, project} ∧ y ∈ {library, module, package}
```

### 3. Predicate Arity and Signature

Formal logical signature for each relation/predicate.

```
Predicate:
  id: imports
  arity: 2
  args:
    0: {role: importer, allowed_types: [module, package, project]}
    1: {role: imported, allowed_types: [library, module, package]}
```

Validation:
```
well_formed(imports(PROJECT, LIB_FASTAPI)) → sinnvoll
well_formed(imports(lechuga, raíz))        → unsinnig (type mismatch)
```

Arity is separate from truth value — well-formedness ≠ truth.

### 4. Dimension vs Relation Distinction

A dimension is a **functional predicate** with special restrictions.

```
Dimension ⊂ Predicate
  functional: true
  cardinality: exactly_one | zero_or_one | many
```

| Type | Restriction | Example |
|------|-------------|---------|
| one-hot | ∀c, exactly one v: D(c)=v | D_PARTE_COMESTIBLE |
| multi-hot | ∀c, subset of values | D_DIETARY_TAGS |
| optional | value may be unobserved | D_HARVEST_SEASON |

General relations are not functional:
```
imports(a, b)     → not functional (can have multiple)
similar_to(a, b)  → symmetric, not functional
calls(a, b)       → many-to-many
```

### 5. Truth, Epistemic, and Semantic States

Separate three distinct state dimensions:

**Truth status** (what is asserted):
```
asserted_true, asserted_false, contradicted, unknown
```

**Epistemic status** (how we know):
```
observed, inferred, assumed, missing, disputed
```

**Semantic status** (Wittgensteinian sense):
```
sinnvoll, sinnlos, unsinnig, outside_context, not_applicable
```

Example:
```
Fact:
  expression: D_LIBRARY_ROLE(LIB_FASTAPI)=web_framework
  truth_status: asserted_true
  epistemic_status: inferred
  semantic_status: sinnvoll
  confidence: 0.91
```

### 6. Provenance / Evidence

Formalize origin of each fact.

**Software evidence:**
```
Evidence:
  id: EV_001
  source_type: file
  path: pyproject.toml
  span: {line_start: 12, line_end: 17}
  extractor: dependency_parser
```

**Text evidence:**
```
Evidence:
  source_type: document
  quote_span: "lechuga es una verdura de hoja"
  confidence: 0.85
```

Fact links to evidence:
```
Fact:
  imports(PROJECT, LIB_FASTAPI)
  evidence: [EV_001, EV_002]
```

Without evidence, the system becomes an invented ontology.

### 7. Inference Rules

Logical, heuristic, statistical, and LLM-based inference.

```
InferenceRule:
  id: R_WEB_CAPABILITY
  type: logical
  when:
    - relation: imports
      args: [PROJECT, X]
    - dimension: D_LIBRARY_ROLE
      subject: X
      value: web_framework
  then:
    - relation: uses_capability
      args: [PROJECT, web_api]
```

Example dimensional inference:
```
D_PARTE_COMESTIBLE(lechuga)=hoja
D_PARTE_COMESTIBLE(espinaca)=hoja
⇒ same_bucket(lechuga, espinaca, D_PARTE_COMESTIBLE.hoja)
```

Separate inference types:
- `logical`: truth-preserving rules
- `heuristic`: domain-specific patterns
- `statistical`: probability-based
- `llm`: model-generated

### 8. Update Operations

How the knowledge base changes over time.

**Minimum operations:**
```
add_concept(c)
merge_concepts(c1, c2)
add_dimension(D)
add_value(D, v)
add_fact(f)
retract_fact(f)
update_context(K)
rebuild_signature(c, K)
recompute_indices()
refine_collision(c1, c2)
materialize_derived_relations()
```

Update algorithm:
```
add_fact(f):
  validate(f)              // check well-formedness
  store(f)                 // persist fact
  update_signature(f.subject, f.context)
  update_matrix(f.dimension, f.context)
  update_indices()
  detect_collisions()
```

Without this, the model is static, not a living system.

### 9. Contradiction Handling

What happens when contradictory facts arrive.

Example contradiction:
```
F_001: D_PARTE_COMESTIBLE(lechuga)=hoja
F_002: D_PARTE_COMESTIBLE(lechuga)=raíz
```

Resolution strategies:
1. Reject the second fact (strict one-hot)
2. Store as contradiction object
3. Version both with provenance
4. Resolve by confidence/provenance

```
Contradiction:
  dimension: D_PARTE_COMESTIBLE
  subject: C_LECHUGA
  conflicting_facts: [F_001, F_002]
  rule_violated: one_hot_exactly_one
  resolution_status: unresolved
  resolution_strategy: prefer_higher_confidence
```

### 10. Context Versioning

Contexts evolve; versions must be tracked.

```
ContextVersion:
  id: K_COCINA_VERDURAS
  version: 2
  parent_version: 1
  changes:
    - added_dimension: D_TEXTURA
```

When context changes, recompute:
- bit_dictionary
- sense_mask
- matrices
- signatures
- indices
- collisions

Without versioning, old signatures become unreadable.

### 11. Compilation and Decompilation

Bidirectional transformation between representations.

**Compilation (NL → ProjectionIR → Signature):**
```
NL: "la lechuga tiene hojas comestibles"
  → ProjectionIR: D_PARTE_COMESTIBLE(C_LECHUGA)=hoja
  → Signature: [1,0,0] under K_COCINA
```

**Decompilation (Signature → explanation):**
```
Signature: bits=[1,0,0]
  → D_PARTE_COMESTIBLE(C_LECHUGA)=hoja
  → "La lechuga se clasifica como hoja comestible en este contexto"
```

Operation:
```
verbalize(signature, context, style) → natural_language_text
```

Important for traceability and explainability.

### 12. Dimension Selection Objective Function

Formalize "best dimension to split on" with multi-criteria optimization.

```
score(D) = w₁·information_gain(D) - w₂·cost(D) - w₃·uncertainty(D)
```

Where:
- `information_gain(D)`: reduces collisions (entropy reduction)
- `cost(D)`: expense of observing/computing that dimension
- `uncertainty(D)`: reliability of facts for that dimension

Goal: not just a correct search tree, but an efficient one.

### 13. Context Types: Domain, Task, Discourse

Separate three context layers that compose in real queries.

| Context Type | Example | Purpose |
|--------------|---------|---------|
| domain_context | K_SOFTWARE_ANALYSIS | defines object types, predicates, dimensions |
| task_context | explain, search, compare | defines sense_mask, objective function |
| discourse_context | "this library", "the previous one" | resolves anaphora, maintains reference |

Query resolution:
```
resolve_reference("esta librería", discourse_context) → PROJECT_X
```

Real query combines all three:
```
"explica los patrones y librerías que tiene esta librería"
  → domain: K_SOFTWARE_ANALYSIS
  → task: explain
  → discourse: {this_library: PROJECT_X}
```

### 14. Pseudo-Proposition Security

Taxonomy of failures when language seems meaningful but system cannot project it.

```
UNKNOWN_CONCEPT          → concept not in universe
UNKNOWN_DIMENSION       → dimension not defined for domain
UNKNOWN_VALUE           → value not in dimension's range
TYPE_MISMATCH           → argument types don't match predicate signature
DIMENSION_NOT_APPLICABLE → dimension doesn't apply to this concept type
OUTSIDE_SENSE_MASK      → question outside current task's sense mask
MALFORMED_SIGNATURE     → bits violate well-formedness rules
NO_DENOTATION           → signature denotes empty set
TAUTOLOGICAL_QUERY      → signature denotes entire universe
AMBIGUOUS_REFERENCE    → discourse reference resolves to multiple candidates
```

Example:
```
Query: "¿qué color tiene el patrón repository?"
  → DIMENSION_NOT_APPLICABLE (color not defined for patterns)
  → semantic_status: outside_context (or unsinnig)
```

This makes the parser robust to malformed input.

### 15. Minimal Internal Language

Canonical notation for the system's "assembly language".

**Basic forms:**
```
D(c) = v                    // dimension application
R(a, b)                     // relation
Q := D=v                     // query: dimension equals value
Q₁ ∧ Q₂                     // conjunction
Q₁ ∨ Q₂                     // disjunction
¬Q                          // negation
```

**With types:**
```
ConceptSignature:    C_LECHUGA
QuerySignature:      D_LIBRARY_ROLE=web_framework
ContrastSignature:   D_PARTE_COMESTIBLE(lechuga) ≠ D_PARTE_COMESTIBLE(zanahoria)
RuleSignature:       imports(PROJECT, x) ∧ D_LIBRARY_ROLE(x)=web_framework → uses_capability(PROJECT, web_api)
```

Example:
```
D_LIBRARY_ROLE(LIB_FASTAPI)=web_framework
imports(PROJECT, LIB_FASTAPI)
imports(PROJECT, x) ∧ D_LIBRARY_ROLE(x)=web_framework
```

This notation is the "assembly language" of the system — the minimal formal language in which all projections, queries, and inferences are expressed.

---

## Summary: Complete Formalization Status

| # | Formalization | Status |
|---|---------------|--------|
| 1 | Identity/equivalence | **Defined** |
| 2 | Minimal type system | **Defined** |
| 3 | Predicate arity | **Defined** |
| 4 | Dimension vs relation | **Defined** |
| 5 | Truth/epistemic/semantic states | **Defined** |
| 6 | Provenance/evidence | **Defined** |
| 7 | Inference rules | **Defined** |
| 8 | Update operations | **Defined** |
| 9 | Contradiction handling | **Defined** |
| 10 | Context versioning | **Defined** |
| 11 | Compilation/decompilation | **Defined** |
| 12 | Dimension selection objective | **Defined** |
| 13 | Context types (domain/task/discourse) | **Defined** |
| 14 | Pseudo-proposition security | **Defined** |
| 15 | Minimal internal language | **Defined** |

The metamodel is now complete: it defines not just what is represented, but what counts as valid representation, how it changes, how it's justified, how it's queried, and how it's explained.

## References
- turn-36.md (complete mathematical formalization: group (𝔹ⁿ, XOR), boolean algebra, semiring, lattice of partitions, full system tuple 𝓒)
- turn-38.md (4-layer architecture: symbolic → signature → grammar Γ → operational; 3 signature types; typed operations Ω)
- turn-44.md (15 missing formalizations now implemented: identity, types, arity, dimension vs relation, truth/epistemic/semantic states, provenance, inference, update operations, contradictions, context versioning, compilation/decompilation, dimension selection, context types, pseudo-proposition security, minimal internal language)

## Version Notes
- Turn 36: comprehensive mathematical formalization — the system is a contextualized boolean algebra with group (XOR), semiring (matrices), and lattice (partitions) structures
- Turn 38: added 4-layer architecture (symbolic → signature → grammar Γ → operational), 3 signature types (Concept/Query/Contrast), typed operations Ω, and LogicalResult structure. Key: algebraic possibility ≠ semantic admissibility under grammar Γ
- Turn 44: **COMPLETED** — all 15 missing formalizations now defined and documented in this file
