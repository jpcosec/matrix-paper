---
topic: truth-table
id: atom-tabla-de-verdad
title: Tabla de Verdad
five_wh_one_plus: what
tags:
- system:matrix
---
# Tabla de Verdad

## 1. Definición Matemática Formal
Una tabla de verdad exhibe el valor de una función lógica $f(x_1, \dots, x_n)$ para cada una de las $2^n$ combinaciones posibles de variables booleanas de entrada. Define un mapeo exhaustivo $f: \{0,1\}^n \to \{0,1\}$.

## 2. Álgebra Matricial Booleana
En vez de evaluar filas condicionales iterativamente, una tabla de verdad puede ser representada topológicamente como una matriz de adyacencia (o hipergrafo). Las combinaciones que retornan '1' definen los vértices activos.

## 3. Traducción al MEEL ($W_i, V_i, S_i$)
El hiper-tensor $V_i$ es literalmente la **Tabla de Verdad Empírica** del contexto $C_i$.
Sin embargo, dado que evaluar una tabla de verdad de $N$ dimensiones iterativamente es intratable ($O(2^n)$), la matriz $V_i$ funciona como una tabla dispersa (Sparse-Block) en JAX. Solo los mintermos que son el caso (1) están activados. $S_i$ actúa como un filtro sobre esta tabla, marcando con $0$ combinaciones que son *Unsinnig* (imposibles), colapsando drásticamente el espacio de búsqueda.
