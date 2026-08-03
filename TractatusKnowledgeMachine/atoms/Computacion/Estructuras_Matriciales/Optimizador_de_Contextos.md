---
topic: context-optimization
use_when: Para referenciar el algoritmo de estructuración e inserción jerárquica de
  Contextos.
id: atom-optimizador-de-contextos
title: Optimizador de Contextos
five_wh_one_plus: what
tags:
- system:matrix
---
# Optimizador de Contextos (Ruteo de Máxima Entropía)

**Categoría Padre:** [[Estructuras_Matriciales]]
**Relaciones 5W1H+:**
* [optimizes:: [[Ruteo_Como_Relacion]]]
* [implemented_by:: [[MatrixFeeder]]]
* [applies:: [[Teorema_Suboptimizabilidad_Diagonal]]]

## Qué es
Es el algoritmo utilizado durante la ingesta de conocimiento para determinar el "mejor orden" y jerarquía estructural de los nodos de ruteo (`Context`). 

## Por qué es necesario
Si los contextos se insertan de forma plana y mutuamente ortogonal, la matriz de ruteo $WC_i$ colapsa en una forma casi diagonal. Según el Teorema de Suboptimizabilidad Diagonal, esto destruye la energía de información del sistema ($E(R) 	o 0.5$) y genera una explosión espacial en la memoria $\mathcal{O}(N^2)$.

## Cómo funciona
El Optimizador estructura los contextos jerárquicamente simulando un árbol de búsqueda binaria o particionamiento k-d tree. El objetivo es que cada salto de ruteo (cada dimensión del contexto) actúe como un bit de Entropía de Shannon perfecto ($H=1$), dividiendo el espacio de búsqueda restante en subconjuntos equiprobables. Esto comprime el costo de ruteo a $\mathcal{O}(N \log_2 N)$ y maximiza la densidad informativa de los bloques locales ($E(R) 	o 0.75$).
