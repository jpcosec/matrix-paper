# Resumen de Artículo Relacionado #4

**Título:** *INSIDE: LLMs’ Internal States Retain the Power of Hallucination Detection*  
**Autores:** Chao Chen, Kai Liu, Ze Chen, Yi Gu, Yue Wu, Mingyuan Tao, Zhihang Fu, Jieping Ye (Alibaba Cloud, Zhejiang University)  
**Publicado en:** ICLR 2024  
**Archivo PDF Local:** `paper4_iclr2024_2402_03744.pdf`

---

## 1. Resumen Ejecutivo
Propone el método **INSIDE**, que analiza las matrices de covarianza y los estados de activación internos de las capas intermedias de los LLMs para detectar alucinaciones de conocimiento sin requerir muestreo externo ni llamadas adicionales al modelo.

---

## 2. Hallazgos Principales
- **Incertidumbre en Capas Internas:** La incertidumbre sobre la veracidad factual no se refleja limpiamente en los logits finales de salida (debido al suavizado de softmax), pero deja huellas en la varianza geométrica de las capas ocultas.
- **Necesidad de Proyección Estructurada:** Medir la incertidumbre en el espacio continuo sin una proyección de subespacio genera falsos positivos.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Demuestra que las capas ocultas continuas almacenan la ambigüedad, pero requieren un marco de proyección (*ProjectionIR* / $V_i, S_i$) para convertir esas señales continuas ruidosas en decisiones de validez deterministas.
- **Cita Sugerida para el Paper:**
  > *"Chen et al. (2024) reveal that while LLM internal states track uncertainty, detecting hallucinations requires structured subspace projections beyond surface logit sampling."*
