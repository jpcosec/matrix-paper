# Reformulación del problema

Sea `W` el mundo entendido como el conjunto de todo aquello que puede, en principio, ser particionado, descrito o indexado por un sistema simbólico. El problema que nos interesa no es representar `W` en su totalidad, sino construir particiones operables de `W` sobre las cuales puedan definirse hechos, consultas y operaciones lógicas de manera computable.

## 1. Contexto

Definimos un contexto `C_i` como un criterio de pertenencia sobre `W`. En su forma más simple, puede entenderse como una función:

`C_i : W -> {0,1}`

tal que `C_i(x) = 1` si `x` pertenece al dominio contextual que queremos estudiar, y `C_i(x) = 0` en caso contrario.

El subconjunto inducido por `C_i` se denota:

`W_i = { x in W | C_i(x) = 1 }`

Por tanto, `W_i` no es el mundo completo, sino la partición del mundo que queda seleccionada por el contexto `C_i`.

La función del contexto no es todavía determinar ni la verdad ni el sentido de las proposiciones, sino fijar el dominio dentro del cual esas preguntas pueden plantearse.

Ejemplos intuitivos de contexto:

- hablar de todos los perros,
- programas de computación escritos en s-expressions,
- diagramas UML restringidos a diagramas de estado y diagramas de componentes.

En todos estos casos, el contexto define un recorte del mundo y, con ello, una familia limitada de objetos, relaciones y signos admisibles.

## 2. Espacio lógico

Una vez fijado `W_i`, definimos `L_i` como el espacio lógico del contexto. `L_i` no representa todavía hechos verdaderos, sino el conjunto de coordenadas proposicionales que pueden formarse de manera válida dentro de `W_i`.

En este sentido, `L_i` cumple dos funciones:

- determina qué tipos de entidades, propiedades y relaciones pueden intervenir en el contexto,
- determina qué combinaciones de esas entidades, propiedades y relaciones están bien formadas.

Por tanto, `L_i` puede entenderse como el conjunto de proposiciones posibles del contexto, o equivalentemente, como la estructura formal que define sus dimensiones de representación.

En el caso más simple, si el contexto contiene objetos `O_i` y propiedades `P_i`, entonces:

`L_i subseteq O_i x P_i`

Cada coordenada `(o, p)` representa una proposición posible del tipo `p(o)`.

En casos más generales, `L_i` puede incluir relaciones de aridad mayor y por tanto adoptar forma tensorial en lugar de matricial.

La función de `L_i` no es decidir si una proposición tiene sentido ni si es verdadera, sino solamente si puede ser construida dentro del marco formal del contexto.

## 3. Verdad

Definimos `V_i` como la función de verdad sobre el espacio lógico del contexto:

`V_i : L_i -> {0,1}`

donde:

- `V_i(x) = 1` indica que la proposición `x` es verdadera en el contexto,
- `V_i(x) = 0` indica que la proposición `x` es falsa en el contexto.

`V_i` describe entonces la distribución factual de los hechos dentro del espacio lógico ya formado.

En el caso objeto-propiedad, `V_i` puede representarse directamente como una matriz de bits.

## 4. Sentido

Definimos `S_i` como la función de sentido o aplicabilidad:

`S_i : L_i^+ -> {0,1}`

donde `L_i^+` denota el espacio lógico base `L_i` o una extensión suya cuando el contexto incorpora dimensiones proyectadas desde subcontextos.

donde:

- `S_i(x) = 1` indica que la proposición `x` tiene sentido, aplica o resulta interpretable dentro del contexto,
- `S_i(x) = 0` indica que la proposición `x` no tiene sentido, no aplica o no debe evaluarse factualemente dentro de ese contexto.

La distinción entre `L_i` y `S_i` es importante:

- `L_i` determina si una proposición puede formarse en el contexto base,
- `S_i` determina si, una vez formada o proyectada al espacio extendido, esa proposición es semánticamente aplicable.

Esto permite distinguir entre tres casos distintos:

- proposiciones bien formadas y con sentido,
- proposiciones bien formadas pero no aplicables,
- expresiones que ni siquiera pertenecen al espacio lógico del contexto.

