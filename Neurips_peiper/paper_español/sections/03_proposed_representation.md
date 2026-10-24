# Representación propuesta

Consideremos la estructura lógica de una partición del mundo $W_i$ mediante el siguiente conjunto simbólico:

1. Un contexto, es decir, una partición sobre el mundo $W$ que limita lo que pertenece a $W_i$.
2. Un espacio lógico $L_i$ que describe las coordenadas de mapeo admisibles, por ejemplo objetos y sus propiedades.
3. Una matriz booleana $V_i$ que describe todas las relaciones que mapean los hechos en relación con su verdad.
4. Una matriz booleana $S_i$ que describe todas las relaciones que mapean los hechos en relación con su significado; es decir, su aplicabilidad dentro del espacio lógico.

![Un contexto $W_i=(C_i,R_i)$ instancia dos capas booleanas sobre la misma grilla $L_i$: la máscara de sentido $S_i$ (cruces admisibles) y la capa de verdad $V_i$ (hechos afirmados). Las consultas ven solo la proyección operativa $W_i^{*}=V_i\odot S_i$: un hecho inyectado fuera de la máscara es estructuralmente invisible. \label{fig:layers}](../figures/fig_layers.pdf){width=100%}

Entonces, podemos definir $W_i$ como la operación booleana AND entre $V_i$ y $S_i$ (véase la Figura~\ref{fig:layers}). Consideremos este pequeño ejemplo;

Table: Matriz $W_i$ que mapea objetos a sus propiedades.

|         | vegetal | alimento | hoja | raíz | tallo |
| ------- | ------- | -------: | ---: | ---: | ----: |
| lechuga | 1       |        1 |    1 |    0 |     0 |
| espinaca | 1      |        1 |    1 |    0 |     0 |
| zanahoria | 1     |        1 |    0 |    1 |     0 |
| apio    | 1       |        1 |    0 |    0 |     1 |

Es importante notar que, dentro de este espacio lógico, las propiedades "vegetal" y "alimento" son verdaderas para todos los objetos contenidos en nuestro $W_i$; es decir, son tautológicas según la definición del Tractatus y, por lo tanto, carecen de sentido (*sinnlos*). Comenzamos eliminándolas para facilitar el análisis posterior. $W^{T}_i$, la transpuesta de esta matriz, sería esencialmente un índice de propiedades y de los objetos a los que pertenecen.

Table: Matriz $W^{T}_i$, el índice transversal de propiedades y sus objetos correspondientes.

|      | lechuga | espinaca | zanahoria | apio |
| ---- | ------: | -------: | --------: | ---: |
| hoja |       1 |        1 |         0 |    0 |
| raíz |       0 |        0 |         1 |    0 |
| tallo |      0 |        0 |         0 |    1 |

Si designamos un semianillo booleano AND/OR sobre este espacio, podemos verificar algunos resultados útiles.

* Si realizamos la multiplicación matricial $W^T_i \otimes W_i$, obtenemos un mapa de co-ocurrencias de propiedades.
* La matriz $W$ sirve como espacio de indexación, lo que significa que podemos tomar un vector de propiedades codificado en one-hot $v_q$ que denota los objetos que queremos encontrar. Y mediante la multiplicación vectorial $W_i \otimes v_q$ encontrar aquellos vegetales que cumplen estas propiedades.

Volviendo a las categorías de sentido definidas en la Sección 2, las restricciones lógicas de este sistema se hacen claras. *Sinnlos* denota operaciones computables que no entregan información distintiva: ya sean tautologías (por ejemplo, buscar "alimento" devuelve todos los objetos) o contradicciones (por ejemplo, buscar simultáneamente "hoja" y "tallo"). Por el contrario, *Unsinnig* corresponde a operaciones que son estructuralmente inexpresables porque no existe una coordenada en $L_i$ (como preguntar por las "puertas" de un vegetal o por una propiedad no mapeada como "sabor dulce").

Hasta este punto, el sistema propuesto concuerda con la lógica booleana estándar sin ofrecer nada nuevo a las obras fundamentales de la lógica y la computación. Sin embargo, su verdadera utilidad emerge una vez que introducimos la indexabilidad y la no ambigüedad, como restricciones que permiten convertir esto en una suerte de máquina lógica de verdad.

