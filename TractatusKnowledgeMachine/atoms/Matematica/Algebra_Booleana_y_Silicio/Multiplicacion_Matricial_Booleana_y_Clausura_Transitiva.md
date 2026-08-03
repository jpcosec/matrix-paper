---
topic: multiplicacion-matricial-booleana-y-clausura-transitiva
use_when: Aplicable al contexto semantico y factual de Multiplicacion Matricial Booleana
  y Clausura Transitiva.
do_not_use_when: No utilizar fuera del dominio formal de discrete-math.
id: atom-multiplicacion-matricial-booleana-y-clausura-transitiva
title: Multiplicacion Matricial Booleana y Clausura Transitiva
five_wh_one_plus: what
tags:
- system:matrix
---
# Multiplicación Matricial Booleana y Clausura Transitiva

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_hardware_bool_mult_py]]]
* [mathematically_proves:: [[Eje_D_Diferenciacion_OWL_KGs_y_Vectorizacion_Bitwise]]]
* [mathematically_proves:: [[RuleMatrixCompiler]]]
* [mathematically_proves:: [[BooleanMatrix]]]

---

## Qué es
Es el sustrato algebraico lineal sobre semianillos Booleanos $(\lor, \land)$ que utiliza el motor MEEL para ejecutar inferencia deductiva Modus Ponens y clausura transitiva de relaciones en tiempo $\mathcal{O}(1)$.

---

## Formulaciones Matemáticas

1. **Modus Ponens Matricial:**
   $$v_{next} = v \otimes I^*$$
   Donde $I^*$ es la matriz de incidencia de reglas proposicionales FBF compilada por `RuleMatrixCompiler`.

2. **Clausura Transitiva de Relaciones ($M_R^*$):**
   $$M_R^* = \bigvee_{k=1}^N M_R^k = M_R \lor M_R^2 \lor \dots \lor M_R^N$$
   Calculada mediante multiplicación matricial Booleana binaria sobre palabras de procesador (`uint64`).
