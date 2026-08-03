---
topic: matrices-puras
use_when: Aplicable al contexto semantico y factual de Matrices Puras.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-matrices-puras
title: Matrices Puras
five_wh_one_plus: what
tags:
- system:matrix
---
# Matrices Puras

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Omnirepresentacion]]]
* [is_solved_by:: [[Contexto_Logico]]]
* [is_solved_by:: [[Matrices_y_Tensores]]]

---

## Qué es
Son matrices booleanas densas, pequeñas y aisladas que representan un único contexto específico sin mezclarlo con otros.

## Por qué es necesario
Es la forma más eficiente de guardar información y realizar cálculos lógicos. Evita el desperdicio de memoria de las matrices gigantes y permite una velocidad de acceso extrema en Rust.

## Cómo funciona
A diferencia de la omnirepresentación, la matriz pura solo tiene los ejes de su $L_i$. Las relaciones con otros contextos no están dentro de la matriz, sino que se resuelven mediante vectores puente ($p$) en el momento de la consulta.

## Cuándo interviene
Es el formato de almacenamiento interno por defecto del motor [[MEEL]].

## Dónde reside
En el núcleo de almacenamiento y cálculo del motor.

## Para qué / Para quién
Para el motor de lógica pura, garantizando que el sistema sea escalable y no sufra de explosión dimensional.
