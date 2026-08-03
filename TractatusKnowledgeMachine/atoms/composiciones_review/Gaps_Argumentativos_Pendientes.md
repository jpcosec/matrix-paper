---
system: matrix
layer: review
domain: gap-tracking
topic: gaps-argumentativos-pendientes
use_when: "Aplicable al contexto semantico y factual de Gaps Argumentativos Pendientes."
do_not_use_when: "No utilizar fuera del dominio formal de gap-tracking."
---

# Gaps Argumentativos Pendientes

**Categoría Padre:** [[composiciones_review]]
**Relaciones 5W1H+:**
* [explains_failure_of:: [[comp_eje_a]]]
* [explains_failure_of:: [[comp_eje_b]]]
* [explains_failure_of:: [[comp_eje_c]]]
* [explains_failure_of:: [[comp_eje_d]]]
* [explains_failure_of:: [[comp_eje_e]]]
* [explains_failure_of:: [[comp_eje_reviewer]]]

---

## Qué es
Es el registro de las preguntas de revisores que **no pueden responderse** con los átomos existentes ni con las fuentes en disco. Cada gap requiere trabajo original (argumento, experimento, o especificación nueva).

---

## Gaps por Eje

### Eje A — Embeddings continuos como causa de alucinación

**GAP-A1: RESUELTO**
- Cerrado por: [[Representacion_Continua_vs_Implementacion_Discreta]]
- Respuesta: distingue entre discretización numérica del hardware y continuidad topológica del espacio semántico $\mathbb{R}^d$, y explica por qué `argmax` no corrige la interpolación continua.

---

### Eje B — Escalabilidad y construcción de matrices

**GAP-B1: Cobertura conceptual parcial**
- **Cerrado en lo conceptual por:** [[Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva]]
- **Respuesta actual:** Matrix no propone una extracción universal ni una "tasa de error de la representación". Propone bootstrapping por contextos cerrados, con LLM como proponente de estructura y auditoría posterior en forma booleana.
- **Sigue abierto:** benchmark empírico a gran escala, automatización sin revisión humana, y costo real a millones de conceptos.
- **Estado:** 🟡 Parcialmente resuelto; falta validación empírica.

**GAP-B2: Cobertura conceptual parcial**
- **Cerrado en lo operacional por:** [[Emergencia_Estructural_de_Si_en_Cruces_de_Contexto]]
- **Respuesta actual:** la diferencia entre ausencia y Unsinnig se decide por contexto, firma lógica y cruce admisible de coordenadas. Si el cruce es inválido, $S_i=0$; si es válido pero falta hecho, $V_i=∅$.
- **Sigue abierto:** cómo aprender automáticamente $S_i$ desde texto crudo en dominios completamente nuevos.
- **Estado:** 🟡 Parcialmente resuelto; falta aprendizaje automático de ontología/sentido.

---

### Eje C — Mecanismo de conexión con LLMs

**GAP-C1: Sigue abierto**
- **Pregunta original:** Q6 — "¿Cuál es el algoritmo concreto para integrar las máscaras de sentido en el mecanismo de atención?"
- **Qué sí puede afirmarse:** [[Integracion_Teorica_con_LLMs_y_Trabajo_Futuro]] deja claro que esta inyección es solo una hipótesis de diseño para Fase 3.
- **No está claro:** capa, heads, alineación símbolo-token, ni manejo de tokens sin mapeo simbólico.
- **Estado:** 🔴 Trabajo futuro.

**GAP-C2: Sigue abierto**
- **Pregunta original:** Q7 — "Durante el entrenamiento: ¿la máscara actúa como mero filtrado de datos? ¿Hay prueba de que mitigue alucinaciones?"
- **Qué sí puede afirmarse:** hoy $S_i$ sirve para auditoría post-generación y detección de inconsistencias lógicas.
- **No está claro:** rol en entrenamiento, regularización, pérdida auxiliar, ni reducción empírica de alucinaciones.
- **Estado:** 🔴 Trabajo futuro.

**GAP-C3: Sigue abierto**
- **Pregunta original:** Q9 — "¿Cómo se calcula la pérdida intermedia (intermediate loss)?"
- **Qué sí puede afirmarse:** $E(R)$ optimiza la representación de la base de datos.
- **No está claro:** ninguna loss híbrida de entrenamiento neuronal; $E(R)$ no debe presentarse como cross-entropy lógica ni como mecanismo de backprop.
- **Estado:** 🔴 Trabajo futuro.

---

### Eje D — Diferenciación con métodos existentes

**GAP-D1: RESUELTO**
- **Cerrado por:** [[Matrix_vs_Verificacion_Formal]]
- **Respuesta actual:** Matrix se diferencia de Coq/Lean/Dafny porque opera sobre hechos proposicionales y evaluación booleana en contextos cerrados, no sobre construcción de pruebas formales paso a paso.
- **Limitación explícita:** la comparación actual es arquitectónica y posicional, no experimental.

---

### Eje E — Opacidad sobre la implementación

**GAP-E1: Evaluación experimental end-to-end**
- **Pregunta original:** Q13 — "¿Dónde están los detalles, métricas o arquitectura ejecutable?"
- **Por qué falta:** `Benchmarks_y_Metricas_Cuantitativas` documenta los 105 tests y las métricas internas ($E(R)$), pero no hay evaluación experimental contra baselines externos.
- **Qué se necesita:** (a) Experimento: tasa de alucinación con/sin $S_i$; (b) Benchmark: latencia bitwise vs. graph traversal en KGs; (c) Escalabilidad: rendimiento con $N$ creciente; (d) Comparación con RAG/KGs en datasets estándar (FEVER, HaluEval).
- **Tipo de trabajo:** Experimento controlado + publicación de resultados.

**GAP-E2: Tests de integración LLM→MEEL rotos**
- **Detalle:** 5 tests de SHRDLU y ragout tienen errores de import y no pasan. Estos son los tests que prueban el pipeline end-to-end.
- **Qué se necesita:** Reparar imports y verificar que `test_shrdlu_*` y `test_ragout_demonstration` pasan.
- **Tipo de trabajo:** Fix de código.

---

### Revisor — Preguntas adicionales

**GAP-R1: Sigue abierto**
- **Pregunta original:** Q16 (ZHLy) — "¿Dónde está la demostración de 'demostramos que los LLMs se pueden usar para mapear lenguaje...' ?"
- **Qué sí existe:** prototipo SHRDLU y walkthrough operacional.
- **No existe todavía:** evaluación robusta de lowering NL→lógica con métricas, dominios y comparación externa.
- **Estado:** 🔴 Trabajo experimental futuro.

**GAP-R2: Sigue abierto**
- **Pregunta original:** Q15 (ZHLy) — "¿Cómo se conecta la representación de la Sección 3 con la arquitectura real de redes neuronales?"
- **Qué sí puede afirmarse:** la implementación actual está desacoplada; el LLM genera texto y Matrix parsea/valida después.
- **No existe todavía:** mapping directo entre coordenadas de $L_i$ y posiciones/tokens internos del Transformer.
- **Estado:** 🔴 Especificación arquitectónica futura.

---

## Resumen final de gaps pendientes

| Tipo | Cantidad | Gaps |
|:---|:---|:---|
| **Especificación arquitectónica futura** | 2 | C1, R2 |
| **Trabajo futuro en integración LLM** | 2 | C2, C3 |
| **Trabajo experimental futuro** | 2 | E1, R1 |
| **Validación/escala aún abierta** | 2 | B1, B2 |
| **Fix de ingeniería** | 1 | E2 |
