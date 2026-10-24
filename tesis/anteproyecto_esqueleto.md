# Lenguaje, operación simbólica y artefactos de razonamiento
## Hacia un marco de procesamiento lógico-simbólico basado en lógica booleana y Wittgenstein

**Esqueleto de anteproyecto — Magíster en Estudios Cognitivos, Universidad de Chile**

**Estado:** esqueleto revisado el 21 de octubre de 2026 tras discusión entre Codex, Agy y Pi mediante Herdr. El objeto de la tesis es construir el andamiaje teórico del marco. Matrix proporciona un modelo de trabajo que obliga a precisar las definiciones. Las afirmaciones bibliográficas llevan referencias y las hipótesis se identifican como propuestas del autor. Véanse [notas_fuentes.md](notas_fuentes.md) y [discusion_agentes.md](discusion_agentes.md).

**Distribución editorial propuesta:** problema y pregunta, una página; fundamentos, una página y media; objetivos y método, una página y media; aporte y referencias, una página. Es una pauta para redactar la versión final, todavía sin paginación. El instructivo de postulación exige un anteproyecto de máximo cinco páginas que delimite y fundamente el tema. [Instructivo, §2, ítem 10][programa]

## 1. Problema de investigación

**Párrafo de apertura: lenguaje y pensamiento.** La relación entre dominio del lenguaje y capacidad de pensamiento constituye un problema explícito de la investigación cognitiva sobre LLMs. Mahowald y colaboradores distinguen la competencia lingüística formal —manejo de patrones y reglas del lenguaje— de la competencia funcional, que comprende su uso en relación con conocimiento, razonamiento y situaciones del mundo. Esa distinción permite preguntar qué operaciones adicionales necesita una arquitectura que produce lenguaje para sostener sus afirmaciones. [Mahowald et al., 2024][mahowald]

**Párrafo sobre el artefacto formal.** Olson estudia cómo la escritura proporciona categorías para reflexionar sobre el lenguaje y cómo lo escrito requiere interpretar lo que el hablante pretende hacer. Clark y Chalmers examinan la participación de soportes externos en la resolución de problemas. A partir de esos antecedentes, se propone distinguir dos funciones del artefacto: estabilizar una expresión para examinarla y explicitar las reglas con que pueden transformarse sus representaciones. El paso de la escritura al cálculo formal será un argumento del proyecto, cuya justificación no se obtiene simplemente de la existencia de textos. [Olson, 1994, caps. 4–5 y comienzo del 6, extracto][olson]; [Clark y Chalmers, 1998, §§2–3][clark]

**Tesis de trabajo del autor.** A los LLMs considerados como procesadores de lenguaje les falta un artefacto formal de operación y control lógico comparable al que los humanos construimos en determinadas prácticas. Para defender esta tesis se definirá «disponer del artefacto» mediante representaciones identificables, reglas declaradas, operaciones inspeccionables y razones explícitas de aceptación o rechazo. Se argumentará que desacoplar la formulación verbal de ese régimen de operación permite pensar dos desarrollos: máquinas simbólicas de reconocimiento y composición, y tipado lógico de enunciados. La extensión a escritura, retórica y ciencia exige especificar las reglas de cada práctica. Esta es la proposición central a defender; su antecedente propio es el desacoplamiento planteado por Matrix. [Matrix, discusión][m-discusion]; [alcance reconocido en la respuesta a revisores, §§1–3][m-review]

**Delimitación del objeto.** El objeto será el andamiaje conceptual y formal que conecta lenguaje, representación y operación simbólica. Formalmente, los mundos locales \(W_i\) se conciben como **grafos relacionales** que operan bajo las propiedades algebraicas de **semianillos booleanos** sobre celdas relacionales \((R, A, B) \in \{0, 1\}\). En esta estructura, las categorías wittgensteinianas (espacio lógico, forma figurativa y límites del sentido) cumplen la función demarcadora de «lo que se puede decir» dentro de un dominio sin incurrir en contrasentido (*unsinnig*). Matrix concreta este modelo mediante mundos locales \(W_i\), coordenadas \(L_i\), verdad \(V_i\), aplicabilidad/sentido \(S_i\) y operaciones booleanas. Su documentación actual define cada WiGame mediante ejes y relación bajo un contexto, y registra capacidades de composición, reflexión y retorno canónico. Estos antecedentes permiten formular problemas teóricos concretos; el desarrollo de una nueva red neuronal queda como una dirección que el marco debe hacer inteligible. [Matrix, representación][m-representacion]; [contexto y WiGame][m-contexto]; [campos semánticos, §§1–10][m-campos]

