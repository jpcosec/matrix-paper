# Context Representation

## Summary
Defines context as a layer that decides which semantic axis is active. Turn 08 introduces context as a core concept with 5 approaches: frame, axis selection, predicate, binary mask, and complete representation.

## Concepts
- **Context**: a layer that decides which semantic axis is active
- **Active axis**: the dimension (ontology, function, state) currently in use
- **Context as frame** (marco): a framing that selects which reading of a word applies
- **Context as mask**: a binary mask over bits that activates/deactivates dimensions
- **Contextual projection**: the operation of projecting a concept onto the active context
- **Preferred relations**: relationships that are relevant in a given context

## Content

### The Problem
Previously (turns 01-07), words like "zanahoria" were represented with multiple parallel axes (ontological, functional, state). But the question remained: how does the system know WHICH axis to use at any given moment?

Turn 07 posed this question; turn 08 answers it: **context decides**.

### Approach 1: Context as "Frame" (Marco)

Context can be a frame that selects which reading applies:

```yaml
contexto:
  marco: cocina
  eje_activo: funcional
  pregunta_actual: "¿se puede comer?"
```

In `cocina` frame, the functional reading wins: `zanahoria → comida`
In `biología` frame, the ontological reading wins: `zanahoria → planta/organismo`
In `estado vital` frame: `zanahoria → viva/muerta/procesada`

(see `binary_dimensions.md` for the bit representation by axis)

### Approach 2: Context as Axis Selection

Context can directly select which axis is active:

```yaml
context:
  active_axis:
    ontology: 0
    function: 1
    state: 0
```

With this context, comparison happens within `function`, not `ontology`.

### Approach 3: Context as Predicate

More powerful: context changes the **relationship**, not the thing itself.

```
zanahoria --es_un--> planta
zanahoria --usada_como--> comida
zanahoria --estado_posible--> viva/muerta
```

Context selects which relationship is relevant:
```yaml
contexto:
  relacion_relevante: usada_como
# activates: zanahoria --usada_como--> comida
```

This is better than forcing a single hierarchy (see `categorization.md` for graph model with typed relationships).

### Approach 4: Context as Binary Mask

Context can be a **mask** over the bits (see `binary_dimensions.md` for bit definitions):

```yaml
bits:
  ontology:
    entidad_fisica: 1
    entidad_biologica: 1
    organismo: 1
    animal: 0
    vegetal: 1
  function:
    alimento: 1
    mascota: 0
  state:
    vivo_muerto_aplica: 1
    vivo: unknown
    muerto: unknown
```

Context mask:
```yaml
# Context: cocina
mask:
  ontology: 0
  function: 1
  state: 0

# Context: biología
mask:
  ontology: 1
  function: 0
  state: 0

# Context: vivo o muerto
mask:
  ontology: 0
  function: 0
  state: 1
```

Conceptual formula:
```
significado_contextual = significado_total × máscara_contextual
```

(Not necessarily strict mathematical multiplication, but as a conceptual operation: context turns dimensions on/off.)

### Approach 5: Complete Representation

The full structure for a concept with contexts:

```yaml
concept: zanahoria
features:
  ontology:
    entity: 1
    physical_entity: 1
    biological_entity: 1
    organism: 1
    plant: 1
    animal: 0
  function:
    food: 1
    ingredient: 1
    pet: 0
  state:
    life_status_applicable: 1
    alive: unknown
    dead: unknown
    processed: unknown
contexts:
  kitchen:
    active_axis: function
    preferred_relations:
      - used_as
      - ingredient_of
  biology:
    active_axis: ontology
    preferred_relations:
      - is_a
      - part_of
  life_status_question:
    active_axis: state
    preferred_relations:
      - has_state
```

### Key Formula

The word "zanahoria" doesn't change its meaning "in itself". What changes is the **contextual projection**:

```
signo_contextual = signo_base + eje_activo + relación_relevante
```

Or more formally:
```
interpretación = proyectar(concepto, contexto)
```

Where `proyectar` means: choose which dimension of the concept matters now.

### Context Structure

Context should be a structured object, not just free text:

```yaml
contexto:
  dominio: cocina / biología / ética / comercio / medicina
  eje: ontología / función / estado / valor / pertenencia
  relación: es_un / usado_como / tiene_estado / parte_de
  pregunta: clasificación / comparación / decisión / explicación
```

This separates things like:
- "zanahoria como comida" from
- "zanahoria como organismo"

without confusing the system.

## Examples

### Zanahoria + Context
| Context | Active Axis | Result |
|---------|-------------|--------|
| cocina | function | alimento / ingrediente |
| biología | ontology | planta / organismo vegetal |
| vivo-muerto | state | entidad biológica con estado vital posible |

## References
- turn-08.md (context as frame, axis selection, predicate, mask, complete representation)
- turn-07.md (question about context representation)
- binary_dimensions.md (for bit representation by axis)
- categorization.md (for graph model with typed relationships)

## Version Notes
- Turn 07: asked about context representation; no new facts added
- Turn 08: introduced context as core concept with 5 approaches; context decides which semantic axis is active; formula: `interpretación = proyectar(concepto, contexto)`
