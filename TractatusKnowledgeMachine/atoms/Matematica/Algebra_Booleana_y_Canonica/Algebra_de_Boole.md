---
topic: boolean-algebra
id: atom-algebra-de-boole
title: Algebra de Boole
five_wh_one_plus: what
tags:
- system:matrix
---
# Álgebra de Boole

## 1. Definición Matemática Formal
Un Álgebra de Boole es una estructura algebraica $(B, \lor, \land, \neg, 0, 1)$ que consiste en un conjunto $B$ con dos operaciones binarias ($\lor$ disyunción, $\land$ conjunción), una operación unaria ($\neg$ negación) y dos elementos distinguidos $0$ y $1$.
Cumple los siguientes postulados (Axiomas de Huntington):
* **Cierre:** $\forall a,b \in B$, $a \lor b \in B$ y $a \land b \in B$.
* **Conmutatividad:** $a \lor b = b \lor a$ y $a \land b = b \land a$.
* **Asociatividad:** $a \lor (b \lor c) = (a \lor b) \lor c$ y $a \land (b \land c) = (a \land b) \land c$.
* **Identidad:** $a \lor 0 = a$ y $a \land 1 = a$.
* **Distributividad:** $a \lor (b \land c) = (a \lor b) \land (a \lor c)$ y $a \land (b \lor c) = (a \land b) \lor (a \land c)$.
* **Complemento:** $\forall a \in B, \exists \neg a$ tal que $a \lor \neg a = 1$ y $a \land \neg a = 0$.

De aquí derivan los Teoremas de De Morgan:
$\neg(a \lor b) = \neg a \land \neg b$
$\neg(a \land b) = \neg a \lor \neg b$

## 2. Álgebra Matricial Booleana (El Semianillo)
Para adaptar el Álgebra de Boole a matrices en JAX, definimos un semianillo booleano $(B, \oplus, \otimes, 0, 1)$ donde:
* La adición matricial $\oplus$ equivale al operador lógico $\lor$.
* La multiplicación matricial $\otimes$ equivale al operador lógico $\land$.

Dadas dos matrices booleanas $A, B \in \{0,1\}^{N \times M}$, el producto punto booleano (para inferencia transitiva) es:
$C_{i,j} = \bigvee_{k} (A_{i,k} \land B_{k,j})$

## 3. Traducción al MEEL ($W_i, V_i, S_i$)
En Matrix, $V_i$ y $S_i$ son tensores que instancian $B^{N \times M}$. Las operaciones lógicas no se evalúan con bucles `if/else`, sino que se resuelven densamente mediante el semianillo booleano. La matriz nula (0) es el estado de desconocimiento/falsedad total, y la matriz identidad (1) en la diagonal mapea relaciones reflexivas (ej. $x=x$).
