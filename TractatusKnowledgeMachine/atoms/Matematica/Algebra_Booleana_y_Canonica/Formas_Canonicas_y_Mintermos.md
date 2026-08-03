---
topic: canonical-forms
id: atom-formas-canonicas-y-mintermos
title: Formas Canonicas y Mintermos
five_wh_one_plus: what
tags:
- system:matrix
---
# Formas Canónicas (Mintermos y Maxtermos)

## 1. Definición Matemática Formal
Toda función lógica $f(x_1, x_2, \dots, x_n)$ sobre un álgebra de Boole puede ser expresada de manera única mediante formas canónicas.
* **Mintermo ($m_i$):** Es una expresión lógica de conjunciones ($\land$) en la que todas las variables aparecen exactamente una vez, ya sea afirmadas o negadas. Una función booleana es verdadera si coincide con al menos uno de sus mintermos.
  * *Forma Canónica Disyuntiva (Suma de Productos - SOP):* $f = \bigvee_{i=0}^{2^n-1} c_i \land m_i$
* **Maxtermo ($M_i$):** Es una expresión de disyunciones ($\lor$). Una función es falsa si coincide con al menos uno de sus maxtermos.
  * *Forma Canónica Conjuntiva (Producto de Sumas - POS):* $f = \bigwedge_{i=0}^{2^n-1} (c_i \lor M_i)$

## 2. Álgebra Matricial Booleana
Para resolver funciones lógicas sobre tensores, cualquier regla condicional compleja (ej. `Si A y (B o no C) entonces D`) se expande algebraicamente a su Forma Canónica Disyuntiva (SOP).
Al estar en SOP, cada mintermo se convierte en un vector columna denso $I_k \in \{0, 1\}^N$ dentro de la Matriz de Incidencia $I$.

## 3. Traducción al MEEL ($W_i, V_i, S_i$)
En nuestro diseño, la Matriz de Incidencia $I$ almacena los Mintermos que rigen las reglas lógicas del espacio $L_i$.
La evaluación de todas las reglas en paralelo para todos los sujetos en la matriz $V_i$ se reduce a:
$V_{t+1} = V_t \lor (V_t \otimes I^*)$
Donde la multiplicación $\otimes$ evalúa todos los conjunciones ($\land$) de los mintermos, y la suma $\lor$ acumula la disyunción canónica.
