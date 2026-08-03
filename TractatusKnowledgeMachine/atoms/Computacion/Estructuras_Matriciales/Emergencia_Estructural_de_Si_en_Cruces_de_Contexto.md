---
system: matrix
layer: sense-structure
domain: context-composition
topic: emergencia-estructural-de-si-en-cruces-de-contexto
use_when: "Aplicable al contexto semantico y factual de Emergencia Estructural de Si en Cruces de Contexto."
do_not_use_when: "No utilizar fuera del dominio formal de context-composition."
---

# Emergencia Estructural de $S_i$ en Cruces de Contexto

**Categoría Padre:** [[Computacion/Estructuras_Matriciales]]
**Relaciones 5W1H+:**
* [implements:: [[Capa_Sentido_Si]]]
* [implements:: [[Distincion_Ausencia_vs_Unsinnig]]]
* [implements:: [[Construccion_Tensor_Jerarquico]]]
* [implements:: [[Contexto_Logico]]]
* [implements:: [[Categorias_Sentido]]]

---

## Qué es
Es el criterio operacional para distinguir entre **ausencia de dato** y **Unsinnig** en dominios reales. La idea central es que $S_i$ no nace como una lista manual de absurdos, sino como una consecuencia estructural de componer contextos cerrados $w_i$ y observar qué cruces de coordenadas son admisibles y cuáles caen fuera de sentido.

## Regla base

### En un contexto base $w_i$
Si el contexto está bien delimitado, puede modelarse de forma casi "cuadrada":

- los objetos del eje pertenecen al mismo tipo local;
- las propiedades fueron elegidas para ese subuniverso;
- gran parte de las coordenadas tiene sentido.

En ese caso:
- $S_i=1$ suele ser casi trivial;
- la pregunta real pasa a ser factual: $V_i=true$, $V_i=false$ o $V_i=∅$.

### Al mezclar contextos
$S_i$ se vuelve necesario cuando se cruzan coordenadas de distintos $w_i$:

- objetos de un dominio
- propiedades de otro dominio
- relaciones que no comparten firma lógica

Ahí aparecen tres clases:

1. **Sinnvoll** — el cruce es admisible
2. **Don’t care / fuera de subcontexto** — no se evalúa en ese bloque
3. **Unsinnig** — el cruce viola la estructura categorial

## Criterio operacional

Dada una proposición candidata $(R,a,b)$:

### Paso 1 — verificar pertenencia al contexto
- ¿$a$ pertenece al eje o subespacio correcto?
- ¿$b$ pertenece al eje o subespacio correcto?
- ¿$R$ está admitida en ese $w_i$?

Si no, la proposición es **Unsinnig**.

### Paso 2 — verificar firma lógica
- ¿la relación $R$ admite un sujeto del tipo de $a$?
- ¿la relación $R$ admite un objeto del tipo de $b$?

Si no, la proposición es **Unsinnig**.

### Paso 3 — verificar que la coordenada exista como cruce admisible
Si la composición por bloques o tensorial define ese cruce como válido, entonces $S_i=1$.

Si el cruce fue excluido por construcción, entonces $S_i=0$.

### Paso 4 — recién entonces consultar $V_i$
Solo si $S_i=1$:
- $V_i=true$ → verdadero
- $V_i=false$ → falso pero válido
- $V_i=∅$ → ausencia de dato

## Fórmula corta

- **Unsinnig** = falla de contexto o de firma
- **Ausencia** = contexto válido + coordenada admisible + sin dato factual

## Ejemplos

### Derecho
- "El automóvil cometió fraude fiscal" → **Unsinnig**
  - `automóvil` no tiene la firma agente moral/jurídico requerida por `cometer_fraude`
- "Juan Pérez tiene multas previas" → **Ausencia** si el historial no fue ingerido
  - la relación sí tiene sentido en ese contexto

### Medicina
- "El tumor cerebral siente tristeza" → **Unsinnig**
  - la propiedad emocional no aplica al tipo `tumor`
- "El tumor presenta mutación IDH1" → **Ausencia** si no se ha cargado la biopsia
  - la coordenada es admisible

### Física
- "La carga del electrón es verde" → **Unsinnig**
  - el cruce entre partícula elemental y color macroscópico no pertenece al contexto válido
- "El espín de este electrón es +1/2" → **Ausencia** si no hay medición cargada
  - la propiedad sí es estructuralmente válida

## Qué aclara respecto a `Distincion_Ausencia_vs_Unsinnig`

`Distincion_Ausencia_vs_Unsinnig` define la separación teórica y el comportamiento del código.

Este átomo agrega **de dónde sale esa decisión en dominios reales**:
- del contexto cerrado,
- de la firma de relaciones,
- y de la composición entre subespacios.

## Limitaciones declaradas

### Sí está claro
- cómo decidir ausencia vs. Unsinnig cuando el contexto $w_i$ ya fue definido;
- por qué $S_i$ aparece sobre todo al componer contextos;
- por qué no hace falta etiquetar manualmente cada absurdo posible.

### No está claro todavía
- cómo aprender automáticamente $S_i$ desde texto crudo en un dominio totalmente nuevo;
- cómo descubrir sin curaduría experta la ontología mínima correcta;
- cómo resolver casos frontera donde un atributo cambia de sentido entre subcontextos.

## Respuesta corta al revisor

La diferencia no se decide por intuición ni por una lista manual de absurdos. Se decide por estructura: si la proposición cae dentro de un cruce admisible del contexto compuesto, $S_i=1$ y puede consultarse $V_i$; si viola la firma lógica o el bloque contextual, $S_i=0$ y la proposición es Unsinnig.
