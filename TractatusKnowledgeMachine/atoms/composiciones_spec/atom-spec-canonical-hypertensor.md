---
id: atom-spec-canonical-hypertensor
title: Spec del CanonicalHypertensor
target_system: CanonicalHypertensor
spec_type: Arquitectura JAX (Memoria/Tensor)
atom_count: 4
tags:
- system:matrix
---

# Spec del CanonicalHypertensor

## Componente/Sistema Objetivo

La clase `CanonicalHypertensor` es la estructura de datos residente en VRAM (o RAM compartida) que almacena el estado global del "Mundo" para el motor Matrix MEEL. En lugar de objetos Python dispersos, condensa toda la ontología en arreglos multidimensionales (tensores).

## Tipo de Especificación

Especificación de Estructura de Memoria y Backend Físico (JAX).

## Cadena de Átomos Fundacionales

1. [[01_El_Mundo_como_Espacio_Tensor]]
2. [[Capa_Verdad_Vi]]
3. [[Capa_Sentido_Si]]
4. [[Vectorizacion_Bitwise_Densa]]

## Detalle de la Especificación

El hipertensor encapsula físicamente dos constructos tractarianos:
- **La Matriz $V_i$ (Capa_Verdad_Vi)**: Un arreglo disperso o por bloques que almacena variables booleanas indicando qué Mintermos (Hechos Atómicos) son verdaderos en el instante `t`.
- **La Matriz $S_i$ (Capa_Sentido_Si)**: Una máscara topológica inmutable que dictamina qué configuraciones en el hiperespacio tienen *Sentido*. 

El backend debe implementarse sobre `jax.numpy.ndarray` para eludir el Memory Wall de Python iterando sobre grafos, utilizando operaciones bit a bit. La actualización de estado es una operación funcional, donde mutaciones (como un *Assert*) retornan un nuevo estado del tensor validado geométricamente contra la máscara $S_i$. Si $V_{new} \otimes S_i = 0$, se lanza un error de absurdo (`Unsinnig`).
