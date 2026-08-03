# Compilation Decompilation

Source anchors:

- `specs/database/database_design.md`
- `specs/formalization/mathematical_formalization.md`

## Core Claim

Natural language should not compile directly to raw bits.

The source corpus introduces an intermediate representation, `ProjectionIR`, between language and signatures.

## Canonical Pipeline

NL -> ProjectionIR -> typed signature -> validation -> execution

And in reverse:

signature or projection -> canonical expression -> explanation or natural language rendering

This atom owns the bidirectional pipeline.
Result explanation itself lives in `atomos/30_operations/explanation.md`.
