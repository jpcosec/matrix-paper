---
topic: inferencia-deductiva-matricial
use_when: Aplicable al contexto semantico y factual de Inferencia Deductiva Matricial.
do_not_use_when: No utilizar fuera del dominio formal de meel-engine.
id: atom-inferencia-deductiva-matricial
title: Inferencia Deductiva Matricial
five_wh_one_plus: what
tags:
- system:matrix
---
# Inferencia Deductiva Matricial

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Compilador_Matricial_Reglas]]]
* [is_solved_by:: [[Algebra_Booleana]]]
* [implements:: [[MEEL]]]

---

## Qué es
Es la ejecución de reglas lógicas deductivas (Modus Ponens, Silogismo Hipotético y Silogismo Disyuntivo) mediante operaciones de multiplicación vectorial-matricial y evaluación de bitmasks sobre el semianillo booleano.

## Por qué es necesario
Garantiza que la deducción formal no dependa de algoritmos iterativos ni de inspección sintáctica de árboles, logrando una velocidad de inferencia a nivel de instrucciones de silicio.

## Cómo funciona
- **Modus Ponens & Silogismo Hipotético:** Dado un vector de premisas verdaderas $v \in \{0, 1\}^N$ y la clausura reflexivo-transitiva de implicaciones $I^*$, el estado deductivo resultante se calcula como:
  $$v^* = v \otimes I^*$$
- **Silogismo Disyuntivo:** Evalúa la combinación de cláusulas disyuntivas reduciendo las máscaras $C^+$ y $C^-$ frente a las literales negadas o afirmadas.

## Cuándo interviene
Durante el procesamiento de inferencias lógicas en consultas o resoluciones de deducciones en el $W_i$.

## Dónde reside
En el motor de ejecución del kernel (`formula_inference.py`), operando sobre las matrices de `RuleMatrixCompiler`.

## Para qué / Para quién
Proporciona deducción formal auditable, exacta y libre de alucinaciones para el sistema de razonamiento.
