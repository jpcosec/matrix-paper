---
topic: procedencia-y-evidencia
use_when: Aplicable al contexto semantico y factual de Procedencia y Evidencia.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-procedencia-y-evidencia
title: Procedencia y Evidencia
five_wh_one_plus: what
tags:
- system:matrix
---
# Rastreo de Procedencia y Evidencia (Provenance & Evidence Tracking)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Modelo_SMG]]]
* [implements:: [[BlockMatrix]]]
* [implements:: [[Capa_Verdad_Vi]]]
* [is_solved_by:: [[Pipeline_Ingesta_Lenguaje_Matrix]]]
* [is_solved_by:: [[Hecho_Atomico_CDV]]]

---

## Qué es
Es la formalización matemática y de software que registra el origen epistémico, la fuente documental, el artefacto ejecutable y el nivel de confianza de cada hecho atómico inscrito en el espacio de coordenadas de *Matrix*.

---

## Por qué es necesario
Impide que el sistema se convierta en un repositorio de ontologías inventadas o sin trazabilidad. Garantiza que cada proposición verdadera ($V_i=1$) mantenga un puntero auditable a su documento fuente o prueba de ejecución.

---

## Estructura Formal (Anexo A.3.6)
Para cada hecho $f = (s, r, o)$ en el espacio $L_i$, se asocia una tupla de procedencia:

$$\text{Prov}(f) = (\text{DocumentId}, \text{SpanOffset}, \text{ConfidenceScore}, \text{ExtractorId})$$

---

## Integración con MEEL
En la matriz $V_i$, los bits afirmativos retienen metadatos de procedencia que son preservados a través de las operaciones de deducción bitwise (`uint64`), permitiendo explicar el origen exacto de cualquier inferencia.
