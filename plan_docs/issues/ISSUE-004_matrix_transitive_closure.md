# ISSUE-004: Reemplazo de Inferencia Relacional por Clausura Transitiva Matricial ($M_R^*$)

**Estado:** ⏳ Pendiente  
**Dependencias:** ISSUE-001  
**Archivos Afectados:** `Matrix/Matrix/src/operational_model/core/transitive_inference.py`, `Matrix/Matrix/src/operational_model/core/commutative_inference.py`, `tests/test_relation_semantics.py`

## Descripción

Actualmente `transitive_inference.py` y `commutative_inference.py` recorren diccionarios de hechos para inferir `(R a c)` a partir de `(R a b)` y `(R b c)`. Se debe reemplazar esta lógica por operaciones puramente matriciales sobre `BooleanMatrix`:
- **Inferencia Transitiva**: Construir la matriz de adyacencia de la relación $M_R$ y calcular su clausura transitiva $M_R^* = \sum_{k=1}^{|T|} M_R^k$ mediante `recursive_power()`.
- **Inferencia Simétrica/Conmutativa**: Calcular $M_R^{\text{simetrica}} = M_R \lor M_R^T$ mediante `transpose()`.

## Tareas

1. Rediseñar `transitive_inference.py` para construir la matriz de adyacencia $M_R$ y llamar a `recursive_power()`.
2. Rediseñar `commutative_inference.py` para operar sobre `transpose()`.
3. Ejecutar la suite de pruebas `tests/test_relation_semantics.py`.
