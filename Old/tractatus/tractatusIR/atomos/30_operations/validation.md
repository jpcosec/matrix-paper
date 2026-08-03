# Validation

Source anchors:

- `specs/operations/boolean_algebra.md`
- `specs/database/database_design.md`

## Core Role

Validation checks whether a signature or IR candidate is admissible under:

- dimension typing
- one-hot or multi-hot rules
- applicability
- sense mask
- required observation state

This atom is operational.
For the formal constraints it depends on, see:

- `atomos/20_formal/well_formedness.md`
- `atomos/20_formal/masks.md`
- `atomos/20_formal/logical_status.md`
