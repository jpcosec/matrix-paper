Si te presento este esquema conceptual, se entiende?

# Especificación del Objeto: Grafo Ontológico Multidimensional

Estructura de datos basada en un multígrafo dirigido plano. La jerarquía y la composición no se modelan mediante anidamiento estructural (nodos dentro de nodos), sino exclusivamente mediante propiedades de las aristas.

## 1. Definición de Nodos (Vértices)
Representan las entidades discretas del sistema. Carecen de jerarquía intrínseca.

**Atributos Base:**
* `id`: Identificador único (UUID o slug alfanumérico).
* `type`: Categoría de la entidad. Valores permitidos:
  * `actor`: Entidades con capacidad de ejecución (agentes, sistemas, humanos).
  * `zone`: Entornos físicos, lógicos o de estado.
  * `artifact`: Modelos de datos, archivos, documentos o artefactos concretos.
  * `process`: Algoritmos o rituales definidos.
* `metadata`: Diccionario clave-valor para atributos específicos (ej. estado de completitud, tamaño, tags).

## 2. Definición de Aristas (Arcos Multidimensionales)
Vectores dirigidos (`source_id` -> `target_id`) que almacenan el espectro completo de interacción entre dos nodos. Una arista no define una única acción, sino el contexto total de la relación a través de 6 dimensiones ortogonales.

**Atributos Base:**
* `source_id`: Referencia al nodo de origen.
* `target_id`: Referencia al nodo de destino.

**Carga Dimensional (Atributos Semánticos):**
* `where` (Topología/Composición): Define la ubicación espacial o la pertenencia estructurada. Reemplaza el anidamiento.
  * *Ejemplo:* `contains`, `is_located_in`, `persists_at`.
* `what` (Semántica Estructural): Define qué le hace un nodo a otro o su relación ontológica pura.
  * *Ejemplo:* `informs`, `organizes`, `validates`, `references_by_id`.
* `when` (Temporalidad/Estado): Define el gatillo de estado, condición temporal o fase en la que la relación ocurre.
  * *Ejemplo:* `during_plan_phase`, `on_audit_failure`, `post_execution`.
* `how` (Mecánica): Define el mecanismo físico o programático que ejecuta la relación.
  * *Ejemplo:* `writes_markdown`, `executes_ast_lock`, `http_post`.
* `why` (Racionalidad/Regla de Negocio): Define el motivo arquitectónico que justifica la existencia de esta arista.
  * *Ejemplo:* `prevent_cyclic_dependencies`, `zero_context_sufficiency`.
* `who` (Contexto de Actor): Define qué actor propicia o audita la relación, útil si el nodo origen no es un actor (ej. Arista de Artefacto A -> Artefacto B, donde `who` es el sistema que hace la conversión).

*(Nota: Una arista válida puede tener campos dimensionales en `null` si esa dimensión no aplica a la relación específica).*

## 3. Representación de Esquema (Pydantic / JSON Schema)

```python
from typing import Optional, List, Literal
from pydantic import BaseModel

NodeType = Literal["actor", "zone", "artifact", "process"]

class Node(BaseModel):
    id: str
    type: NodeType
    metadata: dict = {}

class OntologyEdge(BaseModel):
    source_id: str
    target_id: str
    
    # Payload Dimensional
    where: Optional[str] = None
    what: Optional[str] = None
    when: Optional[str] = None
    how: Optional[str] = None
    why: Optional[str] = None
    who: Optional[str] = None

class OntologyGraph(BaseModel):
    nodes: List[Node]
    edges: List[OntologyEdge]
```

