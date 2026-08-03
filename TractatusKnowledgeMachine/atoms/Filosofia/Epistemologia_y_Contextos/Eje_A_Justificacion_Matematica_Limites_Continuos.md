---
topic: eje-a-justificacion-matematica-limites-continuos
use_when: Aplicable al contexto semantico y factual de Eje A Justificacion Matematica
  Limites Continuos.
do_not_use_when: No utilizar fuera del dominio formal de contextual-logic.
id: atom-eje-a-justificacion-matematica-limites-continuos
title: Eje A Justificacion Matematica Limites Continuos
five_wh_one_plus: what
tags:
- system:matrix
---
# Eje A: Justificación Matemática de los Límites en Espacios Continuos

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [defines:: [[Discretizacion_Logica_vs_Continuo]]]
* [defines:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [defines:: [[Teorema_Suboptimizabilidad_Diagonal]]]

---

## Qué es
Es la demostración matemática rigurosa que demuestra por qué las representaciones en espacios continuos (embeddings y distribuciones de Softmax) son estructuralmente incapaces de modelar decisiones de verdad factual ($V_i$) y aplicabilidad categorial ($S_i$).

## Demostración Matemática y Teoremas
1. **Discontinuidad de las Funciones Indicadoras:**
   * La Verdad Factual ($V_i \in \{0, 1\}$) y el Sentido ($S_i \in \{0, \emptyset, 1\}$) son **funciones indicadoras discontinuas con saltos de etapa escalonados**.
2. **Teorema de Hornik (1991):**
   * Demuestra que las redes neuronales feedforward continuas son aproximadores universales de funciones *continuas*. Sin embargo, aproximar funciones indicadoras discontinuas con funciones continuas genera regiones de interferencia de borde (fenómeno de Gibbs), que es la causa matemática estructural de la alucinación.
3. **Teorema de Hanin (2017) (arXiv:1708.02691):**
   * Demuestra geométricamente que las activaciones continuas ReLU con ancho acotado dividen el espacio en politopos convexos. Aproximar regiones indicadoras arbitrarias requiere un número exponencial de neuronas o regiones.
4. **Barrera del AUROC $\approx 0.48$ (Wei et al. 2024):**
   * El Error Factual de Tipo III tiene un rendimiento de detección en espacios continuos equivalente al azar (AUROC $\approx 0.48$), probando que los embeddings miden la coocurrencia estadística distributiva, no la condición de verdad.

## Inyección en el Paper NeurIPS
Trasladar el análisis matemático de discontinuidades a la Introducción y Estado del Arte, justificando que la separación $V_i \odot S_i$ no es solo un postulado filosófico de Wittgenstein, sino un requisito topológico estricto.
