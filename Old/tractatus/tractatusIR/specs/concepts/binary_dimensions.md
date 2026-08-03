# Binary Dimensions

## Summary
Explores whether categorization hierarchies can be represented using binary signs (bits), where each dimension is a binary distinction. Turn 06 answers: yes, but bits must be **typed binary features** organized by axis, not a flat binary code.

## Concepts
- **Binary sign**: a binary distinction (0/1) representing a dimension
- **Dimension**: a binary axis that separates concepts (e.g., vivo/muerto)
- **Binary representation of hierarchy**: encoding categorical levels as bit patterns
- **Typed binary feature**: a bit that belongs to a specific axis (ontological, functional, state) and answers a specific yes/no question
- **Axis bit** (`bit de eje`): a binary feature that indicates which dimension/axis a concept belongs to (e.g., `es_estado: 1` vs `es_función: 0`)

## Content

### The Question (turn-05.md)

Turn 05 poses:

> "Es posible separarlo en signos binarios? representar esa jerarquia en signos binarios?"
> (Is it possible to separate it into binary signs? represent that hierarchy in binary signs?)

The "hierarchy" refers to the ontological and functional hierarchies established in turns 01-04.

### The Answer (turn-06.md)

**Yes**, but with a key constraint: do not represent the hierarchy as a single flat binary code (e.g., `perro = 010101`). Instead, use **typed binary features** organized by axis.

Each bit should answer a specific yes/no question:
- ¿es entidad física? → 1
- ¿es entidad biológica? → 1
- ¿es organismo? → 1
- ¿es animal? → 1
- ¿es vegetal? → 0
- ¿es alimento? → 0/1 (context-dependent)
- ¿puede estar vivo/muerto? → 1

The three main axes (see [categorization.md](categorization.md) for detail):
- **Eje ontológico**: [entidad_física, entidad_biológica, organismo, animal, vegetal]
- **Eje funcional**: [alimento, mascota, herramienta, material]
- **Eje estado**: [vivo, muerto, procesado, crudo, cocido]

### Key Insight: Typed Bits

The critical point from turn 06: **bits must be typed** (`rasgos tipados`). If you don't type them, you get a bag of 0/1 that mixes ontology, function, and state, and semantics breaks.

Correct representation for `zanahoria`:
```
concepto: zanahoria
bits:
  ontologico:
    entidad_fisica: 1
    entidad_biologica: 1
    organismo: 1
    animal: 0
    vegetal: 1
  funcional:
    alimento: 1
    mascota: 0
  estado:
    vivo_muerto_aplica: 1
    vivo: depende_contexto
    muerto: depende_contexto
```

### Disambiguating with Axis Bits

The question "what word disambiguates vivo/muerto from comida" translates to:
- vivo/muerto → belongs to `eje_estado_de_organismo`
- comida → belongs to `eje_funcional_de_consumo`

The disambiguating category is not just a word, but an **axis bit**:
- For vivo/muerto: `es_estado: 1`, `es_función: 0`
- For comida: `es_estado: 0`, `es_función: 1`

## Examples

### Perro (dog)
```json
{
  "concepto": "perro",
  "bits": {
    "ontologico": [1, 1, 1, 1, 0],
    "funcional": [0, 1, 0, 0],
    "estado": [1, 0, 0, 0, 0]
  }
}
```
Flattened: `[entidad_física:1, biológica:1, organismo:1, animal:1, vegetal:0, alimento:0, mascota:1, vivo:1]`

### Zanahoria (carrot)
```json
{
  "concepto": "zanahoria",
  "bits": {
    "ontologico": [1, 1, 1, 0, 1],
    "funcional": [1, 0, 0, 0],
    "estado": [1, 0, 0, 1, 0]
  }
}
```
Flattened: `[entidad_física:1, biológica:1, organismo:1, animal:0, vegetal:1, alimento:1, mascota:0, vivo:1/cruda]`

Note: zanahoria does not contradict vivo/muerto and comida — it can be both, because they belong to different axes (turn-06.md).

## References
- turn-05.md (question)
- turn-06.md (answer: typed binary features by axis)
- turn-04.md (parallel hierarchies: ontological, functional, state)
- turn-01.md (categorization game)

## Version Notes
- Turn 05: initial question posed — can hierarchies be represented in binary signs?
- Turn 06: answered yes — but bits must be typed/rasgos tipados organized by axis (ontological, functional, state). Introduced the concept of axis bits (`bit de eje`) for disambiguation.
