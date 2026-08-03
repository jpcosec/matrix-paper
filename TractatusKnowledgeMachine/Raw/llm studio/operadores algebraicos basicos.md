A partir de los axiomas formales y la arquitectura propuesta, podemos definir las firmas exactas de los 5 operadores algebraicos centrales. Estas firmas combinan su **definición matemática** (basada en el semianillo booleano) con su **firma computacional en Rust** (usando el patrón _Typestate_ para garantizar seguridad lógica).

### 1. Operador de Proyección Operativa (Validación)

Este es el operador fundacional que transforma los datos crudos en una capa booleana segura y operable, garantizando estructuralmente que no hay afirmaciones verdaderas sobre hechos sin sentido.

- **Firma Matemática:** $W_i^* = Project_i(x) = V_i(x) \land S_i(x)$.
- **Firma Computacional (Rust):** `fn validate(self: UnvalidatedContext) -> Result<ValidatedContext, Error>`
- **Comportamiento:** El motor ejecuta la operación de validación de hardware `(M AND (NOT S))`. Si el resultado es distinto de $0$, la matriz contiene una violación de los axiomas (estado ilegal) y la operación es rechazada devolviendo un error. Si es válido, colapsa el estado trivaluado emitiendo la proyección operativa $W_i^*$.

### 2. Operador de Consulta Vectorial (Select)

Permite buscar satisfactores (entidades) dentro del contexto esquivando el espacio inaplicable (los "Don't Cares") de la máscara de sentido.

- **Firma Matemática:** $Select_i(p) = {o \in O_i \mid V_i(o,p)=1 \land S_i(o,p)=1}$. Algebraicamente equivale a la multiplicación vectorial $W_i^* \otimes v_q$.
- **Firma Computacional (Rust):** `fn query(&self: ValidatedContext, q_m: BitVec, q_mask: BitVec) -> BitVec`
- **Comportamiento:** Recibe la matriz segura, un vector con la verdad esperada (`q_m`) y una máscara que indica qué dimensiones importan (`q_mask`). Se resuelve bit a bit devolviendo las entidades `e` que cumplan estrictamente: `(S[e] AND q_mask) == q_mask && (M[e] AND q_mask) == (q_m AND q_mask)`. Si la consulta contiene coordenadas fuera del espacio lógico ($x \notin L_i$), devuelve `UndefinedContext`.

### 3. Operador de Co-ocurrencia de Propiedades

Operador de análisis estructural que determina qué propiedades o atributos logran coexistir en los mismos objetos dentro de un dominio.

- **Firma Matemática:** $C_i = W_i^{_T} \otimes W_i^_$.
- **Firma Computacional (Rust):** `fn co_occurrence(&self: ValidatedContext) -> Matrix<P, P>`
- **Comportamiento:** Se calcula multiplicando la matriz transpuesta de la proyección validada por la proyección original mediante álgebra booleana (AND/OR). Devuelve una matriz cuadrada Propiedad × Propiedad, donde un valor de 1 en la intersección $[i, j]$ indica co-ocurrencia fáctica de esos dos rasgos en al menos una entidad con sentido.

### 4. Operador de Indistinguibilidad (Ambigüedad)

Calcula las colisiones descriptivas del sistema para saber cuándo dos entidades separadas tienen un comportamiento idéntico ante las propiedades mapeadas y necesitan desambiguación.

- **Firma Matemática:** $A_i = (W_i^* \otimes W_i^{*T}) - \mathbb{I}$.
- **Firma Computacional (Rust):** `fn ambiguity(&self: ValidatedContext) -> Matrix<E, E>`
- **Comportamiento:** Multiplica la proyección validada por su transpuesta para obtener una matriz de colisiones Entidad × Entidad. Como un objeto siempre es idéntico a sí mismo (tautología), el sistema resta algebraicamente la matriz identidad ($\mathbb{I}$) para limpiar la diagonal principal. Cualquier $1$ restante indica qué pares de objetos carecen de dimensiones para ser distinguidos.

### 5. Operador de Composición (Merge / Compose)

Permite conectar como un grafo dirigido dos contextos distintos (ej. "vegetales" y "colores") usando una relación o propiedad de enrutamiento intermedio, propagando el sentido para que el absurdo no contamine el cálculo.

- **Firma Matemática:** $M_C = M_A \otimes R \otimes M_B^T$ $S_C = S_A \otimes R \otimes S_B^T$
- **Firma Computacional (Rust):** `fn compose(&self: ValidatedContext, other: &ValidatedContext, r: RoutingMatrix) -> UnvalidatedContext`
- **Comportamiento:** El motor procesa el triple producto matricial booleano por separado para la Verdad ($M$) y para el Sentido ($S$). Esto asegura que si una propiedad cruzada carece de sentido en el primer contexto (los _unsinnig_), sus ceros viajen como "agujeros negros" a través de $R$ silenciando el resultado final en el contexto compuesto. Como la composición crea una estructura matemática nueva, su salida **debe forzosamente devolver un tipo `UnvalidatedContext`**, obligando al usuario a correr el método `.validate()` antes de operar con la nueva matriz resultante.