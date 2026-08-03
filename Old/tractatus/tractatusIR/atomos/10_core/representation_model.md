# Representation Model

Source anchors:

- `specs/concepts/binary_dimensions.md`
- `specs/data_model/bit_representation.md`
- `specs/data_model/matrix_representation.md`
- `specs/spec_main.md`

## Purpose

This atom normalizes the bridge among:

- dimension
- value
- bit
- signature

It exists because the source corpus is coherent but uses these layers with shifting emphasis.

## Canonical Bridge

1. a dimension defines a semantic question
2. a value is an admissible answer inside that dimension
3. a bit position becomes meaningful only through a dimension-value pairing
4. a signature is an ordered set of such typed bit positions under a context

## Minimal Reading

```text
dimension -> values -> bit dictionary positions -> signature
```

## Immediate Consequences

- no opaque flat binary code is acceptable as canonical representation
- one-hot and multi-hot belong to the dimension-to-value level
- bit semantics depend on dictionary plus context
- signatures are contextual projections, not total descriptions of a concept

## Relationship To Other Atoms

- `dimension.md` defines the semantic question
- `value.md` defines admissible answers
- `signature_types.md` defines typed signature roles
- `well_formedness.md` defines admissibility constraints
- `masks.md` defines context-sensitive restrictions
