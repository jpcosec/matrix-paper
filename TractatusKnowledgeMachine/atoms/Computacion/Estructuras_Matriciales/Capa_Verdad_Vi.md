---
topic: capa-verdad-vi
use_when: Aplicable al contexto semantico y factual de Capa Verdad Vi.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-capa-verdad-vi
title: Capa Verdad Vi
five_wh_one_plus: what
tags:
- system:matrix
---
# Capa de Verdad (Vi)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_matrices_vi_matrix_py]]]
* [is_solved_by:: [[Matrices_y_Tensores]]]

---

## Qué es
El repositorio binario que almacena los hechos positivos y negativos observados o inyectados. Representa "lo que es el caso".

## Por qué es necesario
Separa la factualidad pura de la estructura lógica. Permite actualizar la realidad sin cambiar las reglas de sentido del sistema.

## Cómo funciona
Almacena bits en una matriz de alta densidad. Un '1' representa un hecho positivo; un '0' puede representar un hecho negativo o una falta de información (según el contexto).

## Cuándo interviene
Durante la inyección de datos y el mantenimiento de la base de conocimientos.

## Dónde reside
En el nivel de persistencia de datos (bit-matrices materializadas).

## Para qué / Para quién
Para el motor de evaluación, proveyendo los datos crudos para ser filtrados por la capa de sentido.
