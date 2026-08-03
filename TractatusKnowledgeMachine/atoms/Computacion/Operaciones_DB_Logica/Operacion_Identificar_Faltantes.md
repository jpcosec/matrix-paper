---
id: atom-operacion-identificar-faltantes
title: Operacion Identificar Faltantes
five_wh_one_plus: what
tags:
- system:matrix
---
# Operación: IdentifyUnknowns

## 1. Función Lógica (Álgebra de Boole)
Ecuación base: $U = I_{req} \land \neg V$
Basado en los axiomas formales del álgebra booleana y el tratamiento de tablas de verdad/formas canónicas.

## 2. Conversión a Álgebra Matricial
Sustracción booleana de mintermos faltantes.
Transforma el operador lógico en operaciones tensoriales nativas (multiplicaciones de semianillo, reducciones).

## 3. Traducción al Diseño MEEL ($W_i, C_i, L_i, S_i, V_i$)
Compara la tabla de verdad requerida por la regla con los hechos instanciados en $V_i$.
