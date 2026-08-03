---
topic: owl-feeder
use_when: Para documentar la inyección de ontologías OWL en el Hipertensor.
id: atom-owlfeeder
title: OWLFeeder
five_wh_one_plus: what
tags:
- system:matrix
---
# OWLFeeder

**Categoría Padre:** [[Parsers_y_Runtimes]]
**Relaciones 5W1H+:**
* [implements:: [[MatrixFeeder]]]
* [uses:: [[Parser_OWL2Matrix]]]
* [populates:: [[Hipertensor_Canonico]]]

## Qué es
Implementación del `MatrixFeeder` especializada en la ingesta, canonización y traducción de tripletas RDF y axiomas OWL 2 (Description Logic) a coordenadas hiper-matriciales.

## Por qué es necesario
Permite importar la vasta infraestructura global de la Web Semántica. Abandona la ejecución basada en motores de resolución lentos al convertir rígidamente los grafos en productos tensoriales estáticos evaluables instantáneamente en la matriz.

## Cómo funciona
1. **Declaración de Topología (`feed_schema`):** Parsea IRIs y declara identidades únicas, generando los vectores base del tensor ($L_x, L_y$).
2. **Traducción de Axiomas (`feed_rules`):**
   * Transforma relaciones como `rdfs:subClassOf(A, B)` en una implicación directa enviada al `RuleMatrixCompiler`.
   * El Compilador reduce esto a un Mintermo direccional en la Matriz de Incidencia $I$, tal que $A \implies B$.
   * Reglas de dominios y rangos (`rdfs:domain`) se traducen en restricciones espaciales en la máscara de sentido $S_i$.
3. **Aserciones Empíricas (`feed_facts`):** Escribe el tejido de hechos (ABox) directamente como encendidos binarios en el bloque relacional correspondiente de $V_i$.

## Cuándo interviene
Durante el aprovisionamiento estructural inicial de un $W_i$, consumiendo archivos estáticos (`.owl`, `.ttl`) para establecer las reglas del juego.

## Dónde reside
En la familia de conectores de `Parsers_y_Runtimes`, sirviendo de puente estricto W3C-to-MEEL.

## Para qué / Para quién
Para heredar modelos de mundo estandarizados en la industria, asegurando que su inferencia proceda por álgebra de Boole nativa en lugar de algoritmos iterativos.
