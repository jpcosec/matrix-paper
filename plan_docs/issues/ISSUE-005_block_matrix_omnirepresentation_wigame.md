# ISSUE-005: Compilador de Omnirepresentación por Bloques e Integración en `WiGame`

**Estado:** ⏳ Pendiente  
**Dependencias:** ISSUE-003, ISSUE-004  
**Archivos Afectados:** `Matrix/Matrix/src/operational_model/system/wigame.py`, `Matrix/Matrix/src/operational_model/matrices/block_matrix.py` (Nuevo), `tests/test_operational_model.py`

## Descripción

Integrar todas las capas matriciales en `WiGame` para que las operaciones de consulta (`check`, `ingest`, `assert`, `query`) se resuelvan exclusivamente operando sobre la **Matriz por Bloques de Omnirepresentación** $\mathbf{M} = \begin{pmatrix} \mathbf{WC_i} & \mathbf{S_i} \\ \mathbf{S_i^T} & \mathbf{V_i} \end{pmatrix}$.

## Tareas

1. Crear `block_matrix.py` para representar formalmente la estructura matricial por bloques de contextos, máscaras de sentido y matriz de verdad.
2. Conectar la ingesta y consulta de `WiGame` a la matriz por bloques.
3. Validar la suite completa de 114+ pruebas pasando de forma determinista y limpia.
