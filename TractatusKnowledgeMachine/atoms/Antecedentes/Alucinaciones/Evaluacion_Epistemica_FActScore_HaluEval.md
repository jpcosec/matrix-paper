---
topic: evaluacion-epistemica-factscore-halueval
use_when: Aplicable al contexto semantico y factual de Evaluacion Epistemica FActScore
  HaluEval.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-evaluacion-epistemica-factscore-halueval
title: Evaluacion Epistemica FActScore HaluEval
five_wh_one_plus: what
tags:
- system:matrix
---
# Métricas de Evaluación Epistémica: FActScore y HaluEval

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_factscore2023_pdf]]]
* [explains_failure_of:: [[Diferenciacion_Factualidad_Conocimiento_Alucinacion]]]
* [explains_failure_of:: [[Taxonomia_SOTA_Alucinaciones]]]
* [explains_failure_of:: [[Hecho_Atomico_CDV]]]

---

## Qué es
Es el conjunto de marcos empíricos desarrollados por el SOTA para medir cuantitativamente la precisión fáctica a nivel atómico en las respuestas generadas por Grandes Modelos de Lenguaje.

---

## Métricas Clave

1. **FActScore (Min et al. 2023):** Descompone la respuesta continua del modelo en una serie de proposiciones atómicas individuales $p_1, p_2, \dots, p_n$ y evalúa la veracidad de cada una contra una base de conocimiento oráculo (como Wikipedia).
2. **HaluEval (Li et al. 2023):** Benchmark diseñado para evaluar la capacidad de detección de alucinaciones en preguntas/respuestas, resúmenes y diálogo.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Min et al. (FActScore 2023)**: *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Atom Generation*
  * PDF en Repositorio: [factscore2023.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/factscore2023.pdf)
  * Clave BibTeX: `@inproceedings{factscore2023}`
