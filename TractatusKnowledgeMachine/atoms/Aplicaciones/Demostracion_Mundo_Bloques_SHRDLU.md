---
topic: shrdlu-dialogue-poc
use_when: Aplicable a la demostracion de dialogo en lenguaje natural y razonamiento
  espacial sobre el mundo de bloques SHRDLU.
do_not_use_when: No utilizar fuera del contexto de interaccion en lenguaje natural
  o lowering de SHRDLU.
id: atom-demostracion-mundo-bloques-shrdlu
title: Demostracion Mundo Bloques SHRDLU
five_wh_one_plus: what
tags:
- system:matrix
---
# Demostración de Prueba de Concepto: Mundo de Bloques SHRDLU

**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_language_shrdlu_lowering_py]]]
* [implements:: [[Source_Code_src_operational_model_language_shrdlu_english_parser_py]]]
* [is_solved_by:: [[Prototipo_SHRDLU]]]
* [grounded_by:: [[Source_PDF_winograd1972shrdlu_pdf]]]

---

## Qué es
Es la prueba de concepto de diálogo interactivo en lenguaje natural y razonamiento espacial sobre el universo de bloques de Terry Winograd (`test_shrdlu_dialog.py`, `test_shrdlu_english_parser.py`).

---

## Mecanismo
Convierte comandos en inglés natural (*"the red block is on the green pyramid"*) mediante el parser de lowering a S-Expressions, verificando las relaciones espaciales y condiciones de verdad ($V_i$) sobre la matriz Booleana sin alucinaciones.

---

## Código Ejecutable de Referencia
* Parser de Lowering: `src/operational_model/language/shrdlu_lowering.py`
* Pruebas Pytest: `tests/test_shrdlu_dialog.py`, `tests/test_shrdlu_english_parser.py`
