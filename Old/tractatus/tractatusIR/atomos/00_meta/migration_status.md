# Migration Status

Current phase: initial scaffold.

Current decisions:

- `specs_raw/` uses symlinks during migration.
- `atomos/` is the target canonical source.
- `docs/spec/` will contain compiled mature documents.
- current implementation strategy is to atomize existing `specs/` before inventing missing atoms.

Pending:

- review `specs/` one file at a time
- extract non-duplicated atoms
- define transclusion/build strategy in detail
