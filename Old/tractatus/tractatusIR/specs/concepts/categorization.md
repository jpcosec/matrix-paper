# Word Categorization and Disambiguation

## Summary
Introduces the core problem of word categorization: grouping words by shared categories and finding disambiguating dimensions that separate groups.

## Concepts
- **Category**: a property shared by a group of words (e.g., "forma de vida" / life form)
- **Categorization**: assigning words to categories
- **Disambiguating word**: a word that resolves ambiguity between competing concepts (e.g., vivo/muerto vs. comida)

## Content
The system begins with a simple game: given two groups of words — those sharing a category (perro, gato) and those that do not (zanahoria, lechuga) — find a category that differentiates both groups.

Example:
- Group A: perro, gato → share category "forma de vida" (living being)
- Group B: zanahoria, lechuga → do not belong to "forma de vida"

### Disambiguating "vivo/muerto" from "comida"

The word that best disambiguates the axis "vivo/muerto" from "comida" is **organismo** (turn-02.md).

Reasoning:
- perro / gato → organismos animales
- zanahoria / lechuga → organismos vegetales
- "comida" is not primarily alive or dead as a category; it is a role of use or cultural function
- vivo/muerto applies better to entities first classified as organismos / seres vivos

Ontological tree:
```
organismo
├── animal
│   ├── perro
│   └── gato
└── planta
    ├── zanahoria
    └── lechuga
```

Comida is a separate role/use that some organisms (or parts of organisms) can have. "Entidad biológica" is a more general term, but for the game **organismo** is preferred as it separates the ontological category from the functional category.

### Hierarchical Structure

Turn 03 asks: "necesitaríamos de alguna forma crear jerarquias hacia arriba con eso o no?" (would we need some way to create upward hierarchies with that or not?)

The ontological tree above demonstrates that upward hierarchical categorization is indeed part of the system — `organismo` sits above `animal`/`planta`, which in turn sit above the concrete words. The hierarchy enables broader-to-narrower categorization (turn-03.md).

## Examples
| Group A (same category) | Group B (different category) | Differentiating Category |
|-------------------------|------------------------------|-------------------------|
| perro, gato             | zanahoria, lechuga          | forma de vida           |

## References
- turn-01.md
- turn-02.md
- turn-03.md

### Multiple Parallel Hierarchies (turn-04.md)

Turn 04 introduces that not all concepts ascend the same hierarchy. Different dimensions require separate parallel hierarchies:

1. **Ontological hierarchy**: what something *is*
   ```
   entidad física → entidad biológica → organismo → animal / planta / hongo / bacteria
   ```

2. **Functional/use hierarchy**: what something is *used for*
   ```
   entidad → objeto consumible → alimento → comida → ingrediente / plato / snack
   ```

3. **State hierarchy**: what *state* something is in
   ```
   estado-biológico: viva / muerta / procesada
   ```

Example showing parallel dimensions for "zanahoria":
```
zanahoria
├── es-un: planta / parte de planta
├── puede-ser-usada-como: alimento
└── estado-biológico: viva / muerta / procesada
```

Example for "perro":
```
perro
├── es-un: animal
├── puede-ser-usado-como: mascota / trabajador / compañía
└── estado-biológico: vivo / muerto
```

### Graph Model with Typed Relationships (turn-04.md)

The key insight from turn 04: separate **what is** ≠ **what it's used for** ≠ **what state it's in**.

The system should be modeled as **graphs with typed relationships**, not a single tree. A tree serves for "subir categorías" (ascending categories), but a graph avoids mixing dimensions:

- `zanahoria → es-un → planta` (ontological)
- `zanahoria → puede-funcionar-como → comida` (functional)

This prevents incorrect direct links like `zanahoria → comida` which conflate ontological and functional dimensions.

## Examples
| Group A (same category) | Group B (different category) | Differentiating Category |
|-------------------------|------------------------------|-------------------------|
| perro, gato             | zanahoria, lechuga          | forma de vida           |

## References
- turn-01.md
- turn-02.md
- turn-03.md
- turn-04.md

## Version Notes
- Turn 01: initial proposal of the categorization game; core problem stated but no formal dimension system yet defined.
- Turn 02: answered open question — "organismo" disambiguates vivo/muerto from comida; introduced ontological vs. functional category distinction.
- Turn 03: confirmed that upward hierarchical categorization is part of the system; ontological tree demonstrates broader-to-narrower structure.
- Turn 04: introduced multiple parallel hierarchies (ontological, functional, state); proposed graph model with typed relationships to separate "what is" from "what it's used for" from "what state it's in".
