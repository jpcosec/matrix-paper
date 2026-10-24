

El tractatus de Wittgenstein abre con una frase interesante **el mundo está compuesto por todos los hechos, no cosas**. Definamos cosas como los atomos que "indexan" lo que puede decirse (música, teorema, perro, color), y notemos que las cosas en abstracto no significan nada, estas cobran sentido solo a través de sus relaciones. Una cosa se relaciona con otra cosa a través de los hechos (el perro es blanco, la música suena, el teorema comprueba un axioma). Luego, , lo que nos permite  representar el mundo y darle una estructura lógica, no es la enunciación vacía de las cosas que lo componen, es la totalidad de sus relaciones.

**TLP 1.1: mundo como totalidad de hechos, no cosas. TLP 2.01: hecho como combinación de objetos. TLP 2.0272 y 2.031–2.034: los objetos se configuran en hechos/estructuras.

Una proposicion es una descripción de un hecho en relación a la realidad; un hecho que se expresa de forma perceptible por algun medio (sonido, signo escrito, bits, etc). Una proposición puede ser verdadera o falsa no según el hecho que describe, si no según su relación con la realidad. Y una proposición es capaz de tener sentido, según su capacidad de mostrar la verdad del hecho y su capacidad de articularse en un espacio lógico. Según su estado de sentido, una proposicion puede distinguirse entre 3 estados

* Sinnvoll: proposiciones con sentido, capaces de representar una posible situación del mundo. Por ejemplo, en españa el clima es calido, la novena sinfonía a escribió Beethoven, el fenomeno físico electromagnetico se puede describir por las cuatro ecuaciones elementales de Maxwell.
* Sinnloss: proposiciones que no dicen nada sobre el mundo, pero pertenecen legítimamente al simbolismo lógico, como tautologías y contradicciones.  Se sube hacia arriba, una persona es un humano, el gato de schröedinger está muerto y vivo.
* Unsinnig: formulaciones sin sentido lógico, donde los signos no han recibido una función significativa dentro del sistema, en otras palabras, proposiciones absurdas. El perro cabalga, la razon de la sin razon, p = ~p.

TLP 2.21–2.225, 4.05–4.06: verdad como comparación con la realidad.

Un signo es el medio sensible que permite el mapeo la transmicion de un hecho, un objeto o sus relaciones. Puede ser una señal sonora, una cualidad sobre una señal sonora, texto escrito, una imagen, música, un teorema, un codigo entre muchos. El signo no es el hecho mismo, pero es un mapeo del hecho a lo expresable. El hecho puede expresarse en muchos signos; el perro es amigable, el canino es confiable y  the dog is the best friend of the man expresan el mismo hecho.  00000011, 3 y drei designan la misma cantidad numerica. Del mismo modo un signo puede representar simbolos distintos, gift es regalo en ingles pero es alemán es veneno, el acto de mover la cabeza verticalmente suele ser universalmente aceptado como un gesto afirmativo pero en bulgaria significa no. 

Un simbolo es un signo y una estructura dentro de un espacio logico, usado dentro de un contexto; es decir, dentro de una particion suficientemente determinada de mundo. Un nombre es una referencia a esta estructura lógica, es decir, un mapeo entre signo y simbolo que está suficientemente determinado por el contexto, como para poder discriminarlo de otros simbolos.

Hagamos el ejercicio entonces de describir la totalidad de los hechos $W$, mediante la union del siguiente "conjunto simbólico",
1- Un contexto, es decir partición del mundo $W_i$.
2- Un espacio lógico $L_i$.
2- Una Matriz de valores booleanos que describe la totalidad de las relaciones que mapean los hechos en relacion a su verdad $M_i$.
3- Una matriz de valores booleanos que describe la totalidad de las relaciones que mapean los hechos en relacion a su sentido; es decir, a su aplicabilidad dentro del espacio lógico $S_i$.

Propongamos por ejemplo un caso de $W_i$ donde el mapeo que realizan los hechos sea el de objetos y propiedades, por ejemplo. 

```
           vegetal alimento hoja raiz tallo
lechuga         1       1      1    0    0
espinaca        1       1      1    0    0
zanahoria       1       1      0    1    0
apio            1       1      0    0    1
```

Una cosa que podemos notar inmediatamente es que dentro de este espacio lógico, las propiedades vegetal y alimento son ciertas para todos los objetos que contienen nuestro $W_i$, es decir, son tautologicas bajo la definicion del tractatus y por lo mismo carecen de sentido (sinloss). Comencemos por quitarlos para facilitar el análisis en adelante. La transversa de este W; $W^{T}_i$ sería basicamente un indice de propiedades y a que objeto pertenecen por ejemplo.

