---
topic: dicotomia-hk-minus-vs-hk-plus
use_when: Aplicable al contexto semantico y factual de Dicotomia HK Minus vs HK Plus.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-dicotomia-hk-minus-vs-hk-plus
title: Dicotomia HK Minus vs HK Plus
five_wh_one_plus: what
tags:
- system:matrix
---
# Dicotomía Epistémica: Ignorancia ($HK^-$) vs. Error a Pesar de Saber ($HK^+$)

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_iclr2025_a712d4_pdf]]]
* [explains_failure_of:: [[Diferenciacion_Factualidad_Conocimiento_Alucinacion]]]
* [explains_failure_of:: [[Arquitectura_Neuro_Estocastica]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [explains_failure_of:: [[Matriz_por_Bloques]]]

---

## Qué es
Es la taxonomía epistémica moderna que divide los errores de generación en LLMs en dos fenómenos con causas estructurales distintas:
1. **$HK^-$ (Ignorancia Paramétrica):** El modelo alucina porque la información requerida no fue codificada en los parámetros durante el entrenamiento.
2. **$HK^+$ (Error a Pesar del Conocimiento):** El modelo alucina a pesar de poseer el conocimiento factual correcto en sus representaciones internas latentes.

---

## Mecanismo en Espacios Continuos
Auditar los estados latentes profundos (mediante *linear probes*) revela que las capas intermedias contienen la representación de verdad ($V_i=1$). Sin embargo, la sensibilidad al prompt y la **decodificación estocástica de superficie ($S$) desvía al decodificador**, produciendo una afirmación falsa.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Orgad et al. (ICLR 2025)**: *LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations*
  * PDF en Repositorio: [iclr2025_a712d4.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/iclr2025_a712d4.pdf)
* 📄 **Simhi et al. (2024)**: *Distinguishing Ignorance from Error in LLM Hallucinations*
  * PDF en Repositorio: [arxiv2410_22071.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2410_22071.pdf)

---

## Integración en el Paper NeurIPS (*Epistemic Evaluation / Latent Probing*)
Se incluye en la sección de evaluación epistémica para argumentar que el problema no es falta de datos, sino la infidelidad de la decodificación estocástica continua, **exigiendo la extracción directa desde la Matriz de Verdad Discreta $V_i$**.
