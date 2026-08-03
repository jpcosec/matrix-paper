# Context Layer

## Summary
The context layer is a separate structure that decides which semantic axis is active for a given interpretation, allowing the same concept to project differently depending on context.

## Concepts
- Context as frame (marco)
- Context as axis selection
- Context as predicate/relation selector
- Context as binary mask
- Contextual projection: `interpretación = proyectar(concepto, contexto)`
- Local vs global representation
- Discriminative features (contrast operation)
- Context as discriminative program (sequence of dimensions + applicability conditions)

## Content

### Context as Frame
Instead of storing only `zanahoria = comida`, the context determines which reading applies:
- **Kitchen context**: zanahoria → alimento (functional reading)
- **Biology context**: zanahoria → planta / organismo (ontological reading)
- **Life status context**: zanahoria → viva / muerta / procesada

### Context as Axis Selection
Context activates one axis of the concept's feature vector:
```
context:
  active_axis:
    ontology: 0
    function: 1
    state: 0
```
Interpretation happens within the active axis only.

### Context as Predicate/Relation Selector
Context changes the **relation**, not the thing:
- `contexto: relacion_relevante: usada_como` → `zanahoria --usada_como--> comida`
- `contexto: relacion_relevante: es_un` → `zanahoria --es_un--> planta`

This avoids forcing a single hierarchy.

### Context as Binary Mask
Context acts as a mask over the concept's bits:
```
significado_contextual = significado_total × máscara_contextual
```
Example masks:
- Contexto cocina: `mask: {ontology: 0, function: 1, state: 0}`
- Contexto biología: `mask: {ontology: 1, function: 0, state: 0}`
- Contexto vivo/muerto: `mask: {ontology: 0, function: 0, state: 1}`

### Complete Context Structure
```
contexto:
  dominio: cocina / biología / ética / comercio / medicina
  eje: ontología / función / estado / valor / pertenencia
  relación: es_un / usado_como / tiene_estado / parte_de
  pregunta: clasificación / comparación / decisión / explicación
```

### Formal Definition
```
signo_contextual = signo_base + eje_activo + relación_relevante
interpretación = proyectar(concepto, contexto)
```
Where `proyectar` means: choose which dimension of the concept matters now.

### Local vs Global Representation
Two levels of representation:
1. **Global**: what the thing is in general (e.g., lechuga = planta, organismo, alimento posible, hoja)
2. **Local/contextual**: which features matter to distinguish it from other candidates in current context

Example: lechuga vs zanahoria in kitchen context:
- Common dimensions: [vegetal, alimento, planta]
- Discriminative: lechuga = [hoja_comestible], zanahoria = [raiz_comestible]

The useful category is not the most complete one — it's the one that separates the current candidates.

### Contrast Operation
```
contraste(lechuga, zanahoria, contexto=comida)
→ rasgos que difieren: hoja vs raíz, verde vs naranja, laminar vs alargada
```

The local disambiguator: `parte comestible` (hoja vs raíz) separates them cleanly.

## References
- turn-08.md (complete definition of context layer)
- turn-10.md (local vs global representation, discriminative features)

## Version Notes
- Turn 08: introduced the context layer as a core concept, defining 4 representation approaches
- Turn 10: added local vs global representation, discriminative features, and contrast operation
- Turn 24: redefined context as discriminative program with dimension sequence, applicability conditions, and bit dictionary paths
