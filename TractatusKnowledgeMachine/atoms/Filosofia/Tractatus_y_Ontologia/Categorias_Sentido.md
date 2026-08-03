---
topic: categorias-sentido
use_when: Aplicable al contexto semantico y factual de Categorias Sentido.
do_not_use_when: No utilizar fuera del dominio formal de tractarian-philosophy.
id: atom-categorias-sentido
title: Categorias Sentido
five_wh_one_plus: what
tags:
- system:matrix
---
# Categorías de Sentido

**Categoría Padre:** [[Filosofia]]
**Relaciones 5W1H+:**
* [defines:: [[Regla_Dont_Care]]]
* [defines:: [[Mapas_Karnaugh]]]
* [defines:: [[Capa_Sentido_Si]]]

---

## Qué es
Es la clasificación tripartita de las proposiciones según su relación con la lógica y la realidad:
1. **Sinnvoll**: Con sentido (puede ser verdadero o falso).
2. **Sinnlos**: Sin sentido informativo (tautologías y contradicciones).
3. **Unsinnig**: Absurdo (fuera del espacio lógico).

## Por qué es necesario
Permite al sistema descartar automáticamente operaciones imposibles y detectar información redundante o contradictoria antes de procesar la verdad factual.

## Cómo funciona
A través de la interacción entre $V_i$ y $S_i$. Si una coordenada no existe en $L_i$ es *Unsinnig*. Si existe pero $S_i$ es 0 es *Inapplicable*. Si el álgebra booleana la reduce a una verdad universal es *Sinnlos*.

## Cuándo interviene
En cada intento de inyección o consulta de un hecho. Actúa como el primer filtro del motor.

## Dónde reside
En la lógica de evaluación del motor y en las definiciones de la máscara de sentido $S_i$.

## Para qué / Para quién
Para el motor de inferencia y el usuario, proporcionando errores tipados específicos en lugar de fallos genéricos.
