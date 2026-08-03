---
topic: matrices-y-tensores
use_when: Aplicable al contexto semantico y factual de Matrices y Tensores.
do_not_use_when: No utilizar fuera del dominio formal de matrix-algebra.
id: atom-matrices-y-tensores
title: Matrices y Tensores
five_wh_one_plus: what
tags:
- system:matrix
---
# Matrices y Tensores

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Contexto_Logico]]]
* [mathematically_proves:: [[S_Expressions]]]

---

## Qué es
La estructura física de almacenamiento de hechos. Una matriz 2D representa una relación binaria (ej. Objeto-Propiedad), mientras que un tensor es una composición de matrices que representan relaciones de mayor aridad.

## Por qué es necesario
Permite utilizar el hardware moderno (CPU/GPU) de forma eficiente mediante operaciones de bits y álgebra lineal, evitando la lentitud de los grafos tradicionales de punteros.

## Cómo funciona
Codifica la existencia de un hecho como un bit (1) en una coordenada definida por los ejes del espacio lógico $L_i$.

## Cuándo interviene
En cada operación de escritura (inyección de hechos) o lectura (consulta).

## Dónde reside
En la capa de almacenamiento persistente y en la memoria volátil del motor durante el cálculo.

## Para qué / Para quién
Para el motor de ejecución, proporcionando una estructura de datos de alta densidad y acceso $O(1)$.
