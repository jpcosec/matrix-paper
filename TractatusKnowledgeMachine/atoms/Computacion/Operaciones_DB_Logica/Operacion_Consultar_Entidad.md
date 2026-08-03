---
id: atom-operacion-consultar-entidad
title: Operacion Consultar Entidad
five_wh_one_plus: what
tags:
- system:matrix
---
# Operación: QueryEntity

## 1. Función Lógica (Álgebra de Boole)
Ecuación base: $\bigvee_{x} (V_{a,x} \lor V_{x,a})$
Basado en los axiomas formales del álgebra booleana y el tratamiento de tablas de verdad/formas canónicas.

## 2. Conversión a Álgebra Matricial
Reducción lógica sobre filas/columnas de $V_i$.
Transforma el operador lógico en operaciones tensoriales nativas (multiplicaciones de semianillo, reducciones).

## 3. Traducción al Diseño MEEL ($W_i, C_i, L_i, S_i, V_i$)
Escaneo de $V_i$ para aislar todas las relaciones activas de un símbolo.
