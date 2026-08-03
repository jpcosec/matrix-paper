# Síntesis y Resoluciones de Arquitectura (Motor MEEL)

Este documento recoge los acuerdos fundamentales y las resoluciones a las dudas abiertas planteadas durante el diseño de la Máquina de Estados de Evaluación Lógica (MEEL). Define el alcance estricto del motor que se construirá en Rust.

## 1. Alcance y Límites del Motor Base
El motor a construir en esta fase es exclusivamente la **infraestructura rígida de almacenamiento y operación matricial**.
* **NO incluye:** La traducción de signos a símbolos (NLP), ni algoritmos automáticos de inferencia, ni sistemas de entropía o reestructuración automática (como Indian Buffet Process). 
* **SÍ incluye:**
  1. Creación de espacios lógicos ($L_i$) que actúan como ejes con símbolos.
  2. Inyección de hechos en estos $L_i$ para materializar contextos operativos ($W_i$), guardando referencias (mapeos a textos o funciones).
  3. Creación y operación matemática de las matrices de Sentido ($S_i$).
  4. Manipulación algebraica de los $W_i$ para componer, proyectar, consultar y validar.
  5. Indexación de $W_i$ usando otros $W_i$.

## 2. Estructuras de Datos y Complejidad Relacional ($W_i, L_i$)
* Computacionalmente se utilizarán **tensores compuestos por matrices booleanas 2D**. Las matrices 2D son computacionalmente eficientes y están bien definidas.
* Las relaciones complejas o n-arias no requieren matrices n-dimensionales intratables. Se representan mediante **composición de contextos y proyecciones**, encadenando matrices de la misma forma que las s-expressions (ej: `(((dar libro) juan) maria)`), dividiendo el problema en múltiples $W_i$ interconectados.

## 3. Manejo de Errores y Categorías Lógicas
* El sistema implementará un **tipado fuerte** para las respuestas ante consultas inválidas o colisiones.
* No se colapsarán todos los errores a un simple `false` o `null`. El sistema devolverá la categoría tractariana exacta según el tipo de fallo:
  * **Sinnlos** (Tautología o Contradicción).
  * **Unsinnig** (Absurdo, fuera de las coordenadas lógicas).
  * **Inapplicable** (Dentro del espacio, pero bloqueado por la máscara de sentido $S_i$).

## 4. Operativización del Valor Nulo ($\emptyset$) y el Sentido ($S_i$)
La interacción entre matrices lógicas se regirá por las siguientes reglas algebraicas respecto a la falta de sentido o aplicabilidad:
1. **Regla del "Don't Care" para $\emptyset$:** En operaciones algebraicas (como la evaluación con Mapas de Karnaugh), el valor $\emptyset$ (inaplicable) funciona como un estado "Don't Care". El valor computacional que adopte (0 o 1) será estrictamente aquel que **no afecte el resultado final de la operación**, permitiendo la simplificación de la función lógica a nivel de hardware/bits.
2. **Naturaleza del $\emptyset$ en un Contexto Único ($W_i$):** Dentro de un $W_i$ que representa un contexto aislado y bien definido, **no debería existir el estado $\emptyset$** derivado de incompatibilidad semántica. Los únicos $\emptyset$ permitidos en un $W_i$ local son aquellos que representan "relaciones no mapeadas" (hechos sobre los que simplemente no tenemos información de verdad aún).
3. **Representaciones Multicontexto (Omnirepresentación):** Las matrices globales que consolidan múltiples contextos (donde abundarían los $\emptyset$ por incompatibilidad semántica) son útiles para otros fines, como entrenar LLMs o generar máquinas de estado globales. Sin embargo, para el motor de cálculo lógico actual, el procesamiento operará bajo la **Regla 2**, aislando los contextos en sub-matrices limpias ($W_i$) donde el álgebra se aplica sin ambigüedades.