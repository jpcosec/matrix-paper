# Spec: Representación Semántica Contextual Discriminativa

## Summary
A system where concepts are represented as `concept + context + discriminative features`, enabling simultaneous representation, indexing, and horizontal relations.

## Concepts
- Concept (stable semantic entity with multiple projections)
- Context (perspective/frame for interpretation)
- Local universe (concepts competing in a context)
- Feature (evaluable semantic property, preferably binary)
- Dimension (groups features answering one semantic question)
- Contextual projection (concept representation within a specific context)
- Three dimensions: vertical/hierarchical, local/discriminative, horizontal/relational

## The Three Dimensions

### 1. Vertical / Hierarchical
Represents the path up or down a semantic hierarchy.
```
lechuga → vegetal → planta → organismo → entidad biológica → entidad física
```
Answers: "What is it?", "What category contains it?", "What does it inherit?"
Bits: `[entidad_fisica=1, entidad_biologica=1, organismo=1, planta=1, vegetal=1]`

### 2. Local / Discriminative
Minimal features needed to distinguish concepts within the current universe.
```
universe: [lechuga, zanahoria, apio]
dimension: parte_comestible_principal
lechuga = [1,0,0]  (hoja)
zanahoria = [0,1,0]  (raíz)
apio = [0,0,1]      (tallo)
```
Expands only when collisions occur (e.g., lechuga vs espinaca both `[1,0,0]` → add `forma_hoja`).

### 3. Horizontal / Relational
Relations between concepts that are not strictly hierarchical.
```
lechuga ~ espinaca (both hoja_comestible)
zanahoria ~ betarraga (both raiz_comestible)
lechuga ~ zanahoria (both vegetal + alimento)
```
Similarity: `shared_features / relevant_features`
Contrast: `differ in P, Q, R`

## Base Concepts

### Concept
A stable semantic entity with multiple contextual projections.
```
concept:
  id: C_LECHUGA
  label: lechuga
```
C_LECHUGA is the common node behind all readings (food, plant, product).

### Context
Defines the interpretation perspective.
```
context:
  id: K_COCINA_DIFERENCIAR_VERDURAS
  domain: cocina
  task: diferenciar
  local_universe: [C_LECHUGA, C_ZANAHORIA, C_APIO]
```
Domains: cocina, biología, comercio, medicina, ética, taxonomía, percepción visual
Tasks: diferenciar, clasificar, buscar, comparar, explicar, decidir

### Feature
An evaluable semantic property (prefer binary).
```
feature:
  id: F_HOJA_COMESTIBLE
  label: hoja_comestible
  type: binary
```

### Dimension
Groups features answering one semantic question.
```
dimension:
  id: D_PARTE_COMESTIBLE
  question: "¿Qué parte de la planta se consume principalmente?"
  features: [hoja_comestible, raiz_comestible, tallo_comestible, fruto_comestible]
```

## Complete Representation Model

```
concept:
  id: C_LECHUGA
  label: lechuga

  global:
    vertical:
      is_a: [vegetal, planta, organismo, entidad_biologica, entidad_fisica]
    stable_features:
      entidad_fisica: 1
      entidad_biologica: 1
      organismo: 1
      planta: 1
      vegetal: 1
      animal: 0

  projections:
    - context: K_COCINA_DIFERENCIAR_VERDURAS
      active_dimensions: [D_PARTE_COMESTIBLE]
      local_bits:
        hoja_comestible: 1
        raiz_comestible: 0
        tallo_comestible: 0
      search_path: [alimento, vegetal, parte_comestible: hoja]

  horizontal:
    similar_to:
      - concept: C_ESPINACA
        because: [hoja_comestible, vegetal, alimento]
    contrasts_with:
      - concept: C_ZANAHORIA
        because: [hoja_vs_raiz]
```

## How to Use for Representation

1. **Define context**: domain, task, local universe
2. **Identify shared features**: what candidates have in common (for group location)
3. **Find discriminative features**: what separates candidates
4. **Generate local signature**: convert to bits → contextual hash
5. **Verify collisions**: if two concepts share signature, add dimension

## How to Use for Indexing

