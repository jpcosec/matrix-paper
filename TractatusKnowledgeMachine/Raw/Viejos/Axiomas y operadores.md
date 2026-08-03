# Axiomas y operadores

Este documento fija un nucleo formal minimo para el sistema. Su funcion no es agotar la teoria, sino establecer los axiomas operativos y los operadores algebraicos necesarios para construir, expandir y consultar contextos logicos.

## 1. Primitivos

Para cada contexto `C_i` se asumen los siguientes primitivos:

- un conjunto de entidades `E_i`,
- un conjunto de relaciones `R_i`,
- un sistema de tipos `T_i`,
- un espacio logico `L_i`,
- una funcion de verdad `V_i`,
- una funcion de sentido `S_i`.

## 2. Axiomas estructurales

### Axioma 1. Contextualidad

Toda proposicion evaluable pertenece a un contexto determinado.

Formalmente, no existe evaluacion de `V_i` ni de `S_i` sin referencia a un `C_i`.

### Axioma 2. Formacion

Una proposicion solo puede evaluarse si pertenece al espacio logico del contexto.

Si `x notin L_i`, entonces `x` es `unsinnig` respecto de `C_i`.

### Axioma 3. Separacion de verdad y sentido

Verdad y sentido son funciones distintas.

- `V_i` decide verdad factual,
- `S_i` decide aplicabilidad o sentido.

Por tanto, una proposicion puede tener sentido y ser falsa, o puede carecer de sentido sin ser por ello falsa.

### Axioma 4. Proyeccion operativa

La capa booleana operable del sistema es:

`W_i^*(x) = V_i(x) AND S_i(x)`

`W_i^*` no reemplaza a `V_i` ni a `S_i`; solo las proyecta para efectos de computacion y consulta.

### Axioma 5. Inaplicabilidad

El valor `Ø` no pertenece al algebra booleana interna del sistema. Se interpreta como notacion semantica externa para los casos en que `S_i(x)=0`.

### Axioma 6. Extension controlada

Toda expansion del espacio logico genera nuevas coordenadas cuya verdad y sentido deben determinarse explicitamente.

No existe crecimiento neutro del sistema.

### Axioma 7. Desambiguacion

Si dos entidades son indistinguibles respecto de una base descriptiva dada, el sistema puede:

- introducir nuevas dimensiones,
- crear un subcontexto,
- o proyectar un subcontexto sobre el espacio base con una nueva mascara de sentido.

### Axioma 8. Composicionalidad

Dos contextos o subcontextos pueden componerse si existe una proyeccion comun que preserve:

- coordenadas logicas,
- asignaciones de verdad,
- y mascaras de sentido.

## 3. Operadores de base

## 3.1. Operadores de formacion

### `WellFormed_i(x)`

Devuelve `1` si `x in L_i`, y `0` en caso contrario.

### `Applicable_i(x)`

Devuelve `S_i(x)`.

### `Truth_i(x)`

Devuelve `V_i(x)` cuando `x` es evaluable.

## 3.2. Operador de proyeccion operativa

### `Project_i(x)`

`Project_i(x) = V_i(x) AND S_i(x)`

Este es el operador elemental de consulta booleana.

## 3.3. Operadores de consulta

### Seleccion unaria

Para una propiedad `p`:

`Select_i(p) = {o in O_i | V_i(o,p)=1 and S_i(o,p)=1}`

### Conjuncion

Para propiedades `p_1, ..., p_n`:

`Conj_i(p_1,...,p_n) = intersection_k Select_i(p_k)`

### Disyuncion

`Disj_i(p_1,...,p_n) = union_k Select_i(p_k)`

### Negacion factual restringida

`Neg_i(p) = {o in O_i | S_i(o,p)=1 and V_i(o,p)=0}`

La negacion aqui no recupera lo inapplicable, solo lo falso con sentido.

## 3.4. Operadores de analisis estructural

### Tautologia contextual

Una propiedad `p` es tautologica en `C_i` si:

`forall o in O_i, S_i(o,p)=1 => V_i(o,p)=1`

