# Especificación de Arquitectura: Máquina de Estados de Evaluación Lógica (MEEL)

### 1. Marco Conceptual y Objetivos Operacionales

La Máquina de Estados de Evaluación Lógica (MEEL) constituye un sistema de alta integridad diseñado para la curaduría y operación de grafos de conocimiento mediante la segregación técnica de la **Verdad** y el **Sentido**. A diferencia de los enfoques estocásticos predominantes en los Grandes Modelos de Lenguaje (LLMs), que operan por proximidad probabilística de tokens, la MEEL implementa el sustrato del _Tractatus_ de Wittgenstein para transformar hechos y relaciones en proyecciones booleanas deterministas dentro de particiones del mundo (W_i). Esta arquitectura permite tratar la lógica no como una sugerencia, sino como una restricción estructural infranqueable.

**Misión del Sistema:** La MEEL deberá proyectar espacios lógicos auditables donde cada proposición sea evaluada algebraicamente, permitiendo que el sistema funcione como una capa de **"Logical Loss"** (Pérdida Lógica) para modelos especialistas (SMLs). Esto alinea la máquina con las arquitecturas JEPA/H-JEPA de LeCun, desacoplando el procesamiento del signo (token) de su representación simbólica y lógica.

**Capacidades Críticas:**

- **Representación de Contextos Tipados:** Delimitación de particiones W_i mediante criterios de pertenencia estrictos (C_i).
- **Almacenamiento Segregado:** Repositorios independientes para la Verdad (V_i) y el Sentido (S_i).
- **Detección de Patologías:** Identificación de tautologías y contradicciones (_Sinnlos_) y ambigüedad por indistinguibilidad.
- **Gestión de Subcontextos:** Proyección y refinamiento jerárquico manteniendo la autonomía lógica.

**Impacto Estratégico:** Al transitar de procesos probabilísticos a lógicos deterministas, la MEEL actúa como un filtro de prevención temprana de alucinaciones. En la inferencia, el sistema valida si una salida es _Sinnvoll_ (con sentido) antes de permitir su emisión, asegurando que la superficie de representación sea coherente con el espacio lógico (L_i) definido.

--------------------------------------------------------------------------------

### 2. Arquitectura de Capas del Sistema

La integridad sistémica de la MEEL depende de una segregación estricta en siete capas funcionales. Esta jerarquía asegura que la infraestructura lógica sea agnóstica a la factualidad de los datos.

**Desglose de Capas:**

**1. Firmas y Tipos:** Capa de validación de aridad y tipos. Define la posibilidad de la estructura relacional.

**2. Coordenadas Lógicas:** Representa el Espacio Lógico (L_i) como la envoltura convexa del contexto. Establece los límites de lo que _puede_ ser formado.

**3. Verdad (****V_i****):** Almacén de hechos positivos y negativos. Codificación binaria de la realidad observada.

**4. Sentido (****S_i****):** Máscara de aplicabilidad semántica. Define el límite del lenguaje significativo dentro de W_i.

**5. Proyección Operativa (****W_i^*****):** Capa derivada de la intersección V_i \text{ AND } S_i. Es el único estado operable por procesos de salida.

**6. Índices:** Estructuras materializadas para la optimización de consultas de alta densidad.

**7. Refinamiento:** Protocolos de extensión para la inyección de nuevas dimensiones y subcontextos.

**Matriz de Responsabilidades Técnicas:**

|   |   |   |
|---|---|---|
|Capa|Función Técnica|Concepto Lógico (Wittgenstein)|
|**Firmas**|Validación de tipos/aridad|Forma de los objetos (2.0141)|
|**Coordenadas**|Indexación de L_i|Envoltura convexa/Espacio lógico|
|**Verdad**|Bit-matrix de asignación factual|Hechos positivos/negativos (2.06)|
|**Sentido**|Máscara booleana de aplicabilidad|Límite del lenguaje significativo|
|**Operativa**|Ejecución de V_i \text{ AND } S_i|El mundo operable (W_i^*)|
|**Índices**|Materialización de W_i^*|Consultabilidad inmediata|
|**Refinamiento**|Gestión de subcontextos|Extensión del espacio lógico|

--------------------------------------------------------------------------------

### 3. Modelo de Datos y Estructuras de Coordenadas

El sistema deberá utilizar estructuras de datos rígidamente tipadas para eliminar la ambigüedad estructural.

**Espacio Lógico (****L_i****) y Envoltura Convexa:** El L_i define las fronteras de formación del pensamiento. Si una combinación de objetos y propiedades no pertenece a la envoltura convexa definida por el contexto, el sistema la rechazará _a priori_ como _Unsinnig_ (absurdo). El L_i gestiona la "posibilidad de la estructura", mientras que el S_i filtra la "aplicabilidad".

**Representación Matricial y Tensorial:**