## 5. Proyección operativa

La representación operable del contexto puede definirse como la combinación entre verdad y sentido:

`W_i^* = V_i AND S_i`

donde `W_i^*` ya no designa la partición del mundo, sino la proyección booleana utilizable por la máquina para operar sobre hechos válidos y con sentido.

Conviene distinguir entonces entre:

- `W_i`: el dominio contextual inducido por `C_i`,
- `W_i^*`: la proyección operativa de ese dominio en términos de verdad y sentido.

Esta distinción evita confundir el recorte ontológico del mundo con su representación computable.

## 6. Clasificación lógica de las proposiciones

Dentro de esta formulación, las categorías tractarianas pueden reinterpretarse operativamente del siguiente modo.

### 6.1. Sinnvoll

Una proposición es `sinnvoll` si:

- pertenece a `L_i`,
- tiene `S_i(x) = 1`,
- y admite evaluación de verdad en `V_i`.

Por tanto, una proposición `sinnvoll` puede resultar verdadera o falsa.

### 6.2. Sinnlos

Una proposición u operación es `sinnlos` cuando, siendo formalmente válida y aplicable, no aporta información discriminativa dentro del contexto.

Esto incluye, por ejemplo:

- tautologías contextuales,
- contradicciones estructurales conocidas,
- propiedades universalmente verdaderas o universalmente falsas para una partición dada.

En este sentido, `sinnlos` no significa error, sino validez sin contenido informativo relevante para la tarea.

### 6.3. Unsinnig

Una proposición es `unsinnig` respecto de `C_i` si no puede construirse en `L_i`, o si queda fuera del dominio semántico admisible del contexto.

Operativamente, esto corresponde a expresiones fuera de contexto, fuera de tipo o sin coordenadas válidas dentro del sistema.

## 7. Caso particular de interés

El caso particular que proponemos estudiar es el de aquellos contextos `W_i` cuya proyección operativa `W_i^*` puede representarse mediante matrices de bits y operaciones de lógica booleana.

En este caso:

- los hechos se representan como asignaciones booleanas sobre coordenadas del espacio lógico,
- la verdad se codifica en matrices o tensores de bits,
- el sentido se codifica en máscaras booleanas,
- y las consultas se resuelven mediante operaciones algebraicas sobre dichas estructuras.

Este recorte no pretende agotar la representación de todo lenguaje posible, sino identificar una familia de contextos suficientemente estructurados como para poder ser descritos, auditados y operados algebraicamente.

## 8. Problema central

El problema central puede formularse entonces así:

Dados un contexto `C_i`, un dominio contextual `W_i`, un espacio lógico `L_i`, una función de verdad `V_i` y una función de sentido `S_i`, construir una máquina capaz de:

- representar hechos de manera indexable,
- distinguir entre verdad, falsedad, trivialidad y falta de sentido,
- operar algebraicamente sobre esos hechos,
- detectar tautologías contextuales y contradicciones,
- detectar ambigüedad por indistinguibilidad estructural,
- y refinar el contexto mediante nuevas dimensiones o subcontextos cuando sea necesario.

## 9. Hipótesis de trabajo

La hipótesis de trabajo es que existe una clase no trivial de dominios donde la combinación de:

- partición contextual,
- espacio lógico tipado,
- matrices de verdad,
- y máscaras de sentido,

permite construir un sistema de representación del conocimiento que no solo almacena hechos, sino que además distingue formalmente entre:

- lo verdadero,
- lo falso,
- lo trivial,
- y lo que no tiene sentido dentro de un contexto dado.

## 10. Alcance

La máquina propuesta no pretende reemplazar sistemas estocásticos de lenguaje general ni capturar la totalidad del lenguaje natural. Su alcance es más preciso:

- operar sobre familias de documentos o dominios con estructura lógica suficientemente delimitable,
- permitir indexación, búsqueda, comparación y refinamiento contextual,
- y ofrecer una base algebraica para construir sistemas de conocimiento auditables por contexto, verdad y sentido.

En este marco, el ejemplo de vegetales y propiedades no es una mera ilustración pedagógica, sino la forma mínima de una clase más amplia de espacios lógicos representables por estructuras booleanas.
