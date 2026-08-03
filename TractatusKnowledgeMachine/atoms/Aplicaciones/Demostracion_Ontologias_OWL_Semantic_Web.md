---
topic: owl-parser-poc
use_when: Aplicable a la demostracion de ingesta de ontologias OWL (RDF/XML) y razonamiento
  del Semantic Web.
do_not_use_when: No utilizar fuera del dominio de ontologias formales OWL/RDF.
id: atom-demostracion-ontologias-owl-semantic-web
title: Demostracion Ontologias OWL Semantic Web
five_wh_one_plus: what
tags:
- system:matrix
---
# Demostración de Prueba de Concepto: Ontologías OWL & Semantic Web

**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_language_owl2matrix_py]]]
* [implements:: [[tests/test_owl2matrix.py]]]
* [is_solved_by:: [[Parser_OWL2Matrix]]]
* [mathematically_proves:: [[Multiplicacion_Matricial_Booleana_y_Clausura_Transitiva]]]

---

## Qué es
Es la prueba de concepto de ingesta e inferencia sobre ontologías complejas de la Web Semántica escritas en RDF/XML OWL (`owl2matrix.py`, `test_owl2matrix.py`).

---

## Mecanismo
Parsea clases OWL, propiedades de objetos, individuos nombrados y jerarquías `subClassOf` — contenido **ya estandarizado** que omite la etapa de descomposición — traduciéndolos a S-Expressions canónicas (proposiciones candidato) que se validan por el chequeo de sentido en dos pasos antes de materializarse en la estructura $V_i, S_i$ de `LogicalSystem`.

---

## Código Ejecutable de Referencia
* Parser OWL: `src/operational_model/language/owl2matrix.py`
* Pruebas Pytest: `tests/test_owl2matrix.py` (2 tests passing en 0.18s)
