Para manejar la composición de tensores en relaciones n-arias (aridad mayor a 2), el motor abandona la matriz bidimensional simple y opera mediante una combinación de **tensores booleanos** y **anidación de múltiples contextos ($W_i$)**.

El procedimiento exacto se resuelve en dos niveles:

**1. Generalización Matemática (Tensores e Hiperaristas)** A nivel algebraico formal, el espacio lógico ($L_i$) se expande para soportar el producto cartesiano de múltiples conjuntos. Para una relación $r$ de aridad $n$ (con firma $A_1 \times A_2 \times \dots \times A_n$), la estructura deja de ser matricial y adopta una **forma tensorial**. En este escenario matemático, las entidades siguen actuando como nodos tipados, pero las relaciones verdaderas y las máscaras de sentido se leen como una **familia de tensores booleanos que actúan como hiperaristas** dentro del grafo de conocimiento. Al agregar una nueva relación de este tipo, el sistema utiliza un operador de extensión (`ExtendRelation`) que incorpora la nueva firma y su respectivo "bloque tensorial" al espacio lógico.

**2. Operativización Arquitectónica (S-expressions y subcontextos)** Dado que modelar tensores masivos de alta dimensionalidad provocaría una explosión combinatoria inmanejable en memoria, los documentos proponen operativizar estas relaciones complejas descomponiéndolas en **expresiones anidadas tipo S-expression**.

Si tomamos el ejemplo de una relación 3-aria como `dar(Juan, libro, María)`, el motor no crea un tensor de 3 dimensiones crudo, sino que lo anida lógicamente como `(((dar libro) juan) maria)`. Para calcular y componer esto, el motor divide el problema **conectando varios contextos lógicos ($W_i$) especializados**:

- Crea un $W_i$ para vincular las acciones y los objetos (el hecho `dar` y `libro`).
- Crea otro $W_i$ exclusivo para mapear a los ejecutantes de la acción (`Juan`).
- Crea un tercer $W_i$ para los receptores de la acción (`María`).

**La Composición y el Enrutamiento** Para componer esta red particionada, el sistema utiliza $W_i$ como un **espacio de enrutamiento jerárquico**,. La composición se realiza aplicando álgebra matricial booleana mediante "matrices puente" (relaciones $R$) que conectan los tensores de un contexto con otro.

Dado que el proceso algebraico sobre el semianillo booleano es infinitamente recursivo, el motor puede proyectar, unir y colapsar estas "rutas tensoriales" a voluntad. Aunque la división de hechos complejos provoca una cantidad explosiva de contextos ($W_i$) en una primera instancia, la arquitectura confía en que esta fragmentación se normalizará, permitiendo que el cálculo tensorial pesado sea asimilado eficientemente por operaciones binarias rápidas en el hardware.