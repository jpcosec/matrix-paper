# ISSUE-003: Inferencia Deductiva Proposicional Matricial ($v \otimes I^*$)

**Estado:** ⏳ Pendiente  
**Dependencias:** ISSUE-002  
**Archivos Afectados:** `Matrix/Matrix/src/operational_model/kernel/formula_inference.py`, `tests/test_propositional_inference.py`

## Descripción

Sustituir las funciones de inferencia de `formula_inference.py` (`modus_ponens`, `hypothetical_syllogism`, `disjunctive_syllogism`) para que ejecuten el motor matricial en lugar de inspeccionar el AST mediante bucles de Python:
- **Modus Ponens y Silogismo Hipotético Matricial**: Calculado como $v^* = v \otimes I^*$, donde $I^*$ es la clausura transitiva de la matriz de implicaciones $I$ derivada por `recursive_power()`.
- **Silogismo Disyuntivo Matricial**: Calculado mediante el producto booleano del vector de asignaciones sobre las matrices de cláusulas $(C^+, C^-)$.

## Tareas

1. Refactorizar `modus_ponens` y `hypothetical_syllogism` en `formula_inference.py` para usar multiplicación matricial $v \otimes I^*$.
2. Refactorizar `disjunctive_syllogism` para usar evaluación de bitmasks / matrices de cláusulas.
3. Asegurar que las pruebas existentes en `tests/test_propositional_inference.py` pasen al 100%.
