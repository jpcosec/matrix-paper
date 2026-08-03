# Review: `specs/data_model/matrix_representation.md`

- `archivo actual`: `specs/data_model/matrix_representation.md`
- `rol actual`: modelo matricial de representacion, indice y colision
- `tipo`: normativo + formal
- `duplicaciones detectadas`:
  - matrices y arboles con `specs/operations/boolean_algebra.md`
  - colisiones y expansion con `specs/operations/contextual_insertion.md`
- `afirmaciones canonicas que deben sobrevivir`:
  - roles de `M0`, `M1`, `M1^T`, `M1 x M1^T`
  - buckets como indice invertido
  - colisiones cuando `|bucket(v)| > 1`
  - submatrices recursivas como arbol de busqueda
- `destino propuesto en atomos/`:
  - `20_formal/matrix_model.md`
  - `40_persistence/derived_indices.md`
  - `30_operations/collision_refinement.md`
- `destino final`: archivar como fuente principal del modelo matricial
