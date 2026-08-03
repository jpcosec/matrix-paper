---
topic: omnirepresentacion
use_when: Aplicable al contexto semantico y factual de Omnirepresentacion.
do_not_use_when: No utilizar fuera del dominio formal de logic-optimization.
id: atom-omnirepresentacion
title: Omnirepresentacion
five_wh_one_plus: what
tags:
- system:matrix
---
# Omnirepresentación

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Maquina_Estados_DFA]]]
* [is_solved_by:: [[Enrutamiento_Jerarquico]]]

---

## Qué es
Una Matriz por Bloques (Block Matrix) generalizada que contiene múltiples subcontextos, sus reglas de enrutamiento y hechos en un mismo espacio topológico. 

## Por qué es necesario
Sirve como formato unificado para que las redes neuronales (LLMs) puedan ingerir y generar relaciones lógicas observando el grafo completo.

## Cómo funciona
Se compone de:
1. Una diagonal $m \times m$ ($WC_i$) que activa o desactiva contextos.
2. Bloques cruzados $m \times n$ (Don't Cares) que enrutan qué hechos pertenecen a qué contexto (Máscara de Sentido).
3. Un bloque $n \times n$ con la Matriz de Verdad empírica.

## Cuándo interviene
Principalmente como interfaz de I/O masiva para modelos estocásticos, a diferencia del motor interno que opera con "matrices puras" enrutadas por vectores.

## Dónde reside
En la frontera entre la red neuronal y la base de datos matriz.

## Para qué / Para quién
Para los LLMs, dándoles una visión plana y procesable de un grafo jerárquico complejo.
