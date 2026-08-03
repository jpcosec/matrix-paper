---
topic: alucinaciones-inducidas-por-rag-y-conflicto-de-conocimiento
use_when: Aplicable al contexto semantico y factual de Alucinaciones Inducidas por
  RAG y Conflicto de Conocimiento.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-alucinaciones-inducidas-por-rag-y-conflicto-de-conocimiento
title: Alucinaciones Inducidas por RAG y Conflicto de Conocimiento
five_wh_one_plus: what
tags:
- system:matrix
---
# Alucinaciones Inducidas por RAG y Conflicto de Conocimiento (Knowledge Conflict)

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_arxiv2305_13300_pdf]]]
* [is_solved_by:: [[BlockMatrix]]]
* [is_solved_by:: [[Eje_D_Diferenciacion_OWL_KGs_y_Vectorizacion_Bitwise]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [explains_failure_of:: [[Matriz_por_Bloques]]]

---

## Qué es
Es el fenómeno por el cual la inyección de contexto externo mediante **Generación Aumentada por Recuperación (RAG)** o Grafos de Conocimiento no elimina las alucinaciones y genera **Conflictos de Conocimiento** entre los datos inyectados y los priors memorizados.

---

## Mecanismo de Falla
Ocurre cuando la información inyectada contradice el "conocimiento paramétrico" memorizado durante el pre-entrenamiento. Debido al sesgo de **sobreconfianza (*over-confidence*)**, el LLM ignora el contexto correcto recién inyectado y alucina una combinación híbrida apoyándose en sus sesgos paramétricos previos.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Wei et al. (2024)**: *Measuring and Reducing LLM Hallucination Without Gold-Standard Answers*
  * PDF en Repositorio: [arxiv2402_10412.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2402_10412.pdf)
* 📄 **Feldman et al. (2023)**: *Trapping LLM Hallucinations Using Tagged Context Prompts*
  * PDF en Repositorio: [arxiv2306_06085.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2306_06085.pdf)

---

## Integración en el Paper NeurIPS (*Retrieval & External Knowledge Integration*)
Se incluye en la discusión sobre RAG y Grafos de Conocimiento para advertir que inyectar contexto no basta, **exigiendo la Matriz por Bloques $WC_i$ para desactivar bitwise las proposiciones previas incompatibles**.
