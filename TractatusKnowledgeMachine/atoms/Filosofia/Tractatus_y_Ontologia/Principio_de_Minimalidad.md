---
topic: principio-de-minimalidad
use_when: Aplicable al contexto semantico y factual de Principio de Minimalidad.
do_not_use_when: No utilizar fuera del dominio formal de tractarian-philosophy.
id: atom-principio-de-minimalidad
title: Principio de Minimalidad
five_wh_one_plus: what
tags:
- system:matrix
---
# Principio de Minimalidad Discriminativa

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [defines:: [[TractatusKnowledgeMachine/atoms/Filosofia/Tractatus]]]
* [defines:: [[Representacion_Plana_vs_Tensorial]]]
* [defines:: [[Reduccion_Descriptiva]]]
* [defines:: [[Energia_Informacion]]]

---

## Qué es
Es la regla ontológica y computacional que establece que un juego de lenguaje local ($W_i$) debe contener únicamente el conjunto **mínimo e irreducible** de dimensiones y relaciones indispensables para desambiguar y discriminar las entidades de su universo.

## Por qué es necesario
1. **Prevención de explosión combinatoria:** Si un espacio $W_i$ incluye propiedades ajenas a su contexto local, la matriz se llena de celdas inaplicables (*Unsinnig* / $\emptyset$), degradando el espacio en memoria.
2. **Eficiencia de Cómputo ($E(R)$):** Elimina el gasto computacional de multiplicar ceros o valores nulos redundantes.
3. **Parsimonia Tractariana (TLP 5.4541):** En la lógica no hay nada superfluo. Una representación sobre-especificada introduce ruido y falsa complejidad.

## Cómo funciona
- **Reducción Descriptiva:** Las propiedades tautológicas (verdaderas para todos los elementos del subespacio, ej. `es_fruta`) se remueven de la matriz 2D plana y se promueven a hiperdimensiones de enrutamiento tensorial $C$.
- **Cierre de Desambiguación Mínimo:** La inyección de nuevas dimensiones se detiene exactamente en el punto donde la matriz de colisión $\mathbf{C} = (W_i \otimes W_i^T) - \mathbb{I} = \mathbf{0}$.

## Cuándo interviene
Durante el diseño de `LiSpace`, el refinamiento contextual de colisiones y la optimización de memoria en la ingesta.

## Dónde reside
En la filosofía del proyecto ("Minimal Agglomerative Text Retrieval Index"), los algoritmos de reducción descriptiva (`Reduccion_Descriptiva.md`) y la métrica $E(R)$.

## Para qué / Para quién
Asegura que cada bit almacenado en $V_i$ y $S_i$ contenga la máxima entropía informativa discriminativa con el menor costo de procesamiento posible.
