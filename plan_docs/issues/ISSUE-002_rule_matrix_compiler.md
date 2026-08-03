# ISSUE-002: Compilador de Reglas a Matrices de Incidencia $I$ y Cláusulas $(C^+, C^-)$

**Estado:** ⏳ Pendiente  
**Dependencias:** ISSUE-001  
**Archivos Afectados:** `Matrix/Matrix/src/operational_model/kernel/rule_matrix.py` (Nuevo), `tests/test_rule_matrix_compiler.py` (Nuevo)

## Descripción

Para eliminar la inspección de árboles de sintaxis (AST) durante la inferencia, se necesita un compilador que tome un conjunto de fórmulas proposicionales en S-Expressions o AST y construya sus representaciones matriciales equivalentes:
1. **Matriz de Implicación Directa $I \in \{0, 1\}^{N \times N}$**: Donde $I_{i,j} = 1$ indica que $P_i \implies P_j$.
2. **Matrices de Cláusulas $(C^+, C^-) \in \{0, 1\}^{M \times N}$**: Donde $C^+_{m, n} = 1$ indica presencia positiva de la variable $n$ en la cláusula CNF $m$, y $C^-_{m, n} = 1$ la presencia negada.

## Tareas

1. Crear el módulo `src/operational_model/kernel/rule_matrix.py`.
2. Implementar `RuleMatrixCompiler.compile_implications(premises: list[Formula]) -> BooleanMatrix`.
3. Implementar `RuleMatrixCompiler.compile_cnf_clauses(premises: list[Formula]) -> tuple[BooleanMatrix, BooleanMatrix]`.
4. Agregar suite de pruebas en `tests/test_rule_matrix_compiler.py`.