## 2. Pregunta y conjeturas

**Pregunta principal propuesta**

> ¿Cómo fundamentar un marco de procesamiento lógico-simbólico que desacople la expresión lingüística de las operaciones sobre mundos locales \(W_i\), y qué condiciones debe satisfacer para sustentar máquinas de reconocimiento y composición simbólica y un tipado lógico de los enunciados de un LLM?

**Conjeturas a desarrollar y contrastar**

1. **Desacoplamiento representacional.** Distintas expresiones pueden conducir a una representación operable compartida cuando preservan las relaciones relevantes para una tarea. Se propone estudiar las condiciones de esa traducción, sin asumir que toda variación lingüística sea eliminable. Antecedentes: distinción entre signo y símbolo y discusión del proyecto sobre superficie de representación. [Wittgenstein, *Tractatus*, 3.32–3.327][tlp]; [Matrix, discusión][m-discusion]
2. **Máquinas simbólicas con funciones de reconocimiento, activación y composición.** Se propone investigar cómo una configuración podría activar contextos pertinentes, reconocer relaciones y componer operaciones sobre \(W_i\). La analogía con redes neuronales e intuición exige describir esas funciones y explicar su adquisición o reorganización. Los antecedentes incluyen un cálculo lógico de redes idealizadas y el debate sobre procesos simbólicos y subsimbólicos; ninguno valida por sí mismo la propuesta de Matrix. [McCulloch y Pitts, 1943, §§1–3][mcp]; [Smolensky, 1988, §§2 y 6][smolensky]; [Matrix, campos semánticos, §§3, 6 y 10][m-campos]
3. **Tipado contextual.** La separación entre admisibilidad y evaluación factual permitirá identificar ciertos errores antes de aceptar una proposición. La garantía estará condicionada por el esquema, las reglas y la corrección de la interpretación lingüística. [Matrix, pipeline, etapas 3–5][m-pipeline]; [revisión FJpU, debilidad sobre construcción de esquemas][m-r3]

## 3. Fundamentos que debe desarrollar el texto

### 3.1. Wittgenstein: signo, símbolo, forma lógica y sentido

**Argumento a desarrollar.** El *Tractatus* proporciona distinciones entre signo perceptible, uso lógico-sintáctico, representación de posibilidades y verdad de la representación. Las categorías de Wittgenstein determinan las condiciones de la figuración lógica y demarcan «lo que se puede decir» con sentido en un dominio determinado. También distingue las tautologías y contradicciones (*sinnlos*) de las combinaciones que carecen de forma lógica compartida o violan las condiciones de representación (*unsinnig*). En el marco propuesto, estas categorías fijan la admisibilidad dentro del grafo booleano antes de evaluar la verdad fáctica. Esas distinciones motivan una reconstrucción computacional, cuya correspondencia con el texto debe argumentarse. [Wittgenstein, *Tractatus*, 2.1–2.225, 3.32–3.327, 4.024, 4.46–4.4611][tlp]

**Tensión que debe tratarse.** El desacoplamiento propuesto separa formulación ordinaria y operación en un simbolismo explícito. Su relación con el pensamiento requiere discutir *Tractatus* 3.5 y 4, donde pensamiento y proposición con sentido están estrechamente vinculados, junto con 4.002, sobre el ocultamiento de la forma del pensamiento por el lenguaje ordinario. Esos pasajes impiden atribuir sin argumento a Wittgenstein la independencia general entre lenguaje y pensamiento. [Wittgenstein, *Tractatus*, 3.5–4.002][tlp]

**Contrapunto a desarrollar.** Las *Investigaciones filosóficas* introducen la diversidad de juegos de lenguaje y relacionan, para una amplia clase de casos, significado y uso. Servirán para examinar cómo se delimitan las prácticas de interpretación y qué se pierde al reducirlas a un esquema local. La articulación entre ambos libros será una cuestión del proyecto. [Wittgenstein, *Investigaciones*, §§7, 23 y 43][pi]

**Distinción pendiente.** Precisar cuándo una coordenada ausente indica falta de conocimiento, falta de representación o inadmisibilidad según las reglas. El problema está identificado por la revisión FJpU y no se resuelve llamando *unsinnig* a todo lo que el modelo no contiene. [Revisión FJpU][m-r3]

