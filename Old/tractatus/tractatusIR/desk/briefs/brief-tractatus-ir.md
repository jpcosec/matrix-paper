# Tractatus IR — project brief

Legacy project brief from 2026-06-02. Its 5WH1+ sections were split into atoms
under `desk/atoms/`; what remains here is prose that does not answer a single
5WH1+ question and therefore is not atomizable as-is.

## Patterns

- **Three-dimension architecture**: vertical (hierarchy), local-discriminative (contextual features), horizontal (relations) — used across spec, Lisp implementation, and atomos knowledge units.
- **Turn-based iterative spec development**: 46 incremental turns in `specs/_index.md` each adding precision without deleting prior concepts — establishes a pattern for formal concept crystallization via conversation.
- **Bit-signature as first-class semantic primitive**: concepts are not stored as opaque IDs but as typed binary signatures (one-hot, multi-hot, contrast, mask) with partial operations validated by grammar Γ.
- **Context-activated dimensions**: different contexts activate different dimension sets; the same concept projects differently per context.
- **Collision-driven expansion**: representation detail is added only when two concepts collide in signature space, enforcing minimal discriminative representation.
- **Tractarian core vs domain layer separation**: the formal Tractatus ontology (Object, Name, Sign, Symbol, State of Affairs, Fact, Proposition, Logical Form, Projection, Sense boundary) is kept distinct from domain-specific predicates, dimensions, and parsers.

## State of maturity

Active — the prototype Lisp runtime is implemented and testable, the formal specification is comprehensive (46 turns, covering core ontology through database design), and integration with the broader hum-ecosystem is underway. Stable: signature types and operations, sense computation, discrimination engine, test harness. Moving: NL2Projection compiler (encoding layer), database persistence integration, hum cognition loop integration. The `decoding/` module has an empty component list in the ASDF definition, indicating it is still pending.

## Open questions

- What is the current test pass/fail state? The test framework is documented but no test results were found.
- Whether the `decoding/` module components are deliberately empty or merely not yet implemented.
- Whether the NL2Projection compiler (`encoding/tractatus-nl2projection`) is functional or still scaffolding.
- How the SLDB (`store_index.yaml`, `semantic_dag.yaml`, `semantic_index.yaml`) is populated and consumed — no loader code was examined.
- The relationship between `atomos/` (atomic knowledge units) and `specs/` (turn-based specs) — they appear to be parallel knowledge organization systems but their intended interaction is not documented.

## References

- `lisp/tractatus.asd` — ASDF system definition
- `specs/_index.md` — 46-turn spec index
- `specs/spec_main.md` — comprehensive system specification
- `formal-propositional-model.md` — formal propositional model (Tractarian DB)
- `test/run-all-tests.lisp` — master test runner
- `test/README.md` — test documentation
- `atomos/` — atomic knowledge unit catalog
- `desk/` — active desk contexts, rituals, tasks
- `.sldb/` — runtime system-level database (core + runtime indices)
- `legacy/hashed_tractatus/` — prior iteration (hashed approach)
- Related subprojects: `tools/hum-scrapper/` (downstream consumer of concept disambiguation)
