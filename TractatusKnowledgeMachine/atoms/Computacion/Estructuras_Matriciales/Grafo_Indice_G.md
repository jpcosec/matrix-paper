---
topic: grafo-indice-g
use_when: Aplicable al contexto semantico y factual de Grafo Indice G.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-grafo-indice-g
title: Grafo Indice G
five_wh_one_plus: what
tags:
- system:matrix
---
# Grafo Índice (G)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Modelo_SMG]]]
* [is_solved_by:: [[Representacion_Flotante]]]
* [is_solved_by:: [[Matrices_y_Tensores]]]

---

## Qué es
La capa del modelo que organiza las dimensiones y proyecciones, actuando como un índice público e invertido de la base de datos de hechos.

## Por qué es necesario
Cumple con la filosofía del "juego del lenguaje" de Wittgenstein: los significados deben ser públicos y externos al contexto interno. Permite consultar rápidamente y detectar colisiones lógicas.

## Cómo funciona
Mantiene materializada la Matriz Transpuesta ($M^T$) de los contextos. Si dos conceptos comparten exactamente los mismos valores en la transpuesta, el Grafo detecta una colisión y ejecuta la rutina `expand_collision` para inyectar nuevas dimensiones discriminativas.

## Cuándo interviene
Durante búsquedas inversas ("¿qué conceptos tienen la propiedad X?") y durante la desambiguación.

## Dónde reside
Capa superior del motor, por fuera de las matrices puras individuales ($W_i$).

## Para qué / Para quién
Para el sistema de recuperación de información y refinamiento del árbol de conocimiento.
