# Lenguaje, operación simbólica y artefactos de razonamiento
## Hacia un marco de procesamiento lógico-simbólico basado en semianillos booleanos y Wittgenstein

**Propuesta de investigación — Magíster en Estudios Cognitivos, Universidad de Chile**  
**Postulante:** Juan Pablo Rozas  

---

### 1. Presentación y problema de investigación

El desarrollo reciente de los grandes modelos de lenguaje (LLMs) ha instalado un debate central en las ciencias cognitivas sobre la naturaleza de la comprensión y el razonamiento. Estos sistemas muestran un dominio asombroso de la gramática y el estilo en lenguaje natural; sin embargo, exhiben fallas sistemáticas cuando se les exige sostener cadenas de inferencia válidas, respetar restricciones lógicas o evitar inconsistencias fácticas. 

Esta brecha ilustra con claridad la distinción que Mahowald et al. (2024) establecen entre *competencia lingüística formal* —la habilidad estadística para predecir y articular patrones de la lengua— y *competencia lingüística funcional*, que comprende la capacidad de emplear el lenguaje para razonar sobre situaciones del mundo, planificar y evaluar estados de cosas. La neurociencia cognitiva contemporánea aporta evidencia convergente: tal como sintetizan Fedorenko, Piantadosi y Gibson (2024), las redes neuronales humanas dedicadas al procesamiento del lenguaje están anatómicamente disociadas de las redes que sustentan el razonamiento deductivo, matemático y espacial. El lenguaje parece ser primordialmente una herramienta de comunicación y transmisión, no el medio de cómputo en el que opera el razonamiento lógico.

Si el lenguaje ordinario no es por sí mismo el motor del razonamiento deductivo, ¿qué permite a los seres humanos realizar inferencias rigurosas y examinar sus propios pensamientos? Desde la perspectiva de la mente extendida (Clark & Chalmers, 1998) y la historia de las tecnologías cognitivas (Olson, 1994), la respuesta reside en la construcción de *artefactos externos*. La escritura, y más tarde el cálculo lógico y matemático, funcionaron como soportes que estabilizan las expresiones lingüísticas para someterlas a reglas explícitas de manipulación. Un artefacto formal de razonamiento cumple dos tareas decisivas: objetiva los contenidos eliminando la ambigüedad superficial del habla y establece un régimen de operaciones inspeccionables donde cada paso inferencial debe estar justificado.

El problema que motiva este proyecto es que los modelos de lenguaje actuales carecen de un artefacto formal desacoplado. Al operar exclusivamente como transformadores de secuencias probabilísticas en espacios continuos, confunden la plausibilidad superficial de un enunciado con su consistencia lógica y su admisibilidad semántica.

---

### 2. Propuesta conceptual: mundos locales, grafos booleanos y Wittgenstein

Este proyecto propone diseñar y fundamentar teóricamente un marco donde la generación lingüística se desacople de un sustrato de operación simbólica. En lugar de forzar a un modelo continuo a derivar conclusiones lógicas en su propio texto, se plantea una arquitectura de dos niveles: el lenguaje natural opera como interfaz expresiva de entrada y salida, mientras que la evaluación y la inferencia ocurren en un artefacto simbólico estructurado.

Formalmente, este artefacto se concibe como una red de **mundos locales** organizados como **grafos relacionales** que operan bajo las propiedades algebraicas de **semianillos booleanos**. La unidad básica de representación es la celda o relación diádica:
$$(R, A, B) \in \{0, 1\}$$
donde $R$ designa una relación y $(A, B)$ corresponden a los nodos o argumentos vinculados.

