---
topic: triparticion-contextual
use_when: Aplicable al contexto semantico y factual de Triparticion Contextual.
do_not_use_when: No utilizar fuera del dominio formal de contextual-logic.
id: atom-triparticion-contextual
title: Triparticion Contextual
five_wh_one_plus: what
tags:
- system:matrix
---
# Tripartición Contextual: Dominio, Tarea y Discurso

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[BlockMatrix]]]
* [defines:: [[WiGame]]]
* [defines:: [[Prototipo_SHRDLU]]]
* [defines:: [[Modelo_SMG]]]
* [defines:: [[Matriz_por_Bloques]]]

---

## Qué es
Es la descomposición analítica (Anexo A.3.13) de las necesidades contextuales de una consulta real en tres capas independientes:

```mermaid
flowchart TD
    Consulta["Consulta de Usuario"] --> DomainCtx["1. Domain Context (Tipos y Dimensiones L_i)"]
    Consulta --> TaskCtx["2. Task Context (Máscara de Sentido S_i)"]
    Consulta --> DiscourseCtx["3. Discourse Context (Resolución de Anáforas y Pronombres)"]
```

1. **Domain Context:** Define el vocabulario, tipos y relaciones válidas del universo.
2. **Task Context:** Define la máscara $S_i$ específica para la meta operativa actual.
3. **Discourse Context:** Mantiene la resolución de pronombres y anáforas en el diálogo (vía SHRDLU).
