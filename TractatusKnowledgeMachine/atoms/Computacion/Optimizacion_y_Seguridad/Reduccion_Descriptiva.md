---
topic: reduccion-descriptiva
use_when: Aplicable al contexto semantico y factual de Reduccion Descriptiva.
do_not_use_when: No utilizar fuera del dominio formal de logic-optimization.
id: atom-reduccion-descriptiva
title: Reduccion Descriptiva
five_wh_one_plus: what
tags:
- system:matrix
---
# Reducción Descriptiva

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Categorias_Sentido]]]
* [is_solved_by:: [[Enrutamiento_Jerarquico]]]
* [is_solved_by:: [[Algebra_Booleana]]]
* [is_solved_by:: [[Colapso_Dimensional]]]

---

## Qué es
El operador que detecta y extrae columnas tautológicas (aquellas con valor `1` para todos los objetos del contexto) de una matriz de hechos.

## Por qué es necesario
Las propiedades universalmente verdaderas no aportan información discriminativa interna (son *Sinnlos*). Eliminarlas ahorra cómputo y optimiza el almacenamiento.

## Cómo funciona
Si $\forall o, V_i(o,p) = 1$, la propiedad $p$ se elimina de la matriz booleana interna y se convierte en una **coordenada de ruteo** dentro de un contexto superior (el espacio padre). El espacio padre es otro $W_i$ cuya función es guardar los vectores puente que apuntan hacia los subcontextos correspondientes.

## Cuándo interviene
En la creación, limpieza y factorización de subcontextos (árboles lógicos). Actúa como el mecanismo que "sube" información común hacia la jerarquía superior.

## Dónde reside
En el optimizador del motor y en las reglas de construcción de los grafos jerárquicos.

## Para qué / Para quién
Para el gestor de memoria y el sistema de ruteo jerárquico.
