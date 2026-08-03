---
topic: expansion-submatricial-recursiva
use_when: Aplicable al contexto semantico y factual de Expansion Submatricial Recursiva.
do_not_use_when: No utilizar fuera del dominio formal de disambiguation.
id: atom-expansion-submatricial-recursiva
title: Expansion Submatricial Recursiva
five_wh_one_plus: what
tags:
- system:matrix
---
# Expansión Submatricial Recursiva

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Construccion_Tensor_Jerarquico]]]
* [mathematically_proves:: [[BlockMatrix]]]
* [mathematically_proves:: [[Eje_B_Escalabilidad_Minimizacion_ER_y_Tensor_Jerarquico]]]

---

## Qué es
Es el mecanismo algorítmico (Anexo C) desencadenado dinámicamente cuando se detecta una colisión semántica o ambigüedad en un subcontexto $W_i$.

---

## Mecanismo de Expansión
En lugar de aumentar globalmente las dimensiones de la matriz $N \times N$, el sistema genera un subnodo hijo $W_{i}'$ y proyecta un sub-tensor discriminativo $D_i$, ramificando el árbol jerárquico y acotando el crecimiento de memoria a $\mathcal{O}(N \log N)$.
