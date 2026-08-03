---
topic: compilador-matricial-reglas
use_when: Aplicable al contexto semantico y factual de Compilador Matricial Reglas.
do_not_use_when: No utilizar fuera del dominio formal de meel-engine.
id: atom-compilador-matricial-reglas
title: Compilador Matricial Reglas
five_wh_one_plus: what
tags:
- system:matrix
---
# Compilador Matricial de Reglas

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Inferencia_Deductiva_Matricial]]]
* [implements:: [[S_Expressions]]]
* [is_solved_by:: [[Algebra_Booleana]]]

---

## Qué es
Es el componente que traduce expresiones lógicas en Forma Binaria Formateada (FBF) o S-Expressions hacia estructuras de matrices de incidencia booleana ($I$, $C^+$, $C^-$) sin mantener árboles de sintaxis (AST) en tiempo de ejecución.

## Por qué es necesario
Permite eliminar el sobrecosto de evaluar árboles de código (AST) mediante condicionales en tiempo de ejecución, transformando la inferencia deductiva en productos de matrices sobre procesadores binarios o hardware vectorial.

## Cómo funciona
1. **Matriz de Implicación Directa ($I$):** Codifica reglas $P_i \implies P_j$ en una matriz booleana $N \times N$.
2. **Matrices de Cláusulas ($C^+, C^-$):** Convierte fórmulas a Forma Normal Conjuntiva (CNF) y genera la máscara de presencia positiva ($C^+$) y negada ($C^-$) por cada cláusula disyuntiva.

## Cuándo interviene
Durante la fase de compilación e ingesta de premisas dentro de un juego de lenguaje ($W_i$), antes de realizar consultas o deducciones.

## Dónde reside
En la capa intermedia de runtime (`RuleMatrixCompiler`), actuando entre el parser sintáctico de S-Expressions y el motor de ejecución de matrices.

## Para qué / Para quién
Proporciona al motor matricial ($W_i$) las estructuras compactas necesarias para realizar Modus Ponens y propagación de cláusulas mediante álgebra booleana pura.
