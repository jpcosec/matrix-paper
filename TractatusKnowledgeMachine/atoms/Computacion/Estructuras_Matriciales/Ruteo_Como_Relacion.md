---
topic: routing
use_when: Para referenciar el mecanismo de navegación entre Contextos y WiGames.
id: atom-ruteo-como-relacion
title: Ruteo Como Relacion
five_wh_one_plus: what
tags:
- system:matrix
---
# Ruteo Como Relación (Omnirepresentación del Grafo)

**Categoría Padre:** [[Estructuras_Matriciales]]
**Relaciones 5W1H+:**
* [represented_in:: [[Hipertensor_Canonico]]]
* [unifies_with:: [[Proyeccion_Tensorial]]]

## Qué es
Es el principio arquitectónico que establece que **el Enrutamiento no es una capa de orquestación externa**, sino conocimiento formal representable dentro del mismo sistema. Los `Context` y `WiGame` son simplemente `Symbol`s, y las flechas de ruteo (`routes_to`, `contains`) son simplemente `Relation`s.

## Por qué es fundamental
Si el ruteo fuera externo, necesitaríamos dos bases de datos y dos motores lógicos (uno para buscar contextos y otro para buscar hechos). Al unificarlo, la matriz de ruteo $WC_i$ (Top-Left de la BlockMatrix) se extrae utilizando exactamente la misma **Proyección Tensorial** que se usa para extraer hechos empíricos.

## Cómo funciona
Una regla de ruteo como "El Contexto Biología apunta al WiGame de Evolución" se inyecta en el Hipertensor como una aserción canónica pura:
`(routes_to ctx:biologia wigame:evolucion)`
Para enrutar, el motor simplemente hace una Proyección Tensorial sobre la relación `routes_to`. El sistema es fractal; su propia infraestructura es evaluable como verdad/falsedad matricial.
