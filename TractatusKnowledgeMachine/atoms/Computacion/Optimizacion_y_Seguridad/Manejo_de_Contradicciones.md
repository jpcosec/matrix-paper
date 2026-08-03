---
topic: manejo-de-contradicciones
use_when: Aplicable al contexto semantico y factual de Manejo de Contradicciones.
do_not_use_when: No utilizar fuera del dominio formal de logic-optimization.
id: atom-manejo-de-contradicciones
title: Manejo de Contradicciones
five_wh_one_plus: what
tags:
- system:matrix
---
# Estrategias para el Manejo de Contradicciones

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[WiGame]]]
* [implements:: [[Capa_Verdad_Vi]]]
* [grounded_by:: [[Algoritmo_Minimizacion_ER]]]
* [is_solved_by:: [[Algebra_Booleana]]]
* [is_solved_by:: [[Juego_de_Desambiguacion]]]

---

## Qué es
Es el conjunto de formalizaciones lógicas (Anexo A.3.9) para detectar y resolver afirmaciones contradictorias ($p \land \neg p$) ingresadas en un mismo contexto $W_i$. Opera como el **paso (b) del chequeo de sentido** del [[Pipeline_Ingesta_Lenguaje_Matrix]]: tras la indexación por contexto (paso a), todo candidato admisible se contrasta contra los hechos ya asertados $V_i$; un conflicto emite una **señal explícita de contradicción** (nunca sobrescritura silenciosa), y las 3 estrategias siguientes son las políticas de resolución disponibles una vez emitida la señal.

---

## 3 Estrategias de Resolución

1. **Rechazo Estricto One-Hot:** Si un atributo es exclusivo (one-hot), afirmar un valor distinto genera un rechazo inmediato por violación de invariante.
2. **Objeto de Contradicción Explicitado:** La contradicción se marca como un estado inestable que requiere inyección de una dimensión discriminativa $D_i$ (Juego de Desambiguación).
3. **Resolución por Nivel de Confianza (Confidence-Based):** En ingesta automatizada, el hecho con mayor puntaje de procedencia prevalece, enviando el hecho anterior al historial de contexto.
