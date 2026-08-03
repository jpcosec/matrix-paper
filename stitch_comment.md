# Proyecto: paper_v2 - Editorial Column Browser

## Visión General
paper_v2 es una herramienta de autoría y validación lógica para papers académicos. No es un editor de texto plano; es un entorno de composición donde el contenido se estructura en "átomos" lógicos (Secciones > Párrafos > Notas > Fuentes).

## Arquitectura de la Interfaz (Desktop Focus)
La interfaz se basa en un sistema de **Columnas Editoriales (Pliegos)** que eliminan la estética de "base de datos CRUD" en favor de una experiencia de lectura y edición profunda.

1. **Panel de Manuscrito (Izquierda):** Navegador global y anclaje visual del argumento completo.
2. **Columna de Sección:** Contexto jerárquico y metadatos de alto nivel.
3. **Columna de Párrafo:** El núcleo narrativo. Tipografía Serif (Playfair Display), espaciado generoso y enfoque en el texto como documento físico.
4. **Columna de Notas/Fuentes:** Capas de validación lógica ancladas a cada párrafo.

## Sistema de Diseño: "Paper v2"
- **Paleta:** Tonos cálidos de papel (`#FAF8FF`), contrastes suaves en superficies (`#F2F3FF`) y acentos críticos para validación.
- **Tipografía:** Playfair Display para el cuerpo del paper (autoridad editorial) y fuentes UI funcionales para metadatos.
- **Estado de Validación:** Badges de "Missing" o "Needs Citation" diseñadas para romper la limpieza del papel y exigir rigor lógico.

## Modelo de Datos
- **Compositional Anchoring:** Cada bloque de texto está anclado a un documento de composición.
- **Trazabilidad:** Relación estricta entre una afirmación (párrafo), su intención lógica (nota) y su evidencia (fuente).

## Estado Actual
Hemos evolucionado de un formulario genérico a una interfaz de columnas expandibles en escritorio que permite ver la trazabilidad completa del argumento sin perder el foco en el texto.