### Vertical Index
```
index_vertical:
  planta: [C_LECHUGA, C_ZANAHORIA, C_APIO]
  vegetal: [C_LECHUGA, C_ZANAHORIA, C_APIO]
  organismo: [C_LECHUGA, C_ZANAHORIA, C_APIO]
```

### Contextual Index
```
index_contextual:
  K_COCINA_DIFERENCIAR_VERDURAS:
    parte_comestible_principal:
      hoja: [C_LECHUGA, C_ESPINACA]
      raiz: [C_ZANAHORIA, C_BETARRAGA]
      tallo: [C_APIO, C_ESPARRAGO]
```

### Signature Index (Hash-like)
```
signature_index:
  K_COCINA_DIFERENCIAR_VERDURAS:
    "1-0-0": [C_LECHUGA]
    "0-1-0": [C_ZANAHORIA]
    "0-0-1": [C_APIO]
```
Supports exact search `[0,1,0] → zanahoria` and partial search `[*,1,*] → all raíz_comestible`.

### Horizontal Index
```
index_horizontal:
  C_LECHUGA:
    similar: {concept: C_ESPINACA, score: 0.85, because: [vegetal, alimento, hoja_comestible]}
    contrastive: {concept: C_ZANAHORIA, score: 0.60, because: [hoja_vs_raiz]}
```

## Main Operations

| Operation | Signature | Description |
|------------|------------|-------------|
| `project` | `(concept, context) → projection` | Generate contextual reading |
| `discriminate` | `(concepts, context) → dimensions` | Find best separating dimensions |
| `encode` | `(concept, dimensions) → binary_signature` | Convert projection to bits |
| `lookup` | `(signature, context) → candidates` | Search by exact/partial signature |
| `neighbors` | `(concept, context) → related_concepts` | Get horizontal relations |
| `insert` | `(concept, context)` | Insert new concept into local universe |

### Insert Operation
1. Verify minimal membership (does it belong to the domain?)
2. Project to active context
3. Encode as signature
4. Check for collisions
5. If no collision → insert
6. If collision → add dimension
7. Update all indices
8. Update horizontal relations

## System Rules

1. **Don't represent everything upfront** — represent only what's needed to distinguish in context
2. **Separate what-is, what-it's-used-for, and what-state** — ontología ≠ función ≠ estado
3. **Context activates dimensions** — different contexts activate different dimension sets
4. **Collisions signal missing structure** — add dimensions only when needed
5. **Every bit must be interpretable** — bits should have names, not opaque positions

## Minimum Recommended Schema

```
contexts:
  K_COCINA_VERDURAS:
    domain: cocina
    task: diferenciar
    local_universe: [C_LECHUGA, C_ZANAHORIA, C_APIO]
    active_dimensions: [D_PARTE_COMESTIBLE]

dimensions:
  D_PARTE_COMESTIBLE:
    question: "¿Qué parte se consume principalmente?"
    features: [hoja_comestible, raiz_comestible, tallo_comestible]

concepts:
  C_LECHUGA:
    label: lechuga
    global: {is_a: [vegetal, planta, organismo]}
    projections:
      K_COCINA_VERDURAS:
        bits: {hoja_comestible: 1, raiz_comestible: 0, tallo_comestible: 0}

indices:
  contextual:
    K_COCINA_VERDURAS:
      D_PARTE_COMESTIBLE:
        hoja_comestible: [C_LECHUGA]
        raiz_comestible: [C_ZANAHORIA]
        tallo_comestible: [C_APIO]
  signatures:
    K_COCINA_VERDURAS:
      bit_order: [hoja_comestible, raiz_comestible, tallo_comestible]
      "1-0-0": [C_LECHUGA]
      "0-1-0": [C_ZANAHORIA]
      "0-0-1": [C_APIO]
```

## Tractarian Core

The system is a computational instance of Wittgenstein's Tractatus ontology:

