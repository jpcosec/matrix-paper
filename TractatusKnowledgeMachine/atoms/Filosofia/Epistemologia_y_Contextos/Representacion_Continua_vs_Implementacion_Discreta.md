---
system: matrix
layer: epistemology
domain: contextual-logic
topic: representacion-continua-vs-implementacion-discreta
use_when: "Aplicable al contexto semantico y factual de Representacion Continua vs Implementacion Discreta."
do_not_use_when: "No utilizar fuera del dominio formal de contextual-logic."
---

# Representación Continua vs. Implementación Discreta

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [defines:: [[Arquitectura_Neuro_Estocastica]]]
* [defines:: [[Discretizacion_Logica_vs_Continuo]]]
* [defines:: [[Teorema_Aproximacion_Universal_Hornik]]]
* [defines:: [[Fenomeno_de_Gibbs_en_Funciones_Indicadoras]]]
* [defines:: [[Geometria_de_Politopos_y_Ancho_Acotado_Hanin]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]

---

## Qué es
Es la distinción entre la **discretización numérica del hardware** y el **comportamiento topológico de la representación semántica**. Aunque un LLM corra sobre silicio discreto y almacene tensores con precisión finita, su significado se codifica y opera como un espacio vectorial continuo en $\mathbb{R}^d$.

## La distinción central

| Nivel | Naturaleza | Qué resuelve | Qué no resuelve |
| :--- | :--- | :--- | :--- |
| **Hardware / números** | Discreto-finito | Implementación física de tensores y operaciones | No introduce fronteras lógicas rígidas |
| **Espacio semántico** | Continuo-topológico | Proximidad distribucional, similitud difusa | No puede colapsar verdad/sentido a límites discretos |

El hecho de que el procesador opere con bits no cambia que la función aprendida por la red viva en un espacio de representación continuo, donde las decisiones se organizan por cercanía geométrica y no por coordenadas booleanas inmutables.

## Por qué `argmax` no resuelve el problema

El argumento del revisor confunde dos cosas distintas:

1. **Eliminar muestreo no elimina continuidad.**
   `argmax` hace determinista la selección final del token, pero la elección sigue ocurriendo sobre una distribución producida por un espacio continuo.
2. **La alucinación nace antes de la selección final.**
   Si la representación ya interpoló una región semántica incorrecta, `argmax` solo elige de forma determinista el punto más alto de esa región errónea.
3. **La decodificación determinista no corrige la topología.**
   Quitar azar no convierte un embedding en una coordenada lógica discreta.

Por eso una alucinación puede ser completamente **determinista y segura de sí misma**.

## Fundamento matemático

### 1. Hornik (1991)
Las redes feedforward son aproximadores universales de **funciones continuas**. Esto no garantiza la representación exacta de funciones indicadoras discontinuas como:

$$V_i, S_i \in \{0,1\}$$

### 2. Gibbs
Cuando una función continua intenta aproximar un salto discreto, aparecen regiones de transición suave e interferencia de borde. Allí surgen los errores estructurales de frontera.

### 3. Hanin (2017)
Las redes ReLU con ancho acotado particionan $\mathbb{R}^d$ en politopos convexos. Aproximar fronteras lógicas complejas requiere crecimiento exponencial de regiones.

## Consecuencia para la lógica formal

La verdad factual y la aplicabilidad semántica no son magnitudes graduales; son funciones indicadoras con colapso discreto:

- **Verdad**: $1$ o $0$
- **Sentido**: *Sinnvoll* o *Unsinnig*

Un embedding puede aproximar similitud, pero no puede garantizar estos colapsos sin introducir zonas intermedias. Esas zonas intermedias son exactamente donde aparecen las alucinaciones.

## Respuesta directa a la objeción del revisor

> "Si la red corre sobre silicio discreto y `argmax` es determinista, ¿por qué hablas de estocasticidad o continuidad?"

Porque la continuidad relevante no es la del transistor sino la del **espacio de representación**. El silicio discreto implementa una función cuyo comportamiento semántico sigue siendo continuo en $\mathbb{R}^d$. `argmax` elimina el azar del muestreo final, pero no elimina la interpolación semántica ni la incapacidad topológica de representar fronteras lógicas discretas.

## Para qué sirve

Cierra la objeción de que "todo ya es discreto" mostrando que la diferencia decisiva no está en los bits del hardware sino en la geometría de la representación.

---

## 📚 Fuentes científicas implicadas
* 📄 **Hornik (1991)**: [hornik1991approximation.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/hornik1991approximation.pdf)
* 📄 **Orgad et al. (2025)**: [iclr2025_a712d4.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/iclr2025_a712d4.pdf)
* 📄 **Hanin (2017)**: [hanin2017boundedwidth.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/hanin2017boundedwidth.pdf)
