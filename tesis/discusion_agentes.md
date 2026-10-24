# Discusión del andamiaje teórico mediante Herdr

**Fecha:** 21 de octubre de 2026. **Participantes:** Codex, `w3D:p1`; Agy, `w3D:p3`; Pi, `w3D:p4`. **Documento resultante:** [anteproyecto_esqueleto.md](anteproyecto_esqueleto.md). **Fuentes verificadas y límites:** [notas_fuentes.md](notas_fuentes.md).

Este documento registra una síntesis editorial de los intercambios. Las propuestas de los agentes se sometieron a discusión y lectura de fuentes; no se consideran evidencia académica por sí mismas. No es una transcripción literal de sus respuestas.

## Encargo y precisión del objeto

Se pidió a ambos agentes leer el núcleo de `Matrix/paper_v2`, las revisiones, documentos del motor y el esqueleto, atendiendo a los dos desarrollos del autor: máquinas simbólicas sobre los mundos locales y tipado lógico de enunciados. Agy examinó la articulación lingüística y cognitiva; Pi, las distinciones formales y su relación con el motor.

Durante la conversación con Pi, el autor precisó que el objetivo de la tesis era construir el «andamiaje teórico» y que el programa no era un máster en ingeniería o computación. Esta precisión orienta la revisión: la contribución se define por el argumento, los conceptos y sus condiciones de adecuación. El código aporta casos que fuerzan a precisar las definiciones.

## Aportes y decisiones

### 1. Del artefacto escrito al artefacto formal

**Aportación de Agy, discutida con Codex:** incorporar la escritura como problema de interpretación y reflexión metalingüística permite desarrollar el argumento del artefacto con más profundidad que la referencia general a soportes externos. Se introdujo el extracto de Olson como interlocutor y se mantuvo Clark y Chalmers para la cuestión del acoplamiento cognitivo. [Fuentes y límites: entradas 5 y 9](notas_fuentes.md).

**Decisión:** el anteproyecto distinguirá estabilizar una expresión y declarar un régimen de operación sobre sus representaciones. El vínculo entre ambas funciones debe defenderse. No se deduce que la escritura ni el pensamiento humano sean ya un cálculo booleano.

### 2. Fortalecer el objetivo de máquinas simbólicas

**Objeción de Codex aceptada por ambos agentes:** «operar sin verbalización intermedia» conserva demasiado poco de la propuesta del autor. El objetivo se reformuló como reconocimiento de configuraciones, activación de contextos y composición de operaciones sobre mundos locales.

**Fuentes introducidas por Codex y discutidas con los agentes:** Smolensky ofrece un interlocutor sobre niveles simbólicos y subsimbólicos; McCulloch y Pitts, un antecedente del vínculo entre cálculo lógico y redes idealizadas. Agy desarrolló especialmente el contrapunto con Smolensky. [Fuentes: entradas 10 y 11](notas_fuentes.md).

**Corrección introducida en la discusión:** no presentar a Smolensky como defensor de una dicotomía simple entre intuición y reglas. Su §6 contempla integración. Tampoco la correspondencia expresiva de McCulloch-Pitts demuestra aprendizaje o intuición. El marco debe formular por separado esos problemas.

### 3. La lingüística tiene una función constitutiva

**Aportación de Agy, desarrollada por Codex:** el paso entre lenguaje y mundos debe explicar qué estructura conserva y qué función desempeña un enunciado. La distinción entre afirmar, preguntar o suponer cambia la operación autorizada incluso cuando se comparte contenido. El esqueleto incorpora composicionalidad, función del enunciado y capacidad expresiva, con fuentes identificadas y su grado de lectura. [Fuentes: Bender y Koller, Austin, Partee; entradas 6, 12 y 13](notas_fuentes.md).

**Anclaje en el repo:** [campos semánticos](../Matrix/Matrix/docs/semantic_fields.md) identifica que las celdas por sí solas no proporcionan orden discursivo, cuantificación y recursos metalingüísticos. Sus soluciones parciales permiten formular esas exigencias; no equivalen a una teoría lingüística completa.

**Decisión:** el objeto lingüístico del anteproyecto será la relación entre expresión, interpretación y operación. Se conservarán los casos de lenguaje como instrumentos de examen del marco.

**Ampliación bibliográfica de Codex:** se añadió Pustejovsky como objeción específica al rechazo inmediato por desajuste de tipos. Esta incorporación proviene de la lectura de sus pasajes sobre coerción, y se identifica aparte de los acuerdos iniciales entre agentes. [Fuente: entrada 14](notas_fuentes.md).

### 4. Tipado propuesto y dimensiones diferentes

**Aportación de Pi:** distinguir lo que el sistema puede representar, qué admite, qué conoce y qué vuelve consistente un conjunto de afirmaciones. Su lectura señaló que algunas etiquetas del código tienen usos distintos de los conceptos del paper.

**Discusión:** Pi planteó inicialmente optar entre tipado sortal y admisibilidad. Codex propuso una vía teórica que distinga firma relacional, admisibilidad contextual y precondición de operación. Pi aceptó ese desarrollo con juicios separados y razones explícitas.

**Corrección posterior de Codex:** esas dimensiones no forman cinco clases mutuamente excluyentes. Una proposición puede ser representable, admisible y desconocida; una contradicción depende de lo que se afirma conjuntamente. La condición es mantener diagnósticos diferenciados y explicitar sus interacciones.