### Contradiccion contextual

Una consulta conjuntiva es contradictoria si su interseccion de satisfactores es vacia y todas sus coordenadas tienen sentido.

### Indistinguibilidad

Dados `Q subseteq P_i`, dos entidades `a,b` son indistinguibles respecto de `Q` si:

`forall p in Q, Project_i(a,p) = Project_i(b,p)`

Si se quiere distinguir falsedad de inaplicabilidad en el analisis fino, puede usarse el par ordenado:

`Sigma_i(o,Q) = ((V_i(o,p), S_i(o,p)))_{p in Q}`

en vez de la sola proyeccion booleana.

### Coocurrencia

En el caso binario, si `M_i` es la matriz objeto-propiedad de `W_i^*`, entonces:

- `M_i^T otimes M_i` da coocurrencia de propiedades,
- `M_i otimes M_i^T` da similitud factual entre objetos.

Aqui `otimes` denota producto matricial booleano.

## 3.5. Operadores de extension

### Extension por nueva entidad

`ExtendEntity(C_i, e_new)` produce `C_i'` tal que:

- `E_i' = E_i union {e_new}`
- `L_i'` incorpora todas las coordenadas nuevas relevantes
- `S_i'` y `V_i'` quedan definidos sobre esas coordenadas nuevas

### Extension por nueva propiedad

`ExtendProperty(C_i, p_new, D_new)` produce `C_i'` tal que:

- `P_i' = P_i union {p_new}`
- `L_i'` incorpora `E_i x {p_new}`
- `S_i(o,p_new)` depende de `D_new`
- `V_i(o,p_new)` se evalua solo donde `S_i(o,p_new)=1`

### Extension por nueva relacion

`ExtendRelation(C_i, r_new)` agrega una nueva firma y el bloque tensorial correspondiente al espacio logico.

## 3.6. Operadores de subcontexto y proyeccion

### Restriccion

`Restrict(C_i, E', R') = C_j`

con `E' subseteq E_i` y `R' subseteq R_i`, produce un subcontexto `C_j`.

### Proyeccion de subcontexto

`ProjectSubcontext(C_j -> C_i)` incorpora al espacio base las nuevas dimensiones de `C_j` y genera una nueva mascara de sentido sobre la extension resultante.

### Union contextual

`Merge(C_i, C_j)` solo esta permitida si existe compatibilidad tipada y regla de alineamiento entre sus coordenadas.

## 4. Regimen de evaluacion

Dada una expresion `x`, la evaluacion debe seguir este orden:

1. verificar si `x` esta bien formada,
2. verificar si `x` pertenece a `L_i`,
3. verificar si `S_i(x)=1`,
4. solo entonces consultar `V_i(x)`.

Esto impide confundir:

- fuera de contexto,
- sin sentido,
- falso,
- y verdadero.

## 5. Regimen de consulta

Toda query debe devolver, al menos implícitamente, informacion sobre cuatro estados:

- verdadero,
- falso,
- trivial,
- fuera de contexto o inaplicable.

Si la implementacion requiere una respuesta unica, puede proyectar esos estados a una capa mas simple; pero la teoria no debe perder esa distincion.

## 6. Regimen de composicion

La composicion entre contextos se considera valida si:

- sus firmas pueden alinearse,
- sus dominios de aplicabilidad pueden representarse por mascaras compatibles,
- y existe una proyeccion comun donde la union no destruya la diferencia entre `V_i` y `S_i`.

Este es el punto que permite tratar el sistema como base para grafos de conocimiento composicionales y para modelos entrenables sobre estructuras logicas.

## 7. Cierre

El nucleo algebraico minimo del sistema consiste entonces en:

- un espacio logico tipado,
- una funcion de verdad,
- una funcion de sentido,
- una proyeccion operativa,
- operadores de consulta,
- operadores de extension,
- y operadores de restriccion, proyeccion y composicion.

Con eso ya queda definido un marco suficiente para pasar a una formulacion algoritmica concreta.
