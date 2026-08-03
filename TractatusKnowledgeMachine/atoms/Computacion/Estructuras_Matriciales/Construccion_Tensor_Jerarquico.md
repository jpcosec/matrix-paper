---
topic: construccion-tensor-jerarquico
use_when: Aplicable al contexto semantico y factual de Construccion Tensor Jerarquico.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-construccion-tensor-jerarquico
title: Construccion Tensor Jerarquico
five_wh_one_plus: what
tags:
- system:matrix
---
# Construcción del Tensor Jerárquico

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Tensor_Jerarquico_NxNxC]]]
* [is_solved_by:: [[Representacion_Plana_vs_Tensorial]]]
* [is_solved_by:: [[Enrutamiento_Jerarquico]]]
* [is_solved_by:: [[Matriz_por_Bloques]]]

---

## Qué es
Es el algoritmo paso a paso mediante el cual el motor apila y conecta juegos de lenguaje locales 2D ($W_i$) para construir un espacio tensorial multi-dimensional ($N \times N \times C_1 \times C_2 \dots$).

## Por qué es necesario
Explicita el procedimiento exacto para dividir el espacio de conocimiento en subcontextos enlazados, evitando la explosión combinatoria de celdas inaplicables en matrices 2D planas.

## Cómo funciona
1. **Base 2D ($N \times N$):** Se instancian las entidades $N$ y relaciones generales en un `WiGame` base.
2. **Identificación de Hiperdimensión ($C_k$):** Un atributo o tautología común (ej. `es_vegetal`) se selecciona como dimensión de partición $C_1$.
3. **Creación del Sub-tensor ($W_1$):** Se crea un nuevo `WiGame` hijo que contiene únicamente el subconjunto de entidades de $C_1$ y sus propiedades especializadas (ej. `hoja_rugosa`).
4. **Enlace por Matriz de Ruteo ($WC_i$):** Se crea un `RoutingProjection` $WC_1 \in \{0, 1\}^{|W_0| \times |W_1|}$ que actúa como la matriz de hiperaristas.
5. **Cómputo Multihop:** Las consultas navegan multiplicando las matrices de ruteo secuencialmente: $P_{\text{ruta}} = WC_1 \otimes WC_2 \otimes \dots \otimes WC_k$.

## Cuándo interviene
Durante el diseño de la taxonomía del conocimiento, la ingesta jerárquica y el ruteo de consultas (`route_search`).

## Dónde reside
En `src/operational_model/routing/` (`context.py`, `routing_projection.py`) y en `src/operational_model/system/logical_system_queries.py`.

## Para qué / Para quién
Proporciona la guía exacta de implementación para escalar la Máquina de Conocimiento a millones de hechos y dominios sin degradar el rendimiento.
