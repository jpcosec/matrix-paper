---
topic: prototipo-shrdlu
use_when: Aplicable al contexto semantico y factual de Prototipo SHRDLU.
do_not_use_when: No utilizar fuera del dominio formal de parsers-runtimes.
id: atom-prototipo-shrdlu
title: Prototipo SHRDLU
five_wh_one_plus: what
tags:
- system:matrix
---
# Prototipo SHRDLU y Lowering de Lenguaje Controlado

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Signo_vs_Simbolo]]]
* [implements:: [[S_Expressions]]]
* [is_solved_by:: [[Modelo_SMG]]]
* [is_solved_by:: [[Multiplicacion_Matricial_Booleana_y_Clausura_Transitiva]]]

---

## Qué es
Es la capa cliente prototípica inspirada en el sistema SHRDLU de Terry Winograd que parsea inglés controlado (*Controlled English*), construye *Semantic Frames* y los desciende (*lowering*) a expresiones relacionales $S$-Expressions y operaciones del runtime de Matrix.

## Por qué es necesario
Demuestra la capacidad de la arquitectura Matrix para actuar como el sustrato lógico determinista de interfaces conversacionales en lenguaje natural, resolviendo anáforas y manteniendo referencias situacionales sin depender de alucinaciones neuronales.

## Cómo funciona
1. **Lexicón Estructurado (`lexicon.py`):** Mapea sintagmas simples y multi-palabra (`pick up`, `on top of`, `red block`).
2. **Parser de Inglés Controlado (`english_parser.py`):** Genera *Semantic Frames* (`ImperativeFrame`, `QueryFrame`, `EntityDescriptor`).
3. **Estado de Diálogo (`dialog_state.py`):** Mantiene la pila de enfoque de objetos (*referents*) para resolver anáforas como *"it"* o *"that block"*.
4. **Lowering (`lowering.py`):** Traduce las intenciones de los frames a S-Expressions `(assert wigame:scene (on red-block blue-cube))` o consultas `(check ...)`.

## Cuándo interviene
Durante la interacción entre el usuario (vía texto en lenguaje natural) y el motor relacional de Matrix.

## Dónde reside
En la carpeta `prototypes/shrdlu/` (`proto.py`, `lowering.py`, `english_parser.py`, `lexicon.py`).

## Para qué / Para quién
Proporciona la prueba de concepto ejecutable de que el lenguaje natural puede ser proyectado rígidamente hacia coordenadas de espacios lógicos $W_i$.
