---
topic: formal-grammar
id: atom-gramatica-formal
title: Gramatica Formal
five_wh_one_plus: what
tags:
- system:matrix
---
# Gramática Formal

## 1. Definición Matemática Formal
Una Gramática Formal $G$ se define como una tupla $G = (N, \Sigma, P, S)$ donde:
* $N$ es el conjunto de símbolos no terminales.
* $\Sigma$ es el conjunto de símbolos terminales (alfabeto).
* $P$ es un conjunto de reglas de producción de la forma $(\Sigma \cup N)^* N (\Sigma \cup N)^* \to (\Sigma \cup N)^*$.
* $S \in N$ es el símbolo inicial.
El lenguaje $L(G)$ generado por la gramática es el conjunto de todas las cadenas de $\Sigma^*$ derivables desde $S$ aplicando reglas de $P$.

## 2. Álgebra Matricial Booleana
Para lenguajes finitos regulares (suficientes para la lógica proposicional MEEL), las reglas gramaticales pueden compilarse en autómatas finitos, cuyas transiciones de estado de aceptación/rechazo se mapean a una Máscara Matricial de Coordenadas.

## 3. Traducción al MEEL ($L_i, S_i$)
En Matrix:
* **El Alfabeto ($\Sigma$):** Está definido directamente por el Espacio Lógico $L_i(C_i, R_i)$.
* **Sintaxis (Sinnvoll vs Unsinnig):** La matriz $S_i$ es la manifestación tensorial de la gramática formal. Si la regla de producción para la proposición $p \notin L(G)$, entonces $S_i(p) = 0$. Esto garantiza que el motor deductivo JAX nunca ejecute operaciones algebraicas sobre proposiciones que, aunque formadas por símbolos válidos, violan las reglas sintácticas del contexto.