## 4. Reglas Topológicas y Restricciones
* **Grafo Plano:** La propiedad `nodes` es un array unidimensional. La composición topológica se resuelve escaneando todas las aristas donde `where="contains"` (ej. para saber qué tareas hay en un board, se busca: `Edge(source_id="board_1", target_id="task_2", where="contains")`).
* **Aciclicidad por Dimensión:** El grafo completo puede tener ciclos (ej. un loop de auditoría), pero los sub-grafos filtrados por ciertas dimensiones deben ser DAGs (Grafos Acíclicos Dirigidos). Específicamente, el sub-grafo de composición espacial (`where: contains`) y el de dependencias de flujo (`what: depends_on`) no deben tener ciclos funcionales.
* **Sobrecarga de Aristas:** Permitido. Si dos nodos interactúan de maneras conceptualmente distintas y asíncronas, se declaran dos aristas separadas entre ellos en lugar de fusionar semánticas mutuamente excluyentes en un solo vector.


El Grafo Ontológico opera computacionalmente como un **metagrafo o base de datos orientada a grafos**. Los diagramas estándar (UML, AST, BPMN) no existen como estructuras de datos separadas, sino como **proyecciones ortogonales** (subgrafos) obtenidas al aplicar filtros dimensionales sobre las aristas.

### Mecánica de Proyección Topológica (Filtros por Dimensión)

Al aplicar consultas sobre las dimensiones `[where, what, when, how, who, why]`, el sistema compila diferentes modelos formales de arquitectura:

* **Proyección AST (Abstract Syntax Tree) / Árbol Léxico**
    * **Filtro:** `where="contains"` + `what="invokes"` + `type="artifact"` (Código fuente).
    * **Resultado:** Jerarquía estática de paquetes, módulos, clases y funciones.
* **Proyección UML de Clases (Diseño Estático)**
    * **Filtro:** `what="inherits" | "implements" | "composes"` + `when="PlanPhase"`.
    * **Resultado:** Contratos e interfaces (ej. los modelos Pydantic `TaskModel` heredando de `BaseModel`).
* **Proyección UML de Secuencia (Flujo Dinámico/Tiempo)**
    * **Filtro:** Ordenación estricta por `when` + aislamiento por `how` (ej. llamadas a API, comandos CLI) + nodos limitados a `actor` y `artifact`.
    * **Resultado:** Trazabilidad determinista de mensajes entre LLMs, CLI y el FileSystem.
* **Proyección de Máquina de Estados (Ciclo de Vida)**
    * **Filtro:** Nodos centrados en un `artifact` específico (ej. `Task`) + aristas filtradas por `what="transitions_to"`.
    * **Resultado:** Grafo de transiciones válidas (`open` -> `in_progress` -> `closed`), gatilladas por el `who` (CLI o Executor).
* **Proyección DAG de Dependencias (Orquestación de Workers)**
    * **Filtro:** `what="depends_on"` + `when="ExecPhase"`.
    * **Resultado:** Árbol de resolución para ejecución paralela y prevención de deadlocks.

### Implementación del Motor de Proyección

Para materializar estas vistas a nivel de CLI, se requiere un motor de consulta sobre la estructura base:

```python
from typing import List, Callable

def project_subgraph(
    graph: OntologyGraph, 
    node_filter: Callable[[Node], bool] = lambda n: True,
    edge_filter: Callable[[OntologyEdge], bool] = lambda e: True
) -> OntologyGraph:
    """Extrae un subgrafo validado según restricciones dimensionales."""
    
    valid_nodes = {n.id: n for n in graph.nodes if node_filter(n)}
    
    valid_edges = [
        e for e in graph.edges 
        if edge_filter(e) 
        and e.source_id in valid_nodes 
        and e.target_id in valid_nodes
    ]
    
    return OntologyGraph(
        nodes=list(valid_nodes.values()), 
        edges=valid_edges
    )

# Ejemplo: Proyectar el DAG de dependencias para el despachador paralelo
dag_execution = project_subgraph(
    graph=global_state,
    node_filter=lambda n: n.type == "artifact" and n.metadata.get("artifact_type") == "Task",
    edge_filter=lambda e: e.what == "depends_on"
)
```

