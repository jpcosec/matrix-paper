---
topic: mascara-sentido-en-mecanismos-atencion
use_when: Aplicable al contexto semantico y factual de Mascara Sentido en Mecanismos
  Atencion.
do_not_use_when: No utilizar fuera del dominio formal de logic-optimization.
id: atom-mascara-sentido-en-mecanismos-atencion
title: Mascara Sentido en Mecanismos Atencion
five_wh_one_plus: what
tags:
- system:matrix
---
# Máscara de Sentido en Mecanismos de Atención y Pérdida Lógica

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Capa_Sentido_Si]]]
* [is_solved_by:: [[Acoplamiento_Neuro_Estocastico_Simbolico]]]
* [implements:: [[MEEL]]]
* [is_solved_by:: [[Matriz_por_Bloques]]]

---

## Qué es
Es la propuesta de integración de Fase 3 (Discusión del manuscrito NeurIPS) donde la Máscara de Sentido Booleana $S_i$ se inyecta directamente dentro de la matriz de atención del Transformer durante el entrenamiento o la inferencia:

$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{QK^T}{\sqrt{d_k}} + \mathbf{M}_{S_i}\right) V$$

Donde $\mathbf{M}_{S_i}$ aplica una penalización $-\infty$ a las posiciones con $S_i = 0$, actuando como una **Función de Pérdida Lógica** que modula el gradiente durante el aprendizaje por refuerzo (RL).