- **Matrices de Bits:** Para relaciones binarias (Objeto-Propiedad), se emplearán matrices N \times M donde el acceso sea O(1).
- **Tensores de Relación:** Para relaciones de aridad n > 2, se utilizarán formas tensoriales donde la firma relacional valide las dimensiones antes de cualquier operación de escritura.
- **Gray Code:** Las coordenadas en las matrices se ordenarán mediante Código Gray. Esto garantiza que las celdas adyacentes difieran en un solo bit, permitiendo el uso eficiente de Mapas de Karnaugh para la detección proactiva de tautologías.

--------------------------------------------------------------------------------

### 4. Invariantes Estructurales y Lógica de Evaluación

El motor de evaluación deberá respetar cinco invariantes fundamentales para evitar estados inconsistentes:

1. **Pertenencia de Coordenadas:** Toda entrada en `truthStore` debe existir previamente en el `logicSpace` (L_i).
2. **Derivabilidad Operativa:** W_i^* es estrictamente una capa derivada. Ningún proceso puede escribir directamente en la Capa Operativa.
3. **Consistencia de Máscara:** Toda coordenada en `senseStore` debe pertenecer a L_i o a una extensión declarada.
4. **Reconstruibilidad:** Los índices deben ser 100% reconstruibles desde las capas primarias (L_i, V_i, S_i).
5. **Herencia de Contexto:** Todo subcontexto debe declarar explícitamente su autonomía o su grafo de herencia.

**Cálculo de la Capa Operativa y Caso de Estudio:** La fórmula de ejecución es W_i^* = V_i \text{ AND } S_i.

- **Caso "Vegetales":** En un contexto botánico, la propiedad "Smooth" (Liso) es aplicable a "Lettuce" (S_i=1). Si la lechuga es lisa, V_i=1, resultando en W_i^*=1.
- Sin embargo, para "Carrot" (Zanahoria), la propiedad "Smooth" es inaplicable (S_i=0). Aunque un sensor erróneo intente marcar V_i=1, la proyección W_i^* será **0**, clasificándola como información inaplicable antes de la evaluación factual.

**Categorización del Sentido:**

```markdown
[Entrada: Proposición x]
       │
       ▼
¿x ∈ L_i? ── NO ──> [Unsinnig] (Fuera de contexto/Tipo incorrecto)
       │
       SÍ
       ▼
¿S_i(x) = 1? ── NO ──> [Inapplicable] (Sin sentido en este contexto)
       │
       SÍ
       ▼
¿Aporta Info? ── NO ──> [Sinnlos] (Tautología/Contradicción - Mapas de Karnaugh)
       │
       SÍ
       ▼
[Sinnvoll] ──> Evaluar V_i (True / False con Sentido)
```

--------------------------------------------------------------------------------

### 5. Gestión de Contextos y Subcontextos

La MEEL permite la expansión controlada mediante proyecciones de subcontextos. Al realizar esta operación, es **obligatorio** conservar los casos etiquetados como _Inapplicable_ (S_i=0). Esto previene que una propiedad irrelevante en un subdominio sea malinterpretada como falsa en el dominio base.

**Protocolo de Extensión:** Toda inyección de nuevas entidades o relaciones disparará un recálculo local de índices. El sistema deberá soportar consultas conjuntivas sobre la Capa Operativa, permitiendo que los patrones relacionales se resuelvan mediante álgebra booleana pura sobre las matrices de bits materializadas.

--------------------------------------------------------------------------------

### 6. Índices Críticos y Decisiones de Diseño

La eficiencia en entornos de alta densidad exige la materialización mandatoria de los siguientes índices:

- **Índice de Firma Relacional:** Validación estructural inmediata.
- **Índice de Entidad/Propiedad:** Optimización de queries por rasgos.
- **Índice de Colisiones Descriptivas:** Identificación de entidades indistinguibles por sus rasgos actuales (Principio de Identidad de Wittgenstein).

**Detección de Tautologías (**_**Sinnlos**_**):** El uso de **Mapas de Karnaugh** sobre el almacenamiento ordenado en Gray Code permite simplificar expresiones complejas y detectar proactivamente estados _Sinnlos_. Si una función lógica se reduce a una verdad universal dentro del contexto, se marca como no informativa, optimizando el ancho de banda del procesamiento cognitivo del sistema.

--------------------------------------------------------------------------------

### 7. Conclusión y Proyección Operativa Final

La Máquina de Estados de Evaluación Lógica (MEEL) trasciende la representación documental para convertirse en una infraestructura de validación ontológica. Su diseño por capas garantiza una implementación agnóstica (C++, Rust, o aceleración por hardware/FPGA) y una estabilidad total frente a la naturaleza estocástica de los LLMs.

Al separar rígidamente la Verdad del Sentido, la MEEL provee una auditoría lógica total. En última instancia, el sistema no solo almacena datos; define los límites de lo que puede ser operado con sentido, asegurando que cada salida sea no solo verdadera, sino lógicamente impecable y contextualmente pertinente.