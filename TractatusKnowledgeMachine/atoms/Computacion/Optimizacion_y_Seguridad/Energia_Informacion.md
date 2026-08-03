---
topic: energia-informacion
use_when: Aplicable al contexto semantico y factual de Energia Informacion.
do_not_use_when: No utilizar fuera del dominio formal de logic-optimization.
id: atom-energia-informacion
title: Energia Informacion
five_wh_one_plus: what
tags:
- system:matrix
---
# Energía de Información E(R)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Modelo_SMG]]]
* [is_solved_by:: [[Representacion_Plana_vs_Tensorial]]]
* [grounded_by:: [[Principio_de_Minimalidad]]]

---

## Qué es
Es la métrica cuantitativa que mide la densidad informativa, calidad de discriminación y eficiencia de compresión de un juego de lenguaje matricial $W_i$.

## Por qué es necesario
Permite al motor evaluar de forma objetiva si un espacio lógico $W_i$ está optimizado, si contiene dimensiones superfluas (tautologías o redundancias) o si necesita ser reestructurado/desambiguado.

## Cómo funciona

### 1. Implementación en Código (`wi_game_queries.py`)
En el motor ejecutable, $E(R) \in (0, 1]$ se calcula como el promedio equilibrado de 4 densidades:
$$E(R) = \frac{1}{4} \left( c + i + o + d \right)$$

- **$c$ (Densidad de Sentido):** Fracción de celdas con sentido $S_i = \text{SINNVOLL}$ sobre el total $|A| \times |B|$.
- **$i$ (Verdad Factual):** Fracción de hechos empíricamente verdaderos ($V_i = 1 \land S_i = 1$).
- **$o$ (Observabilidad):** Proporción de hechos observados e ingestados.
- **$d$ (Poder Discriminativo):** Proporción de columnas no tautológicas:
  $$d = \frac{M - |\text{columnas tautológicas}|}{M}$$

### 2. Modelo Teórico General (*Whitepaper*)
En el marco funcional de gran escala, $E(R)$ pondera cuatro métricas topológicas:
$$E(R) = \alpha C(M) + \beta L(T \mid S) + \gamma Q(M, G) + \delta D(M)$$
donde $C$ es compresión semántica, $L$ es costo de reconstrucción textual, $Q$ es calidad de indexación en $G$, y $D$ es poder discriminatorio frente a colisiones.

## Cuándo interviene
Al ejecutar `wigame.information_energy()`, durante los procesos de desambiguación y al decidir la promoción de propiedades a hiperdimensiones tensoriales.

## Dónde reside
En `src/operational_model/system/wi_game_queries.py` y en los analizadores de optimización de grafo.

## Para qué / Para quién
Proporciona la función de pérdida lógica (*Logical Loss*) que permite al motor auto-optimizar la estructura de sus matrices y guiar la poda de dimensiones.