```
          lechuga zanahoria apio espinaca
hoja         1        0      0        1
raiz         0        1      0        0
tallo        0        0      1        0
```

Si designamos  semianillo booleano AND/OR sobre este espacio  se puede comprobar algunos resultados utiles. 
* Si multiplicamos matricialmente $W^T_i \otimes W_i$ podemos obtener un mapa de "coocurrencia de propiedades.
* La matriz $W$ sirve como un "espacio de indexación", es decir puedo tomar un vector de propiedades encodeadas en one hot $v_q$; por ejemplo quiero encontrar vegetales que tengan propiedad 

```

hoja         0 
raiz         0
tallo        1 
```
Y mediante multiplicación vectorial $W_i \otimes v_q$ encontrar aquellos vegetales que  cumplan estas propiedades. 

Volvamos un poco a wittgenstein;  cuales son las restricciones lógicas de este sistema?, aquellas de dan las categorías sobre el sentido que se definen en el tractatus. Una operación sobre este espacio lógico es **sinnlos** cuando la operacion puede realizarse, pero no dice nada, y se separan basicamente en 2.

* Tautología, cuando la propiedad da positivo para todos los casos, como las propiedades alimento y vegetal en el ejemplo original.
* Contradiccion, cuando el vector de busqueda da una combinacion de propiedades que no devuelve ningun objeto, como sería el caso de buscar hoja y tallo en nuestro caso.

Por otro lado wittgenstein define la categoría de **unsinnig**, absurdo o que no tiene significado. En nuestro caso, esta categoría se define como aquella que no tiene coordenada en el espacio que designan las dimensiones de $W_i$, como por ejemplo preguntar por las puertas del vegetal, o en nuestro universo pequeño, alguna propiedad que no hemos mapeado asi como por ejemplo  de sabor dulce.

Lógicamente, el sistema propuesto no propone mucho que no se haya propuesto ya en trabajos fundamentales de la lógica y la computación. El sistema toma utilidad cuando empezamos a extenderlo para que cumpla con las propiedades minimas de un sistema que permita buscar resultados individuales. Se puede extender y cada objeto contiene una combinacion de propiedades  individuales que permite indexarlo inequivocamente.
Sobre lo primero, extender $W_i$ para que pueda contener nuevos hechos,  es bastante facil, se busca la coordenada que designa objeto, propuedad y se cambia su valor a verdadero. El problema puede ocurrir cuando queremos meter hechos no estén mapeados por los ejes actuales. 



Sobre la ambiguedad en el $W_i$, en el sistema propuesto, esta  detectar se mediante una operacion algebraica elemental.  
* $W^i \otimes W^T_i$ nos da una matriz de objetos contra objetos, que contiene todos los hechos que denotan alguna propiedad en el mapa, notese que en este caso la capa de sentido $S_i$ puede ignorarse ya que lo que nos importa es solamente ver los objetos que comparten alguna propiedad en la realidad, el cruce de cualquier cosa con ∅ lo podemos simplemente considerar 0.
* $(W^i \otimes W^T_i) -  \mathbb{I}$ nos permite limpiar la diagonal que solo contiene valores que no nos importan al ser resultados tautologicos.
* Finalmente, al colapsar dimensionalmente esta matriz multiplicandola por un vector de unos, podemos detectar aquellos objetos que no estan desambiguados en $W_i$. 
 
Para desambiguar estos objetos,  el mecanismo es basicamente introducir una nueva propiedad que nos permita diferenciarlos. En nuestro caso, como la dimension de colapso es hoja, lo mas facil es agregar propiedades herederas de ella, por ejemplo rugosa y lisa.

```
            hoja raiz tallo (hoja)rugosa (hoja)lisa
lechuga       1    0    0       0           1
espinaca      1    0    0       1           0
zanahoria     0    1    0       Ø           Ø
apio          0    0    1       Ø           Ø

```

Notamos ahora otro detalle, si hacemos una partición de lechuga  y espinaca, sobre las propiedades relacionadas a hoja, y los objetos lechuga y espinaca, notamos que la  hoja se convierte en una propiedad tautológica.  Mientras que para para los objetos zanahoria y apio, la propiedades relacionadas a hoja se vuelven unsinnging $\emptyset$, es decir, la operación de busqueda que inclua esas propiedades se puede hacer y devolverá algun valor, pero no dice nada util sobre el grado de verdad que esa coordenada tiene para estos. La solución puede tener 2 vias:

