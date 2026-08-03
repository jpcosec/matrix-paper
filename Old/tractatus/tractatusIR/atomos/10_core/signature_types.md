# Signature Types

Source anchors:

- `specs/data_model/bit_representation.md`
- `specs/formalization/mathematical_formalization.md`
- `specs/database/database_design.md`

## Core Categories Present In Source Corpus

- concept signature
- query signature
- contrast signature
- mask signature
- rule signature

## Distinctions That Must Survive

From the source corpus:

- a `ConceptSignature` represents one concrete state in context
- a `QuerySignature` can allow disjunctive selections not valid for concept states
- a `ContrastSignature` naturally hosts XOR differences

## Binary Form

At minimum, a signature may carry:

- `bits`
- `valid_mask`
- context reference
- type tag

Later sources also add:

- `observed_mask`
- metadata

For the bridge from dimensions and values to bit positions and signatures, see `atomos/10_core/representation_model.md`.
