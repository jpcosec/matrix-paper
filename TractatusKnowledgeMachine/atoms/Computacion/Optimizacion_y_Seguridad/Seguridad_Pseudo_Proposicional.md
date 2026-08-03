---
topic: seguridad-pseudo-proposicional
use_when: Aplicable al contexto semantico y factual de Seguridad Pseudo Proposicional.
do_not_use_when: No utilizar fuera del dominio formal de logic-optimization.
id: atom-seguridad-pseudo-proposicional
title: Seguridad Pseudo Proposicional
five_wh_one_plus: what
tags:
- system:matrix
---
# Seguridad Pseudo-Proposicional y Taxonomía de Errores

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Capa_Sentido_Si]]]
* [is_solved_by:: [[Ausencia_de_Senal_de_Fallo_Determinista]]]
* [implements:: [[S_Expressions]]]
* [is_solved_by:: [[Algebra_Booleana]]]

---

## Qué es
Es la taxonomía de seguridad y rechazo en tiempo de compilación (Anexo A.3.14) que intercepta formulaciones engañosas que parecen lenguaje con sentido pero que no pueden proyectarse en el espacio $L_i$.

---

## Taxonomía de Errores de Seguridad

* `UNKNOWN_DIMENSION`: Intento de referenciar dimensiones no mapeadas en el contexto.
* `TYPE_MISMATCH`: Asignación de un objeto a una propiedad fuera de su tipo formal.
* `DIMENSION_NOT_APPLICABLE`: Violación de la Máscara de Sentido ($S_i=0$).
* `UNBOUND_PRONOUN`: Falla en la resolución de anáforas en la capa de discurso.
