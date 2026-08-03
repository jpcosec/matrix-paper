# Database Design & NL Parser

## Summary
The system admits a hybrid database (relational + binary indices) plus a NL→Projection compiler (not just a parser) that translates natural language to typed signatures through an intermediate representation (ProjectionIR).

## Concepts
- **Hybrid DB**: relational/document for concepts/dimensions/contexts + binary matrices for fast search
- **ProjectionIR**: intermediate representation between NL and binary signatures
- **NL2Projection compiler**: normalizes text → detects intent → maps to dimensions/values → compiles to typed signature → validates
- **Typed outputs**: ConceptAssertion, Query, Contrast, SimilarityRequest, InsertConcept, DefineDimension, RefineCollision, Explain
- **Hybrid architecture**: LLM proposes candidates → deterministic resolver validates IDs/rules → sense validator decides status → operation engine executes

## Database Schema (SQL-Approach)

### Core Tables

```sql
CREATE TABLE concepts (
  id TEXT PRIMARY KEY,
  label TEXT NOT NULL,
  aliases JSONB,
  global_features JSONB
);

CREATE TABLE dimensions (
  id TEXT PRIMARY KEY,
  label TEXT NOT NULL,
  type TEXT NOT NULL,  -- one_hot | multi_hot | boolean | ordinal | scalar_bucket
  question TEXT,
  applies_when JSONB
);

CREATE TABLE dimension_values (
  id TEXT PRIMARY KEY,
  dimension_id TEXT REFERENCES dimensions(id),
  value TEXT NOT NULL,
  bit_key TEXT
);

CREATE TABLE contexts (
  id TEXT PRIMARY KEY,
  domain TEXT,
  task TEXT,
  universe JSONB,
  active_dimensions JSONB,
  sense_mask JSONB,
  rules JSONB
);

CREATE TABLE bit_dictionary (
  context_id TEXT REFERENCES contexts(id),
  bit_index INT,
  dimension_id TEXT REFERENCES dimensions(id),
  value_id TEXT REFERENCES dimension_values(id),
  PRIMARY KEY (context_id, bit_index)
);

CREATE TABLE signatures (
  id TEXT PRIMARY KEY,
  concept_id TEXT REFERENCES concepts(id),
  context_id TEXT REFERENCES contexts(id),
  signature_type TEXT,  -- concept | query | contrast | mask | rule
  bits BIT VARYING,
  valid_mask BIT VARYING,
  observed_mask BIT VARYING,
  metadata JSONB
);

CREATE TABLE projection_ir (
  id TEXT PRIMARY KEY,
  raw_text TEXT,
  parsed JSONB,
  context_id TEXT,
  signature_type TEXT,
  bits BIT VARYING,
  valid_mask BIT VARYING,
  validation_status TEXT,
  created_at TIMESTAMP DEFAULT now()
);
```

### Derived Indices (Runtime)

```sql
-- Index by dimension (from bit_dictionary)
CREATE INDEX idx_bit_dict_context ON bit_dictionary(context_id);
CREATE INDEX idx_signatures_context ON signatures(context_id, concept_id);

-- For fast lookup by signature
CREATE INDEX idx_signatures_bits ON signatures(context_id, bits);
```

## ProjectionIR (Intermediate Representation)

The key missing piece: NL doesn't go directly to bits. It passes through a typed intermediate representation:

```yaml
ProjectionIR:
  raw_text: "busca vegetales cuya parte comestible sea raíz"
  intent: lookup
  context:
    resolved: K_COCINA_VERDURAS
    confidence: 0.92
  references:
    concepts: []
    dimensions:
      - D_PARTE_COMESTIBLE
    values:
      - raíz
  constraints:
    - dimension: D_PARTE_COMESTIBLE
      operator: equals
      value: raíz
  signature_type: query
  compilation:
    bit_order: [D_PARTE.hoja, D_PARTE.raíz, D_PARTE.tallo]
    bits: [0,1,0]
    valid_mask: [1,1,1]
  validation:
    status: SINNVOLL
```

This IR is **key for debugging** — you can inspect what the compiler produced before execution.

## NL2Projection Compiler Pipeline

```
Natural language input
    ↓
normalize
    ↓
detect intent        → lookup | contrast | insert | explain | define_dimension
    ↓
detect context       → resolve from candidate contexts
    ↓
extract entities     → map words to concepts/dimensions/values
    ↓
build typed expression → ConceptSignature | QuerySignature | ContrastSignature
    ↓
compile to signature → bits + masks
    ↓
validate with sense rules (Γ) → SINNVOLL | SINNLOS | UNSINNIG | OUTSIDE_CONTEXT
    ↓
execute operation
```

### Intent Types

| Intent | Description | Output Type |
|--------|-------------|-------------|
| ConceptAssertion | "lechuga es hoja" | ConceptSignature |
| Query | "busca vegetales de raíz" | QuerySignature |
| Contrast | "en qué se diferencian lechuga y zanahoria" | ContrastSignature |
| SimilarityRequest | "qué concepto es similar a lechuga" | Similarity computation |
| InsertConcept | "agrega repollo" | InsertResult |
| DefineDimension | "separemos por textura" | DimensionProposal |
| RefineCollision | "refinar colisión en hoja" | RefineResult |
| Explain | "por qué esto es sinnvoll" | Explanation |

