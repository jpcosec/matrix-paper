---
topic: estados-verdad-epistemicos-semanticos
use_when: Aplicable al contexto semantico y factual de Estados Verdad Epistemicos
  Semanticos.
do_not_use_when: No utilizar fuera del dominio formal de contextual-logic.
id: atom-estados-verdad-epistemicos-semanticos
title: Estados Verdad Epistemicos Semanticos
five_wh_one_plus: what
tags:
- system:matrix
---
# Tripartición de Estados: Verdad, Epistémico y Semántico

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [defines:: [[Tractatus]]]
* [is_solved_by:: [[Capa_Verdad_Vi]]]
* [is_solved_by:: [[Capa_Sentido_Si]]]
* [defines:: [[Status_Evaluation]]]
* [defines:: [[Matriz_por_Bloques]]]

---

## Qué es
Es la separación explícita entre tres dimensiones semánticas y operativas independientes para cada proposición dentro de un espacio de mundos $W_i$:

```mermaid
flowchart LR
    Prop["Proposición p"] --> Semantico["1. Estado Semántico (Si)\nSinnvoll (1) / Unsinnig (0)"]
    Prop --> Epistemico["2. Estado Epistémico\nObservado / Inferido / Hipotético"]
    Prop --> Verdad["3. Estado de Verdad (Vi)\nAsserted True (1) / Asserted False (0)"]
```

---

## Las Tres Dimensiones

1. **Estado Semántico ($S_i$):** Categoría Gramatical de Aplicabilidad (*Sinnvoll*, *Sinnlos*, *Unsinnig*).
2. **Estado Epistémico:** Grado de justificación u origen (*Observado Directamente*, *Deducido por Modus Ponens*, *Inyectado RAG*).
3. **Estado de Verdad ($V_i$):** Evaluación veritativa contingente Booleana ($1$ o $0$).

---

## Importancia Teórica
Evita confundir la ausencia de datos con la falsedad o el absurdo, permitiendo auditorías precisas sobre sistemas de inteligencia artificial.