Esta formulación no es una reducción simplista a tablas estáticas. Por el contrario, un grafo booleano sobre tuplas $(R, A, B)$ posee una gran versatilidad expresiva, capaz de mapear directamente:
1. **Asignación de propiedades:** enunciados atributivos donde una entidad $A$ posee la propiedad $B$ bajo la relación de predicación $R$.
2. **Secuencias temporales y causalidad:** ordenamientos y precedencias entre eventos o estados sucesivos ($t_1 \prec t_2$).
3. **Operaciones y conectivas lógicas:** deducciones mediante caminos en el grafo, composiciones relacionales y evaluaciones de conjunción o disyunción.
4. **Mapeo contextual y reflexividad:** relaciones donde los propios nodos $(A, B)$ o el predicado $R$ apuntan a *contextos o mundos locales particulares*. De este modo, los contextos se convierten en nodos de un meta-grafo, permitiendo la navegación, la herencia y el enrutamiento contextual sin recurrir a una ontología única universal.

Sobre esta base formal, la filosofía del lenguaje de Ludwig Wittgenstein proporciona el criterio regulador indispensable. En el *Tractatus Logico-Philosophicus*, Wittgenstein plantea que una proposición es una figura lógica de la realidad y que existe una frontera estricta entre:
- La verdad o falsedad de un hecho contingente.
- Las proposiciones formales que muestran la estructura de la lógica (*sinnlos*, como la tautología y la contradicción).
- Las combinaciones que violan las reglas de la forma lógica y carecen de sentido (*unsinnig*, contrasentido).

En nuestro marco, las categorías de Wittgenstein cumplen la función de definir **lo que se puede decir** dentro de un mundo local determinado: delimitan qué combinaciones relacionales son estructuralmente admisibles (dotadas de sentido en ese ámbito) antes de verificar si son fácticamente verdaderas o falsas. A su vez, la perspectiva de las *Investigaciones Filosóficas* permite entender cada mundo local como la formalización de un *juego de lenguaje* específico, con reglas y límites propios que dependen de la práctica en la que se inscribe.

---

### 3. Pregunta y objetivos de investigación

#### Pregunta general
> ¿Cómo fundamentar un marco cognitivo-simbólico que desacople la expresión en lenguaje natural de la operación sobre mundos locales modelados como grafos en semianillos booleanos, y de qué modo las nociones de sentido y contexto de Wittgenstein permiten gobernar y tipar lógicamente las afirmaciones de un sistema de lenguaje?

#### Objetivos específicos
1. **Reconstruir conceptualmente las nociones tractarianas** de signo, símbolo, espacio lógico, sentido (*Sinn*) y contrasentido (*Unsinn*), justificando su empleo formal como mecanismo para demarcar la admisibilidad y los límites de lo decible en grafos relacionales.
2. **Definir las condiciones de adecuación lingüística para la ida y vuelta** entre lenguaje ordinario y grafos booleanos, garantizando la preservación composicional de participantes, negación, modalidad y fuerza ilocucionaria (afirmación, pregunta o suposición).
3. **Analizar la capacidad de modelado del formalismo de grafos sobre $(R, A, B)$**, demostrando cómo una misma base algebraica puede representar propiedades, orden temporal, deducción de caminos y relaciones de anclaje contextual.
4. **Articular un esquema de tipado lógico estratificado** que distinga con claridad entre representabilidad, firma relacional, admisibilidad contextual y valor de verdad factual, proporcionando un modelo conceptual para inspeccionar y prevenir alucinaciones en modelos de lenguaje.

---

### 4. Diálogo interdisciplinar y antecedentes teóricos

El proyecto se sitúa en el cruce entre tres disciplinas fundamentales del programa de Estudios Cognitivos:

- **Filosofía del lenguaje y de la mente:** Se examina la vigencia de Wittgenstein para la ciencia cognitiva contemporánea, junto con la teoría de los actos de habla de Austin (1962). Se busca clarificar cómo la fuerza de una emisión condiciona la operación autorizada sobre una creencia: no es lo mismo registrar un hecho que explorar una hipótesis contrafáctica.
- **Lingüística teórica y formal:** La traducción entre texto y grafo exige dialogar con la semántica composicional (Montague, 1970; Partee, 2012) y con el tratamiento del significado léxico y la coerción de tipos de Pustejovsky (1991). Esto previene descartar erróneamente como "sinsentido" expresiones metafóricas o flexibles que el lenguaje admite mediante ajustes semánticos legítimos.
- **Modelos cognitivos y arquitecturas de razonamiento:** La articulación entre el procesamiento fluido de texto y la operación deductiva en grafos retoma el clásico debate entre conexionismo y sistemas simbólicos planteado por Smolensky (1988), así como las reflexiones de Kahneman y Klein (2009) sobre la intuición experta como reconocimiento rápido de patrones relacionales en entornos estructurados.

