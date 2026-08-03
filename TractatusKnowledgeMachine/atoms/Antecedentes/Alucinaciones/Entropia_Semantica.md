---
topic: entropia-semantica
use_when: Aplicable al contexto semantico y factual de Entropia Semantica.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-entropia-semantica
title: Entropia Semantica
five_wh_one_plus: what
tags:
- system:matrix
---
# Entropía Semántica (Semantic Entropy)

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_selfcheckgpt2023_pdf]]]
* [explains_failure_of:: [[Origen_Geometrico_y_Espacio_Vectorial]]]
* [explains_failure_of:: [[Arquitectura_Neuro_Estocastica]]]
* [explains_failure_of:: [[Algebra_Booleana]]]

---

## Qué es
Es la métrica probabilística desarrollada por Farquhar et al. (Nature 2024) para detectar alucinaciones por confabulación midiendo la incertidumbre y divergencia estadística no a nivel de superficie de tokens, sino a nivel de **clases de equivalencia de significado semántico**.

---

## Mecanismo
Muestrea múltiples respuestas continuas para una misma consulta y las agrupa según su equivalencia lógica. Si la entropía entre las clases semánticas es alta, se clasifica como una alucinación por confabulación.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **SelfCheckGPT (Manakul et al. 2023)**: *SelfCheckGPT: Zero-Resource LLM Hallucination Detection via Sampling Consistency*
  * PDF en Repositorio: [selfcheckgpt2023.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/selfcheckgpt2023.pdf)
  * Clave BibTeX: `@article{selfcheckgpt2023}`