* Marcamos la propiedad como unsinnig, mediante una mascara de sentido $S_i$ en torno a los hechos que son indexables por esos objetos y propiedades.
* Indexando sobre los objetos que pueden representarse mediante la propiedad hoja, creamos otra matriz $W_i '$ con un nuevo contexto que indexe solo los vegetales con hoja. 


```
            rugosa  lisa
lechuga       0      1
espinaca      1      0
```

Luego, la operacion para poder buscar vegetales que tengan hojas rugosas, pasa a ser $W_i \otimes W_i  \otimes p_i$. Con esto, hemos logrado dos cosas;  $W_i$ pasa a convertirse en un espacio de ruteo jerarquico sobre las propiedades que pueden tener los objetos, es decir un "indice de contextos" y logramos crear un espacio tensorial, indexado por los objetos que componen el mundo donde podemos identificar por las propiedades sin necesidad de usar $S_i$ como mascara de sentido. Este proceso puede iterarse sobre las categorias, contextos, objetos y relaciones que se quieran. Y siempre que respetemos el orden de los índices dimensionales, podemos reorganizar los $W_i'$ como queramos. Particionarlos a contextos distintos, unirlos mediante el cruce de sus coordenadas y recuperar la representación "plana" que queramos, mediante el calculo de los $S_i$ que la combinación de las "dimensiones tensoriales" requiera. 

La consecuencia es evidente, hemos creado un espacio generalizado de lógicas operables según contextos que a su vez son indexables, usando las herramientas del mismo espacio. Definir propiedades como ser_vivo.animal.cuadrupedo.peludo.canino, identificar los objetos que se relaciónan con ello, y poder comprobar que los hechos que estos pueden comprobar, asi como su estado de sentido pasa a ser un tema de "gramatica lógica" calculable de manera algebraica mediante operaciones booleanas.

Ahora, aca el $W_i$ que seleccionamos está restringido a los hechos que relacionan objetos con propiedades. Lo interesante de este enfoque es que es lo que pasa cuando expandimos el enfoque a otros dominios de hechos.  Evento que antecede a evento, calculo que produce resultado, s-expressions de lisp, maquinas de estado, etc. 

Mediante el mapeo de una categoría de objetos a otra, podemos definir cualquier tipo de relación que pueda ser mostrada mediante la lógica y contenga algun valor de realidad, es decir, todo evento logico y comprobable que pueda ser hablado mediante lenguaje, pero desacoplando el signo de su representación. En palabras de Wittgenstein, hemos definido una proyección directa entre el pensamiendo y su imagen lógica, representada en bits y operable mediante lógica booleana.




## Relación con el lenguaje

La tarea de tomar un texto y extraer una lógica semantica desde esta no es para nada algo nuevo Los trabajos existentes suelen traducir lenguaje a formas lógicas, grafos o tareas de inferencia; pero no siempre formalizan explícitamente la diferencia entre verdad, aplicabilidad/sentido, contexto lógico y desambiguación algebraica del signo [@vossel2025advancing; @liu2025code4logic; @lee2025entailment; @choi2025knowledge; @cheng2025empowering; @bian2025llm; @liang2025survey].  Mas aún, de lo revisado en el estado del arte, ningun trabajo actual parece estar tomando el uso del par contexto, lógica y sentido como  propiedades extraibles y operables sobre distintos documentos. Una primera aproximación interesante a como la separación de la lógica en sus capas de sentido es que la formalizacion propuesta en este trabajo permitiría generar familias de documentos, donde la logica compartida puede ser auditada no solamente por sus grados de verdad, si no tambien por sus estados de sentido. Dicho de otra forma, el uso de las herramientas propuestas nos permitiría crear grafos de conocimiento curados, preparados para operar sobre dominios particulares con limites explicitos sobre el contexto que admiten.

Una limitación importante a notar a esta altura es que, tal y como adelanta el tractatus, la distinción entre el concepto que se representa en un grafo de conocimiento, y el signo textual que lo denota (token o palabra) no pertenece al terreno de la lógica formal. El universo de contextos posibles involucrados entre el lenguaje natural y su lógica subyacente hace que el calculo exacto de todos sea intractable. Dicho de otra manera, hay una posibilidad real, de que el mapeo de palabras a simbolos sea inequivocamente de naturaleza estocástica. Por suerte para nosotros, los avances recientes de los modelos de procesamiento de lenguaje natural y en especial las LLM hace de esta tarea algo muchisimo mas abordable que o que solía ser hace algunos años. Y un poco mas allá, la propuesta presentada en este trabajo rechaza explicitamente la posibilidad de un mapeo completo de universos logicos universales y computables. El caso del proyecto UNL, *Universal Network Language*, del Institue of Advanced Studies de Naciones Unidas, es prueba de la dificultad de abarcar un lenguaje completo, que sea capaz de mantener la coherencia lógica a la vez que la extensibilidad.

