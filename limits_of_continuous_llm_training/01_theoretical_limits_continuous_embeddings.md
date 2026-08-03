# Limites Teóricos de las Representaciones Continuas en LLMs

Este documento sintetiza los fundamentos matemáticos, computacionales y lingüísticos que demuestran por qué el entrenamiento continuo de modelos de lenguaje basados en embeddings de espacio vectorial no puede resolver de manera aislada los problemas de alucinación y consistencia deductiva.

---

## 1. El Problema de la Falta de Anclaje (*Symbol Grounding Problem*)

### Harnad (1990) & Lyre (2024)
- **Premisa:** Un sistema que solo procesa relaciones estadísticas entre cadenas de signos sin conectar dichos signos a un espacio de estados o coordenadas del mundo vive en una "cárcel sintáctica".
- **Aplicación a LLMs:** Las distribuciones de embeddings vectoriales en $\mathbb{R}^d$ calculan proximidad semántica distribucional ($A$ suele aparecer cerca de $B$), pero no poseen anclaje categorial ($A$ es de tipo $T_i$ y pertenece al dominio de aplicabilidad $S_i$).

---

## 2. El Test del Pulpo y la Forma vs. Significado

### Bender & Koller (2020) — *Climbing towards NLU: On meaning, form, and understanding*
- **Demostración:** El significado (*meaning*) es una relación entre la forma lingüística y la intención en el mundo real. Aprender exclusivamente sobre la forma (*form*, cadenas de texto) nunca permite derivar el significado formal o la verdad empírica.
- **Consecuencia para los LLMs:** La probabilidad $P(w_t \mid w_{<t})$ mide la plausibilidad formal de la superficie del lenguaje ($S$), pero no la validez veritativa ($V_i$) ni el sentido ($S_i$).

---

## 3. El Colapso de Modelo (*Model Collapse*) en Datos Recursivos

### Shumailov et al. (2024, Nature) — *AI models collapse when trained on recursively generated data*
- **Descubrimiento:** Cuando los LLMs continuos se entrenan con datos generados por otros modelos de lenguaje (retroalimentación continua), las colas de la distribución de probabilidad se borran gradualmente. El modelo pierde la capacidad de representar hechos raros pero verdaderos, colapsando en una varianza degenerada.
- **Por qué ocurre:** Las representaciones vectoriales continuas suavizan y difuminan los límites de discontinuidad discreta. Sin un filtro simbólico determinista ($S_i$), el ruido probabilístico se acumula recursivamente.

---

## 4. Entropía Semántica y Colapso de Varianzas

### Farquhar et al. (2024, Nature) — *Detecting hallucinations using semantic entropy*
- **Descubrimiento:** Las alucinaciones no son fallas de vocabulario, sino divergencias en el espacio de significados equivalentes. Medir la entropía sobre tokens individuales no detecta alucinaciones; se requiere agrupar las salidas continuas en clases de equivalencia de significado.
- **Conexión con Matrix:** Reafirma que la evaluación de verdad requiere colapsar el espacio vectorial continuo a clases de equivalencia discreta ($M \to G$).

---

---

## 5. Modelos Basados en Energía y Arquitecturas Predictivas (JEPA)

### LeCun (2022) & Dawid & LeCun (2024) — *A Path Towards Autonomous Machine Intelligence*
- **Crítica de Yann LeCun a los LLMs Autorregresivos:** La predicción token a token en espacios continuos acumula un error exponencial. A medida que la cadena de texto se alarga, la probabilidad de salirse de la superficie de validez tiende a $1$.
- **Propuesta:** Se requieren arquitecturas de incrustación conjunta (*Joint-Embedding Predictive Architectures - JEPA*) y modelos basados en energía (*Energy-Based Models - EBM*) que acoten el espacio de estados posibles mediante restricciones de energía $E(R)$.

---

## 6. Teorema de Aproximación Universal y sus Límites en Discontinuidades Lógicas

### Hornik (1991) — *Approximation capabilities of multilayer feedforward networks*
- **Demostración Clásica:** Demuestra que las redes neuronales feedforward con funciones de activación continuas son aproximadores universales de funciones *continuas* en subconjuntos compactos de $\mathbb{R}^n$.
- **El Límite Lógico:** La verdad factual ($V_i \in \{0, 1\}$) y las máscaras de aplicabilidad semántica ($S_i \in \{0, \emptyset, 1\}$) son **funciones indicadoras discontinuas con saltos abruptos**. Intentar aproximar discontinuidades discretas con funciones continuas genera regiones de transición suave e interferencia de borde (fenómeno tipo Gibbs), las cuales son exactamente las zonas donde el LLM genera alucinaciones.

### Hanin (2017) — *Universal Function Approximation by Deep Nets with Bounded Width and ReLU Activations* (arXiv:1708.02691)
- **Límites de Ancho y Profundidad:** Demuestra cuantitativamente los límites geométricos de aproximación de redes ReLU continuas con ancho acotado. Las activaciones continuas dividen el espacio en politopos convexos donde la aproximación de funciones indicadoras arbitrarias requiere un número exponencial de regiones o neuronas.
- **Implicación para Matrix:** Aporta el respaldo matemático formal para el **Teorema de Colapso de Resolución en Espacios Continuos**, justificando por qué es necesario separar las funciones lógicas discretas ($V_i, S_i$) en un sustrato Booleano independiente.

