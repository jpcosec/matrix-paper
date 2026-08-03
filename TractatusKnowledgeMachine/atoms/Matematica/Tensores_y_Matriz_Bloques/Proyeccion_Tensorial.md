---
topic: projection
use_when: Para definir la extracción matemática de sub-matrices desde el hipertensor
  canónico.
id: atom-proyeccion-tensorial
title: Proyeccion Tensorial
five_wh_one_plus: what
tags:
- system:matrix
---
# Proyección Tensorial (Slicing)

**Categoría Padre:** [[Tensores_y_Matriz_Bloques]]
**Relaciones 5W1H+:**
* [extracts_from:: [[Hipertensor_Canonico]]]
* [generates:: [[Capa_Verdad_Vi]]]
* [generates:: [[Capa_Sentido_Si]]]

## Qué es
Es la operación algebraica mediante la cual se extrae una sub-matriz bidimensional densa a partir del espacio n-dimensional disperso del `Hipertensor_Canonico`.

## Por qué es necesario
Porque las inferencias de Modus Ponens ($v \otimes I^*$) requieren matrices locales bidimensionales ($V_i$, $S_i$). No se puede hacer algebra matricial rápida directamente sobre una base de datos 3D masiva sin antes proyectar los ejes relevantes.

## Cómo funciona
Dada una Relación $R_k$ y dos subconjuntos de Símbolos $A$ (dominio) y $B$ (codominio), la proyección se define como:
$P(A, R_k, B) = \mathcal{H}[A, R_k, B]$
Donde cada elemento $(x, y)$ de la matriz resultante corresponde a la evaluación de la proposición $(R_k, A_x, B_y)$ en el hipertensor.
