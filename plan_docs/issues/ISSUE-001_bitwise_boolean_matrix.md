# ISSUE-001: Vectorización Bitwise Denso de `BooleanMatrix`

**Estado:** ⏳ Pendiente  
**Dependencias:** Ninguna  
**Archivos Afectados:** `Matrix/Matrix/src/operational_model/matrices/boolean_matrix.py`, `tests/test_bool_mult.py`

## Descripción

Actualmente, `BooleanMatrix` representa los valores de la matriz como `values: list[list[Any]]` y calcula la multiplicación matricial booleana mediante bucles disjuntos `for` anidados en Python. Para que el motor sirva como base de cómputo matricial eficiente en silicio o JAX/NumPy, `BooleanMatrix` debe soportar vectorización de bits usando enteros o arrays densos de bits (`bitmasks` / `uint64`), acelerando `bool_mult()`, `transpose()`, `collapse_similarity()` y `recursive_power()`.

## Tareas

1. Optimizar `BooleanMatrix` para soportar representación bitwise eficiente por filas/columnas.
2. Asegurar compatibilidad bidireccional con exportación a listas/diccionarios `to_dict()` y `from_dict()`.
3. Mantener y verificar los algoritmos de potencia matricial `recursive_power()` y simetría `collapse_similarity()`.
4. Ejecutar pruebas unitarias asociadas y validar rendimiento.
