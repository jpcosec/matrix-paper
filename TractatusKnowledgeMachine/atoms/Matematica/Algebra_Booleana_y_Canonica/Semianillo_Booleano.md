---
id: atom-semianillo-booleano
title: Semianillo Booleano
five_wh_one_plus: what
tags:
- system:matrix
---
# Semianillo Booleano

Estructura algebraica $(B, \oplus, \otimes, 0, 1)$ donde:
* $\oplus$ representa la disyunción lógica (OR, $\lor$).
* $\otimes$ representa la conjunción lógica (AND, $\land$).

En JAX, las operaciones tensoriales sobre $V_i$ y $S_i$ reemplazan la adición escalar por OR lógico y la multiplicación escalar por AND lógico para ejecutar inferencias sin usar control flow (if/else).
