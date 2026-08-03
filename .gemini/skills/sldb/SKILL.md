---
name: sldb
description: Comprehensive skill guide for using sldb (Single Source Database), the structured Markdown IR, AST parser, and semantic/physical retrieval engine. Activate this skill whenever tracking Markdown documents, defining StructuredNLDoc models, searching store ASTs, or performing sldb database queries.
---

# `sldb` (Single Source Database) Skill Guide

`sldb` is an AI-first database engine that parses, tracks, indexes, and queries structured Markdown documents as an Intermediate Representation (IR) and Abstract Syntax Tree (AST).

---

## 1. Core Command Categories & Primary Surfaces

### Store Lifecycle (`sldb stores`)
* **`sldb stores init`**: Initialize an `.sldb` store in a project directory.
* **`sldb stores status`**: Check store status and registered models.

### Models & Contracts (`sldb models`)
* **`sldb models list`**: List registered `StructuredNLDoc` model contracts in the active store.
* **`sldb models schema`**: Show internal node and edge schemas for registered models.
* **`sldb models add <module:Class>`**: Register a custom Python model contract into the store.

### Document Tracking (`sldb docs`)
* **`sldb docs track --model <ModelName> <path>`**: Track an existing Markdown file into the store under a specific model contract.
* **`sldb docs list`**: List all tracked documents in the active store.
* **`sldb docs create --model <ModelName> -o <output> <payload>`**: Create a new tracked document from a YAML/JSON payload.

### Unified Search (`sldb find`)
* **`sldb find <term> --in physical --type doc|section|field`**: Search physical token names, section titles, or file paths.
* **`sldb find <tag> --in semantic`**: Search documents by semantic tags or metadata fields.
* **`sldb find <term> --select doc,field,value --where 'value = "..."'`**: Execute projected field queries.

### AST & Field Mutators (`sldb ast`, `sldb fields`, `sldb sections`)
* **`sldb ast show <doc-name>`**: Display the full Abstract Syntax Tree of a tracked Markdown document.
* **`sldb fields list / edit`**: Inspect or mutate specific fields inside tracked Markdown files without rewriting the full file.
* **`sldb sections`**: Navigate section headers, breadcrumbs, and content blocks.

---

## 2. Practical Examples

```bash
# 1. Track a knowledge atom into the store under AtomDoc
sldb docs track --model AtomDoc TractatusKnowledgeMachine/atoms/Matematica/Optimizacion_y_Desambiguacion/Fenomeno_de_Gibbs_en_Funciones_Indicadoras.md

# 2. Search for all tracked atoms related to 'gibbs'
sldb find gibbs --in physical --type doc

# 3. Inspect AST structure of a tracked document
sldb ast show Fenomeno_de_Gibbs_en_Funciones_Indicadoras
```
