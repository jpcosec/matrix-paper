---
topic: feeder
use_when: Para referenciar el protocolo abstracto de ingesta de conocimiento al Hipertensor.
id: atom-matrixfeeder
title: MatrixFeeder
five_wh_one_plus: what
tags:
- system:matrix
---
# MatrixFeeder (Abstract Ingestion Protocol)

**Categoría Padre:** [[Parsers_y_Runtimes]]
**Relaciones 5W1H+:**
* [populates:: [[Hipertensor_Canonico]]]
* [is_implemented_by:: [[SExprFeeder]]]
* [is_implemented_by:: [[OWLFeeder]]]
* [is_implemented_by:: [[AtomFeeder]]]

## Qué es
Es un contrato abstracto (Protocol / Abstract Base Class) que estandariza cómo cualquier fuente de conocimiento externo se compila inyecta en el motor de Matrix. No guarda estado propio.

## Por qué es necesario
Para evitar el "Bypass Arquitectónico". Antes, formatos como OWL se forzaban a pasar por S-Expressions antes de llegar al motor, lo que generaba un embudo y pérdida de control tipológico. El Feeder garantiza que todo parser hable el mismo idioma matricial directo.

## Cómo funciona
Define una interfaz universal con tres responsabilidades estrictas:
1. `feed_schema`: Declarar los ejes del dominio ($L_i$) resolviendo los IDs de `Symbol` y `Relation`.
2. `feed_rules`: Compilar restricciones estructurales y lógicas de sentido ($S_i$).
3. `feed_facts`: Inyectar aserciones empíricas puras directo en las coordenadas correspondientes del `Hipertensor_Canonico`.