| Tractarian Entity | System Equivalent | Description |
|-------------------|-------------------|-------------|
| Object / Gegenstand | Concept | Stable identifier, projectable entity |
| Name / Name | Symbol (logical role) | Symbol occupying argument position in proposition |
| Sign / Zeichen | Sign | Perceptible surface (e.g., "lechuga", "lettuce", `[1,0,0]`) |
| Symbol / Symbol | Sign + logical-syntactic use | Sign used within context with logical role |
| State of Affairs / Sachverhalt | Well-formed predicate application | `D_LIBRARY_ROLE(LIB_FASTAPI)=web_framework` |
| Fact / Tatsache | StateOfAffairs + truth_status | Asserted/evidenced state of affairs |
| Proposition / Satz | Projection of possible state of affairs | Contextual representation of concept |
| Logical Form / logische Form | Γ (grammar) | Rules enabling well-formed projections |
| Logical Space / logischer Raum | Context K | Set of possible combinations under context |
| Projection / Projektion | Sign/Symbol → Signature/Matrix | Compilation rule |
| Limit of Sense / Grenze des Sinns | sinnvoll / sinnlos / unsinnig | Boundary of representability |

### Sign → Symbol → Concept Pipeline

```
Sign (surface: "lechuga")
    ↓
Symbol (sign + context K + logical role: name)
    ↓
Concept (C_LECHUGA, stable node)
```

- **Sign**: perceptible vehicle/projection (text, binary signature, visual node)
- **Symbol**: sign + logical-syntactic use in context
- **Concept**: stable node being projected

### Sense Boundaries

| Status | Meaning | Condition |
|--------|---------|-----------|
| `unsinnig` | Nonsensical | No valid projection possible in context K |
| `sinnlos` | Senseless | Valid form, but no informative state of affairs selected |
| `sinnvoll` | Meaningful | Valid form projecting a proper possibility |

```
representable(E, K) ⟺ E can project to well-typed form within logical space K
representability_limit(K) = Γ_K (logical form, typing, applicability, sense rules)
```

## Architecture Layers

### Tractarian Core (from Tractatus)
- Object, Name, Sign, Symbol
- Proposition, State of Affairs, Fact
- Logical Form, Logical Space, Projection
- Sense statuses: sinnvoll / sinnlos / unsinnig
- Constraints: propositions articulated, names in propositions, predicates constrain arguments

### Domain Layer (defined by us)
- Domain-specific object types
- Predicates / dimensions per domain
- Values per dimension
- Contexts (domain + task combinations)
- Sense masks per task
- Parsers (NL → symbols/propositions)
- Indices (vertical, contextual, signature, horizontal)

Example domain (software analysis):
```
object_types: [project, package, module, class, function, library, pattern]
predicates: [imports, defines, calls, implements]
dimensions:
  D_LIBRARY_ROLE: applies_to: library, values: [web_framework, validation, orm, testing, cli]
  D_ARCHITECTURAL_PATTERN: applies_to: project, values: [repository, service_layer, mvc]
```

## Architecture Summary

```
Concept/Object (stable node)
    ↓
Sign (surface projection: "lechuga", [1,0,0])
    ↓
Symbol (sign + logical use in context)
    ↓
Context (logical space K)
    ↓
Projection (Symbol → Signature/Matrix)
    ↓
State of Affairs (well-formed combination)
    ↓
Fact (asserted state of affairs)
    ↓
Signature (interpretable binary encoding)
    ↓
Indices (vertical, contextual, signature, horizontal)
```

The three dimensions:
1. **Vertical**: What is it / what category does it belong to
2. **Local-discriminative**: What features distinguish it from candidates in this context
3. **Horizontal-relational**: What it resembles, what it contrasts with, and why

Key phrase: *A concept is a stable node. A context selects a projection. The projection generates a signature. The signature serves as hash, search path, and basis for horizontal relations.*

## References
- turn-16.md (complete spec defining three dimensions, base concepts, operations, rules, and schema)
- turn-46.md (Tractarian core: Object/Name/Sign/Symbol/State-of-Affairs/Fact/Proposition/LogicalForm/Projection/Limit of Sense; domain layer vs core distinction)

## Version Notes
- Turn 16: comprehensive spec defining the entire system architecture across all three dimensions
- Turn 46: added Tractarian core ontology, Sign→Symbol→Concept pipeline, sense boundaries (sinnvoll/sinnlos/unsinnig), architecture layers (core vs domain), representability limits
