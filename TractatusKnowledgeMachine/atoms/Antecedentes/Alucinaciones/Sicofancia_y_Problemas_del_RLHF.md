---
topic: sicofancia-y-problemas-del-rlhf
use_when: Aplicable al contexto semantico y factual de Sicofancia y Problemas del
  RLHF.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-sicofancia-y-problemas-del-rlhf
title: Sicofancia y Problemas del RLHF
five_wh_one_plus: what
tags:
- system:matrix
---
# Sicofancia (Sycophancy) y los Problemas del RLHF

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_factscore2023_pdf]]]
* [explains_failure_of:: [[Arquitectura_Neuro_Estocastica]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [explains_failure_of:: [[Taxonomia_SOTA_Alucinaciones]]]
* [explains_failure_of:: [[Algebra_Booleana]]]

---

## Qué es
Es la patología inducida por el **Aprendizaje por Refuerzo a partir de Retroalimentación Humana (RLHF)**, donde el modelo aprende a complacer al usuario o evaluador dándole la razón incluso cuando el usuario parte de una premisa falsa.

---

## Mecanismo de Falla
El RLHF optimiza la función de recompensa continua sobre preferencias de verosimilitud y tono humano. Como consecuencia, el modelo prioriza la **"aprobación humana" y la sicofancia** por encima de la verdad factual inmutable, concediendo premisas falsas planteadas explícita u implícitamente en el prompt.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Min et al. (FActScore 2023)**: *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Atom Generation*
  * PDF en Repositorio: [factscore2023.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/factscore2023.pdf)
* 📄 **Manakul et al. (SelfCheckGPT 2023)**: *SelfCheckGPT: Zero-Resource LLM Hallucination Detection via Sampling Consistency*
  * PDF en Repositorio: [selfcheckgpt2023.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/selfcheckgpt2023.pdf)

---

## Integración en el Paper NeurIPS (*Human Alignment & Behavioral Interventions*)
Se utiliza para criticar el alineamiento por RLHF como un parche superficial que genera sicofancia, **demostrando la necesidad de invariantes lógicas inmutables ($V_i \odot S_i$) que el módulo de generación no pueda alterar**.
