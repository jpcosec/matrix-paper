---
id: atom-tractatus-ir-how
title: Tractatus IR — How it's made
five_wh_one_plus: how
tags:
- project:tractatus-ir
- source:legacy-brief
- kind:code
provenance: atom-tractatus-ir.md::How it's made
---

# Tractatus IR — How it's made

## Answer

Common Lisp (ASDF system `:tractatus`, ~1579 lines across 10+ source files) organized into layers: `datype+operations` (signature types and bit-vector ops), `sin-mask+tractatus logic` (semantic masks and sense computation), `higher functions` (discrimination, inference, selection, security, versioning), `encoding` (parser, NL2Projection compiler), `decoding`, and `utils` (DB persistence, demo). Test suite in `test/` (run-all-tests.lisp) covers signatures, semantics, discrimination, parser, and DB. System definitions, formal specs, and design docs live in `specs/` (46-turn spec index, formalization, data models, database design). A SLDB (system-level database) in `.sldb/` stores runtime semantic DAGs and indices. The atomos directory at `atomos/` catalogs atomic knowledge units across meta, core, formal, operations, persistence, and example categories.
