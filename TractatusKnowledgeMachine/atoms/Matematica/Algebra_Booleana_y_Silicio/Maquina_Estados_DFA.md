---
topic: maquina-estados-dfa
use_when: Aplicable al contexto semantico y factual de Maquina Estados DFA.
do_not_use_when: No utilizar fuera del dominio formal de discrete-math.
id: atom-maquina-estados-dfa
title: Maquina Estados DFA
five_wh_one_plus: what
tags:
- system:matrix
---
# Máquina de Estados DFA Matricial

**Categoría Padre:** [[Matematica]]
**Relaciones 5W1H+:**
* [mathematically_proves:: [[Omnirepresentacion]]]
* [mathematically_proves:: [[Algebra_Booleana]]]

---

## Qué es
La capacidad del motor lógico de comportarse como un Autómata Finito Determinista (DFA) realizando multiplicaciones recursivas de la matriz sobre sí misma ($W^{k+1} = W^k \otimes W^k$).

## Por qué es necesario
Permite introducir mutación de estado y ejecución de reglas lógicas dinámicas sin escribir bucles `if/else` en software, delegando todo al álgebra lineal (hardware).

## Cómo funciona
Si se inyecta un bit en la zona de ruteo de una omnirepresentación, ese bit actúa como regla de transición. Al multiplicar la matriz, la suma booleana propaga ese valor mutando los hechos. El estado es estable (idempotente) si los "don't cares" y la máscara de sentido bloquean la propagación.

## Cuándo interviene
Al ejecutar razonamientos de múltiples saltos o al simular dinámicas cambiantes en un contexto.

## Dónde reside
En el núcleo de ejecución de multiplicaciones tensoriales de [[MEEL]].

## Para qué / Para quién
Para el módulo de inferencia y simulación dinámica del motor lógico.
