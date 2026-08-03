# Graphlang Prototype

This directory contains the executable `graphlang` prototype code and smoke tests.

## What Lives Here

- Common Lisp prototype runtime
- smoke tests
- temporary execution artifacts

## What Does Not Live Here

- current-state documentation
  - see `docs/architecture/graphlang/`
- active work notes and plans
  - see `desk/graphlang/`
- pending metamodel closures
  - see `desk/pendientes/`
- architectural decisions
  - see `desk/adrs/`

## Main Runtime Files

- `tractatus-core.lisp`
- `tractatus-periphery.lisp`
- `tractatus-semantics.lisp`
- `tractatus-worlds.lisp`
- `tractatus-ring.lisp`
- `tractatus-axes.lisp`
- `tractatus-discrimination.lisp`
- `tractatus-persistence.lisp`

## Main Smoke Tests

- `smoke-test.lisp`
- `world-smoke-test.lisp`
- `semantics-smoke-test.lisp`
- `ring-smoke-test.lisp`
- `axes-smoke-test.lisp`
- `discrimination-smoke-test.lisp`
- `persistence-smoke-test.lisp`

## Rule

The root of `graphlang/` should contain code, tests, and this `README.md` only.
