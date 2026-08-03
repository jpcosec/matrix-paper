---
topic: mascaras-estructurales
use_when: Aplicable al contexto semantico y factual de Mascaras Estructurales.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-mascaras-estructurales
title: Mascaras Estructurales
five_wh_one_plus: what
tags:
- system:matrix
---
# Máscaras Estructurales

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Capa_Verdad_Vi]]]
* [is_solved_by:: [[Capa_Sentido_Si]]]
* [is_solved_by:: [[Matriz_por_Bloques]]]

---

## Qué es
El conjunto de cuatro máscaras booleanas paralelas que acompañan a un diccionario de conceptos para proteger la base de datos: `valid` (validez estructural), `sense` (sentido contextual), `observed` (verdad empírica) y `discriminative` (capacidad de distinguir).

## Por qué es necesario
Para evitar el colapso de información que ocurre al usar un solo vector de bits. Evita confundir "falso" con "absurdo", "no observado" o "no discriminativo".

## Cómo funciona
Cada hecho atómico es filtrado secuencialmente por estas máscaras antes de operar. Solo lo que es válido, tiene sentido y ha sido observado pasa a formar parte de la matriz operable final.

## Cuándo interviene
En cada inserción de un nuevo hecho y en la evaluación de una consulta.

## Dónde reside
En el motor de almacenamiento de matrices en Rust.

## Para qué / Para quién
Para el Validador de Tipos y el evaluador de [[W_Operativo]].
