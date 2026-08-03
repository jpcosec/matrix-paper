# Resumen de Artículo Relacionado #7

**Título:** *DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models*  
**Autores:** Yung-Sung Chuang, Yujia Xie, Hongyin Luo, Yoon Kim, James Glass, Pengcheng He (MIT, Microsoft)  
**Publicado en:** ICLR 2024  
**Archivo PDF Local:** `paper7_iclr2024_2309_03883.pdf`

---

## 1. Resumen Ejecutivo
Presenta **DoLa** (*Decoding by Contrasting Layers*), una estrategia de decodificación que reduce alucinaciones contrastando las probabilidades de salida de capas superiores e inferiores en transformers.

---

## 2. Hallazgos Principales
- **Localización Layer-wise de Hechos:** El conocimiento factual se concentra principalmente en las capas finales de la red, mientras que las capas intermedias procesan gramática y sintaxis.
- **Limitación del Muestreo Continuo:** Aunque la decodificación contrastiva mejora la precisión factual, sigue dependiendo de funciones suaves de distribución de probabilidad, sin poder garantizar la ausencia total de alucinaciones.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Muestra que modificar el algoritmo de decodificación sobre distribuciones continuas alivia los síntomas pero no elimina el problema de raíz, sirviendo de puente para proponer la decodificación restringida por la máscara booleana $S_i$ (*Masked Logit Decoding*).
- **Cita Sugerida para el Paper:**
  > *"Chuang et al. (2024) demonstrate that factual knowledge is localized in higher transformer layers, but decoding optimizations over continuous logits remain vulnerable without hard symbolic constraints."*
