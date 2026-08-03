---
topic: eje-c-mecanismo-conexion-llm-y-shrdlu
use_when: Aplicable al contexto semantico y factual de Eje C Mecanismo Conexion LLM
  y SHRDLU.
do_not_use_when: No utilizar fuera del dominio formal de parsers-runtimes.
id: atom-eje-c-mecanismo-conexion-llm-y-shrdlu
title: Eje C Mecanismo Conexion LLM y SHRDLU
five_wh_one_plus: what
tags:
- system:matrix
---
# Eje C: Mecanismo de Conexión con LLMs e Interfaz SHRDLU

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Prototipo_SHRDLU]]]
* [implements:: [[S_Expressions]]]
* [is_solved_by:: [[Modelo_SMG]]]
* [is_solved_by:: [[Pipeline_Ingesta_Lenguaje_Matrix]]]
* [is_solved_by:: [[Matriz_por_Bloques]]]

---

## Qué es
Es la clarificación explícita de las fases de integración entre el LLM (modelo estocástico de superficie) y el motor Matrix/MEEL (kernel Booleano discreto).

## Arquitectura por Fases
1. **Fase 2 (Implementación Actual Ejecutable):**
   * El LLM (propuesta: **LLM chica**) opera como **Descompositor de Superficie** — etapa 1 del [[Pipeline_Ingesta_Lenguaje_Matrix]]: separa el significado del azúcar sintáctico y lo expresa en una representación estandarizada (S-Expressions canonicalizadas `(assert ...)`, `(check ...)`, RDF/Turtle u OWL), absorbiendo la variabilidad de signos (anclaje y alias plegados aquí). **No toma decisiones lógicas**.
   * El motor **MEEL** recibe las proposiciones candidato y ejecuta el chequeo de sentido en dos pasos (indexación por contexto + contradicción) y las validaciones $S_i$ y $V_i$ de manera inmutable fuera del LLM.
   * Prototipo funcional: `prototypes/shrdlu/` y runtime `SExpressionRuntime`.
2. **Fase 3 (Trabajo Futuro):**
   * Modificación profunda de las máscaras de atención latente y pérdidas intermedias durante el entrenamiento de la red neuronal.

## Inyección en el Paper NeurIPS
Aclarar que la Fase 3 es trabajo futuro y documentar en detalle la Fase 2 actual (LLM como parser de S-Expressions e interfaz SHRDLU).
