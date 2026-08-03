# Local Universe And Discrimination

Source anchor:

- `specs/spec_main.md`

## Core Heuristic

Useful representation is local to the current competing candidates, not globally maximal from the start.

Source example:

```text
universe: [lechuga, zanahoria, apio]
dimension: parte_comestible_principal
lechuga = [1,0,0]
zanahoria = [0,1,0]
apio = [0,0,1]
```

## Rule

Represent only the minimal discriminative structure needed for the current context.

If two concepts collide under the current dimension, expand the representation with another dimension.

Example from the source:

```text
lechuga vs espinaca both [1,0,0] -> add forma_hoja
```

## Why This Matters

The local universe explains why the same concept can require different useful representations in different tasks or domains.
