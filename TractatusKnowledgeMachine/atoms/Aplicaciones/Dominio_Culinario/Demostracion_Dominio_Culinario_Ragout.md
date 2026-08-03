---
topic: demostracion-dominio-culinario-ragout
use_when: Aplicable al contexto semantico y factual de Demostracion Dominio Culinario
  Ragout.
do_not_use_when: No utilizar fuera del dominio formal de cooking-ragout.
id: atom-demostracion-dominio-culinario-ragout
title: Demostracion Dominio Culinario Ragout
five_wh_one_plus: what
tags:
- system:matrix
---
# Demostración en Dominio Culinario: Ragout de Champiñones

**Categoría Padre:** [[Aplicaciones]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_examples_ragout_demonstration_py]]]
* [is_solved_by:: [[MEEL]]]
* [is_solved_by:: [[BlockMatrix]]]
* [restricts:: [[WiGame]]]
* [restricts:: [[Acoplamiento_Neuro_Estocastico_Simbolico]]]
* [restricts:: [[Matriz_por_Bloques]]]
* [restricts:: [[Juego_de_Desambiguacion]]]
* [restricts:: [[Colapso_Dimensional]]]

---

## Qué es
Es la demostración end-to-end ejecutable (`examples/ragout_demonstration.py`) que ilustra cómo el motor Booleano MEEL resuelve las ambigüedades categoriales y evita alucinaciones en un dominio culinario real mediante un pipeline de 5 etapas.

---

## Flujo de la Demostración Culinaria

```mermaid
sequenceDiagram
    autonumber
    actor LLM as Parser Semántico LLM
    participant Engine as MEEL Runtime
    participant World as Partición W_ragout

    LLM->>Engine: 1. Ingesta Hechos Atómicos: (ragout_carne tiene_ingrediente carne/cebolla/vino)
    Engine->>World: 2. Reducción Descriptiva: W_base = cebolla ^ vino ^ coccion_lenta
    LLM->>Engine: 3. Consulta de Desambiguación: Ragout de Champiñones (D_i = champiñon)
    Engine->>World: 4. Filtro Si Booleano: S_i=1 (Ingrediente Válido) & V_i=1 (champiñon)
    Engine-->>LLM: 5. Matriz Resultante W* = (Vi v Di) ^ Si (Sin Alucinación)
```

---

## Código Ejecutable de Referencia
* Script Ejecutable: `Matrix/Matrix/examples/ragout_demonstration.py`
* Prueba Pytest: `Matrix/Matrix/tests/test_ragout_demonstration.py` (120/120 tests passing)
