---
topic: politica-simbolos-kernel
use_when: Aplicable al contexto semantico y factual de Politica Simbolos Kernel.
do_not_use_when: No utilizar fuera del dominio formal de meel-engine.
id: atom-politica-simbolos-kernel
title: Politica Simbolos Kernel
five_wh_one_plus: what
tags:
- system:matrix
---
# Política de Símbolos del Kernel

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Signo_vs_Simbolo]]]
* [is_solved_by:: [[Sistema_Tipos_Ti]]]
* [is_solved_by:: [[Algebra_Booleana]]]

---

## Qué es
Es la frontera estricta entre los símbolos propios del núcleo (*Kernel*) y las relaciones del espacio de conocimiento ($W_i$).

## Por qué es necesario
Evita que el núcleo ejecutable del motor se contamine hardcodeando ontologías de dominio (como causalidad, pertenencia o temporalidad), manteniendo el kernel pequeño y formal.

## Cómo funciona
- **Conectivas del Kernel:** `and`, `or`, `not`, `if`.
- **Meta-Relaciones del Kernel:** `instance` (tipado de símbolos) y `equivalent` (unificación de alias y nombres canónicos).
- **Atoms del Kernel:** Llevan el prefijo `kern:{symbol}` (ej. `kern:true`, `kern:false`).
- **Relaciones de $W_i$:** Vocabularios de hechos como `has_property`, `in_state`, `part_of`, `depends_on`, `causes`.

## Cuándo interviene
Durante el parsing de S-Expressions, tipado de firmas y canonización de símbolos.

## Dónde reside
En `src/operational_model/kernel/symbol_policy.py` y `symbol_spaces.py`.

## Para qué / Para quién
Asegura la modularidad, interoperabilidad con ontologías externas y portabilidad de storage.
