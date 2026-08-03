---
topic: funcion-objetivo-seleccion-dimensiones
use_when: Aplicable al contexto semantico y factual de Funcion Objetivo Seleccion
  Dimensiones.
do_not_use_when: No utilizar fuera del dominio formal de disambiguation.
id: atom-funcion-objetivo-seleccion-dimensiones
title: Funcion Objetivo Seleccion Dimensiones
five_wh_one_plus: what
tags:
- system:matrix
---
# Función Objetivo de Selección de Dimensiones

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Algoritmo_Minimizacion_ER]]]
* [mathematically_proves:: [[Construccion_Tensor_Jerarquico]]]
* [mathematically_proves:: [[Eje_B_Escalabilidad_Minimizacion_ER_y_Tensor_Jerarquico]]]

---

## Qué es
Es la fórmula matemática multicriterio (Anexo A.3.12) utilizada por el motor MEEL para elegir deterministamente la dimensión discriminativa óptima $D$ al colapsar o dividir subespacios semánticos.

---

## Fórmula Matemática

$$\text{score}(D) = w_1 \cdot \text{IG}(D) - w_2 \cdot \text{Cost}(D) - w_3 \cdot \text{Uncertainty}(D)$$

Donde:
* $\text{IG}(D)$: Ganancia de Información obtenida al incorporar la dimensión $D$.
* $\text{Cost}(D)$: Costo computacional de extender la matriz por bloques.
* $\text{Uncertainty}(D)$: Entropía residual restante tras la división.
