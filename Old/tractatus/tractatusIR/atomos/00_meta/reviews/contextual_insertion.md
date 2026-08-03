# Review: `specs/operations/contextual_insertion.md`

- `archivo actual`: `specs/operations/contextual_insertion.md`
- `rol actual`: algoritmo de insercion contextual y hashing semantico
- `tipo`: operacional + heuristico
- `duplicaciones detectadas`:
  - insercion con `specs/spec_main.md`
  - colisiones y arbol con `specs/data_model/matrix_representation.md`
- `afirmaciones canonicas que deben sobrevivir`:
  - algoritmo de insercion en 8 pasos
  - separar representacion local y global
  - hash contextual distinto del global
  - arbol de decision dinamico
  - relaciones horizontales desde bits compartidos
- `destino propuesto en atomos/`:
  - `30_operations/insertion.md`
  - `15_heuristics/why_indexing_becomes_representation.md`
  - `30_operations/collision_refinement.md`
- `destino final`: archivar como fuente operacional
