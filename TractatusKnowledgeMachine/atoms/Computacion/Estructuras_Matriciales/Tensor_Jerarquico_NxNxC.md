---
topic: tensor-jerarquico-nxnxc
use_when: Aplicable al contexto semantico y factual de Tensor Jerarquico NxNxC.
do_not_use_when: No utilizar fuera del dominio formal de block-matrix.
id: atom-tensor-jerarquico-nxnxc
title: Tensor Jerarquico NxNxC
five_wh_one_plus: what
tags:
- system:matrix
---
# Tensor Jerárquico (N x N x C^k)

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [is_solved_by:: [[Enrutamiento_Jerarquico]]]
* [is_solved_by:: [[Matrices_Puras]]]
* [is_solved_by:: [[Matrices_y_Tensores]]]
* [is_solved_by:: [[Representacion_Plana_vs_Tensorial]]]

---

## Qué es
La evolución del espacio lógico hacia una estructura multidimensional donde cada nivel de la jerarquía conceptual (ej. Objetos > Comidas > Italiana > Pizza) añade una nueva dimensión tensorial ($C_1, C_2, C_k$). El tensor final tiene una forma $N \times N \times C_1 \times C_2 \times \dots \times C_k$.

## Por qué es necesario
Permite que el sistema sea infinitamente recursivo y jerárquico. Cada nivel de "abstracción" es una dimensión que filtra el espacio de búsqueda, permitiendo que el motor maneje billones de hechos fragmentados en contextos manejables sin colapsar.

## Cómo funciona
Funciona como un sistema de **direccionamiento por capas**. Si queremos llegar a los hechos sobre la pizza:
1. La dimensión $C_{objetos}$ selecciona la región de "Comidas".
2. La dimensión $C_{comidas}$ selecciona la región de "Italiana".
3. La dimensión $C_{italiana}$ selecciona el contexto "Pizza".
4. Finalmente, se accede a la matriz $N \times N$ de hechos específicos (ej. ingredientes).
Matemáticamente, es una cadena de proyecciones donde cada coordenada en una dimensión superior actúa como el selector de la "rebanada" (slice) en la dimensión inferior.

## Cuándo interviene
Siempre que se realiza una consulta que requiere navegación ontológica o descendencia en el árbol de conocimiento.

## Dónde reside
En la arquitectura de direccionamiento tensorial del motor de alto nivel.

## Para qué / Para quién
Para el motor de ruteo, permitiendo que la "dirección" de un hecho sea su ruta completa en el árbol jerárquico.

