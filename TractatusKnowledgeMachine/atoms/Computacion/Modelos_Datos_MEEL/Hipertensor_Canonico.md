---
topic: hypertensor
use_when: Para referenciar la base de datos central (SSOT) de todos los hechos en
  memoria JAX.
id: atom-hipertensor-canonico
title: Hipertensor Canonico
five_wh_one_plus: what
tags:
- system:matrix
---
# Hipertensor Canónico (Facts DB)

**Categoría Padre:** [[Modelos_Datos_MEEL]]
**Relaciones 5W1H+:**
* [acts_as:: [[SSOT_Hechos]]]
* [projected_into:: [[WiGame]]]
* [projected_into:: [[Capa_Verdad_Vi]]]
* [projected_into:: [[Capa_Sentido_Si]]]
* [populated_by:: [[MatrixFeeder]]]

## Qué es
Es la base de datos central y global de todos los hechos conocidos por el sistema. Matemáticamente se comporta como un tensor 3D disperso (Entidades × Relaciones × Entidades) o superior, respaldado en silicio (JAX).

## Por qué es necesario
Para resolver el error arquitectónico de tener hechos almacenados localmente dentro de cada partición (`WiGame`). El Hipertensor centraliza la verdad empírica y el sentido ontológico, permitiendo que las operaciones locales sean simples lecturas/vistas (slices) de la memoria global.

## Cómo funciona
El `MatrixFeeder` inyecta datos exclusivamente aquí. Las dimensiones de este tensor están definidas por los catálogos de `Symbol` y `Relation`. Cada coordenada contiene un `TruthValue`, un `SenseValue` y metadata.
