# Índice: Símbolo a Coordenada

En la teoría clásica de bases de datos, un índice (como un B-Tree o Hash) es una estructura auxiliar para acelerar la búsqueda de registros. En la arquitectura MEEL (basada en el Tractatus), el índice no es opcional ni puramente optimizador: es fundamentalmente **geométrico y ontológico**.

- **El Índice como Función Biyectiva:** Se define como $\mathcal{I}: \text{Símbolo} \rightarrow \mathbb{N}^k$. Esta función mapea cada proposición atómica (o concepto abstracto) a una dimensión ortogonal y específica dentro del Espacio Lógico.
- **Acceso $O(1)$ Estructural:** No existe el concepto de "recorrer tablas" (table scans). Conocer la representación simbólica de un hecho es, por definición, conocer su posición exacta y precalculada en el hiper-tensor.
- **El Esquema es el Diccionario:** La indexación deja de ser un auxiliar de rendimiento para convertirse en el esquema mismo de la base de datos. El vocabulario del sistema (el conjunto de todas las proposiciones atómicas posibles) *es* su sistema de coordenadas cartesianas.