De todas maneras, una particularidad poco explorada del lenguaje es que, definiendo un set cerrado de signos y hechos, el mapeo de esos signos y hechos a lenguaje puede pasar de ser de un proceso estocastico a un proceso lógico deterministico, determinado por 2 procesos lógicos separados. En primer lugar el conocimiento estructurado en la manera que ya presentamos en la sección anterior, y en segundo lugar una capa de "superficie de representación", determinado por la estructura del documento y la gramática del lenguaje a representar. La combinación de estos, permitiría representar cualquier tipo de documento de "lenguaje estructurado", mediante la combinación de 2 arboles sintacticos abstractos, y el algebra booleana que ya describimos arriba. No está demas decir que si bien este tipo de representación tendría problemas serios al representar ciertos dialectos o documentos mas artisticos y creativos como la poesía, le vendría muy bien otro tipo de documentos que por naturaleza tienden a ser mas estructurados, como reportes, diccionarios, documentación tecnica o código computacional.

# Relacion con las LLM

Una primera aproximación interesante a como la propuesta puede relacionarse con el buyante campo de los neural network based Language Models es la relación que la mascara de sentido $S$ puede tener en los mecanismos de atención. Obtenida una base de conocimiento lo suficientemente grande, sobre el mismo cuerpo de documentos sobre los que se está entrenando, obtener una mascara de sentido sobre el texto de input al momento de entrenar permitiría un control temprano de que información importa mas y menos, mediante la deteccion de sentidos. De la misma manera, la deteccion de sentido al texto generado permitiría una nueva forma automatizada de perdida al texto generado, lo que permitiría una nueva dimensión dentro del reinforcement learning, synthetic dataset generation, e incluso, como prevención temprana de los outputs que puede generar el modelo al momento de hacer inferencia.

Por otro lado, al introducir el contexto como limite a la familia de textos que podemos unir en un universo lógico que tenga sentido, estamos dando herramientas certeras de curación de datasets, a la vez que facilitando quizas el entrenamiento para modelos que funcionen no como maquinas universales de lenguaje, si no como maquinas especialistas sobre dominios concretos (cosa buscada hoy en dia por las SML). El efecto de esto se vería ampliamente amplificado si además de la perdida directa en el procesamiento y generación de texto, introdujeramos una perdida lógica en las capas intermedias, separando de esta forma el procesamiento del lenguaje como signo, con todas las impresiciones y "gramatic sugar" que le es propio, de la representación simbolica y el sentido.

Esto ultimo, se alinea de forma directa con lo que viene proponiendo LeCun y compañía en JEPA y H-JEPA. En el caso de ellos, el desacoplar la representación abstracta del signo "token por token", se esta intentando mediante la combinación de 2 dos cosas, el uso de energia escalar para medir la compatibilidad entre entrada y salida, y el uso de embedings multidominio, cosa que en nuestro caso podria desacoplarse en 2 niveles independientes, el dato como signo y la representación de su logica y sentido.

Finalmente, cabe preguntarse sobre la posibilidad de que una maquina lógica, con suficiente "conocimiento" sería capaz de reemplazar lo que hoy en dia pueden hacer las LLMs. Y la respuesta a esta pregunta es que lo mas probable es que no, la capacidad de generalización de una maquina basada solo en hechos y operaciones lógicas sobre ellos es por definición nula. Si bien mediante la combinación apropiada de algoritmos y arboles de hechos y contextos  es posible representar una cantidad importante de tareas y sus soluciones, una maquina construida de esta manera siempre tendrá problemas para enfrentarse a soluciones nuevas, si no tiene la capacidad "creativa" que le da el uso de algoritmos estocasticos. De todas maneras, considerando que hoy los algoritmos estocasticos en computación los estamos generando en base sistemas digitales que también funcionan a nivel de bits, cabe preguntarse que tan estocastico es tambien el entrenamiento y operación de las redes neuronales de las que se componen las LLM.

# Relación con  tecnicas base