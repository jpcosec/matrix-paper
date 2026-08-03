---
topic: lattice
id: atom-reticulo-matematico-lattice
title: Reticulo Matematico Lattice
five_wh_one_plus: what
tags:
- system:matrix
---
# Retículo (Lattice)

## 1. Definición Matemática Formal
Un Retículo es un conjunto parcialmente ordenado (poset) $(L, \le)$ donde para cualquier par de elementos $x, y \in L$ existe:
1. **Supremo (Join, $\lor$):** El menor de los cotas superiores, $x \lor y = \sup(x,y)$.
2. **Ínfimo (Meet, $\land$):** El mayor de las cotas inferiores, $x \land y = \inf(x,y)$.
Cumple los axiomas de conmutatividad, asociatividad, absorción ($a \lor (a \land b) = a$) e idempotencia.

## 2. Álgebra Matricial Booleana
La estructura del retículo puede ser representada matricialmente usando la clausura transitiva de su matriz de adyacencia (relaciones de orden parcial). Si $M$ es la matriz de adyacencia de $\le$, el supremo se encuentra calculando los ancestros comunes.

## 3. Traducción al MEEL ($W_i, C_i, L_i$)
Los **Contextos Lógicos ($C_i$)** se estructuran jerárquicamente formando un Retículo.
* Si $C_1$ es "Física" y $C_2$ es "Biología", $C_1 \land C_2$ (Ínfimo) podría ser "Física Cuántica Biológica", mientras que $C_1 \lor C_2$ (Supremo) es "Ciencias Naturales".
* El Ruteo ($WC_i$) es simplemente la navegación a lo largo de los ejes $\le$ de este Retículo. Para consultar un hecho multidisciplinario, Matrix busca el Supremo de los contextos involucrados para aislar el espacio lógico integrador $L_{sup}$.