**Otra distinción constitutiva.** Separar la constancia de una propiedad en la tabla actual, su condición de pertenencia a un contexto y la tautología bajo todas las valuaciones pertinentes. El uso local de «no discriminante» en Matrix requiere una definición propia para conectarse con *sinnlos*. [*Tractatus*, 4.46–4.4611][tlp]; [Matrix, representación, ejemplo de verduras][m-representacion]

### 3.2. Lenguaje y pensamiento como capacidades distinguibles

**Argumento a desarrollar.** Fedorenko, Piantadosi y Gibson reúnen evidencia de disociación entre lenguaje y otras capacidades cognitivas y defienden una función primordialmente comunicativa del lenguaje. Se utilizará este antecedente para motivar la separación de funciones; la elección de una realización booleana seguirá siendo una propuesta específica de esta investigación. [Fedorenko et al., 2024][fedorenko]

**Definición de trabajo propuesta.** En el modelo se llamará «operación simbólica» a una transformación explícita de representaciones bajo reglas declaradas. Su relación con el pensamiento será objeto de discusión, evitando definir todo pensamiento mediante la implementación que se pretende evaluar. El marco operativo de partida es el compilador de reglas y el motor de inferencia de Matrix. [Arquitectura booleana, §§2–3][m-booleana]

### 3.3. Fundamento lingüístico: de la expresión a la operación

**Problema a desarrollar.** Bender y Koller distinguen forma lingüística y significado, e interrogan qué puede aprenderse de la forma por sí sola. Esa discusión ayuda a formular una exigencia para Matrix: especificar qué relación existe entre el enunciado y su interpretación, además de mostrar que la representación resultante puede ejecutarse. [Bender y Koller, 2020][bender]

**Composicionalidad y preservación.** Partee presenta la relación sistemática entre estructura sintáctica e interpretación, incluyendo condiciones de verdad y dependencia contextual. El marco propuesto deberá indicar qué conserva al pasar de una expresión a sus coordenadas: participantes, predicado, negación, alcance, condiciones y dependencias del contexto. La lista constituye una exigencia teórica del proyecto para el fragmento elegido. [Partee, 2012, §§1 y 3][partee]; [Matrix, pipeline, §§1–3][m-pipeline]

**Función del enunciado.** Austin distingue el acto de decir algo de lo que se hace al decirlo. Esa diferencia exige que el marco trate de manera explícita la afirmación, la pregunta, la suposición y la instrucción. La forma `(R a b)` debe acompañarse de un modo de uso y de condiciones de interpretación; compartir contenido no implica autorizar la misma operación sobre el estado de conocimiento. [Austin, 1962, lección VIII, pp. 98–101][austin]; [Matrix, pipeline, etapas 2–3][m-pipeline]

**Tipado e interpretación flexible.** Pustejovsky analiza coerción de tipos y polisemia sistemática: una combinación aparentemente incompatible puede admitir una interpretación mediante una operación semántica. El marco deberá distinguir esa posibilidad de una incompatibilidad efectivamente justificada. Esto proporciona una objeción lingüística concreta a tratar cualquier desajuste inicial como sinsentido. [Pustejovsky, 1991, pp. 424–430][pustejovsky]

**Restricción del desacoplamiento.** Pustejovsky también exige atender a la estructura sintáctica para explicar el significado. La variación superficial y la organización que aporta a la interpretación deberán distinguirse al formular el desacoplamiento. [Pustejovsky, 1991, introducción, p. 410][pustejovsky]

**Capacidad expresiva y formalismo de grafos.** Un conjunto de celdas relacionales operando en un semianillo booleano conforma un grafo capaz de mapear cualquier tipo de operación lógica formalizable en tuplas \((R, A, B) \in \{0, 1\}\). Esta capacidad abarca dimensiones heterogéneas:
1. *Asignación de propiedades:* predicación directa donde \(A\) posee el atributo \(B\) bajo la relación \(R\).
2. *Secuencias temporales y de estado:* codificación de orden cronológico, precedencia y relaciones de transición entre eventos.
3. *Operaciones y conectivas lógicas:* composición booleana, implicación de caminos y evaluación de condiciones.
4. *Metamapas relacionales y anclaje contextual:* mapeo reflexivo donde una relación \(R\) o un par de entidades \((A, B)\) se proyectan hacia *contextos particulares*, posibilitando el enrutamiento y la interacción entre mundos locales.

