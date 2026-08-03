---
topic: ley-del-ocultamiento-del-conocimiento-knowledge-overshadowing
use_when: Aplicable al contexto semantico y factual de Ley del Ocultamiento del Conocimiento
  Knowledge Overshadowing.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-ley-del-ocultamiento-del-conocimiento-knowledge-overshadowing
title: Ley del Ocultamiento del Conocimiento Knowledge Overshadowing
five_wh_one_plus: what
tags:
- system:matrix
---
# La Ley del Ocultamiento del Conocimiento (Knowledge Overshadowing)

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_arxiv2501_12345_pdf]]]
* [explains_failure_of:: [[Causas_Estructurales_y_de_Entrenamiento]]]
* [explains_failure_of:: [[Arquitectura_Neuro_Estocastica]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [explains_failure_of:: [[Hecho_Atomico_CDV]]]

---

## Qué es
Es la ley empírica que establece que la tasa de alucinaciones aumenta de forma predecible porque el conocimiento dominante o hiper-popular en los datos de entrenamiento **"eclipsa" o solapa geométricamente al conocimiento menos prominente (la "cola larga")**.

---

## Mecanismo en Espacios Continuos
En los espacios de embeddings continuos, la alta frecuencia de coocurrencia de entidades populares atrae las dimensiones de proyección latentes. Durante la decodificación, esta asimetría fuerza al modelo a fabricar detalles inexactos cuando se le consulta sobre entidades de la cola larga.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Kommers et al. (2025)**: *Why Slop Matters: Knowledge Overshadowing in Large Language Models*
  * PDF en Repositorio: [kommers2025slop.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/kommers2025slop.pdf)
* 📄 **Shumailov et al. (Nature 2024)**: *AI models collapse when trained on recursively generated data*
  * PDF en Repositorio: [shumailov2024.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/shumailov2024.pdf)

---

## Integración en el Paper NeurIPS (*Data-Centric Limitations & Long-Tail Knowledge*)
Se utiliza en la sección sobre limitaciones de datos para demostrar el sesgo de frecuencia de la geometría continua, **justificando la equidad bitwise del semianillo Booleano (donde 1 hecho de la cola larga ocupa 1 bit inmutable)**.
