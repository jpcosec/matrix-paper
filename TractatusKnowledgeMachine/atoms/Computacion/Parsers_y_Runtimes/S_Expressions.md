---
topic: s-expressions
use_when: Aplicable al contexto semantico y factual de S Expressions.
do_not_use_when: No utilizar fuera del dominio formal de parsers-runtimes.
id: atom-s-expressions
title: S Expressions
five_wh_one_plus: what
tags:
- system:matrix
---
# S_Expressions (Simbolismo)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_language_s_expressions_py]]]
* [is_solved_by:: [[Signo_vs_Simbolo]]]
* [is_solved_by:: [[Enrutamiento_Jerarquico]]]
* [is_solved_by:: [[Compilador_Matricial_Reglas]]]
* [is_solved_by:: [[Politica_Simbolos_Kernel]]]
* [is_solved_by:: [[Hecho_Atomico_CDV]]]

---

## Qué es
La representación lógica canonizada de hechos y fórmulas en Forma Binaria Formateada (FBF) mediante expresiones canónicas de tipo `(R a b)` o conectivas `(if a b)`, `(and a b)`.

## Por qué es necesario
Provee un puente natural entre el lenguaje (texto/código) y la estructura matricial, permitiendo representar relaciones relacionales y relativas al kernel de forma unificada.

## Cómo funciona
Cada s-expression se analiza distinguiendo entre símbolos del kernel (`kern:{symbol}`, `instance`, `equivalent`, conectivas) y relaciones relacionales de $W_i$. El compilador traduce estas expresiones a matrices de incidencia booleana ($I, C^+, C^-$).

## Cuándo interviene
Durante el parsing de entrada (`s_expressions.py`), la ingesta de premisas y la construcción de rutas de consulta.

## Dónde reside
En la capa de interpretación de superficie (`src/operational_model/language/`), conectando parsers como SHRDLU con el kernel matricial.

## Para qué / Para quién
Para el sistema de ingesta y para el desarrollador, facilitando la expresión de hechos y reglas de forma legible pero rígidamente estructurada.
