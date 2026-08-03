$C_i$ es un contexto, es decir, una función limite sobre $W$ que marca un limite entre lo que es y no es parte de Wi. Es decir una indexación que nos permite decir que algo pertenece o no a $W_i$.  Por ejemplo

Hablar de todos los perros 
* hablar = signo
* todos = cardinalidad 
* perros = conjunto 
Programas de computación escritos en s-expressions 
* s-expressions = signo
* programas de computación = conjunto

Nótese que un contexto, puede ser a su vez un contexto de contextos como por ejemplo:

Diagramas de  flujos de estado y diagramas de componente 
* signo = diagramas UML, 
* conjunto =  flujos de estado $\cup$ componentes

$L_i$ es la dimension de la estructura lógica dentro de $W_i$, es decir las "reglas del lenguaje" que permiten mapear TODO lo que esta en $W_i$ de manera convexa. $L_i$ sería la funcion que determina si una coordenada puede existir dentro de $W_i$, pero no necesariamente si tiene un sentido en $S_i$ o si tiene un valor lógico en $V_i$. $L_i$ es en otras palabras, es la funcion que determina las dimensiones de $W_i$, o mas bien "la envoltura convexa" que puede recubrir a un $W_i$.  

Por ejemplo, al decir vivos o muertos tenemos un mapeo que permite identificar un grupo (vivos) y otro (muertos) pero hay un espacio entre medio que si pertenece al Wi que determina el contexto (vivos y muertos, vivos XOR muertos). Lo mismo aplica para los contextos que dimos arriba en el caso de los diagramas, puede haber un UML donde el flujo de estado sea igual a diagrama de componente, pero lo normal es que este no sea el caso.  

$V_i$ seria la funcion que determina el mapeo lógico de algo dentro de $W_i$ para alguna expresion que denote un hecho cualquiera en relación con la realidad, según su evaluación puede ser 
* *Sinnvol*: verdadera o falsa, 
* *Sinnlos*: tautologica o contradictoria
* *Unsinnig*: Fuera de contexto

Finalmente $S_i$ es la funcion máscara que separa dentro del espacio que denota $C_i$ todo lo que tiene de lo que no tiene sentido.

El caso particular que proponemos estudiar en la formulación, son todos aquellos $W_i$ que pueden describirse mediante matrices de bits y lógica booleana 
* signo= matrices de bits 
* conjunto= operaciónes de logica booleana sobre bits
* cardinalidad=  todos (cosa que es valor tautologico asi que no importa

La maquina que proponemos construir tiene que hacer basicamente una cosa; operar sobre hechos que se puedan definir como matrices de verdad (Y sentido). Importante notar aca que en el caso particular que proponemos el caso se puede definir desde la union de  formulaciones "completas", es decir, mediante la union de matrices que no tienen una mascara $S_i$, y la obtienen al hacer el cruce de dimensiones que "no son compatibles lógicamente". De ahi el ejemplo de los vegetales en [proposal]
