# OntoMap

Implementación de un **Grafo Ontológico Multidimensional** sobre RDF/OWL.  
Un multigrafo dirigido plano donde jerarquía y composición se modelan exclusivamente mediante propiedades de aristas, no anidamiento estructural.

---

## Arquitectura

```
ontology/
  core.ttl        ← Definición OWL: clases, propiedades, axiomas, SHACL
  workspace.ttl   ← Instancias concretas (nodos + aristas)

converters/
  dims.py         ← Mapping dimensiones ↔ propiedades OWL
  mermaid.py      ← load/dump Mermaid
  puml.py         ← load/dump PlantUML
  owl_viz.py      ← Visualizador de estructura OWL (sin instancias)

queries/
  projections.sparql  ← Proyecciones SPARQL estándar

output/           ← Archivos generados por el CLI
cli.py            ← CLI principal
```

---

## Modelo de datos

### Nodos
Entidades planas con tipo y metadata. Sin jerarquía intrínseca.

| Tipo | Descripción |
|------|-------------|
| `Actor` | Agente con capacidad de ejecución (LLM, CLI, humano) |
| `Zone` | Entorno físico, lógico o de estado |
| `Artifact` | Modelo de datos, archivo, documento |
| `Process` | Algoritmo o ritual definido |

Cada tipo es extensible vía `rdfs:subClassOf`:
```
LLMAgent → Actor
Document → Artifact
FileSystem → Zone
```

### Aristas (6 dimensiones)

Cada arista es un individuo OWL (`OntologyEdge`) con `source` y `target`, más hasta 6 dimensiones semánticas ortogonales:

| Dimensión | Tipo OWL | Descripción | Ejemplos de valores |
|-----------|----------|-------------|---------------------|
| `where` | ObjectProperty | Topología / composición | `contains`, `isLocatedIn`, `persistsAt` |
| `what` | ObjectProperty | Semántica estructural | `informs`, `validates`, `dependsOn`, `transitionsTo` |
| `when` | DatatypeProperty | Fase / estado temporal | `"InitPhase"`, `"ExecPhase"`, `"AuditPassed"` |
| `how` | DatatypeProperty | Mecanismo de ejecución | `"writes_markdown"`, `"http_post"`, `"executes_git"` |
| `why` | DatatypeProperty | Regla de negocio / rationale | `"zero_context_sufficiency"`, `"strict_traceability"` |
| `who` | ObjectProperty | Actor que propicia la relación | IRI de un `Actor` |

Los valores concretos de `where` y `what` son **sub-propiedades OWL**, lo que habilita inferencia automática:
- `onto:contains` es `TransitiveProperty` + `IrreflexiveProperty`
- `onto:dependsOn` es `AsymmetricProperty` + `IrreflexiveProperty`

---

## CLI

```
python cli.py parse <input> <output>
```

**Detección automática de formato por extensión:**

| Extensión | Formato |
|-----------|---------|
| `.ttl` | Turtle (RDF) |
| `.owl` | OWL/XML |
| `.rdf` | RDF/XML |
| `.n3` | Notation3 |
| `.mmd` | Mermaid |
| `.puml` | PlantUML |

**Ejemplos:**
```bash
# Ontología → Mermaid (visualiza jerarquía OWL)
python cli.py parse ontology/core.ttl output/core.mmd

# Instancias → PlantUML
python cli.py parse ontology/workspace.ttl output/workspace.puml

# Mermaid → OWL/XML
python cli.py parse diagrama.mmd output/diagrama.owl

# PlantUML → Turtle
python cli.py parse diagrama.puml output/diagrama.ttl
```

**Detección automática de modo para `.mmd`:**
- Si el grafo contiene `OntologyEdge` → renderiza instancias (nodos, aristas con dimensiones)
- Si no → renderiza estructura OWL (jerarquía de clases y propiedades)

---

## Proyecciones SPARQL

El mismo grafo base produce múltiples vistas filtrando por dimensión:

| Proyección | Filtro | Resultado |
|------------|--------|-----------|
| Árbol topológico | `where=contains` | Jerarquía espacial de zonas |
| Flujo de estados | `what=transitionsTo` + orden por `when` | Pipeline de fases |
| Interacciones de actores | `source a Actor` | Qué hace cada actor y por qué |
| DAG de dependencias | `what=dependsOn` | Árbol de resolución paralela |
| Check de ciclos | `ASK { A contains B . B contains A }` | Validación de aciclicidad |

```bash
python test_graph.py  # corre las 4 proyecciones sobre workspace.ttl
```

---

## Round-trip garantizado

```
workspace.ttl  →  Mermaid  →  reload  →  36/36 aristas ✓
workspace.ttl  →  PlantUML →  reload  →  36/36 aristas ✓
```

Las aristas con múltiples dimensiones se preservan completas en ambos formatos.  
La jerarquía de zonas se serializa como flechas `{where: contains}` al no poder anidar subgraphs en Mermaid.
