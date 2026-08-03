---
topic: anclaje-simbolos-grounding
use_when: Aplicable al contexto semantico y factual de Anclaje Simbolos Grounding.
do_not_use_when: No utilizar fuera del dominio formal de parsers-runtimes.
id: atom-anclaje-simbolos-grounding
title: Anclaje Simbolos Grounding
five_wh_one_plus: what
tags:
- system:matrix
---
# Anclaje de Símbolos (Symbol Grounding)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Signo_vs_Simbolo]]]
* [is_solved_by:: [[Politica_Simbolos_Kernel]]]
* [is_solved_by:: [[Grafo_Indice_G]]]
* [is_solved_by:: [[Hecho_Atomico_CDV]]]

---

## Qué es
Es el proceso de mapear signos perceptibles (tokens de texto, cadenas de caracteres o identificadores externos) a símbolos unificados y normalizados dentro del catálogo del sistema.

## Por qué es necesario
Previene la duplicación y ambigüedad de conceptos (ej. "drei", "3", "tres" apuntando a diferentes identificadores) y gestiona la unificación mediante la meta-relación `equivalent` y el tipado `instance`.

## Cómo funciona
1. **Normalización de Nombres (`Name`):** Asigna el signo lingüístico al catálogo del sistema.
2. **Asignación de Símbolo (`Symbol`):** Mapea el signo a una coordenada $L_i$.
3. **Unificación via Kernel (`equivalent`):** Pliega alias y sinónimos a un único representante canónico.

## Cuándo interviene
Durante el registro de entidades (`register_thing`), parsing de entradas y resolución de referencias.

## Dónde reside
En el catálogo de registro del núcleo (`logical_system_registry.py`) y en los espacios de símbolos (`symbol_spaces.py`).

## Para qué / Para quién
Asegura que el cálculo matricial booleano opere sobre dimensiones unificadas y sin colisiones de nombres.