La tesis debe explicar qué estructura conserva este mapeo de grafos, qué aporta cada modalidad al marco y qué inferencias licencia rigurosamente; por ejemplo, encontrar un término medio entre dos relaciones permite recorrer una ruta en el grafo, pero inferir una conclusión formal exige justificar la regla lógica correspondiente. [Matrix, campos semánticos, §§1–8][m-campos]; [implementación de composición, función `compose`][m-composicion]

**Lectura teórica a incorporar.** Contrastar esta traducción con la semántica formal y composicional de Montague. *Universal grammar* queda como referencia de trabajo cuyo desarrollo técnico debe leerse antes de fijar las afirmaciones del anteproyecto sobre composicionalidad y tipos; en esta versión se verificó su registro bibliográfico. [Montague, 1970][montague]

**Vocabulario provisional de los juicios.** La siguiente tabla es una propuesta de organización teórica. En este documento «aplicabilidad contextual» designa el juicio de admisibilidad contextual. El «estatus factual» registra el respaldo disponible; no se usa como sinónimo de conocimiento completo ni de admisibilidad. Las filas describen dimensiones que pueden combinarse. Los problemas que motivan esta organización están documentados en las revisiones y en el modelo de trabajo. [Revisión FJpU][m-r3]; [contexto y WiGame][m-contexto]; [operatoria][m-recetas]

| Juicio propuesto | Pregunta | Diagnósticos por precisar | Fundamento del juicio |
|---|---|---|---|
| Representabilidad | ¿El esquema puede expresar el candidato? | Representable / esquema insuficiente | Vocabulario y estructuras representativas |
| Firma o tipado relacional | ¿Los argumentos cumplen la firma declarada? | Compatibles / incompatibles / información insuficiente | Tipos y firma de la relación |
| Admisibilidad contextual | ¿El contexto autoriza esta combinación? | Admitida / excluida / pendiente de determinación | Reglas y alcance del contexto |
| Habilitación operacional | ¿Se cumplen las condiciones para ejecutar la operación? | Habilitada / no habilitada / pendiente | Precondiciones y estado de la máquina |
| Estatus factual | ¿Qué respaldo tiene el contenido? | Respaldado / refutado / no determinado | Evidencia y compromisos del estado factual |
| Consistencia | ¿Qué ocurre al incorporar el contenido al conjunto de compromisos? | Compatible / conflicto derivable / examen pendiente | Afirmaciones, negaciones y reglas de consecuencia |

**Retorno como problema lingüístico.** Se propondrán condiciones para pasar del resultado operado a una expresión que preserve contenido, contexto, modalidad de uso y respaldo. El retorno canónico del motor es un antecedente parcial; el problema teórico incluye qué debe conservar una formulación verbal y cómo declarar las pérdidas de la traducción. [Modelo de trabajo: emisión canónica][m-retorno]; [composicionalidad: Partee][partee]; [función del enunciado: Austin][austin]

### 3.4. Artefactos formales e intuición

**Interlocutor teórico.** Smolensky distingue procesamiento intuitivo e interpretación de reglas, discute la explicación subsimbólica y contempla su integración con mecanismos simbólicos. El proyecto debe argumentar en qué sentido el reconocimiento y la composición sobre \(W_i\) ofrecen una alternativa o una articulación con esas funciones. La posibilidad de expresar cálculo y redes en un mismo formalismo requiere además distinguir correspondencia computacional, aprendizaje y explicación cognitiva. [Smolensky, 1988, §§2.3–2.4 y 6][smolensky]; [McCulloch y Pitts, 1943][mcp]

**Analogía por precisar.** El estudio de la intuición experta proporciona condiciones sobre regularidades y aprendizaje que pueden orientar esa discusión. En Matrix deben distinguirse la representación ya construida, la selección de operaciones y la formación o modificación de contextos: la documentación actual mantiene abierta la búsqueda de particiones. [Kahneman y Klein, 2009][intuicion]; [Matrix, campos semánticos, §§6 y 10][m-campos]

## 4. Objetivos propuestos

**Objetivo general:** construir y fundamentar un marco teórico que articule interpretación lingüística, representación lógica contextual y operación simbólica, utilizando Matrix como modelo de trabajo para precisar sus conceptos y condiciones de adecuación. [Antecedentes propios: representación][m-representacion] y [campos semánticos][m-campos]

