# Dudas abiertas del sistema

Este documento recoge las dudas que permanecen abiertas sobre el sistema computacional logico-algebraico propuesto. No son objeciones al enfoque general, sino puntos que conviene fijar con precision para convertirlo en una formulacion matematica estable y luego en una arquitectura implementable.

## 1. Estatuto exacto de `W_i`

No queda completamente fijado si `W_i` designa:

- una particion del mundo,
- la estructura de conocimiento asociada a esa particion,
- o el resultado operativo de combinar verdad y sentido.

La duda aparece porque en algunos pasajes `W_i` parece ser el dominio contextual mismo, mientras que en otros parece comportarse como una matriz booleana ya materializada.

Preguntas asociadas:

- `W_i` es un contexto, una base de hechos, o ambas cosas a la vez?
- Si `W_i = V_i AND S_i`, entonces donde vive formalmente la particion del mundo que delimita el sistema?
- Conviene distinguir entre contexto `C_i` y representacion operable `W_i`?

<!--  respuesta usuario: 


 -->

## 2. Contenido formal de `L_i`

`L_i` se describe como espacio logico o espacio de coordenadas admisibles, pero falta fijar si eso significa:

- solo un conjunto de ejes tipados posibles,
- un sistema de formacion de proposiciones,
- o una gramatica logica completa con restricciones de composicion.

Preguntas asociadas:

- `L_i` contiene tipos de entidades y relaciones?
- `L_i` contiene firmas relacionales de aridad mayor que 2?
- `L_i` define tambien reglas de buena formacion?

## 3. Distincion entre tautologia contextual y proposicion no informativa

En el ejemplo de verduras, `vegetable` y `food` son verdaderas para todos los objetos del contexto. Eso las vuelve tautologicas dentro de ese recorte y, por tanto, `sinnlos` en sentido tractariano-operativo.

Sin embargo, queda por fijar si toda propiedad constante en una particion debe considerarse necesariamente:

- tautologia contextual,
- verdad estructural,
- o simplemente propiedad no discriminativa.

Preguntas asociadas:

- toda columna constante debe eliminarse del espacio de busqueda?
- una propiedad universal puede seguir siendo util para enlazar contextos distintos?
- la nocion de `sinnlos` es local al contexto o global al sistema?

## 4. Estatuto del valor `Ø`

`Ø` parece usarse para representar hechos sin sentido o no aplicables, por ejemplo propiedades de hojas aplicadas a zanahoria o apio. Pero no queda completamente fijado si `Ø` es:

- un tercer valor logico,
- un marcador de no-aplicabilidad,
- una mascara semantica,
- o un valor que solo aparece en la representacion pero no en el algebra base.

Preguntas asociadas:

- `Ø` participa en las operaciones algebraicas?
- `Ø AND 1` da `Ø` o `0`?
- `Ø` debe conservarse durante el calculo y colapsarse solo al final?
- conviene tratarlo como valor semantico y no como valor booleano?

## 5. Articulacion entre `V_i` y `S_i`

Se entiende que `V_i` expresa verdad y `S_i` expresa sentido, pero no queda fijado el regimen de composicion.

Preguntas asociadas:

- se calcula primero la verdad y luego se enmascara por sentido?
- se calcula primero el sentido para restringir las operaciones permitidas?
- `V_i` y `S_i` se almacenan siempre por separado?
- existe una estructura derivada `W_i` solo para consulta eficiente?

## 6. Relaciones de aridad mayor

El ejemplo principal usa objetos contra propiedades, lo cual da una matriz de aridad 2. Pero muchos hechos reales requieren mas posiciones relacionales.

Ejemplo:

- `dar(Juan, libro, Maria, Madrid, t)`

Preguntas asociadas:

- estas relaciones viven en tensores de orden superior?
- se reifican como nodos intermedios?
- cada tipo relacional tiene su propio subespacio logico?
- como se consulta una relacion parcial, por ejemplo `dar(Juan, ?, Maria, ?, ?)`?

## 7. Criterio para crear subcontextos

El texto propone dos soluciones cuando algunas propiedades solo tienen sentido para una subclase de objetos:

- mantener una mascara de sentido `S_i`,
- o crear otra matriz `W'_i` especializada.

Pero no queda definido el criterio de decision.

Preguntas asociadas:

- cuando conviene usar mascara y cuando conviene factorizar el contexto?
- la decision depende de costo computacional, claridad semantica o ambas?
- los subcontextos forman una jerarquia o una red arbitraria?