---

### 5. Metodología

La investigación es de carácter teórico-conceptual y formal, complementada con el análisis sistemático de casos contrastivos:

1. **Análisis conceptual y reconstrucción bibliográfica:** Examen crítico de las fuentes textuales para fundamentar rigurosamente el paso desde los conceptos filosóficos y lingüísticos hacia su formulación operativa.
2. **Formalización analítica del marco:** Definición de los componentes de un mundo local (espacio relacional, operadores del semianillo booleano, criterios de admisibilidad contextual y capas de tipado).
3. **Evaluación mediante casos contrastivos:** Examen del marco frente a problemas semánticos y cognitivos clásicos, evaluando cómo responde el sistema ante:
   - Variaciones de paráfrasis frente a cambios genuinos de contexto.
   - Diferencias en la fuerza del enunciado (aserto factual vs. pregunta vs. hipótesis).
   - Distinción entre ignorancia o falta de datos (un hecho no registrado) e inadmisibilidad lógica (un contrasentido categorial).
   - Invariancias locales frente a verdades lógicas tautológicas.
   - Navegación intercontextual a través de términos medios compartidos.
   - Retorno al lenguaje natural con preservación de la incertidumbre y sin invención de hechos.

---

### 6. Aporte esperado y motivación de ingreso

Este proyecto busca aportar al programa de Magíster una reflexión sistemática sobre el lugar de los artefactos simbólicos en la arquitectura de la cognición humana y artificial. Frente a la tendencia actual a considerar los modelos de aprendizaje profundo como explicaciones suficientes de la mente o como solucionadores universales, esta investigación defiende que el razonamiento riguroso exige herramientas formales complementarias de control e inspección.

El Magíster en Estudios Cognitivos de la Universidad de Chile ofrece el espacio interdisciplinario ideal para desarrollar este trabajo, permitiendo madurar el diálogo entre la precisión lógica de los grafos relacionales y la profundidad conceptual de la filosofía del lenguaje y la lingüística cognitiva.

---

### 7. Referencias bibliográficas

- Austin, J. L. (1962). *How to do things with words*. Oxford University Press.
- Bender, E. M., & Koller, A. (2020). Climbing towards NLU: On meaning, form, and understanding in the age of data. *Proceedings of the 58th Annual Meeting of the ACL*, 5185–5198.
- Clark, A., & Chalmers, D. (1998). The extended mind. *Analysis*, 58(1), 7–19.
- Fedorenko, E., Piantadosi, S. T., & Gibson, E. A. (2024). Language is primarily a tool for communication rather than thought. *Nature*, 630, 575–586.
- Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist*, 64(6), 515–526.
- Mahowald, K., Ivanova, A. A., Blank, I. A., Kanwisher, N., Tenenbaum, J. B., & Fedorenko, E. (2024). Dissociating language and thought in large language models. *Trends in Cognitive Sciences*, 28(6), 517–540.
- Montague, R. (1970). Universal grammar. *Theoria*, 36(3), 373–398.
- Olson, D. R. (1994). *The world on paper: The conceptual and cognitive implications of writing and reading*. Cambridge University Press.
- Partee, B. H. (2012). *Introduction to formal semantics and compositionality*. Lectures in Formal Semantics, RGGU.
- Pustejovsky, J. (1991). The generative lexicon. *Computational Linguistics*, 17(4), 409–441.
- Smolensky, P. (1988). On the proper treatment of connectionism. *Behavioral and Brain Sciences*, 11(1), 1–23.
- Wittgenstein, L. (1922). *Tractatus Logico-Philosophicus*. Kegan Paul, Trench, Trubner & Co.
- Wittgenstein, L. (1953). *Philosophische Untersuchungen*. Blackwell.
