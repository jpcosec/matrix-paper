# Formal Propositional Model (Tractarian DB)

Version: `0.1-draft`

## 1. Core Thesis

The database does not store "things" only. It stores **projectable propositions** (Sachverhalte).
Meaning is derived from the structured connection between names/objects.

- **facts**: asserted states of affairs.
- **relations**: possible forms of connection between objects.
- **rules**: conditions under which those connections have sense (Grammar).

Example: A fact is not "lettuce" or "leaf", but:
`D_PARTE_COMESTIBLE(C_LECHUGA) = hoja`

---

## 2. Fact Storage (Atomic Propositions)

Facts are stored as **typed atomic propositions**, not just generic triples.

### Fact Structure
- **id**: Unique identifier.
- **subject**: The concept (e.g., `C_LECHUGA`).
- **predicate**: The dimension or relation (e.g., `D_PARTE_COMESTIBLE`).
- **object**: The value (e.g., `V_HOJA`).
- **context**: The world/welt of assertion.
- **logical_form**: Meta-description of the proposition (arity, kind).
- **truth_status**: Asserted truth value.
- **provenance**: Source, confidence, and evidence.
- **masks**: `valid`, `senseful`, `observed`.

---

## 3. Relation Levels

The system distinguishes between three distinct levels of relations:

### 3.1 External Factual Relations
Empirical connections between entities (e.g., `imports(A, B)`).
These are Tractarian elementary propositions `R(a, b)`.

### 3.2 Dimensional Relations
Functional assignments that feed the discriminative engine.
`D(c) = v` (e.g., `D_LIBRARY_ROLE(FastAPI) = web_framework`).
These compile directly into bit-signatures and matrices.

### 3.3 Internal / Derived Relations
Formal relations that "show themselves" in the structure of the representation.
`similar_to(a, b)` exists because `∃D,v : D(a)=v ∧ D(b)=v`.
These are computed on-demand from `M_D · M_Dᵀ` and are not stored as primary facts.

---

## 4. Logical Form (The Grammar of Sense)

Rules of sense are the conditions for a proposition to have meaning. They are **not** facts within the world, but the boundary of the world.

- **Rule**: `D_LIBRARY_ROLE` applies when `concept_type = library`.
- **Fact**: `concept_type(FastAPI) = library`.

The rule authorizes the proposition; the fact fills it.

---

## 5. Operations on Semantic Encodings (Signatures)

Operations on bit-vectors are **partial** because they must preserve the **Grammar of Sense (Γ)**.

### Signature Types
- **ConceptSignature**: Represents a concrete object. Must satisfy strict constraints (e.g., one-hot exactly one).
- **QuerySignature**: Represents a logical filter. May allow disjunctions (e.g., one-hot at least one).
- **ContrastSignature**: Represents a difference vector (result of XOR).
- **MaskSignature**: Represents applicability or sense boundaries.

### Operational Logic
- `op_bool : 𝔹ⁿ × 𝔹ⁿ → 𝔹ⁿ` (Always exists algebraically).
- `op_sem  : Σ × Σ ⇀ Σ` (Partial map, validated by Γ).

An expression has computable sense (`sinnvoll`) when its projection produces a valid, non-empty, and non-total selection within the local logical space.
