---
id: atom-spec-rule-matrix-compiler
title: Spec de Feeders y RuleMatrixCompiler
target_system: RuleMatrixCompiler y Feeders
spec_type: Compilación AOT e Ingesta
atom_count: 3
tags:
- system:matrix
---

# Spec de Feeders y RuleMatrixCompiler

## Componente/Sistema Objetivo

El pipeline de ingesta (`AtomFeeder`, `OWLFeeder`) y su motor de reducción estructural (`RuleMatrixCompiler`). Actúan como el "Driver" que traduce el mundo exterior al lenguaje de Mintermos.

## Tipo de Especificación

Especificación de Compilación AOT (Ahead-of-Time).

## Cadena de Átomos Fundacionales

1. [[Formas_Canonicas_y_Mintermos]]
2. [[Suma_de_Productos_SOP]]
3. [[04_Forma_Logica_como_Matriz_Si]]

## Detalle de la Especificación

El flujo de ingesta obliga a destruir toda la gramática o sintaxis abstracta entrante antes de tocar el hipertensor.
1. Un `MatrixFeeder` serializa la entrada en Cláusulas (por ejemplo de RDF u Ontologías).
2. `RuleMatrixCompiler` reduce la abstracción a *Suma de Productos (SOP)* y mapea cada variable a una coordenada jacobiana (Mintermo).
3. Las reglas lógicas de dominio (ej. "Un gato es un felino") se incrustan (AOT) en la **Matriz $S_i$**. Todo antecedente enciende el vector del consecuente espacialmente. Esto garantiza que la inferencia deductiva durante runtime sea simplemente propagar electricidad booleana por caminos topológicamente prefijados.