Abordamos primero su extensibilidad. Extender $W_i$ para contener nuevos hechos es una operación directa. Si el hecho tiene una coordenada definida (objeto, propiedad) que es mapeable al $L_i$ actual, el mecanismo consiste en encontrar la coordenada y fijar su valor en verdadero. En caso contrario, la operación requerirá agregar un nuevo objeto o propiedad a las coordenadas y verificar su veracidad $W_i$ y su sentido $S_i$ para cada otra proposición que la adición dimensional genere.

Respecto de la ambigüedad en $W_i$, el sistema propuesto permite detectarla mediante una operación algebraica elemental.

* $W_i \otimes W^T_i$ entrega una matriz de objetos contra objetos, que contiene todos los hechos que denotan alguna veracidad en el mapa. Nótese que, en este caso, dado que nos interesan solo los objetos que comparten alguna propiedad en la realidad, la capa de sentido $S_i$ puede simplemente ignorarse. Además, la intersección de cualquier cosa con ∅ puede considerarse simplemente 0.

* $(W_i \otimes W^T_i) - \mathbb{I}$ limpia la diagonal, que contiene solo resultados tautológicos.

* Finalmente, al colapsar dimensionalmente esta matriz multiplicándola por un vector de unos, podemos detectar aquellos objetos que colisionan en alguna propiedad en $W_i$.

Entonces, para desambiguar estos objetos, introducimos una nueva propiedad en $L_i$ que permitirá diferenciarlos. En nuestro caso, dado que la dimensión de colapso es una hoja, lo más fácil es agregarle propiedades heredadas, por ejemplo, rugosa y lisa.

Table: Matriz extendida con propiedades heredadas y máscara de sentido ($\emptyset$) para coordenadas inválidas.

|         | hoja | raíz | tallo | (hoja) rugosa | (hoja) lisa |
| ------- | ---: | ---: | ---: | -----------: | ------------: |
| lechuga |    1 |    0 |    0 |            0 |             1 |
| espinaca |   1 |    0 |    0 |            1 |             0 |
| zanahoria |  0 |    1 |    0 |            Ø |             Ø |
| apio    |    0 |    0 |    1 |            Ø |             Ø |

Otro detalle se hace evidente: si particionamos por lechuga y espinaca sobre las propiedades relacionadas con la hoja, "hoja" se convierte en una propiedad tautológica (*sinnlos*). Sin embargo, para zanahoria y apio, estas propiedades de hoja recién introducidas son *unsinnig*: cualquier valor de verdad calculado para ellas carece estructuralmente de significado. La solución puede abordarse de dos maneras:

* Usar una máscara de sentido $S_i$ alrededor de los hechos que son indexables por estos objetos y propiedades, fijando el resultado en 0 para todo caso posible si se consulta por verdad.

* Crear otra matriz $W_i'$ que indexe solo los vegetales de hoja. Entonces, la operación de buscar vegetales por la propiedad de sus hojas pasa a ser $W_i \otimes p'_i \otimes W'_i \otimes p'_i$.

Esto produce algunos resultados interesantes:

- $W_i$ es básicamente un espacio de enrutamiento jerárquico que particiona $W_i \cup W'_i$; en otras palabras, un índice de contexto sobre un espacio lógico tensorial donde podemos identificar objetos por sus propiedades sin necesidad de usar $S_i$.
- La expansión y el colapso tensoriales son reversibles: $S( W_i \cup W'_i)$ puede recuperarse rellenando con Ø los hechos que las propiedades de $L'_i$ no mapean en $L_i$.
- El proceso es infinitamente recursivo, y permite uniones, intersecciones y toda otra operación de conjuntos que admita un anillo booleano. Y mientras permutemos correctamente las dimensiones, podemos reorganizar las rutas tensoriales como queramos.
- La introducción de jerarquías de contextos permite el uso de esta lógica como un índice de búsqueda en árbol. O bien, tratar un índice de búsqueda en árbol como una combinación de matrices de verdad y de sentido.
- En el ejemplo propuesto trabajamos con un $L_i$ que mapeaba objetos a propiedades, pero $L$ contiene toda relación expresable con lógica booleana. Las máquinas de estados, las s-expressions, los flujos if-else, entre otros, son solo instancias de lo que puede computarse con la combinación de sentido y lógica.
- Finalmente, mediante el uso de estos resultados, podemos obtener particiones de $S$, como un conjunto de reglas gramaticales lógicas algebraicamente computables para contextos determinados.

En palabras de Wittgenstein, hemos definido una proyección directa entre el pensamiento y su imagen lógica, representada en bits y operable mediante lógica booleana.
