# Concept

Source anchor:

- `specs/spec_main.md`

## Definition

A concept is a stable semantic entity that can admit multiple contextual projections.

```yaml
concept:
  id: C_LECHUGA
  label: lechuga
```

The stable concept node is the common anchor behind multiple readings of the same thing.

Examples mentioned in the source spec:

- food reading
- plant reading
- product reading

## Canonical Role

The concept is not identical to a single representation.
It is the stable node from which contextual projections are generated.

## Immediate Constraints From Source Spec

- a concept can appear in multiple contexts
- contextual representation should not replace stable identity
- the same concept may participate in vertical, local, and horizontal structure

## Early Hierarchical Insight From Source Corpus

The earliest concept work in `specs/concepts/categorization.md` adds that a concept can participate in multiple parallel typed hierarchies rather than a single tree.

For example, `zanahoria` may simultaneously appear under:

- ontological classification
- functional or use classification
- state classification

This supports the rule that a concept is a stable node while its roles and projections vary by relation and context.
