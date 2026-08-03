# Discrimination Game

## Thesis

The germinal intuition of the system is not "semantic encoding" in the abstract.
It is a discrimination game.

We begin with groups of words or concepts that partially overlap and ask:

- what category groups some of them together?
- what category separates them from competing candidates?
- what word, feature, or question disambiguates one axis from another?

The canonical early example is:

- `perro`, `gato`
- `zanahoria`, `lechuga`
- the disambiguating word between `vivo/muerto` and `comida`

The first strong answer is `organismo`.

This answer matters because it separates:

- ontological category
- functional role

`comida` is not primarily an ontological kind in the same sense as `organismo`.
It is a use-role or cultural function.

## First Structural Rule

The system therefore begins by refusing to collapse everything into a single hierarchy.

It must distinguish at least:

- what something is
- what it can be used as
- what state it is in

This yields parallel structured views rather than one universal ladder.

Examples:

```text
zanahoria
  es_un -> planta
  puede_funcionar_como -> alimento
  estado_biologico -> viva / muerta / procesada
```

```text
perro
  es_un -> animal
  puede_funcionar_como -> mascota / trabajador
  estado_biologico -> vivo / muerto
```

## Why Representation Starts Here

The system does not start by asking for a full definition of a thing.
It starts by asking for the minimum articulation needed to separate candidates without mixing dimensions.

That means representation is born from a practical question:

```text
What must be said here so these candidates stop collapsing into one another?
```

This is why the earliest heuristic is not encyclopedic but discriminative.

## Upward Hierarchy Without Confusion

Upward hierarchy still matters.
We often need to climb toward broader categories.

For instance:

```text
perro -> animal -> organismo -> entidad biologica -> entidad fisica
zanahoria -> planta -> organismo vegetal -> entidad biologica -> entidad fisica
```

But not every useful distinction is upward in the same sense.
Some are ontological, some are functional, some are state-like.

So the right picture is:

- tree when we need broader-to-narrower ascent within one axis
- graph when we need multiple typed relations across axes

## Economy Of Articulation

Once the discussion moves from broad categorization to local differentiation, a new rule appears:

do not represent everything at once.

Instead:

1. identify the current candidates
2. identify what they share
3. identify the smallest difference that separates them

Example:

```text
lechuga vs zanahoria
```

Both may share:

- vegetal
- planta
- alimento

Those common traits locate the group, but they do not discriminate it.

The useful question is more local:

```text
Que parte de la planta se consume principalmente?
```

And the useful distinction becomes:

- `lechuga -> hoja`
- `zanahoria -> raiz`

## Representation As Minimal Discrimination

At this stage, the system can be stated as:

```text
representation = concept + context + minimal discriminative articulation
```

This means:

- a concept has a stable identity anchor
- a context selects the relevant comparison regime
- the representation used now should be only as large as needed to reduce ambiguity

This is not merely an engineering optimization.
It is the conceptual birth of the system.

## Collision As Productive Event

The local strategy immediately implies collisions.

If we use only `parte_comestible_principal`, then:

- `lechuga -> hoja`
- `espinaca -> hoja`

The collision is not a failure of the world.
It is evidence that the current articulation is insufficient.

So the system expands only when a collision forces it to.

This is the second major germinal rule:

```text
articulate only as much as needed, and expand only when discrimination demands it
```

## Consequence

The origin of the model is not:

- database first
- logic first
- embeddings first

It is:

- discrimination first
- representation as controlled articulation
- economy of semantic structure under local necessity

This is the base heuristic on top of which the rest of the system is built.
