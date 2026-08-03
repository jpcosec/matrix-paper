# Matrix Model

Source anchors:

- `specs/data_model/matrix_representation.md`
- `specs/operations/boolean_algebra.md`

## Matrix Family

- `M0`: concept x feature
- `M1`: concept x discriminant value
- `M1^T`: discriminant value x concept
- `M1 x M1^T`: concept x concept co-membership

## Canonical Role

The matrix layer simultaneously supports:

- representation
- inverted indexing
- collision detection
- recursive refinement
- horizontal relations

To avoid overlap:

- this atom owns the formal matrix family
- `atomos/30_operations/collision_refinement.md` owns the refinement operation
- `atomos/40_persistence/derived_indices.md` owns the persisted or materialized index view