**Pasajes de control:** [registro de proposiciones, `register_proposition`](../Matrix/Matrix/src/operational_model/system/wi_game_registry.py), [estado local, `get_status`](../Matrix/Matrix/src/operational_model/system/wi_game_queries.py) y [objeción de FJpU](../Matrix/review/response3.md).

### 5. Reconstrucción de Wittgenstein

**Acuerdo:** fundamentar signo y símbolo mediante pasajes precisos, y examinar las relaciones entre ambos libros. Codex incorporó además la tensión entre el desacoplamiento propuesto y *Tractatus* 3.5–4.002: no basta citar «el lenguaje disfraza el pensamiento» para atribuir independencia general entre ambos.

**Punto que sigue abierto:** Agy sugirió interpretar «localmente sinnlos» como una extensión de la no discriminación. La revisión mantiene esa posibilidad como definición por justificar. La constancia de una columna en los datos actuales no demuestra tautología lógica. [Localizadores filosóficos y deuda de fundamentación](notas_fuentes.md).

### 6. Qué permite atribuir al modelo de trabajo

**Aportación de Pi y comprobación de Codex:** el motor contiene recursos concretos para enrutamiento, composición por término medio y emisión de formas canónicas. Se utilizarán como casos de realización parcial.

**Correcciones discutidas:**

- Una ruta que une dos relaciones por un término medio no define automáticamente una relación conclusiva. [Implementación: `compose`](../Matrix/Matrix/src/operational_model/routing/middle_term.py).
- Bajo OR/AND, el producto entre filas detecta al menos una coordenada compartida. La igualdad de perfiles exige condiciones adicionales. Esto es una observación algebraica de la revisión sobre el cálculo presentado en [la sección de representación](../Matrix/paper_v2/sections/03_proposed_representation.md).
- La documentación actual describe límites del criterio de energía y mantiene abierta la búsqueda de particiones. [Campos semánticos, §§6 y 10](../Matrix/Matrix/docs/semantic_fields.md).
- La multiplicación de matrices no implica por sí sola costo total constante. No se empleará esa afirmación como fundamento cognitivo.
- El retorno a una forma canónica no acredita por sí mismo fidelidad de toda verbalización ni preservación de cualquier estructura contextual. [Emisión canónica](../Matrix/Matrix/src/operational_model/system/projection_emit.py).

## Criterios de la versión revisada

1. Argumentar el artefacto formal y sus funciones mediante premisas, interlocutores y objeciones.
2. Formular el desacoplamiento con alcance explícito: interpretación, representación, operación y expresión.
3. Dar a la lingüística la tarea de establecer condiciones de adecuación entre esas capas.
4. Conservar máquinas simbólicas e intuición como problema constructivo del marco, precisando funciones y límites.
5. Proponer juicios de tipado diferenciados y rastreables.
6. Examinar la teoría mediante reconstrucción textual, especificación formal y casos contrastivos. Los experimentos comparativos quedan como desarrollo que podrá derivarse del marco.

## Pendientes que la discusión no resuelve

- Definir cómo se construyen y justifican los contextos y las firmas de relación.
- Defender qué aporta el marco frente a semánticas formales, sistemas de tipos y arquitecturas simbólicas o subsimbólicas existentes, sin adjudicarles carencias generales.
- Desarrollar el mecanismo que relacionaría aprendizaje o reorganización con las operaciones sobre mundos locales.
- Profundizar las fuentes de retórica y práctica científica si se incorporan como parte del argumento y no solo como motivación.
- Leer completo el artículo de Montague y fijar las ediciones de Wittgenstein que se citarán en la postulación.
- Convertir este esqueleto anotado en un anteproyecto de cinco páginas. La revisión actual desarrolla el argumento y conserva las notas de trabajo; todavía no es esa versión final.

## Última revisión del documento integrado

Agy leyó los tres documentos y no señaló nuevas objeciones sustantivas. Pi añadió tres observaciones: variación del vocabulario de los juicios entre secciones, ausencia de un objetivo explícito para el retorno de representación a expresión y atribución imprecisa de la introducción de algunas fuentes.

Se corrigieron mediante una tabla provisional de seis juicios en §3.3, su referencia común en objetivos y método, la inclusión de ida y vuelta en el objetivo 2 y de un caso de retorno, y la aclaración de la atribución bibliográfica en este registro. La tabla es una propuesta teórica para desarrollar; no se presenta como clasificación ya implementada.

## Precisión del autor sobre mundos locales y grafos booleanos

En la sesión de cierre, el autor explicitó dos definiciones ontológicas y formales constitutivas:
1. **Naturaleza algebraica y demarcatoria:** Los mundos locales \(W_i\) son esencialmente **grafos** que operan bajo propiedades de **semianillos booleanos** sobre tuplas \((R, A, B) \in \{0, 1\}\). Las categorías de Wittgenstein (espacio lógico y límites del sentido) actúan formalmente como la frontera de «lo que se puede decir» sin perder el sentido (*unsinnig*).
2. **Poder de mapeo operacional y contextual:** El formalismo de grafos sobre \((R, A, B)\) mapea cualquier operación lógica expresable en esa base relacional, cubriendo:
   - Atribución de propiedades.
   - Relaciones temporales y secuencias de estado.
   - Conectivas y operaciones lógicas.
   - Metamapas relacionales (proyección de relaciones \(R\) o pares \(A, B\) hacia contextos específicos), formalizando el enrutamiento y la composicionalidad intercontextual.

Estas precisiones quedaron formalmente incorporadas en las secciones 1, 3.1 y 3.3 de [anteproyecto_esqueleto.md](anteproyecto_esqueleto.md).
