---
topic: taxonomia-sota-alucinaciones
use_when: Aplicable al contexto semantico y factual de Taxonomia SOTA Alucinaciones.
do_not_use_when: No utilizar fuera del dominio formal de contextual-logic.
id: atom-taxonomia-sota-alucinaciones
title: Taxonomia SOTA Alucinaciones
five_wh_one_plus: what
tags:
- system:matrix
---
# Taxonomía SOTA de Alucinaciones y Límites Geométricos en LLMs

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [defines:: [[Discretizacion_Logica_vs_Continuo]]]
* [defines:: [[Signo_vs_Simbolo]]]
* [defines:: [[Modelo_SMG]]]
* [defines:: [[Tractatus]]]
* [defines:: [[Teorema_Suboptimizabilidad_Diagonal]]]

---

## Qué es
Es la clasificación formal del Estado del Arte (SOTA) que explica las alucinaciones en Grandes Modelos de Lenguaje (LLMs) no como errores superficiales, sino como **consecuencias inherentes de la geometría continua de los espacios de embeddings y la decodificación estocástica**, fundamentada en la literatura científica reciente descargada e indexada en el proyecto.

## Por qué es necesario
Demuestra la limitación teórica insuperable del entrenamiento continuo: el Error Fáctico (Tipo III) posee un rendimiento de detección geométrica equivalente al azar (AUROC $\approx 0.48$). Por lo tanto, no es posible erradicar las alucinaciones dentro del espacio vectorial continuo sin introducir un filtro discreto Booleano ($V_i \odot S_i$).

---

## Cinco Dimensiones Fundamentales del SOTA

### 1. Dicotomía entre Ignorancia ($HK^-$) y Error a Pesar del Conocimiento ($HK^+$)
* **Fuentes primarias:**
  * **Orgad et al. (ICLR 2025)**: *LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations* ([iclr2025_a712d4.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/iclr2025_a712d4.pdf))
  * **Simhi et al. (2024)**: *Distinguishing Ignorance from Error in LLM Hallucinations* ([arxiv2410_22071.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2410_22071.pdf))
* **Mecanismo:**
  * **$HK^-$ (Ignorancia Paramétrica):** El modelo alucina porque la información requerida simplemente no está en sus parámetros.
  * **$HK^+$ (Error a Pesar de Saber):** El modelo codifica internamente la respuesta correcta en sus representaciones latentes profundas, pero la decodificación estocástica (que maximiza la verosimilitud del siguiente token) genera afirmaciones falsas. Prueba que las alucinaciones no son solo falta de datos, sino fallas de decodificación.

### 2. La "Ilusión de la Autocorrección" (*The Self-Correction Illusion*) y la Prosa Infiel
* **Fuentes primarias:**
  * **Nezhad et al. (2025, SymCode)**: *SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation* ([symcode2025.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/symcode2025.pdf))
  * **Vossel et al. (2025)**: *Advancing Natural Language Formalization to First Order Logic with Fine-tuned LLMs* ([vossel2025advancing.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/vossel2025advancing.pdf))
* **Mecanismo:**
  * Los LLMs fracasan al intentar corregirse a sí mismos en sus propias cadenas de razonamiento en prosa (*Chain-of-Thought*). Las explicaciones narradas no son un registro fiel de la computación subyacente. En espacios continuos no existe una **señal de fallo determinista clara**, lo que imposibilita los bucles de autocorrección sin un verificador simbólico externo.

### 3. Sicofancia (*Sycophancy*) y las Limitaciones del RLHF
* **Fuentes primarias:**
  * **Min et al. (2023, FActScore)**: *FActScore* ([factscore2023.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/factscore2023.pdf))
  * **Manakul et al. (2023, SelfCheckGPT)**: *SelfCheckGPT* ([selfcheckgpt2023.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/selfcheckgpt2023.pdf))
* **Mecanismo:**
  * El aprendizaje por refuerzo a partir de retroalimentación humana (RLHF) induce **sicofancia**: el modelo aprende a complacer al usuario priorizando la aprobación o coherencia aparente por encima de la verdad factual, cediendo ante premisas falsas planteadas en la consulta.

### 4. Alucinaciones Inducidas por RAG (Conflicto de Conocimiento / *Knowledge Conflict*)
* **Fuentes primarias:**
  * **Wei et al. (2024)**: *Measuring and Reducing LLM Hallucination Without Gold-Standard Answers* ([arxiv2402_10412.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2402_10412.pdf))
  * **Feldman et al. (2023)**: *Trapping LLM Hallucinations Using Tagged Context Prompts* ([arxiv2306_06085.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2306_06085.pdf))
* **Mecanismo:**
  * Ocurre cuando la información externa recuperada mediante RAG contradice el conocimiento paramétrico memorizado durante el preentrenamiento. Debido al sesgo de sobreconfianza (*over-confidence*), el LLM ignora el contexto correcto inyectado y alucina apoyándose en sus sesgos previos.

### 5. Ley del Ocultamiento del Conocimiento (*Knowledge Overshadowing*)
* **Fuentes primarias:**
  * **Kommers et al. (2025)**: *Why Slop Matters* ([kommers2025slop.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/kommers2025slop.pdf))
  * **Shumailov et al. (2024, Nature)**: *AI models collapse when trained on recursively generated data* ([shumailov2024.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/shumailov2024.pdf))
* **Mecanismo:**
  * Establece que la tasa de alucinaciones aumenta porque el conocimiento muy popular en el preentrenamiento eclipsa log-linealmente al conocimiento menos prominente. Durante la generación, esta asimetría fuerza al modelo a fabricar detalles inexactos sobre la "cola larga" de datos.

---

## 🎯 Argumento Maestro para Justificar la Arquitectura Matrix

> *"La literatura reciente (Orgad et al., 2025; Simhi et al., 2024; Quigley, 2025; Nezhad et al., 2025; Vossel et al., 2025) evidencia que modelar el razonamiento exclusivamente como un proceso de decodificación estocástica sobre un espacio continuo es estructuralmente insuficiente. Aunque los modelos logran codificar conocimiento fáctico en sus representaciones latentes, la decodificación probabilística prioriza la verosimilitud estadística sobre el rigor lógico, resultando en alucinaciones (fenómeno $HK^+$) y cadenas de razonamiento infieles a la computación real subyacente. Como señala la investigación en IA neuro-simbólica y marcos como SymCode, la ausencia de señales de fallo deterministas en los espacios continuos impide que el modelo restrinja su propio flujo lógico, haciendo imperativa la integración de representaciones simbólicas discretas (Matrix) para garantizar la validez del razonamiento."*
