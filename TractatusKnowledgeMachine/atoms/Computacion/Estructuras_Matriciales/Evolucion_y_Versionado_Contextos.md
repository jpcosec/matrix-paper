---
topic: evolucion-y-versionado-contextos
use_when: Aplicable al contexto semantico y factual de Evolucion y Versionado Contextos.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-evolucion-y-versionado-contextos
title: Evolucion y Versionado Contextos
five_wh_one_plus: what
tags:
- system:matrix
---
# Evolución y Versionado de Contextos (ContextVersion)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[WiGame]]]
* [implements:: [[BlockMatrix]]]
* [grounded_by:: [[Eje_B_Escalabilidad_Minimizacion_ER_y_Tensor_Jerarquico]]]
* [is_solved_by:: [[Matrices_y_Tensores]]]

---

## Qué es
Es el mecanismo algorítmico (Anexo A.3.8, A.3.10) que gestiona los cambios temporales de la base de conocimiento y los esquemas lógicos sin corromper la lectura de firmas bitwise previas.

---

## Mecanismo de `ContextVersion`
Cuando se introduce un nuevo símbolo o relación en $L_i$, la dimensión de las matrices $V_i$ y $S_i$ se incrementa. Para evitar desalineaciones bitwise:
* Cada estado del sistema almacena un `ContextVersion`.
* Las operaciones de actualización (`add_fact`, `update_context`) aplican un re-indexado por máscaras de bits, manteniendo compatibilidad backward entre versiones.
