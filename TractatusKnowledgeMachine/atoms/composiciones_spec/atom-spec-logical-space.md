topic: atom-spec-logical-space
id: atom-spec-logical-space
title: Spec de LogicalSpace (JAX Era)

# Spec de LogicalSpace (JAX Era)

El `LogicalSpace` es el registro central (Registry) que actúa como puente entre la semántica humana (símbolos, strings, URIs) y el álgebra matricial de alto rendimiento (ejes e índices tensoriales en JAX).

## Responsabilidades Principales
1. **Mapeo Bidireccional $O(1)$:** Traduce conceptos (ej. "Llueve", "Regla_14") a coordenadas enteras para que el `CanonicalHypertensor` pueda procesarlos, y viceversa para presentar resultados al usuario.
2. **Control Dimensional (Shape Management):** Administra los límites y el tamaño de los tensores. Cuando el Feeder descubre una nueva proposición, el `LogicalSpace` registra el índice y actúa como fuente de verdad para que el `CanonicalHypertensor` asigne memoria.
3. **Desacoplamiento Absoluto:** Asegura que ni un solo string o metadato semántico contamine la capa matemática (VRAM/JAX), manteniendo las matrices de JAX puramente numéricas y eficientes.

## Contexto Semántico (6D)
- **WHO**: Consumido agresivamente por el `RuleMatrixCompiler` (para codificar la entrada a índices) y el `MEELEngine` (para decodificar la salida matemática a respuestas legibles).
- **WHAT**: Implementado como un Registry in-memory (Hash Maps bi-direccionales de alto rendimiento).
- **WHERE**: Se ejecuta en el Nodo de Aplicación (Python CPU), sin tocar el acelerador de hardware (GPU/TPU).
- **WHEN**: Se muta durante la fase de Ingesta (registro de axiomas) y se lee intensivamente durante la fase de Consulta (Deducción).
- **HOW**: Usando diccionarios de Python o árboles Radix, garantizando traducciones simbólicas sin overhead computacional.
