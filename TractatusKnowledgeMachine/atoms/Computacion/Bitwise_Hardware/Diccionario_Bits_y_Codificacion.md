---
topic: diccionario-bits-y-codificacion
use_when: Aplicable al contexto semantico y factual de Diccionario Bits y Codificacion.
do_not_use_when: No utilizar fuera del dominio formal de bitwise-hardware.
id: atom-diccionario-bits-y-codificacion
title: Diccionario Bits y Codificacion
five_wh_one_plus: what
tags:
- system:matrix
---
# Diccionario de Bits y Esquemas de Codificación (One-Hot vs Multi-Hot)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Vectorizacion_Bitwise_Densa]]]
* [implements:: [[Eje_D_Diferenciacion_OWL_KGs_y_Vectorizacion_Bitwise]]]
* [implements:: [[BooleanMatrix]]]
* [is_solved_by:: [[Algebra_Booleana]]]
* [is_solved_by:: [[Contrastes_XOR_Booleanos]]]

---

## Qué es
Es el componente que mapea posiciones discretas de bits en palabras de procesador (`uint64`) a pares atributo-valor (Anexo B), estableciendo la distinción entre codificaciones exclusivas (one-hot) e inclusivas (multi-hot).

---

## Codificación de Bits

* **Codificación One-Hot (Exclusiva):** Garantiza que solo un bit del grupo puede estar encendido a la vez (p. ej., estado de un interruptor: prendido XOR apagado).
* **Codificación Multi-Hot (Non-Exclusiva):** Permite múltiples bits activos simultáneamente (p. ej., lista de ingredientes de una receta).
