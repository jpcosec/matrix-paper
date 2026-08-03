# Status Model

Document statuses used during migration:

- `canonical-atom`: authoritative source atom
- `compiled-doc`: generated or compiled reading document
- `archived-source`: preserved source material
- `working-note`: active exploratory note
- `architecture-rationale`: architectural explanation, not canonical semantic source
- `implementation-plan`: plan or execution note

Authority order during migration:

1. `atomos/`
2. compiled `docs/` derived from `atomos/`
3. `specs_raw/` as traceable source archive
