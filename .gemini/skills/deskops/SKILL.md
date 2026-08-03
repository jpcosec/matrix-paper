---
name: deskops
description: Comprehensive skill guide for using deskops (the workflow-domain CLI layer built on top of sldb) to manage desk workspaces, task lifecycle gates, inbox notes, atom tag namespaces, and KGDB graph snapshots across repositories. Activate this skill whenever working with deskops, sldb, desk workspaces, task gates, or knowledge graphs.
---

# `deskops` Workflow & Engineering Knowledge Skill Guide

`deskops` is a workflow-domain CLI layer built on top of `sldb` for managing repository-local desk workspaces, task progression gates, knowledge atoms, and Knowledge Graph DB (KGDB) snapshots.

> [!IMPORTANT]
> **DEVELOPMENT ERROR LOGGING PROTOCOL:** `deskops` is an active tool under continuous development. Whenever an execution error, invalid argument failure, unexpected behavior, or workflow friction occurs while running `deskops`, **you MUST immediately log it into the desk inbox** so the user/team can improve `deskops`.

---

## 1. Error & Friction Logging Protocol (`deskops inbox`)

When any `deskops` command fails or presents unexpected behavior, run:

```bash
# Log an error, confusion, or CLI issue
deskops inbox "<Detailed error description, command executed, and stack trace or message>" --kind unclear --title "<Short Title>"

# Log a suggestion for improvement or missing CLI option
deskops inbox "<Feature suggestion or architectural improvement>" --kind suggestion --title "<Short Title>"
```

---

## 2. Quick Reference & Core Commands

### Bootstrap & Initialization
* **`deskops bootstrap`**: Prepares the global model registry and validates the `sldb` installation.
* **`deskops init .`**: Scaffold local `desk/` workspace and initialize `.sldb` database in the current repository.
* **`deskops status --root .`**: Check workspace health and operational status.
* **`deskops doctor --root . --repair`**: Detect and automatically repair broken desk states.

### Task & Workflow Management
* **`deskops add task --root . --title "..." --goal "..." --scope "..." --validation "..."`**: Create a new tracked task.
* **`deskops list tasks --root .`**: List active tasks.
* **`deskops show task <task-id> --root .`**: Display task details.
* **`deskops next task <task-id> --root .`**: Show the next valid gate transition without mutating state.
* **`deskops advance task <task-id> --root .`**: Advance a task through routine gates.

### Inbox & Note Promotion
* **`deskops inbox "<message>" --kind unclear|suggestion --title "<title>"`**: Log an error or suggestion into the inbox.
* **`deskops inbox --list`**: View inbox notes.
* **`deskops inbox --show <selector>`**: Show specific inbox note details.
* **`deskops promote --root .`**: Promote inbox notes to formal tasks or boards.

### Atoms & Tag Namespaces (`deskops atoms`)
* **`deskops atoms new`**: Create a new knowledge atom.
* **`deskops atoms list / show`**: Inspect existing knowledge atoms.
* **`deskops atoms add-namespace`**: Register atom tag namespaces in `desk/atoms/tag-namespaces.yaml`.
* **`deskops atoms validate`**: Validate materializations of atoms.

### Knowledge Graph DB (`deskops graph`)
* **`deskops graph build`**: Build the KGDB graph snapshot runtime artifact.
* **`deskops graph neighbors`**: View incoming and outgoing neighbors for a graph node.
* **`deskops graph missing`**: Report dangling references or missing graph targets.
* **`deskops graph trace`**: Trace a graph node back to its root sources.
* **`deskops graph reflect`**: Generate review-only self-reflection findings.

---

## 3. Typical Operational Workflow

```bash
# 1. Initialize repo desk
deskops bootstrap
deskops init .

# 2. Log an error or suggestion when deskops fails or needs improvement
deskops inbox "Argument --root failed on deskops inbox" --kind unclear --title "Inbox CLI options"

# 3. Create task and track
deskops add task --root . --title "OWL2Matrix Parser" --goal "Parse RDF/XML to S-Expressions" --validation "pytest"

# 4. Audit graph health
deskops graph build
deskops graph missing

# 5. Check health & advance gates
deskops status --root .
deskops advance task task-owl2matrix-parser --root .
```
