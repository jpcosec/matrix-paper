# Why Encoding Becomes Knowledge

Source anchors:

- `specs/concepts/binary_dimensions.md`
- `specs/data_model/bit_representation.md`

## Core Claim

Binary encoding becomes interpretable knowledge only when bits are typed and read inside a context.

The source corpus insists on three conditions:

1. bits must be typed by axis or dimension
2. bit positions must be decoded through a bit dictionary
3. the context explains why those bits matter now

## Negative Rule

Do not use a flat opaque code such as:

```text
perro = 010101
```

without dimension and value semantics.

## Positive Rule

Use structures of the form:

```yaml
bit_dictionary:
  0: {dimension: D_PARTE_COMESTIBLE, value: hoja}
```

Then a bit vector answers discriminative questions rather than storing an uninterpreted hash.

For the canonical bridge among dimension, value, bit, and signature, see `atomos/10_core/representation_model.md`.
