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
* [is_solved_by:: [[Manejo_de_Contradicciones]]]
* [is_solved_by:: [[Hecho_Atomico_CDV]]]
* [is_solved_by:: [[Matriz_por_Bloques]]]

---

## Qué es
Es el flujo formal de 4 etapas que transforma lenguaje natural —o contenido ya estandarizado (S-Expressions, RDF/Turtle, OWL)— en coordenadas de matrices booleanas $V_i, S_i, W_i^*$.

## Por qué es necesario
Garantiza que la información exterior pase por un proceso estricto de descomposición, canonización y **chequeo de sentido en dos pasos** antes de poder alterar el espacio veritativo factual.

## Cómo funciona
1. **Descomposición en Forma Estándar:** Separa el significado del azúcar sintáctico y lo expresa en una representación estandarizada (S-Expressions, RDF/Turtle u OWL). Propuesta: LLMs chicas como descompositores de superficie — absorben la variabilidad de signos (incluido el anclaje signo→símbolo a coordenadas $L_i$ y el plegado de alias vía `equivalent`) pero **no toman decisiones lógicas**. El contenido ya estandarizado (archivos `.owl`, `.ttl`, streams de S-expressions) omite esta etapa y entra directamente en la siguiente.
2. **Reducción a Proposiciones Candidato:** Produce la forma homogénea `(R a b)` — proposiciones *candidato* que aún no tienen estatus de verdad ni presencia en el sistema.
3. **Chequeo de Sentido en Dos Pasos:**
   * **(a) Indexación por contexto:** El candidato se enruta al contexto que indexa su cruce; si ningún contexto admite la combinación (dominio, relación), $S_i = 0$ y se rechaza como *Unsinnig* — el absurdo se evita por construcción, **antes** de cualquier evaluación de verdad.
   * **(b) Chequeo de contradicción:** Los candidatos admisibles se contrastan contra los hechos ya asertados $V_i$ del contexto; un conflicto produce una **señal explícita de contradicción**, nunca una sobrescritura silenciosa (ver [[Manejo_de_Contradicciones]]).
4. **Cómputo Matricial ($V_i, W_i^*$):** Solo los candidatos que pasan ambos chequeos actualizan o consultan $V_i$; la inferencia procede por multiplicación matricial booleana y colapso dimensional bitwise, calculando la proyección operativa final:
   $$W_i^* = V_i \odot S_i$$

## Cuándo interviene
Cada vez que un texto en lenguaje natural, un comando de usuario, una sugerencia de un LLM o un artefacto estandarizado (`.owl`, `.ttl`, S-expressions) entra al sistema.

## Dónde reside
En la arquitectura de fronteras del sistema (`docs/language_to_matrix_pipeline.md`) conectando los parsers de superficie con el motor [[MEEL]].

## Para qué / Para quién
Proporciona la garantía de integridad que permite al motor relacional razonar sin riesgo de alucinaciones sobre datos provenientes del lenguaje natural.