## Parser Pseudocode

```pseudo
parse_nl(text, candidate_contexts) -> List[ProjectionIR]:
  normalized = normalize(text)
  intent = detect_intent(normalized)
  entities = extract_entities(normalized)
  context_candidates = resolve_context(normalized, candidate_contexts)
  dimension_candidates = map_terms_to_dimensions(normalized)
  value_candidates = map_terms_to_values(normalized)

  ir_candidates = build_ir_candidates(
    intent=intent,
    entities=entities,
    context_candidates=context_candidates,
    dimension_candidates=dimension_candidates,
    value_candidates=value_candidates
  )

  return ir_candidates
```

```pseudo
compile_ir(ir, db) -> Signature:
  K = db.get_context(ir.context)
  bits = zeros(K.bit_count)
  valid = zeros(K.bit_count)

  for constraint in ir.constraints:
    bit_index = resolve_bit(db, dimension=constraint.dimension, value=constraint.value)
    bits[bit_index] = 1
    valid[bit_index] = 1

  return Signature(
    signature_type=ir.signature_type,
    bits=bits,
    valid_mask=valid
  )
```

## Sense Validation of IR

```pseudo
validate_ir(ir, db) -> LogicalResult:
  signature = compile_ir(ir, db)
  validation = validate(signature, ir.context)

  if validation == UNSINNIG:
    return LogicalResult(status=UNSINNIG, explanation="Violates grammar Γ")

  if validation == OUTSIDE_CONTEXT:
    return LogicalResult(status=OUTSIDE_CONTEXT,
      explanation="Dimension not in sense_mask for this context")

  S = denote(signature, ir.context)
  if size(S) == 0:
    return LogicalResult(status=SINNLOS_CONTRADICTION)
  if size(S) == size(U):
    return LogicalResult(status=SINNLOS_TAUTOLOGY)

  return LogicalResult(status=SINNVOLL, denotation=S)
```

## Hybrid Architecture: LLM + Deterministic Resolver

The parser should NOT be 100% LLM. Use a hybrid:

```
LLM candidate parser
    → produces IR candidates
        ↓
Deterministic resolver
    → revises IDs, allowed values, types, masks
        ↓
Sense validator (Γ)
    → decides sinvoll/sinnlos/unsinnig
        ↓
Operation engine
    → executes search/contrast/insert
```

### Example

```
User: "la zanahoria está viva"
LLM proposes: {dimension: D_ESTADO_VITAL, value: vivo, concept: C_ZANAHORIA}

Validator reviews:
  context: K_COCINA_VERDURAS
  sense_mask: [..., D_ESTADO_VITAL=0, ...]
Result:
  status: OUTSIDE_CONTEXT
  reason: "D_ESTADO_VITAL not enabled in K_COCINA_VERDURAS"

Same input in biology context:
  context: K_BIOLOGIA_ORGANISMOS
  sense_mask: [..., D_ESTADO_VITAL=1, ...]
Result:
  status: SINNVOLL
```

## Dimension Learning

When the parser can't find a dimension, it proposes a new one:

```
Input: "distínguelas por si son crujientes o blandas"
Parser:
  type: DefineDimension
  candidate_dimension:
    label: textura
    type: one_hot_or_multi_hot
    values: [crujiente, blanda]
    applies_when: {alimento: 1}

System should NOT auto-accept. Register as:
  DimensionProposal:
    status: pending_review
Then extend grammar Γ after review.
```

## Three-Layer Data Architecture

```
┌────────────────────┐
│ Natural language    │
└─────────┬────────────┘
          │
          ▼
┌────────────────────┐
│ NL2Projection       │
│ parser/compiler     │
└─────────┬────────────┘
          │
          ▼
┌────────────────────┐
│ ProjectionIR        │
└─────────┬────────────┘
          │
          ▼
┌────────────────────┐
│ Sense Validator Γ   │
└─────────┬────────────┘
          │
     ┌────┴────┐
     │         │         │
     ▼         ▼         ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ UNSINNIG │ │ SINNLOS  │ │ SINNVOLL │
└─────────┘ └─────────┘ └────┬────┘
                                 │
                                 ▼
                        ┌────────────────────┐
                        │ Query/Operation     │
                        │ engine              │
                        └────────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────────┐
                    │ DB + indices        │
                    │ matrices, trees, relations │
                    └────────────────────────────┘
```

## Key Formal Statement (Turn 39-40)

> The database stores the logical space. The parser translates natural language to coordinates of that space. The validator decides if those coordinates make sense.

> Not every operation defined on bits is defined on meanings. The grammar Γ decides.

More formal:
```
op_bool : 𝔹ⁿ × 𝔹ⁿ → 𝔹ⁿ          # always exists (full space)
op_sem  : Σ × Σ ⇀ Σ                     # partial (must preserve Γ)
```
The arrow `⇀` indicates partiality — the operation may fail or return `UNSINNIG`.

## References
- turn-40.md (hybrid DB schema SQL, NL2Projection compiler pipeline, ProjectionIR, typed intents, hybrid LLM+deterministic architecture)

## Version Notes
- Turn 40: full database design (SQL schema for concepts/dimensions/contexts/signatures/IR) + NL→Projection compiler with intermediate ProjectionIR + hybrid LLM/deterministic architecture
