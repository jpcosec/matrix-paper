# Interpretacion y formulacion matematica

Este documento presenta una formulacion matematica compacta del sistema propuesto. Su objetivo es fijar, con la menor cantidad posible de ambiguedades, la relacion entre contexto, espacio logico, verdad, sentido, composicion y consulta.

## 1. Estructura general

Sea `C_i` un contexto formal. Un contexto queda caracterizado por la tupla:

`C_i = (E_i, R_i, T_i, L_i, V_i, S_i)`

donde:

- `E_i` es el conjunto de entidades del contexto,
- `R_i` es el conjunto de relaciones disponibles,
- `T_i` es el sistema de tipos del contexto,
- `L_i` es el espacio logico de proposiciones bien formadas,
- `V_i` es la funcion de verdad,
- `S_i` es la funcion de sentido o aplicabilidad.

La estructura operativa relevante no es el mundo en general, sino un recorte formalizable del mundo sobre el cual pueden construirse proposiciones, evaluarse hechos y componerse consultas.

## 2. Espacio logico

`L_i` es el conjunto de coordenadas proposicionales admisibles dentro del contexto. Su funcion es fijar que expresiones pueden construirse de manera valida, no si son verdaderas ni si tienen aplicabilidad factual.

### 2.1. Caso binario

Si el contexto contiene objetos `O_i` y propiedades `P_i`, entonces:

`L_i subseteq O_i x P_i`

Cada coordenada `(o,p)` representa una proposicion del tipo `p(o)`.

### 2.2. Caso general

Para cada relacion `r` de aridad `n` con firma:

`r : A_1 x A_2 x ... x A_n`

definimos:

`L_i(r) subseteq A_1 x A_2 x ... x A_n`

y el espacio logico total como:

`L_i = union_r ({r} x L_i(r))`

Asi, `L_i` puede representarse matricialmente en el caso binario y tensorialmente en el caso n-ario.

## 3. Verdad y sentido

La verdad se modela por:

`V_i : L_i -> {0,1}`

donde `V_i(x) = 1` indica que `x` es verdadera en el contexto y `V_i(x) = 0` que es falsa.

El sentido se modela por:

`S_i : L_i^+ -> {0,1}`

donde `L_i^+` denota un espacio logico potencialmente extendido de coordenadas consultables, y:

- `S_i(x) = 1` indica que `x` aplica o tiene sentido,
- `S_i(x) = 0` indica que `x` no aplica o no debe evaluarse factualemente.

La separacion entre `V_i` y `S_i` permite distinguir entre:

- proposiciones con sentido pero falsas,
- proposiciones con sentido y verdaderas,
- proposiciones sin aplicabilidad,
- expresiones fuera del espacio logico.

## 4. Proyeccion operativa

La proyeccion operativa del contexto queda definida por:

`W_i^*(x) = V_i(x) AND S_i(x)`

`W_i^*` no sustituye al contexto, sino que constituye su capa booleana operable. Su utilidad principal es permitir consultas, composiciones y proyecciones sin colapsar la diferencia entre falsedad y falta de sentido.

En esta formulacion, `Ø` no se toma como un tercer valor booleano interno. Se interpreta semanticamente como manifestacion de `S_i(x) = 0`.

## 5. Ejemplo base: verduras

Sea:

- `O_i = {lettuce, spinach, carrot, celery}`
- `P_i = {vegetable, food, leaf, root, stem}`
- `L_i = O_i x P_i`

La funcion de verdad queda dada por la matriz:

| object   | vegetable | food | leaf | root | stem |
| -------- | --------- | ---- | ---- | ---- | ---- |
| lettuce  | 1         | 1    | 1    | 0    | 0    |
| spinach  | 1         | 1    | 1    | 0    | 0    |
| carrot   | 1         | 1    | 0    | 1    | 0    |
| celery   | 1         | 1    | 0    | 0    | 1    |

En la formulacion minima, todas las coordenadas del ejemplo tienen aplicabilidad:

`S_i(o,p) = 1` para todo `(o,p) in L_i`

por lo que inicialmente:

`W_i^* = V_i`

## 6. Tautologia contextual y reduccion descriptiva

Una propiedad `p` es tautologica en el contexto si:

`forall o in O_i, V_i(o,p) = 1`

En el ejemplo, `vegetable` y `food` son tautologicas. No deben eliminarse de la ontologia, pero si pueden excluirse de operadores de discriminacion interna. La base descriptiva reducida queda entonces:

- `P_i' = {leaf, root, stem}`

## 7. Ambiguedad y desambiguacion

Dos entidades `a` y `b` son indistinguibles respecto de un conjunto de propiedades `Q subseteq P_i` si:

`forall p in Q, V_i(a,p) = V_i(b,p)`

En el ejemplo reducido, `lettuce` y `spinach` son indistinguibles. La desambiguacion requiere introducir nuevas dimensiones o un subcontexto especializado.

Sea el subcontexto:

- `E_leaf = {lettuce, spinach}`
- `P_leaf = {rough, smooth}`
- `L_leaf = E_leaf x P_leaf`

