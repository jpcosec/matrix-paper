---
topic: pipeline-ingesta-lenguaje-matrix
use_when: Aplicable al contexto semantico y factual de Pipeline Ingesta Lenguaje Matrix.
do_not_use_when: No utilizar fuera del dominio formal de parsers-runtimes.
id: atom-pipeline-ingesta-lenguaje-matrix
title: Pipeline Ingesta Lenguaje Matrix
five_wh_one_plus: what
tags:
- system:matrix
---
# Pipeline de Ingesta del Lenguaje a Matrix

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Modelo_SMG]]]
* [is_solved_by:: [[Signo_vs_Simbolo]]]
* [is_solved_by:: [[Anclaje_Simbolos_Grounding]]]
* [implements:: [[S_Expressions]]]
* [is_solved_by:: [[Capa_Sentido_Si]]]
* [is_solved_by:: [[Capa_Verdad_Vi]]]
* [is_solved_by:: [[Hecho_Atomico_CDV]]]
* [is_solved_by:: [[Matriz_por_Bloques]]]

---

## Qué es
Es el flujo formal de 5 etapas que transforma enunciados de lenguaje natural (o salidas estocásticas de LLMs) en coordenadas de matrices booleanas $V_i, S_i, W_i^*$.

## Por qué es necesario
Garantiza que la información exterior pase por un proceso estricto de traducción, canonización y validación de sentido antes de poder alterar el espacio veritativo factual.

## Cómo funciona
1. **Anclaje de Símbolos (*Symbol Grounding*):** Mapea signos lingüísticos exteriores a identificadores de símbolo normalizados $L_i$ y pliega alias vía `equivalent`.
2. **Parseo Semántico & Frames:** Extrae intenciones y estructuras (`ImperativeFrame`, `QueryFrame`, UNL, OWL).
3. **Reducción a Forma Canónica ($S$-Expressions):** Produce la representación intermedia homogénea `(R a b)`.
4. **Validación por Máscara de Sentido ($S_i$):** Si $S_i = 1$ (*Sinnvoll*), aprueba la ingesta; si $S_i = 0$ (*Unsinnig*), rechaza la proposición como absurdo semántico.
5. **Cómputo Matricial ($V_i, W_i^*$):** Actualiza la matriz de verdad $V_i$ y calcula la proyección operativa final:
   $$W_i^* = V_i \odot S_i$$

## Cuándo interviene
Cada vez que un texto en lenguaje natural, un comando de usuario o una sugerencia de un LLM entra al sistema.

## Dónde reside
En la arquitectura de fronteras del sistema (`docs/language_to_matrix_pipeline.md`) conectando los parsers de superficie con el motor [[MEEL]].

## Para qué / Para quién
Proporciona la garantía de integridad que permite al motor relacional razonar sin riesgo de alucinaciones sobre datos provenientes del lenguaje natural.
