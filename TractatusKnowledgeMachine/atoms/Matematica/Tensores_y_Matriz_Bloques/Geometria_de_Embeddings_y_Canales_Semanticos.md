---
topic: geometria-de-embeddings-y-canales-semanticos
use_when: Aplicable al contexto semantico y factual de Geometria de Embeddings y Canales
  Semanticos.
do_not_use_when: No utilizar fuera del dominio formal de matrix-algebra.
id: atom-geometria-de-embeddings-y-canales-semanticos
title: Geometria de Embeddings y Canales Semanticos
five_wh_one_plus: what
tags:
- system:matrix
---
# Geometría de Embeddings y Canales Semánticos en $\mathbb{R}^d$

**Categoría Padre:** [[Matematica/Tensores_y_Matriz_Bloques]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Origen_Geometrico_y_Espacio_Vectorial]]]
* [mathematically_proves:: [[Representacion_Plana_vs_Tensorial]]]
* [mathematically_proves:: [[Teorema_Suboptimizabilidad_Diagonal]]]

---

## Qué es
Es la formulación algebraica lineal que describe la topología de los espacios de embeddings continuos en redes neuronales profundas y la geometría de los "canales semánticos" de alta dimensión.

---

## Formulación de Canales Semánticos

Dado un conjunto de vectores de embedding $v \in \mathbb{R}^d$, las respuestas afirmativas coherentes en un dominio forman una subvariedad o canal lineal guiado por la matriz de covarianza de las activaciones.

La similitud entre dos conceptos $u, v \in \mathbb{R}^d$ se calcula mediante la distancia del coseno:

$$\text{Sim}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$

---

## El Fallo de Discriminación Factual
Puesto que $\text{Sim}(u, v)$ es una medida de coocurrencia estocástica continua y no un operador veritativo, afirmaciones falsas pero semánticamente afines (Error Fáctico Tipo III) permanecen dentro del canal típico de la subvariedad, resultando en un rendimiento de discriminación geométricamente equivalente al azar (**AUROC $\approx 0.478$**).

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Wei et al. (2024)**: *Measuring and Reducing LLM Hallucination Without Gold-Standard Answers*
  * PDF en Repositorio: [arxiv2402_10412.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/arxiv2402_10412.pdf)
  * Clave BibTeX: `@article{wei2024measuring}`
