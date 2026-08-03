# Review: `specs/database/database_design.md`

- `archivo actual`: `specs/database/database_design.md`
- `rol actual`: schema de persistencia e IR de compilacion NL
- `tipo`: normativo + operacional
- `duplicaciones detectadas`:
  - firma tipada con `specs/formalization/mathematical_formalization.md`
  - facts/relations con `specs/database/facts_and_relations.md`
- `afirmaciones canonicas que deben sobrevivir`:
  - ProjectionIR como capa intermedia obligatoria
  - parser como compilador NL -> IR -> firma
  - arquitectura hibrida LLM + resolver determinista + validador de sentido
  - schema SQL base para conceptos, dimensiones, contexts, signatures e IR
- `destino propuesto en atomos/`:
  - `30_operations/compilation_decompilation.md`
  - `40_persistence/database_schema.md`
  - `40_persistence/storage_model.md`
- `destino final`: archivar como fuente principal de parser y persistencia
