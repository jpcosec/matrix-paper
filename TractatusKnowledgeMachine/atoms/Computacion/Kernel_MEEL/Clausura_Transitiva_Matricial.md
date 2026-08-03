---
topic: clausura-transitiva-matricial
use_when: Aplicable al contexto semantico y factual de Clausura Transitiva Matricial.
do_not_use_when: No utilizar fuera del dominio formal de meel-engine.
id: atom-clausura-transitiva-matricial
title: Clausura Transitiva Matricial
five_wh_one_plus: what
tags:
- system:matrix
---
# Clausura Transitiva Matricial

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_inference_transitive_closure_py]]]
* [is_solved_by:: [[Matrices_y_Tensores]]]
* [is_solved_by:: [[W_Operativo]]]

---

## Qué es
Es la resolución de la transitividad ($aRb \land bRc \implies aRc$) y simetría de relaciones de dominio mediante operaciones de matriz de adyacencia y potenciación matricial reflexivo-transitiva.

## Por qué es necesario
Reemplaza la exploración iterativa de hechos mediante grafos y listas por operaciones de producto matricial Booleano $M_R^* = \sum M_R^k$.

## Cómo funciona
1. **Construcción:** Se crea la matriz de adyacencia binaria $M_R \in \{0, 1\}^{|T| \times |T|}$ para la relación $R$.
2. **Clausura:** Se calcula $M_R^* = (M_R \lor \mathbb{I})^N$ mediante potenciación binaria (`transitive_closure()`).
3. **Simetría:** Para relaciones conmutativas, se calcula $M_R^{\text{sym}} = M_R \lor M_R^T$.

## Cuándo interviene
Cada vez que se ingesta una nueva relación transitiva o simétrica en el $W_i$.

## Dónde reside
En el motor relacional (`transitive_inference.py` y `commutative_inference.py`), integrado con `BooleanMatrix`.

## Para qué / Para quién
Deriva automáticamente todas las conexiones relacionales implícitas con complejidad computacional reducida en $\log_2(N)$ pasos matriciales.
