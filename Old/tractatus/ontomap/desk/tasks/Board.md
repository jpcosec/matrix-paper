# OntoMap Tasks Board

## Current State Summary

- Objective: deliver a stable semantic edge model and one proven projection path

## Delivery Phases

### Phase 1 - Stabilize the core model
- `desk/tasks/001-define-canonical-edge-model.md`
- `desk/tasks/002-define-projection-contract.md`

### Phase 2 - Prove one projection path
- `desk/tasks/003-create-ecosystem-ontology-fixture.md`
- `desk/tasks/004-implement-canonical-projection.md`

### Phase 3 - Prove downstream utility
- `desk/tasks/005-validate-projection-roundtrip.md`

## Active

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| 001 | model | Define canonical edge model | p0 | none |
| 002 | projection | Define projection contract | p0 | 001 |
| 003 | fixtures | Create ecosystem ontology fixture | p1 | 001, 002 |
| 004 | projection | Implement canonical projection | p1 | 001, 002, 003 |
| 005 | validation | Validate projection roundtrip | p1 | 004 |

## Blocked

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| - | - | none | - | - |

## Working Rules

1. Start from `desk/SPEC.md`.
2. Define the edge model before projection logic.
3. Prove each phase with fixtures before advancing.
