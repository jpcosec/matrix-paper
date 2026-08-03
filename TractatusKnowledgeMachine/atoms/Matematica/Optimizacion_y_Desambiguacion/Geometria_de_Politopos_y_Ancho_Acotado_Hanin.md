---
topic: geometria-de-politopos-y-ancho-acotado-hanin
use_when: Aplicable al contexto semantico y factual de Geometria de Politopos y Ancho
  Acotado Hanin.
do_not_use_when: No utilizar fuera del dominio formal de disambiguation.
id: atom-geometria-de-politopos-y-ancho-acotado-hanin
title: Geometria de Politopos y Ancho Acotado Hanin
five_wh_one_plus: what
tags:
- system:matrix
---
# Geometría de Politopos y Ancho Acotado (Hanin 2017)

**Categoría Padre:** [[Matematica/Optimizacion_y_Desambiguacion]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Fenomeno_de_Gibbs_en_Funciones_Indicadoras]]]
* [mathematically_proves:: [[Eje_A_Justificacion_Matematica_Limites_Continuos]]]
* [mathematically_proves:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]

---

## Qué es
Es la prueba geométrica desarrollada por Boris Hanin (2017) que establece los límites fundamentales de expresividad de las redes neuronales profundas con activaciones ReLU y ancho de capa acotado.

---

## Formulación Geométrica

Una red ReLU subdivide el espacio de entrada $\mathbb{R}^d$ en una malla de politopos convexos lineales a trozos. El número máximo de regiones o politopos convexos $\mathcal{N}$ que una red de profundidad $L$ y ancho acotado $w \le d$ puede crear está acotado polinomialmente:

$$\mathcal{N}(w, L) \le \sum_{j=0}^{d} \binom{w L}{j}$$

---

## Implicación en el Razonamiento Discreto
Para representar fronteras lógicas complejas no convexas o regiones discontinuas de sentido ($S_i$), una red continua requiere un número exponencial de neuronas o regiones. Intentar acotarlas en espacios continuos fuerza el solapamiento de politopos, produciendo interferencia lógica y alucinaciones.

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Hanin (2017, arXiv:1708.02691)**: *Universal Approximate Characteristics of Neural Networks with Bounded Width*
  * PDF en Repositorio: [hanin2017boundedwidth.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/hanin2017boundedwidth.pdf)
  * Clave BibTeX: `@article{hanin2017universal}`
