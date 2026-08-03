---
topic: juego-de-desambiguacion
use_when: Aplicable al contexto semantico y factual de Juego de Desambiguacion.
do_not_use_when: No utilizar fuera del dominio formal de disambiguation.
id: atom-juego-de-desambiguacion
title: Juego de Desambiguacion
five_wh_one_plus: what
tags:
- system:matrix
---
# El Juego de la Desambiguación

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_game_wi_game_py]]]
* [mathematically_proves:: [[Colapso_Dimensional]]]
* [mathematically_proves:: [[Representacion_Flotante]]]
* [mathematically_proves:: [[Enrutamiento_Jerarquico]]]
* [mathematically_proves:: [[Capa_Sentido_Si]]]

---

## Qué es
Es el procedimiento algebraico y relacional mediante el cual el motor detecta colisiones de indistinguibilidad entre dos o más entidades ($a_1, a_2$) en un espacio lógico $W_i$ y fuerza la inyección de dimensiones discriminativas o la partición en subcontextos.

## Por qué es necesario
Cuando dos objetos comparten la misma combinación de bits para todas las propiedades mapeadas en $W_i$, son lógicamente colisionantes y devuelven falsos positivos en las búsquedas. El juego de desambiguación garantiza que cada entidad tenga una firma binaria única sin recurrir a esencias ocultas o vectores latentes continuos.

## Cómo funciona
1. **Detección de Colisión:** Se calcula la matriz de colisión de objetos:
   $$\mathbf{C} = (W_i \otimes W_i^T) - \mathbb{I}$$
   Si $\mathbf{C}_{i, j} > 0$, los objetos $i$ y $j$ colisionan (ej. *lechuga* y *espinaca* con la propiedad `hoja`).
2. **Estrategia A (Inyección de Dimensión Discriminativa $D_i$):** Se expande el espacio de coordenadas $L_i$ agregando una nueva propiedad discriminatoria (ej. `hoja_rugosa` vs `hoja_lisa`).
3. **Estrategia B (Refinamiento Contextual $W_i'$):** Se crea un subcontexto hijo $W_i'$ que hereda la propiedad diferenciadora y se ajusta la máscara de sentido $S_i$ para marcar como inaplicables ($\emptyset$) esas propiedades en objetos fuera de la categoría (ej. *zanahoria* o *apio*).

## Cuándo interviene
Al ejecutar la operación `collapse_similarity()`, al resolver consultas ambiguas en $W_i$, o al expandir el conocimiento de una Máquina de Estados de Evaluación Lógica.

## Dónde reside
En el núcleo algebraico matricial (`BooleanMatrix.collapse_similarity()`), en los índices invertidos y en los algoritmos de refinamiento contextual.

## Para qué / Para quién
Proporciona la garantía matemática de que el universo de conocimiento puede crecer infinitamente manteniendo cero ambigüedades descriptivas entre sus elementos.
