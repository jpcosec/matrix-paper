# Gap Assessment After Atomization

This file records the gaps that remain visible after decomposing the current `specs/` corpus.

## Persistence Rule

This is a persistent canonical working document inside `atomos/`.

It should not be treated as a temporary migration note.
Open gaps remain listed here until they are either:

- resolved by a canonical atom update
- split into a more precise sub-gap
- explicitly discarded

Rule of use:

- do not silently remove items
- when a gap is resolved, rewrite its section as resolved or move the resolved content into the target atom and leave a short resolution note here

## Already Resolved By Atomization Structure

- `specs/` is no longer a single undifferentiated canonical layer
- tractarian substrate now has explicit atoms
- heuristics now have explicit atoms
- persistence and operations are no longer mixed into one macro-spec

## Real Gaps Still Open

### 1. Representation Bridge

The corpus still shifts between these vocabularies:

- feature
- dimension
- value
- bit
- signature

This is coherent enough to work with, but not fully normalized.

Needed status:

- canonical clarification, not necessarily new theory

### 2. Identity And Equivalence

The system names identity issues, but the final semantics of:

- same concept
- alias
- translation
- projection equivalence
- subtype or subconcept

is not fully frozen.

Needed status:

- real design closure later

### 3. Contradiction Policy

The corpus clearly requires first-class contradictions, but does not fully settle:

- reject vs store
- confidence-based resolution
- versioning of conflicts
- allowed contradictions inside one local world

Needed status:

- policy decision later

### 4. Versioning Semantics

Contexts and signatures need versioning, but the stable policy is not closed yet.

Needed status:

- real design closure later

### 5. Inference Discipline

Inference is clearly required, but the boundary among:

- logical inference
- heuristic inference
- statistical inference
- LLM-suggested inference

is still only sketched.

Needed status:

- real design closure later

### 6. Query And Explanation Evidence Policy

`ProjectionIR`, facts, relations, and explanation are present, but evidence propagation and explanation guarantees are not fully normalized.

Needed status:

- clarification and closure later

### 7. Build And Transclusion Mechanics

The conceptual use of indices as documentation ASTs is now explicit, but the concrete compilation mechanics are not yet specified.

Needed status:

- implementation closure later

## Likely New Canonical Atom Needed

The atomization exposed one especially useful missing atom:

- `10_core/representation_model.md`

Reason:

- several files overlap because the bridge between dimension, value, bit, and signature is distributed instead of centered.

## Practical Rule

Anything in this file should be treated as an explicit open item rather than a hidden inconsistency.
