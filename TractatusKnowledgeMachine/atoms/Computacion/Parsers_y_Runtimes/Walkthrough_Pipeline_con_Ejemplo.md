---
system: matrix
layer: operational-pipeline
domain: walkthrough
topic: walkthrough-pipeline-con-ejemplo
use_when: "Aplicable al contexto semantico y factual de Walkthrough Pipeline con Ejemplo."
do_not_use_when: "No utilizar fuera del dominio formal de walkthrough."
---

# Walkthrough del Pipeline Operacional con Ejemplo Concreto

**Categoría Padre:** [[Computacion/Parsers_y_Runtimes]]
**Relaciones 5W1H+:**
* [implements:: [[Pipeline_Ingesta_Lenguaje_Matrix]]]
* [implements:: [[Interrupcion_Decodificacion_Si_Cero]]]
* [implements:: [[Acoplamiento_Neuro_Estocastico_Simbolico]]]
* [implements:: [[Distincion_Ausencia_vs_Unsinnig]]]

---

## Qué es
Es el recorrido paso a paso del pipeline completo desde la entrada en lenguaje natural hasta la decisión de aceptar o rechazar una proposición, con un ejemplo concreto ejecutado.

## Ejemplo: "El ragout tiene champiñones"

### Paso 1 — Anclaje de Símbolos (Symbol Grounding)

```
Input:  "El ragout tiene champiñones"
        ↓
LLM extrae: sujeto="ragout", relación="tiene_ingrediente", objeto="champinon"
        ↓
Anclaje:
  sign("ragout")     → Symbol("ragout")
  sign("champiñones") → Symbol("champinon")  (normalización de alias)
  sign("tiene")      → Relation("tiene_ingrediente")
```

### Paso 2 — Parseo a S-Expression Canónica

```
Input canónico: (tiene_ingrediente ragout champinon)
```

### Paso 3 — Identificación del WiGame

```
MEEL evalúa: ¿Qué WiGame acepta (tiene_ingrediente ragout champinon)?
  → WiGame "cocina" admite:
     axis_a: [ragout, risotto, paella, ...]
     axis_b: [champinon, arroz, azafran, ...]
     relation: tiene_ingrediente
  → Resultado: wigame:cocina
```

### Paso 4 — Validación por Máscara de Sentido ($S_i$)

```
Si.get("ragout", "champinon")?

Caso A: Si = "sinnvoll"  → ✅ La combinación es categorialmente válida
Caso B: Si = "unsinnig"  → 🚫 RECHAZAR: "El ragout no puede tener champiñones como ingrediente en este contexto"
Caso C: Fuera de ejes    → 🚫 RECHAZAR: "La proposición no pertenece a este espacio lógico"
```

### Paso 5 — Evaluación de Verdad ($V_i$)

```
(Continuación del Caso A: Si = sinnvoll)

Vi.get("ragout", "champinon")?

Resultado posible:
  "true"  → ✅ "Sí, el ragout tiene champiñones."
  "false" → ❌ "No, el ragout no tiene champiñones."
  "∅"     → ⚠️ "No se sabe si el ragout tiene champiñones (ausencia de dato)."
```

### Paso 6 — Decisión Final

```python
# Código real de s_expression_runtime.py (_eval_check)

if not wigame.accepts(proposition):
    return OperationResult(status="reject", sinn="unsinnig",
                          reason="target WiGame does not accept this proposition")

truth = wigame.Vi.get(proposition.subject_symbol_id, proposition.object_symbol_id)
sense = wigame.Si.get(proposition.subject_symbol_id, proposition.object_symbol_id)

return OperationResult(status="accept", sinn=sense,
                       payload={"truth": truth, "exists": truth != "∅"})
```

## Ejemplo de Rechazo: "El electrón tiene color rojo"

```
Paso 1: sujeto="electron", relación="tiene_color", objeto="rojo"
Paso 2: (tiene_color electron rojo)
Paso 3: Buscar WiGame → "fisica:particulas" tiene axis con electrones
        pero la relación "tiene_color" NO está en este WiGame
Paso 4: accepts() = False → OperationResult(status="reject", sinn="unsinnig")
Paso 5: No se ejecuta — la proposición fue rechazada antes de evaluar verdad
```

## El Pipeline Completo como S-Expression

```lisp
; Inicialización
(create symbol electron "electrón")
(create symbol rojo "color rojo")
(create relation tiene_color "tiene color")
(create li li_fisica tiene_color (axis-a electron neutrón quark) (axis-b rojo azul verde))
(create wigame wg_fisica li_fisica)

; Consulta
(check (tiene_color electron rojo))
;; → reject, sinn=unsinnig (electrón no tiene color por principio)

; Ingesta válida
(ingest wigame:cocina (tiene_ingrediente ragout champinon))
;; → accept, sinn=sinnvoll, truth=true
```
