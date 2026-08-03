# Tractarian Core & Domain Layer

## Summary
The Tractatus gives us the **core ontology**: Object, Name, Sign, Symbol, State-of-Affairs, Fact, Proposition, Logical Form, Logical Space, Projection, Limit of Sense. We define the **domain layer** ourselves (concepts, dimensions, values, contexts, parsers). The core determines *what counts as representation*; the domain determines *what we represent*.

## Concepts
- **Tractarian Core** (from Tractatus): Object/Gegenstand, Name/Name, Sign/Zeichen, Symbol/Symbol, State-of-Affairs/Sachverhalt, Fact/Tatsache, Proposition/Satz, Logical Form/logische Form, Logical Space/logischer Raum, Projection/Projektion, Limit of Sense/Sinngrenze
- **Domain Layer** (defined by us): Concept, Dimension, Value, Context, Signature, Parser, Indices
- **Sign → Symbol pipeline**: `Sign` (surface) + logical-syntactic use → `Symbol` (operationally meaningful)
- **Projection**: Symbol + Context → Signature/Projection
- **Limit of Sense**: Grammar Γ determines what projections are possible

## Tractarian Core (The "What Counts" Layer)

### Entity Diagram
```
Tractarian Core:
  Object (Gegenstand)
    ↓
  Name (Name) — refers to object
    ↓
  Sign (Zeichen) — sensible surface form
    ↓ (+ logical-syntactic use)
  Symbol (Symbol) — operationally meaningful in context
    ↓
  Proposition (Satz) — Symbol combination
    ↓
  State-of-Affairs (Sachverhalt) — existence/non-existence of states
    ↓
  Fact (Tatsache) — true proposition (state that exists)
```

### Key Distinctions

| Term | Tractatus German | Our Mapping | Description |
|------|-----------------|-------------|-------------|
| **Object** | Gegenstand | `Concept` — stable node |
| **Name** | Name | `concept_id` — identifier |
| **Sign** | Zeichen | `Sign` — surface form: "lechuga", "lettuce", `S_LECHUGA_ES` |
| **Symbol** | Symbol | `Symbol` — sign + logical-syntactic use in context |
| **State-of-Affairs** | Sachverhalt | `StateOfAffairs` — `D(c)=v` combination |
| **Fact** | Tatsache | `Fact` — true state-of-affairs |
| **Proposition** | Satz | `Signature` — projection of symbol |
| **Logical Form** | logische Form | `LogicalForm` / grammar Γ |
| **Logical Space** | logischer Raum | `LogicalSpace_K` — set of possible projections |
| **Projection** | Projektion | `projection` — mapping from sign to signature |
| **Limit of Sense** | Sinngrenze | `sense_mask` + grammar Γ |

### Sign vs Symbol (Critical Distinction)

From `tractatus_tree_de`: the sign is perceptible; the symbol results from logical-syntactic use. The same sign can belong to different symbols.

```yaml
Sign:
  id: S_LECHUGA_ES
  surface: "lechuga"
  sign_system: spanish_common_language
  projects_to: C_LECHUGA

Symbol:
  id: SYM_LECHUGA_COCINA
  sign: S_LECHUGA_ES
  context: K_COCINA_VERDURAS
  logical_use: "name in proposition D_PARTE=hoja"
  denotes: C_LECHUGA
```

Rule: **To recognize the symbol, you must look at the meaningful use — not just the sign.**

### Projection: Sign → Symbol → Proposition

```
Sign "lechuga"
  → Symbol in K_COCINA: "lechuga as D_PARTE.hoja"
    → Projection: [1,0,0]
       → Proposition: "lechuga is hoja-comestible"
```

From `tractatus_tree_de`: the proposition is a projection of a possible situation; the logical form shows itself and cannot be said within the system.

### Logical Space & Limit of Sense

```yaml
LogicalSpace_K:
  context: K_COCINA_VERDURAS
  possible_projections:
    - ConceptSignature × Context → Signature
  limit: sense_mask + grammar Γ
```

What can be projected with sense in K:
```
representable(K) = {s ∈ 𝔹ⁿ | well_formed(s,K) ∧ applicable(s,K) ∧ senseful(s,K)}
```

What cannot: `unsinnig` (violates grammar) or `outside_context` (valid but not in sense mask).

## Domain Layer (Defined by Us)

On top of the Tractarian core, we define domain-specific structures:

