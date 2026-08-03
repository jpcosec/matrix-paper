# Query: Operador de Máscara y Proyección Tensorial

En SQL o bases NoSQL, un "Query" recorre datos aplicando condiciones lógicas de filtrado (`SELECT * FROM T WHERE X=1`). En el entramado matemático de MEEL, el Query es puramente una **operación del álgebra lineal booleana**.

- **El Vector de Consulta (Query Tensor):** Una petición a la base de datos se formula inyectando los parámetros de búsqueda en un tensor máscara $Q$. Las dimensiones sobre las cuales se indaga asumen valores específicos (ej. $1$ o $0$ lógico), mientras que las variables irrelevantes quedan como dimensiones "comodín" o proyectivas.
- **Ejecución como Producto Punto:** Resolver el Query equivale a aplicar un producto tensorial contraído (o producto punto) entre el hiper-tensor del Mundo $W$ (los datos) y el tensor máscara $Q$.
- **El Equivalente al JOIN/Conjunción:** Las operaciones complejas, como conjunciones lógicas o cruces relacionales, se reducen a la multiplicación de las correspondientes matrices de adyacencia. Consultar la base de datos no es "buscar iterando", sino proyectar el Espacio Lógico total sobre un subespacio de menor dimensión definido por el Query.
