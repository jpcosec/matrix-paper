# Context

Source anchors:

- `specs/spec_main.md`
- later reconciliation target: `specs/concepts/context.md`, `specs/concepts/context_layer.md`

## Definition

Context defines the interpretation perspective for a concept projection.

```yaml
context:
  id: K_COCINA_DIFERENCIAR_VERDURAS
  domain: cocina
  task: diferenciar
  local_universe: [C_LECHUGA, C_ZANAHORIA, C_APIO]
```

## Core Components Present In The Source Spec

- domain
- task
- local universe
- active dimensions

## Canonical Role

The context determines:

- which concepts are competing locally
- which semantic questions matter now
- which dimensions are active
- which projection becomes useful or meaningful

## Additional Source Roles

From `specs/concepts/context.md` and `specs/concepts/context_layer.md`, context is also described as:

- frame or `marco`
- axis selector
- preferred relation selector
- binary mask over semantic bits
- discriminative program

Canonical formulas preserved from the source corpus:

```text
interpretacion = proyectar(concepto, contexto)
```

```text
significado_contextual = significado_total x mascara_contextual
```

The second formula is conceptual, not yet a frozen mathematical operator.

## Local Versus Global

The source corpus distinguishes:

- global representation: what the thing is in general
- local representation: what matters to distinguish it now

This distinction is central and should remain attached to the context model.

## Examples Mentioned In Source Spec

Domains:

- cocina
- biologia
- comercio
- medicina
- etica
- taxonomia
- percepcion visual

Tasks:

- diferenciar
- clasificar
- buscar
- comparar
- explicar
- decidir
