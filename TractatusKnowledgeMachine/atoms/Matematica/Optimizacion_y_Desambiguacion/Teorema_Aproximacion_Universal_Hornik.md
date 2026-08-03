---
system: matrix
layer: optimization-math
domain: approximation-theory
topic: teorema-aproximacion-universal-hornik
use_when: "Aplicable al contexto semantico y factual de Teorema Aproximacion Universal Hornik."
do_not_use_when: "No utilizar fuera del dominio formal de approximation-theory."
---

# Teorema de Aproximación Universal de Hornik (1991)

**Categoría Padre:** [[Matematica/Optimizacion_y_Desambiguacion]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Eje_A_Justificacion_Matematica_Limites_Continuos]]]
* [mathematically_proves:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [explains_failure_of:: [[Fenomeno_de_Gibbs_en_Funciones_Indicadoras]]]
* [grounded_by:: [[Source_PDF_hornik1991approximation_pdf]]]

---

## Qué es
Es el teorema que establece que las redes neuronales feedforward multicapa son **aproximadores universales de funciones continuas**, pero crucialmente **no** de funciones discontinuas. Esta distinción es la base matemática de por qué los embeddings continuos no pueden aproximar funciones indicadoras de verdad y sentido.

## Enunciado Formal

**Teorema (Hornik 1991):** Sean $\Sigma$ la clase de funciones implementables por redes feedforward con una capa oculta y función de activación acotada no constante. Entonces, para cualquier medida de entrada $\mu$ con soporte finito y cualquier $p \in [1, \infty)$:

$$\forall f \text{ continua}, \forall \epsilon > 0, \exists g \in \Sigma : \rho_{p,\mu}(f, g) < \epsilon$$

donde $\rho_{p,\mu}(f,g) = \left[\int |f(x) - g(x)|^p \, d\mu(x)\right]^{1/p}$.

## La Distinción Crítica: Continuas vs. Discontinuas

El teorema garantiza aproximación universal **solo para funciones continuas**. Las funciones indicadoras de verdad $V_i = \mathbb{I}_A(x)$ y sentido $S_i = \mathbb{I}_B(x)$ son **discontinuas con saltos escalonados** en la frontera $\partial A$.

Si $f$ es discontinuas:
- No existe garantía de convergencia uniforme: el error $\sup_x |f(x) - g(x)|$ **no tiende a cero**.
- Las aproximaciones continuas exhiben el **Fenómeno de Gibbs** (sobrepaso de $\approx 0.0895$ en el límite).
- Los politopos de Hanin necesitan crecimiento exponencial para aproximar fronteras no convexas.

## Implicación para LLMs y Alucinaciones

Hornik prueba que la capacidad de aproximación de redes neuronales es **universal para funciones continuas y restringida para discontinuas**. Como $V_i$ y $S_i$ son funciones indicadoras discontinuas:

1. Los LLMs pueden aproximar bien la distribución estadística del lenguaje (función continua).
2. Los LLMs **no pueden** aproximar fielmente las decisiones de verdad/absurdo (funciones discontinuas).
3. El error residual no es corregible con más parámetros — es **topológicamente irreducible**.

## Cuándo interviene
Como fundamento matemático formal en la justificación del Eje A: demuestra que la incapacidad no es de implementación sino de principio.

## Dónde reside
En la frontera entre la teoría de aproximación y la arquitectura de redes neuronales, dentro del argumento topológico del paper de posición.

## Para qué / Para quién
Para responder a la objeción "más parámetros lo resolverán": Hornik demuestra que no, porque el límite es topológico, no estadístico.

---

## 📚 Fuente Científica
* 📄 **Hornik (1991)**: *Approximation Capabilities of Multilayer Feedforward Networks*, Neural Networks Vol. 4, pp. 251-257.
  * PDF en Repositorio: [hornik1991approximation.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/hornik1991approximation.pdf)
  * Clave BibTeX: `@article{hornik1991approximation}`