## 8. Naturaleza de la ambiguedad

Se propone detectar ambiguedad mediante colisiones algebraicas entre objetos que comparten propiedades. La idea se entiende, pero falta fijar que cuenta exactamente como ambiguedad.

Preguntas asociadas:

- ambiguedad significa indistinguibilidad respecto del conjunto actual de propiedades?
- dos objetos pueden ser distintos ontologicamente pero equivalentes para una consulta dada?
- la desambiguacion siempre exige agregar nuevas propiedades?
- el contexto puede desambiguar sin ampliar dimensiones?

## 9. Capa signo -> simbolo

Filosoficamente, el texto distingue bien entre signo, simbolo y nombre. Pero computacionalmente falta fijar donde vive esa transicion.

Preguntas asociadas:

- la interpretacion de signos pertenece al sistema o a un modulo externo?
- esa capa es determinista, probabilistica o hibrida?
- el sistema recibe simbolos ya resueltos o tambien gestiona la resolucion lexical y contextual?

## 10. Regimen de respuestas ante consultas invalidas

No queda fijado que debe devolver el sistema cuando una consulta no encuentra coordenadas validas en `L_i`.

Casos distintos:

- la propiedad no existe,
- la propiedad existe pero no aplica al objeto,
- la propiedad aplica pero es falsa,
- la propiedad es tautologica y no informa.

Preguntas asociadas:

- todos esos casos deben colapsarse al mismo resultado?
- conviene distinguir `False`, `Undefined`, `Inapplicable` y `Trivial`?
- una consulta invalida debe devolver error de tipado, resultado vacio o mascara nula?

## 11. Regimen de crecimiento del sistema

Extender el sistema agregando objetos, propiedades o relaciones parece posible, pero falta fijar como evitar explosion combinatoria.

Preguntas asociadas:

- cada nueva dimension obliga a recalcular todas las mascaras de sentido?
- hay reglas de herencia entre contextos?
- puede haber plantillas de contextos para evitar recomputacion total?

## 12. Alcance de la nocion de sentido

Una duda de fondo es si `S_i` representa:

- buena formacion logica,
- aplicabilidad ontologica,
- pertinencia contextual,
- o una mezcla de las tres.

Esta distincion importa porque cada una induce reglas de inferencia distintas.

## 13. Relacion con inferencia

El sistema parece muy fuerte para indexacion, filtrado, deteccion de contradicciones y desambiguacion. Queda por fijar el alcance inferencial.

Preguntas asociadas:

- hay reglas para derivar hechos nuevos?
- las inferencias se expresan tambien como tensores o mascaras?
- la maquina es solo de seleccion y consistencia, o tambien de produccion de conocimiento?

## 14. Identidad entre objetos, tipos y propiedades

En el ejemplo, algunos ejes parecen ser clases (`vegetable`), otros propiedades (`leaf`), y otros posibles atributos heredados (`rough`, `smooth`). Queda por fijar si el sistema diferencia formalmente:

- pertenencia a clase,
- propiedad monadica,
- relacion n-aria,
- metapropiedad contextual.

## 15. Nivel exacto de algebra necesario

El texto habla de anillos booleanos, semianillos, productos tensoriales, mascaras y colapsos dimensionales. Conviene fijar una base algebraica precisa.

Preguntas asociadas:

- el algebra base es booleana binaria `{0,1}`?
- hace falta una extension trivaluada `{0,1,Ø}`?
- las operaciones se definen por contexto y por tipo de consulta?
- el producto usado es matricial booleano clasico o tensorial con mascaras tipadas?

## Cierre

La intuicion general del sistema si resulta inteligible: una maquina de hechos indexados por contexto, con separacion explicita entre verdad y sentido. Lo que falta fijar es el contrato formal entre sus componentes, sobre todo en torno a `W_i`, `L_i`, `S_i`, `V_i`, `Ø` y los criterios de expansion contextual.









Respuestas a Dudas.md
Siento que hay un par de cosas que son mas o menos obvias
.
1- primitivos logicos: ambos, imaginate una matriz con la siguiente forma; 

![[representacion.xlsx]]

se entiende como puede definirse ambos dentro de una misma matriz?
palabra/logica

