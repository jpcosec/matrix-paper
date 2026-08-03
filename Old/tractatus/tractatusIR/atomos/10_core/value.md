# Value

Source anchors:

- `specs/data_model/bit_representation.md`
- `specs/data_model/matrix_representation.md`

## Definition

Values are the admissible positions or answers inside a dimension.

Examples from the source corpus:

- `D_PARTE_COMESTIBLE = {hoja, raiz, tallo}`
- `D_USO_CULINARIO = {ensalada, sopa, sofrito, jugo}`

## Canonical Role

Values support:

- local partitioning
- bit dictionary entries
- one-hot or multi-hot encoding
- bucket construction in inverted indices

## Encoding Note

In the binary encoding model, a bit position becomes meaningful only through a pairing of:

- dimension
- value

This pairing is carried by the bit dictionary.

For the full bridge to dimensions, bits, and signatures, see `atomos/10_core/representation_model.md`.
