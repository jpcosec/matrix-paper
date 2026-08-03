---
topic: contrastes-xor-booleanos
use_when: Aplicable al contexto semantico y factual de Contrastes XOR Booleanos.
do_not_use_when: No utilizar fuera del dominio formal de discrete-math.
id: atom-contrastes-xor-booleanos
title: Contrastes XOR Booleanos
five_wh_one_plus: what
tags:
- system:matrix
---
# Contrastes XOR Booleanos

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Algebra_Booleana]]]
* [mathematically_proves:: [[BooleanMatrix]]]
* [mathematically_proves:: [[Vectorizacion_Bitwise_Densa]]]

---

## Qué es
Es la formulación matemática mediante la cual las diferencias entre dos particiones de mundo $W_1$ y $W_2$ o entre hechos contradictorios se calculan instantáneamente mediante la operación lógica **OR Exclusivo (XOR)** a nivel de bits:

$$\Delta(W_1, W_2) = W_1 \oplus W_2$$

---

## Aplicación
Permite identificar con complejidad $\mathcal{O}(1)$ en palabras `uint64` exactamente qué bits de verdad ($V_i$) o sentido ($S_i$) han variado entre dos contextos o versiones documentales.
