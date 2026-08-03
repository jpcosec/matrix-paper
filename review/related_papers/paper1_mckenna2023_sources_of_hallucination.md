# Resumen de Artículo Relacionado #1

**Título:** *Sources of Hallucination by Large Language Models on Inference Tasks*  
**Autores:** Nick McKenna, Tianyi Li, Liang Cheng, Mohammad Javad Hosseini, Mark Johnson, Mark Steedman (University of Edinburgh, Google Research, Macquarie University)  
**Publicado en:** EMNLP 2023 (Findings)  
**Archivo PDF Local:** `paper1_emnlp2023_182.pdf`

---

## 1. Resumen Ejecutivo
Este estudio investiga las causas fundamentales de las alucinaciones en modelos de lenguaje (LLMs) durante tareas de inferencia lógica (NLI), preguntas y respuestas (QA) y resumen de textos. Los autores demuestran empíricamente que las alucinaciones no son errores aleatorios, sino el resultado directo de sesgos de coinserción en los datos de preentrenamiento y la incapacidad de las representaciones continuas de preservar restricciones deductivas formales.

---

## 2. Hallazgos Principales
- **Falla en Tareas de Inferencia (NLI):** Los LLMs tienden a alucinar premisas no sustentadas cuando las palabras clave de la conclusión tienen alta coocurrencia en el corpus de preentrenamiento, priorizando la asociación léxica continua por encima de la validez deductiva.
- **Incapacidad de Acotar Limites Lógicos:** Los vectores de activación continuos suavizan las fronteras entre proposiciones válidas e inválidas, haciendo que el modelo genere oraciones semánticamente plausibles pero formalmente falsas.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Respalda directamente la postura de *tractatusBIt*: la alucinación es un problema estructural de representación. La asociación estadística en embeddings continuos no puede reemplazar la verificación binaria de sentido ($S_i$) y verdad ($V_i$).
- **Cita Sugerida para el Paper:** 
  > *"As shown by McKenna et al. (2023), LLMs consistently hallucinate on inference tasks because continuous vector associations prioritize lexical co-occurrence over formal deductive constraints."*
