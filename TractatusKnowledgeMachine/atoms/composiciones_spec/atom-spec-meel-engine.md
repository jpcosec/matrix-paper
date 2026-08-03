---
id: atom-spec-meel-engine
title: Spec del MEELEngine
target_system: MEELEngine
spec_type: API de Software y Orquestación Lógica
atom_count: 3
tags:
- system:matrix
---

# Spec del MEELEngine

## Componente/Sistema Objetivo

La fachada de alto nivel `MEELEngine` en Python, diseñada para orquestar la interacción del usuario o de otros agentes (ej. LLMs o SHRDLU) con el `CanonicalHypertensor`. Provee semántica de lógica proposicional (Assert, Deduce, Query) sobre el álgebra geométrica de JAX.

## Tipo de Especificación

Especificación de Interfaz de Programación (API) de Python.

## Cadena de Átomos Fundacionales

1. [[Inferencia_Deductiva_Matricial]]
2. [[Multiplicacion_Matricial_Booleana_y_Clausura_Transitiva]]
3. [[02_query_como_proyeccion_tensorial]]

## Detalle de la Especificación

El engine se inicializa acoplando el `LogicalSpace` (el diccionario $O(1)$) y el `CanonicalHypertensor` (el tensor físico).

- `deduce()`: No recorre ningún árbol lógico; implementa una operación de *Multiplicación Matricial Booleana* (producto Hadamard/Cruz) hasta alcanzar la convergencia, materializando la *Clausura Transitiva Matricial*.
- `query()`: Tampoco recorre relaciones. Aplica el teorema de *Proyección Tensorial*, multiplicando el estado del mundo $V_i$ por una máscara (creada a partir de los parámetros de búsqueda del query) y verificando la condición residual.

Toda la API debe tener validaciones de tipado estricto (`TypeState`) para evitar que el usuario ingrese datos no representables lógicamente, encapsulando completamente JAX detrás del motor.
