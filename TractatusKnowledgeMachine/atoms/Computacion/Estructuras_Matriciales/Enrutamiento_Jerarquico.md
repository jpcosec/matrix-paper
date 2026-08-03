---
topic: enrutamiento-jerarquico
use_when: Aplicable al contexto semantico y factual de Enrutamiento Jerarquico.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-enrutamiento-jerarquico
title: Enrutamiento Jerarquico
five_wh_one_plus: what
tags:
- system:matrix
---
# Enrutamiento Jerárquico

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Colapso_Dimensional]]]
* [implements:: [[S_Expressions]]]

---

## Qué es
El mecanismo que permite navegar entre diferentes contextos ($W_i$) utilizando el resultado de una operación en un contexto como el índice de búsqueda en el siguiente.

## Por qué es necesario
Permite mantener matrices pequeñas y eficientes. Evita la necesidad de una "matriz universal" gigante, fragmentando el conocimiento en módulos especializados y conectados.

## Cómo funciona
Utiliza proyecciones y colapsos dimensionales recursivos. El resultado de operar sobre la dimensión de nivel superior ($C_{base}$) genera el vector de selección para la dimensión inmediatamente inferior ($C_{sub}$), y así sucesivamente hasta aterrizar en la matriz de hechos $N \times N$. Es un encadenamiento de multiplicaciones de tensores donde cada paso "abre" la siguiente capa de la jerarquía.

## Cuándo interviene
En consultas que atraviesan múltiples dominios de conocimiento o en razonamientos que requieren descender desde categorías generales a hechos específicos.

## Dónde reside
En el motor de orquestación de contextos del motor [[MEEL]].

## Para qué / Para quién
Para el motor de búsqueda, permitiendo una navegación determinista y rápida por el grafo de contextos.
