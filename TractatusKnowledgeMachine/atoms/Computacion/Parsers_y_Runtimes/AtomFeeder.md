---
topic: atom-feeder
use_when: Para inyecciones pragmáticas y atómicas directas al espacio hiper-matricial.
id: atom-atomfeeder
title: AtomFeeder
five_wh_one_plus: what
tags:
- system:matrix
---
# AtomFeeder

**Categoría Padre:** [[Parsers_y_Runtimes]]
**Relaciones 5W1H+:**
* [implements:: [[MatrixFeeder]]]
* [populates:: [[Hipertensor_Canonico]]]

## Qué es
La implementación de alto rendimiento del `MatrixFeeder`, encargada de inyectar proposiciones atómicas, hechos singulares puros e identidades base de forma aislada, evitando la latencia de cualquier proceso de parseo profundo.

## Por qué es necesario
Cuando la información ya ha sido destilada a unidades lógicas indivisibles (datos relacionales, flujos de sensores), aplicar gramáticas abstractas o ASTs genera un overhead inaceptable. `AtomFeeder` provee un pasaje $O(1)$ sin fricción hacia la matriz.

## Cómo funciona
1. **Traducción Espacial Directa:** Resuelve inmediatamente los símbolos dados a sus vectores espaciales $L_x, L_y$ en el diccionario canónico.
2. **Micro-Compilación Minterm:** Esquiva el análisis recursivo del `RuleMatrixCompiler`. El propio `AtomFeeder` localiza el Mintermo trivial asociado a la tupla lógica aislada.
3. **Inyección en $V_i$ e $I$:** Para un hecho, se enciende la coordenada directamente en la Matriz Veritativa $V_i$. Si es un átomo de implicación simple, impacta el bit correspondiente en la Matriz de Incidencia $I$.

## Cuándo interviene
Durante ráfagas asíncronas de datos (Streaming Ingestion), telemetría, o cuando un componente enriquece la base de hechos en un solo pulso sin dependencias sintácticas.

## Dónde reside
Al borde de las interfaces de ingesta de bajo nivel dentro de `Parsers_y_Runtimes`.

## Para qué / Para quién
Proporciona eficiencia extrema y latencia mínima a sistemas que necesitan poblar el modelo de mundo matricial masivamente sin negociar costosas capas semánticas.
