---
topic: modus-ponens-poc
use_when: Aplicable a la demostracion de compilacion de reglas proposicionales a matrices
  de incidencia e inferencia Modus Ponens.
do_not_use_when: No utilizar fuera del motor de compilacion de reglas Booleano.
id: atom-demostracion-compilacion-reglas-y-modus-ponens
title: Demostracion Compilacion Reglas y Modus Ponens
five_wh_one_plus: what
tags:
- system:matrix
---
# Demostración de Prueba de Concepto: Compilador de Reglas & Modus Ponens

**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_compiler_rule_matrix_compiler_py]]]
* [implements:: [[Source_Code_src_operational_model_inference_propositional_inference_py]]]
* [is_solved_by:: [[Compilador_Matricial_Reglas]]]
* [mathematically_proves:: [[Multiplicacion_Matricial_Booleana_y_Clausura_Transitiva]]]

---

## Qué es
Es la prueba de concepto de compilación de fórmulas bien formadas (FBF) proposicionales a matrices de incidencia ($I, C^+, C^-$) y ejecución de inferencia inductiva/deductiva en tiempo $\mathcal{O}(1)$.

---

## Mecanismo
Compila reglas lógicas complejas ($p \implies q$, $q \implies r$) en matrices de bits densas `uint64` y resuelve la clausura de deducción mediante multiplicación Booleana $v_{next} = v \otimes I^*$.

---

## Código Ejecutable de Referencia
* Compilador de Reglas: `src/operational_model/compiler/rule_matrix_compiler.py`
* Inferencia Proposicional: `src/operational_model/inference/propositional_inference.py`
* Pruebas Pytest: `tests/test_rule_matrix_compiler.py`, `tests/test_propositional_inference.py`
