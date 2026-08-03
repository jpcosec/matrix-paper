---
topic: ilusion-de-la-autocorreccion
use_when: Aplicable al contexto semantico y factual de Ilusion de la Autocorreccion.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-ilusion-de-la-autocorreccion
title: Ilusion de la Autocorreccion
five_wh_one_plus: what
tags:
- system:matrix
---
# La Ilusión de la Autocorrección (The Self-Correction Illusion)

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_symcode2025_pdf]]]
* [explains_failure_of:: [[Eje_A_Justificacion_Matematica_Limites_Continuos]]]
* [is_solved_by:: [[Eje_E_Implementacion_MEEL_y_Compilador_Matricial]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [explains_failure_of:: [[Maquina_Estados_DFA]]]

---

## Qué es
Es el fenómeno empírico demostrado por el SOTA según el cual pedirle a un LLM que revise o autocratique su propio trabajo en prosa (*Chain-of-Thought*) no reduce las alucinaciones y con frecuencia las amplifica.

---

## Causa Estructural
Los modelos son capaces de corregir errores en textos externos, pero fracasan al evaluar sus propias explicaciones porque las cadenas de razonamiento autorregresivas son **"infieles" a la computación real subyacente**. En un espacio continuo, el modelo no recibe una **señal de fallo determinista** (un *"error de compilación"*), por lo que inventa racionalizaciones falsas para mantener la coherencia probabilística de su salida.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Nezhad et al. (SymCode 2025)**: *SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation*
  * PDF en Repositorio: [symcode2025.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/symcode2025.pdf)
* 📄 **Vossel et al. (2025)**: *Advancing Natural Language Formalization to FOL*
  * PDF en Repositorio: [vossel2025advancing.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/vossel2025advancing.pdf)
* 📄 **Quigley (2025)**: *Neurosymbolic Deep Learning Semantics*
  * PDF en Repositorio: [quigley2025.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/quigley2025.pdf)

---

## Integración en el Paper NeurIPS (*Reasoning Limits & Behavioral Interventions*)
Se incluye en la sección de límites del razonamiento autónomo para demostrar que la autocorrección en prosa es una ilusión, **exigiendo la señal de fallo Booleana determinista de la Máscara de Sentido $S_i = 0$**.