1. Precisar las relaciones entre signo, símbolo, sentido, verdad y contexto utilizadas por el marco, explicitando su reconstrucción de Wittgenstein. [Antecedentes: *Tractatus*][tlp]; [*Investigaciones*][pi]
2. Establecer condiciones de adecuación para la ida y vuelta entre expresión lingüística y representación operable, atendiendo a composicionalidad, función del enunciado, contexto y respaldo que debe conservar la formulación del resultado. [Antecedentes: Partee][partee], [Austin][austin], [pipeline SMG][m-pipeline] y [retorno canónico][m-retorno]
3. Delimitar las funciones de reconocimiento, activación y composición de máquinas sobre \(W_i\), argumentando su relación con las nociones de intuición y procesamiento neuronal. [Antecedentes: Smolensky][smolensky], [McCulloch y Pitts][mcp] y [campos semánticos][m-campos]
4. Proponer un marco de tipado lógico que articule los juicios de representabilidad, firma relacional, admisibilidad contextual, habilitación operacional, estatus factual y consistencia definidos provisionalmente en §3.3, y examinarlo mediante casos contrastivos. [Antecedentes propios: pipeline][m-pipeline], [política de símbolos][m-kernel] y [revisión FJpU][m-r3]

## 5. Método: construcción teórica y examen de condiciones de adecuación

**Reconstrucción conceptual.** Examinar los textos filosóficos y cognitivos, formular el argumento del artefacto y reconstruir sus objeciones. Producir una tabla: concepto fuente → definición propuesta → función dentro del marco → condición que podría mostrar su insuficiencia. Las correspondencias se defenderán textualmente y por sus consecuencias conceptuales. [Fuentes de partida: *Tractatus*][tlp], [*Investigaciones*][pi], [Olson][olson] y [Smolensky][smolensky].

**Especificación formal.** Definir los objetos del marco y desarrollar los juicios de la tabla de §3.3. Se proponen tres requisitos: distinguir esos juicios y explicar sus interacciones; declarar qué estructura conserva cada traducción, incluida la formulación del resultado; y explicitar las reglas que justifican cada operación. Su formulación responde a problemas documentados del proyecto. [Revisión FJpU][m-r3]; [pipeline][m-pipeline]; [campos semánticos][m-campos]

**Casos contrastivos.** Trabajar un conjunto breve de casos que someta las definiciones a dificultades diferentes. Cada caso contendrá expresión, contexto, representación, operación autorizada, resultado y objeción. Los siguientes son diseños del anteproyecto, motivados por los antecedentes indicados:

| Caso propuesto | Pregunta para el marco | Antecedente |
|---|---|---|
| Paráfrasis y cambio de contexto | ¿Cuándo debe conservarse la representación y cuándo variar? | [Signo y símbolo, TLP 3.32–3.327][tlp]; [WiGame][m-contexto] |
| Afirmación, pregunta y suposición sobre el mismo contenido | ¿Qué se puede incorporar al estado factual? | [Austin, lección VIII][austin]; [pipeline][m-pipeline] |
| Desajuste inicial de tipos e interpretación recuperable | ¿Qué autoriza una coerción y qué justifica rechazar? | [Pustejovsky, pp. 424–430][pustejovsky] |
| Coordenada desconocida, falta de evidencia e inadmisibilidad declarada | ¿Qué diagnóstico exige ampliar el contexto, consultar evidencia o rechazar? | [Revisión FJpU][m-r3] |
| Columna constante y tautología | ¿Qué diferencia la falta de discriminación local de la verdad lógica? | [TLP 4.46–4.4611][tlp]; [tabla de verduras][m-representacion] |
| Dos mundos que comparten un término | ¿Qué permite recorrerlos y qué regla permite concluir algo? | [Composición por término medio][m-composicion] |
| Resultado desconocido o dependiente de un contexto, formulado de regreso | ¿La expresión conserva esa limitación o introduce una afirmación adicional? | [Retorno canónico][m-retorno]; [función del enunciado: Austin][austin] |
| Misma operación bajo reglas de prácticas diferentes | ¿Qué significa tipar una operación en su contexto de uso? | [Operatoria de recetas y máquinas de estados][m-recetas] |

**Criterios de examen.** Considerar consistencia interna, adecuación de la reconstrucción, conservación de diferencias lingüísticas y poder para formular problemas que puedan discutirse con otras teorías. La implementación servirá para inspeccionar qué distinciones se realizan y cuáles requieren desarrollo. Estos son criterios metodológicos propuestos para la tesis; su aplicación podrá conducir a modificar el marco. [Problemas de partida: revisiones][m-review] y [límites actuales de Matrix, campos semánticos §10][m-campos]