Pero, para guardar informacion de forma ordenada la forma de arriba no es optima (porque es una forma menos eficiente de usar el espacio); es mejor un "tensor" de solo matrices bien definidas; cada una con un contexto particular y las "propiedades mapeables" escritas como vector entre tensor y tensor
. De esta forma podemos representar mas facilmente y seleccionar los contextos que necesitamos
. La representacion de arriba sirve para que una red neuronal la tome como input o la entregue como output (y aprenda de ella, lógicamente); el calculo logico mejor qque tome la otra forma
. Lo importante es notar que tanto las propiedades, las palabras, las operaciones logicas como tambien el mapeo de los wi (osea, la seleccion de contextos) se pueden representar como matrices booleanas
.
2- valor nulo: Hay que descubrir como "operativizarlo": El algebra booleana y en poarticular los mapas de karnaugh nos pueden ayudar en esto
. Ayudame a darle una vuelta a eso. Depende absolutamente de cual es la operacion, como se van a operativizar los S
.
3- Orden de la articulacion matematica: La verdad depende de los hechos que estamos representando en los Wi
. Los Si salen de 2 cosas 1- hechos no mapeados (sobre los que no tenemos información de verdad) 2- si partimos desde matrices "bien formadas", composiciones que dejan espacios incompatibles o sin significado (por ejemplo el caso de la propiedad verdura para todas las verduras en el paper, intentar meter/consultar un hecho contradictorio con algo que este en la matriz o bien algunos resultados de algunas proyecciones, como puede ser por ejemplo en el calculo de las colisiones)
. Si es sinnvoll, sinnlos y unsinnig; lo bonito de que wittgenstein haya escrito el tractatus en aleman es que ese sinn se refiere a sentido, pero tambien se refiere a tener o no tener significado
.
4- Complejidad y relaciones n-arias: tu ejemplo esta malo porque puede ser (en s-expression) (dar_libro juan maría), ahora, como representamos eso en simbolos atómicos sería (((dar libro) juan) maria)
. Osea, tenemos un Wi; entre acciones y objetos (con el hecho dar y libro) un Wi de ejecutantes de acciones y un Wi de receptores de acciones
. En una primera instancia naturalmente la cantidad de Wis se volverá explosiva, pero con el tiempo se ira normalizando
. De todas maneras; el motor rust lo necesito para guardar datos y ejecutar operaciones; la lógica que hay detras se ejecuta de otra forma y es materia de otro paper
.
5- Control de crecimiento del sistema: Los contextos funcionan como arboles
. Al insertar un hecho nuevo este puede entrar y meter ruido en una rama, sin embargo esto no tiene por qque afectar al resto
. De todas maneras, estamos vendo el motor por ahora, luego pasaremos a una aplicacion concreta
. Algo importante que notar aca si es que en algun momento vamos a tener que meter algo asi como entropía de shannon o indian buffet/chinese restaurant process para poder hacer que el sistema vaya buscando mejores representaciónes
. De todas maneras, no es materia de lo que estamos intentando lograr ahora
.
6-Regimen de respuestas: Tenemos una division categorica basica bastante rica en los textos de wittgenstein (y tenemos de hecho, información ahi que no estamos aprovechando ahora)
. Cada error debe tener su propia categoría, en que sistema decente has visto que todos los errores son el mismo?
7- Capa signo a simbolo: no es materia de lo que estamos viendo ahora, estamos diseñando un motor que guarda hechos (relaciones entre simbolos) y opera sobre ellos
.
8- la base de datos permite componer contextos y proyectar (por ejemplo si en un lado guardamos que los perros son mamiferos y que firulais es un perro, deberia ser capaz de decirnos que firulais es un mamifero)
. Cómo se logra esto es materia de mas adelante (muy posiblemente vamos a necesitar de un LLM, algun otro algoritmo o un operador que manualmente seleccione los contextos)
.
Sobre todo: Hay operaciones que son realizables matricialmente; y hay operaciones que no
. Lo que pueda ser realizable matricialmente deberia hacerse matricialmente
. NO estamos diseñando el sistema final; solo necesitamos algo que: 1- permita crear los LI (ejes con simbolos basicamente)
 2- permita inyectar hechos en los LI para usarlos como Wi (guardando una lista de los hechos para poder mapearlos a algo, como por ejemplo una ubicacion en un texto o el resultado de alguna funcion)
 3- permita crear los Si y sepa como operarlos
 4- permita manipular los Wi para poder componer, proyectar, consultar, validar, etc
 5- Permita indexar los Wi usando otros Wi
