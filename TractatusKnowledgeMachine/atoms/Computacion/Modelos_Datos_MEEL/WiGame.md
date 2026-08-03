---
topic: wigame
use_when: Para referenciar una partición local o juego de lenguaje evaluable.
id: atom-wigame
title: WiGame
five_wh_one_plus: what
tags:
- system:matrix
---
# WiGame (Juego de Lenguaje)

**Categoría Padre:** [[Modelos_Datos_MEEL]]
**Relaciones 5W1H+:**
* [is_projection_of:: [[Hipertensor_Canonico]]]
* [contains:: [[Capa_Verdad_Vi]]]
* [contains:: [[Capa_Sentido_Si]]]
* [implements:: [[Source_Code_src_operational_model_system_wigame_py]]]

## Qué es
Es un juego de lenguaje local o partición de evaluación. A diferencia del diseño legacy, un WiGame **no almacena hechos propios**. Es estrictamente una proyección (vista/slice) del `Hipertensor_Canonico`.

## Por qué es necesario
Permite aislar contextualmente las evaluaciones matriciales de Modus Ponens ($v \otimes I^*$). En vez de operar sobre todo el universo, se extrae una sub-matriz específica para los ejes ($L_i$) de interés.

## Cómo funciona
Se define por `axis_a` (dominio), `axis_b` (codominio) y una `relation`. Al instanciarse, realiza una consulta al Hipertensor Canónico para materializar sus matrices densas $V_i$ y $S_i$ en JAX para inferencia rápida.
