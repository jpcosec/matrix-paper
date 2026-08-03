---
topic: sexpr-feeder
use_when: Para documentar la inyección de expresiones simbólicas al motor MEEL.
id: atom-sexprfeeder
title: SExprFeeder
five_wh_one_plus: what
tags:
- system:matrix
---
# SExprFeeder

**Categoría Padre:** [[Parsers_y_Runtimes]]
**Relaciones 5W1H+:**
* [implements:: [[MatrixFeeder]]]
* [uses:: [[S_Expressions]]]
* [populates:: [[Hipertensor_Canonico]]]

## Qué es
Implementación de `MatrixFeeder` para la captura y decodificación de S-Expressions LISP-like, operando como la interfaz canónica e intermedia entre abstracciones dinámicas y el sistema matricial.

## Por qué es necesario
Las S-Expressions ofrecen una representación funcional pura libre de ambigüedad gramatical. Proveen un acoplamiento perfecto para serializar reglas dinámicas estructuradas permitiendo su absorción directa en un esquema rígido.

## Cómo funciona
1. **Despliegue del AST Lógico:** Expande el árbol sintáctico (ej. `(Implies (And P Q) R)`).
2. **Reducción de Aridad:** Transforma los nodos del árbol en un grafo dirigido de literales booleanos.
3. **Inyección vía Compilador:** Pasa el grafo resultante al `RuleMatrixCompiler`.
   * El compilador reduce el AST de la expresión a Formas Canónicas (Mintermos).
   * Modifica la Matriz de Incidencia $I$, asignando a cada variable de la S-Expression su respectiva dimensión ortogonal y asegurando que la evaluación se vuelva un producto lógico matricial $O(1)$.

## Cuándo interviene
En el tránsito dinámico (Etapa 3 del pipeline de ingesta), transformando abstracciones o deducciones en reglas rígidamente estructuradas listas para su solidificación.

## Dónde reside
En el núcleo de `Parsers_y_Runtimes`.

## Para qué / Para quién
Para el razonamiento intermedio y agentes que requieren inyectar constructos lógicos complejos dentro de las fronteras de un $W_i$ de manera determinista.
