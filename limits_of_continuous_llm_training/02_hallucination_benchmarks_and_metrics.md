# Benchmarks y Métricas de Evaluación de Alucinaciones en LLMs

Este documento detalla la evidencia empírica recopilada en la literatura reciente sobre la persistencia de las alucinaciones a pesar del escalamiento masivo de parámetros y datos de preentrenamiento.

---

## 1. Evaluación Atómica de Precisión Factual (FActScore)

### Min et al. (2023, EMNLP) — *FActScore*
- **Metodología:** Descompone las respuestas generadas por los LLMs en hechos atómicos individuales $(s, r, o)$ y verifica la veracidad factual de cada hecho frente a bases de datos de referencia.
- **Resultado Clave:** Incluso los modelos de lenguaje más avanzados (GPT-4, LLaMA-2) sufren una degradación dramática en precisión factual cuando las consultas abordan entidades de media o baja frecuencia.

---

## 2. Benchmark de Alucinaciones a Gran Escala (HaluEval)

### Li et al. (2023, EMNLP) — *HaluEval*
- **Metodología:** Un conjunto de datos de 35,000 muestras diseñado para evaluar la detección de alucinaciones en preguntas/respuestas, diálogo y resumen.
- **Resultado Clave:** Los LLMs tienen serias dificultades para distinguir entre respuestas verdaderas y respuestas falsas pero semánticamente similares (alucinaciones de alta verosimilitud).

---

## 3. Detección de Alucinaciones en Caja Negra (SelfCheckGPT)

### Manakul et al. (2023, EMNLP) — *SelfCheckGPT*
- **Metodología:** Mide la inconsistencia estocástica entre múltiples estadios de muestreo del mismo LLM sin acceder a las probabilidades internas de los tokens.
- **Resultado Clave:** La variabilidad entre respuestas confirma que los LLMs generan afirmaciones contradictorias sobre el mismo hecho dependiendo del muestreo estocástico.

---

## 4. Perspectiva Interna del Modelo sobre Alucinaciones

### Orgad et al. (2025, Apple ML / ICLR) — *Language Models Know More Than They Show*
- **Hallazgo:** Los LLMs a menudo "saben" internamente que una respuesta es incierta (reflejado en sus representaciones internas), pero los decodificadores continuos proyectan afirmaciones categóricas falsas.
- **Implicación para Matrix:** La capa de decodificación continua de la red neuronal destruye la señal de incertidumbre; se requiere una máscara de sentido ($S_i$) que bloquee la emisión de proposiciones fuera de dominio.