**Producto.** Un argumento defendido, un vocabulario conceptual, un esquema formal y casos trabajados. La comparación experimental de sistemas y el entrenamiento neuronal podrán derivarse posteriormente de las hipótesis que el marco consiga formular. [Dirección del proyecto: discusión][m-discusion] y [estado de integración con LLMs][m-review]

## 6. Aporte esperado y cierre

**Aporte propuesto.** Un andamiaje teórico para entender el artefacto formal que conecta expresión, representación y operación, y para precisar dos desarrollos: máquinas de reconocimiento y composición simbólica y tipado lógico de las emisiones de un LLM. La contribución lingüística consiste en explicar las condiciones de ese paso y retorno; la cognitiva, en argumentar la relación entre prácticas simbólicas, artefactos e hipótesis sobre pensamiento e intuición. [Antecedentes propios: discusión][m-discusion] y [campos semánticos][m-campos]; [interlocutores: Olson][olson] y [Smolensky][smolensky].

**Cierre por redactar.** Explicar qué aporta esta investigación al estudio de la relación entre lenguaje, pensamiento y artefactos de razonamiento, distinguiendo el resultado formal de sus posibles interpretaciones cognitivas. [Antecedentes para la discusión: Mahowald et al.][mahowald], [Fedorenko et al.][fedorenko] y [Clark y Chalmers][clark].

## 7. Referencias

La lista bibliográfica completa, los localizadores y el alcance de cada fuente están en [notas_fuentes.md](notas_fuentes.md). En la versión de postulación deberán incorporarse aquí las referencias efectivamente utilizadas y comprobarse el límite total de cinco páginas.

[programa]: https://filosofia.uchile.cl/dam/jcr:58d4451c-c338-482a-9680-e5064cb42cd6/MAG%C3%8DSTER%20EN%20ESTUDIOS%20COGNITIVOS.pdf
[mahowald]: https://mahowak.github.io/assets/pdf/mahowald2024dissociating.pdf
[fedorenko]: https://doi.org/10.1038/s41586-024-07522-w
[clark]: https://www.consc.net/papers/extended.html
[bender]: https://aclanthology.org/2020.acl-main.463/
[tlp]: https://www.gutenberg.org/files/5740/5740-pdf.pdf
[pi]: https://www.wittgensteinproject.org/w/index.php/Philosophische_Untersuchungen
[montague]: https://doi.org/10.1111/j.1755-2567.1970.tb00434.x
[intuicion]: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf
[m-representacion]: ../Matrix/paper_v2/sections/03_proposed_representation.md
[m-discusion]: ../Matrix/paper_v2/sections/04_discussion.md
[m-conclusion]: ../Matrix/paper_v2/sections/09_conclusion.md
[m-pipeline]: ../Matrix/Matrix/docs/language_to_matrix_pipeline.md
[m-booleana]: ../Matrix/Matrix/docs/pure_boolean_matrix_architecture.md
[m-recetas]: ../Matrix/Matrix/docs/operatoria_recetas.md
[m-review]: ../Matrix/review/summary_response_current_state.md
[m-r3]: ../Matrix/review/response3.md
[olson]: https://people.duke.edu/~wj25/ereserves/WJ-Olson.pdf
[smolensky]: https://home.csulb.edu/~cwallis/382/readings/482/smolensky.proper.treat.pdf
[mcp]: https://gwern.net/doc/ai/nn/1943-mcculloch.pdf
[austin]: https://pure.mpg.de/pubman/item/item_2271128_6/component/file_2271430/austin_1962_how-to-do-things-with-words.pdf
[partee]: https://people.umass.edu/partee/RGGU_Web_12/materials/RGGU121_2up.pdf
[pustejovsky]: https://aclanthology.org/J91-4003.pdf
[m-contexto]: ../Matrix/Matrix/docs/context_and_wigame.md
[m-campos]: ../Matrix/Matrix/docs/semantic_fields.md
[m-kernel]: ../Matrix/Matrix/docs/kernel_symbol_policy.md
[m-composicion]: ../Matrix/Matrix/src/operational_model/routing/middle_term.py
[m-retorno]: ../Matrix/Matrix/src/operational_model/system/projection_emit.py