```yaml
DomainLayer:
  concepts:
    - C_LECHUGA (type: vegetable)
    - LIB_FASTAPI (type: library)
  dimensions:
    - D_PARTE_COMESTIBLE (applies_when: planta=1, alimento=1)
    - D_LIBRARY_ROLE (applies_when: concept_type=library)
  values:
    - V_HOJA, V_RAIZ, V_WEB_FRAMEWORK
  contexts:
    - K_COCINA_VERDURAS (task: differentiate)
    - K_SOFTWARE_ANALYSIS (task: explain)
  signatures:
    - ConceptSignature, QuerySignature, ContrastSignature
  parsers:
    - NL2Projection compiler
  indices:
    - matrices, transposes, buckets, trees
```

## The Combined Architecture

```
┌────────────────────────────────────────────────────┐
│ Tractarian Core (from Tractatus)              │
├────────────────────────────────────────────────────┤
│ Object → Name → Sign → Symbol           │
│ State-of-Affairs → Fact → Proposition   │
│ Logical Form → Limit of Sense (Γ)        │
│ Projection → Logical Space                   │
└──────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────┐
│ Domain Layer (defined by us)                │
├────────────────────────────────────────────────────┤
│ Concept, Dimension, Value, Context        │
│ Signature (typed), Parser, Indices        │
│ Matrices, Rules, Masks                    │
└────────────────────────────────────────────────────┘
```

## Formal Definition: Combined System

```
𝓢 = (TC, DL, Γ, ⟦·⟧)
where:
  TC = Tractarian Core = (Object, Name, Sign, Symbol,
                              StateOfAffairs, Fact, Proposition,
                              LogicalForm, LogicalSpace, Projection)
  DL = Domain Layer  = (Concept, Dimension, Value,
                              Context, Signature, Parser,
                              Index, Matrix, Rule)
  Γ  = sense grammar (what projections are admissible)
  ⟦·⟧ = denotation function: Signature → 𝒫(U)
```

### Sign → Symbol → Projection Pipeline

```pseudo
sign_to_symbol(sign, context K) -> Symbol | UNSINNIG:
  if sign not in K.allowed_signs:
    return UNSINNIG
  return Symbol(sign=sign, context=K, logical_use=...)

symbol_to_projection(symbol, K) -> Signature | OUTSIDE_CONTEXT:
  if not K.sense_mask allows symbol:
    return OUTSIDE_CONTEXT
  return compile_to_signature(symbol, K)
```

## What the Tractus Gives Us

| Question | Tractatus Answer | Our Implementation |
|----------|-------------------|--------------------|
| What is a "thing"? | Object (Gegenstand) | `Concept` |
| How do we refer? | Name → Sign → Symbol | `Sign` → `Symbol` |
| What is a fact? | State-of-affairs that exists | `D(c)=v` affirmed true |
| What is sense? | Projection within logical space | `sinnvoll` = well-formed + applicable + senseful + proper subset |
| What is nonsense? | Violates logical grammar | `unsinnig` / `outside_context` |
| What is the limit? | Logical form shows itself | Grammar Γ + `sense_mask` |
| Can we say the form? | No — it shows itself | Γ defined but not "said" as fact |

## What We Define

| Question | Our Answer |
|----------|------------|
| What concepts exist? | Domain-specific (vegetables, libraries, ...) |
| What dimensions? | Domain-specific (D_PARTE, D_LIBRARY_ROLE, ...) |
| What values? | Domain-specific (hoja, web_framework, ...) |
| What contexts? | Domain-specific (K_COCINA, K_SOFTWARE, ...) |
| What indices? | Implementation choice (SQL, JSON, in-memory) |
| What parser? | NL2Projection compiler (LLM + deterministic) |

## Key Formulation (Turn 45-46)

> **Wittgenstein defines the "signs" — they are basically the possible projections of a concept. The heart of Tractus Logicus covers the "limits of representability" and a "core" minimal ontology. The rest depends on us.**

Compact:
> **Tractarian core**: what counts as representation, proposition, sense, and limit.
> **Domain layer**: what we choose to represent, in which contexts, with which dimensions.

## References
- turn-45.md (question: signs as possible projections; no new facts)
- turn-46.md (Tractarian core: Object/Name/Sign/Symbol/SoA/Fact/Proposition; core vs domain layer; sign→symbol→projection pipeline)

## Version Notes
- Turn 46: THE critical architecture turn — separates Tractarian core (what counts as representation) from domain layer (what we represent). Sign→Symbol→Projection pipeline. Grammar Γ is the limit of sense.