con tabla:

| object   | rough | smooth |
| -------- | ----- | ------ |
| lettuce  | 0     | 1      |
| spinach  | 1     | 0      |

La desambiguacion no se entiende entonces como expansion ciega del contexto general, sino como refinamiento localizado.

## 8. Proyeccion de subcontextos y recuperacion de `S_i`

Un subcontexto como `W_leaf` puede proyectarse sobre el espacio base del contexto principal. Si `P_leaf` son nuevas propiedades introducidas localmente, definimos:

`L_i^+ = L_i union (E_i x P_leaf)`

Esta extension no basta por si sola, porque las nuevas coordenadas no aplican a todos los objetos del contexto base. Por tanto, la proyeccion induce una mascara:

- `S_i(o,p) = 1` si `p` aplica a `o`,
- `S_i(o,p) = 0` si `p` no aplica, aunque la coordenada exista en `L_i^+`.

Este punto es estructural: la proyeccion de subcontextos permite enriquecer el espacio base sin destruir la informacion sobre aplicabilidad. En consecuencia, `S_i` deja de ser un accesorio local y pasa a ser la condicion de composicionalidad del sistema.

## 9. Composicion de tablas de verdad

Si dos estructuras logicas parciales pueden proyectarse sobre un mismo espacio booleano ampliado y conservan su mascara de sentido, entonces pueden componerse sin perder la distincion entre:

- verdad,
- falsedad,
- e inaplicabilidad.

Esto vale tanto para objetos y propiedades como para pares mas generales, por ejemplo sujeto-predicado o antecedente-consecuente. La composicion no consiste solo en unir matrices, sino en unir matrices bajo una ley de aplicabilidad explicita.

## 10. Grafos de conocimiento matriciales

La representacion matricial de hechos induce directamente una representacion como grafo de conocimiento.

- en el caso binario, una matriz booleana puede leerse como matriz de incidencia o adyacencia,
- en el caso n-ario, una familia de tensores booleanos puede leerse como familia de hiperaristas,
- las entidades actuan como nodos tipados,
- las relaciones verdaderas actuan como aristas o hiperaristas,
- las mascaras de sentido delimitan las regiones semanticamente validas del grafo.

El grafo no es entonces una estructura separada del algebra, sino una lectura estructural del mismo sistema de hechos.

## 11. Crecimiento del sistema

El agregado de un hecho nuevo admite dos casos.

### 11.1. Caso base

Si el hecho ya corresponde a una coordenada existente `x in L_i`, agregarlo consiste en actualizar su valor factual:

- asignar `V_i(x) = 1` o `V_i(x) = 0`,
- y verificar o conservar `S_i(x)`.

### 11.2. Caso de expansion

Si el hecho introduce una nueva entidad, una nueva propiedad o una nueva relacion, el espacio logico debe expandirse.

Para una nueva entidad `e_new`:

- `E_i' = E_i union {e_new}`
- `L_i' = L_i union ({e_new} x P_i)`

Para una nueva propiedad `p_new`:

- `P_i' = P_i union {p_new}`
- `L_i' = L_i union (E_i x {p_new})`

En ambos casos, toda nueva coordenada obliga a evaluar dos cosas:

- si tiene sentido,
- y si, teniendolo, es verdadera o falsa.

El crecimiento del sistema nunca es puramente sintactico; es siempre una extension simultanea de forma, sentido y verdad.

## 12. Consultas

Una consulta simple por propiedad queda definida como:

`Ans(p) = {o in O_i | S_i(o,p)=1 and V_i(o,p)=1}`

Una consulta conjuntiva queda definida como:

`Ans(p1 AND p2) = {o in O_i | W_i^*(o,p1)=1 and W_i^*(o,p2)=1}`

Si una consulta no pertenece a `L_i`, no debe evaluarse como falsa sino como fuera de contexto:

- si `x notin L_i`, entonces `Eval(x) = UndefinedContext`

## 13. Relectura operativa de las categorias tractarianas

En este marco:

- `sinnvoll`: proposiciones en `L_i` con `S_i(x)=1` y valor de verdad evaluable,
- `sinnlos`: proposiciones u operadores validos pero no informativos para la tarea, como tautologias contextuales,
- `unsinnig`: expresiones fuera de `L_i` o sin coordenadas admisibles en el contexto.

## 14. Alcance conceptual

El resultado es una familia de contextos logicos que puede representarse en espacios booleanos matriciales o tensoriales, componerse por proyeccion, refinarse por desambiguacion y consultarse algebraicamente. Esto permite pensar el sistema no solo como almacenamiento factual, sino como base para maquinas de representacion logica donde contexto, verdad, sentido y desambiguacion formen una unica estructura operable.

En esta linea, el sistema no apunta primariamente a modelar lenguaje en cuanto signo, sino a modelar su proyeccion logica computable. Por eso puede servir como base para grafos de conocimiento auditables y eventualmente para modelos entrenables sobre estructuras de verdad y sentido: no `Language Models`, sino `Logic Representational Models` o `Wittgenstein Thought Models`.
