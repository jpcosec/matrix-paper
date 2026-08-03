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
Es el recorrido paso a paso del pipeline completo (4 etapas) desde la entrada en lenguaje natural hasta la decisión de aceptar o rechazar una proposición, con un ejemplo concreto ejecutado.

## Ejemplo: "El ragout tiene champiñones"

### Paso 1 — Descomposición en Forma Estándar

El descompositor de superficie (propuesta: LLM chica, sin decisiones lógicas) separa el significado del azúcar sintáctico y lo expresa en una representación estandarizada. El anclaje de símbolos ocurre **plegado aquí**:

```
Input:  "El ragout tiene champiñones"
        ↓
Descomposición: sujeto="ragout", relación="tiene_ingrediente", objeto="champinon"
        ↓
Anclaje (plegado en esta etapa):
  sign("ragout")     → Symbol("ragout")
  sign("champiñones") → Symbol("champinon")  (normalización de alias)
  sign("tiene")      → Relation("tiene_ingrediente")
```

### Paso 2 — Reducción a Proposición Candidato

La forma estándar se reduce a una proposición candidato homogénea, **aún sin estatus de verdad**:

```
Candidato: (tiene_ingrediente ragout champinon)
```

### Paso 3 — Chequeo de Sentido, paso (a): Indexación por Contexto

```
MEEL evalúa: ¿qué contexto indexa el cruce (tiene_ingrediente, ragout, champinon)?
  → WiGame "cocina" admite:
     axis_a: [ragout, risotto, paella, ...]
     axis_b: [champinon, arroz, azafran, ...]
     relation: tiene_ingrediente
  → Resultado: wigame:cocina

Si ningún contexto admite el cruce → Si = "unsinnig" → 🚫 RECHAZAR
(el absurdo se evita por construcción, antes de cualquier evaluación de verdad)

Casos al consultar Si.get("ragout", "champinon"):
Caso A: Si = "sinnvoll"  → ✅ La combinación es categorialmente válida
Caso B: Si = "unsinnig"  → 🚫 RECHAZAR: absurdo semántico en este contexto
Caso C: Fuera de ejes    → 🚫 RECHAZAR: "La proposición no pertenece a este espacio lógico"
```

### Paso 4 — Chequeo de Sentido, paso (b): Contradicción contra $V_i$

```
(Caso A: candidato admisible)

¿Conflicto con hechos ya asertados en V_i del contexto?

Sin conflicto  → continuar al cómputo matricial
Con conflicto  → 🚫 SEÑAL EXPLÍCITA DE CONTRADICCIÓN
                 (nunca sobrescritura silenciosa; ver Manejo_de_Contradicciones)

Ejemplo: (sonido gato ladra) tras haber asertado (sonido gato maulla)
  → pasa (a): el cruce es admisible en el contexto
  → falla (b): contradicción con el hecho existente
```

### Paso 5 — Cómputo Matricial y Decisión Final ($V_i$)

```
(Solo si pasó (a) y (b))

Vi.get("ragout", "champinon")?

Resultado posible:
  "true"  → ✅ "Sí, el ragout tiene champiñones."
  "false" → ❌ "No, el ragout no tiene champiñones."
  "∅"     → ⚠️ "No se sabe si el ragout tiene champiñones (ausencia de dato)."
```

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
Paso 1: descomposición → sujeto="electron", relación="tiene_color", objeto="rojo"
Paso 2: candidato (tiene_color electron rojo)
Paso 3a: indexación por contexto → "fisica:particulas" tiene axis con electrones
        pero la relación "tiene_color" NO está indexada en este contexto
        → accepts() = False → OperationResult(status="reject", sinn="unsinnig")
Pasos 3b-5: no se ejecutan — el candidato fue rechazado antes de evaluar verdad
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
