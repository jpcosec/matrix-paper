---
topic: falla-de-representabilidad
use_when: Aplicable al contexto semantico y factual de Falla de Representabilidad.
do_not_use_when: No utilizar fuera del dominio formal de llm-pathologies.
id: atom-falla-de-representabilidad
title: Falla de Representabilidad
five_wh_one_plus: what
tags:
- system:matrix
---
# La Alucinación como Falla de Representabilidad

**Categoría Padre:** [[Antecedentes/Alucinaciones]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_symcode2025_pdf]]]
* [explains_failure_of:: [[Prueba_Necesidad_Representacion_Simbolica_Discreta]]]
* [is_solved_by:: [[Capa_Sentido_Si]]]
* [explains_failure_of:: [[Discretizacion_Logica_vs_Continuo]]]
* [explains_failure_of:: [[Matriz_por_Bloques]]]
* [explains_failure_of:: [[Teorema_Suboptimizabilidad_Diagonal]]]

---

## Qué es
Es la redefinición teórica central formulada en la discusión del manuscrito, la cual sostiene que las alucinaciones no deben tratarse únicamente como un problema de "mala recuperación de información" (RAG), sino como una **incapacidad estructural de representabilidad**.

---

## Tesis Central
Una alucinación ocurre cuando un sistema continuo intenta procesar o emitir proposiciones que violan la gramática de sentido local de un dominio (*Unsinnig*). Erradicar las alucinaciones exige restringir la representabilidad del sistema mediante un kernel Booleano.
