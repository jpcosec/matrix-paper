# Dimension

Source anchor:

- `specs/spec_main.md`

## Definition

A dimension groups features that answer one semantic question.

```yaml
dimension:
  id: D_PARTE_COMESTIBLE
  question: "¿Que parte de la planta se consume principalmente?"
  features: [hoja_comestible, raiz_comestible, tallo_comestible, fruto_comestible]
```

## Canonical Role

Within the source spec, a dimension provides the structured basis for local discrimination.

It is used to:

- partition the local universe
- generate contextual bit signatures
- reveal collisions when multiple concepts receive the same local encoding

## Parallel Axes From Early Corpus

Before later formalization, the source corpus already distinguishes at least three major dimension families:

- ontological
- functional
- state

This separation comes from `specs/concepts/categorization.md` and `specs/concepts/binary_dimensions.md` and preserves the rule:

`what it is` != `what it is used for` != `what state it is in`

## Later Matrix Reading

From `specs/data_model/matrix_representation.md`, dimensions also behave as discriminative questions of the form:

```text
D: C -> V
```

where a dimension induces buckets over the local universe and can be encoded one-hot or multi-hot depending on its type.

For the bridge to values, bits, and signatures, see `atomos/10_core/representation_model.md`.

## Note For Later Reconciliation

This atom still reflects the earlier `feature` vocabulary of `specs/spec_main.md`.
Later specs may require splitting this more cleanly into:

- dimension
- value
- bit or feature encoding
