---
topic: wigame-contexto-desambiguacion
use_when: Para razonar sobre la identidad de un WiGame, el rol constitutivo del contexto,
  y la desambiguacion de simbolos por acumulacion de contextos.
do_not_use_when: No utilizar para describir el almacenamiento fisico de hechos (usar
  [[Hipertensor_Canonico]]) ni para la logica interna de una sola proposicion (usar
  [[WiGame_Wi]]).
id: atom-wigame-contexto-desambiguacion
title: WiGame Contexto y Desambiguacion
five_wh_one_plus: what
tags:
- system:matrix
---
# WiGame, Contexto y Desambiguación

**Categoría Padre:** [[Modelos_Datos_MEEL]]
**Relaciones 5W1H+:**
* [defines:: [[WiGame]]]
* [defines:: [[Contexto_Logico]]]
* [defines:: [[Emergencia_Estructural_de_Si_en_Cruces_de_Contexto]]]
* [implements:: [[Capa_Sentido_Si]]]
* [is_solved_by:: [[Juego_de_Desambiguacion]]]
* [mathematically_proves:: [[Colapso_Dimensional]]]
* [restricts:: [[Hipertensor_Canonico]]]

---

## Qué es
Es la tesis estructural de que un `WiGame` **no** es un par de ejes bajo una relación, sino ese mismo par de ejes **bajo un contexto**. La relación fija la forma de jugada `(R a b)`; los ejes fijan qué términos pueden ocupar cada posición; el contexto fija *qué jugadas admisibles tienen sentido y valor aquí*.

Dos WiGames con los mismos ejes y la misma relación pero distinto contexto **no son el mismo objeto**.

## Por qué es necesario
Sin el contexto como parte de la identidad del WiGame, el sistema solo puede representar un espacio plano donde todo término es homónimo de todo término con el mismo signo. Eso hace imposible distinguir `she@marie_curie` de `she@rosalind_franklin`, y convierte la acumulación de información en acumulación de ambigüedad.

El contexto es además lo que hace computable el espacio: refina las coordenadas admisibles en lugar de explotar dimensionalmente.

## Cómo funciona
1. **Sentido local:** `Si` es la máscara de admisibilidad del contexto. `unsinnig` significa "fuera de este contexto", no "falso". Un signo como `she` es `sinnvoll` en `ctx:marie_curie` y `unsinnig` donde el referente nunca fue introducido.
2. **Árbol de contextos:** `Context` rutea a subcontextos (`ContextRoute` con `target_kind=CONTEXT`) o a hojas `WiGame` (`target_kind=WIGAME`). El refinamiento contextual agrega restricciones.
3. **Desambiguación acumulativa:** cada contexto nuevo aporta restricciones; cada hecho es una pregunta de split sobre el campo semántico. El referente es la intersección que sobrevive a todos los contextos. El signo deja de importar: importa la hoja/ruta donde convergen las ocurrencias.
4. **Identidad entre contextos:** `RoutingProjection` vincula ejes de sujetos de dos WiGames. La proyección es no vacía solo si comparten un referente canónico. Decidir que dos ocurrencias denotan el mismo referente es una decisión revisada, no una normalización automática del string.
5. **Refinamiento o discriminación:** cuando dos entidades colisionan en todas las propiedades mapeadas, se aplica [[Juego_de_Desambiguacion]]: inyectar una dimensión discriminativa `D_i` o crear un subcontexto hijo `W_i'` ajustando `Si`.

## Cuándo interviene
Al crear o indexar WiGames (el `context_id` es obligatorio como parte de la identidad), al cruzar coordenadas de distintos contextos, al resolver consultas ambiguas, y al decidir si dos ocurrencias del mismo signo son el mismo referente.

## Dónde reside
En `WiGame.context_id`, en el grafo `Context`/`ContextRoute`, en `RoutingProjection`, y en los índices de ocurrencias por contexto. Los hechos viven en el [[Hipertensor_Canonico]]; el WiGame es su proyección local bajo contexto.

## Para qué / Para quién
Para que la KB pueda crecer indefinidamente sin colapsar contextos: más información estrecha el referente en lugar de multiplicar homónimos, y la respuesta a "¿qué significa este símbolo?" pasa a ser "la hoja donde converge", no "el string".
