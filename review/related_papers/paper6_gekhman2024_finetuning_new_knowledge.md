# Resumen de Artículo Relacionado #6

**Título:** *Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?*  
**Autores:** Zorik Gekhman, Gal Yona, Roee Aharoni, Matan Eyal, Amir Feder, Roi Reichart, Jonathan Herzig (Technion, Google Research)  
**Publicado en:** EMNLP 2024 (Main)  
**Archivo PDF Local:** `paper6_emnlp2024_444.pdf`

---

## 1. Resumen Ejecutivo
Evalúa experimentalmente si intentar inyectar nuevo conocimiento factual a un LLM mediante ajuste fino supervisado (SFT) incrementa la tendencia a alucinar. 

---

## 2. Hallazgos Principales
- **Aumento Drástico de Alucinaciones:** El ajuste fino sobre datos no vistos durante el preentrenamiento degrada la precisión factual del modelo y aumenta la tasa de alucinaciones en preguntas relacionadas.
- **Límite Paramétrico:** Las redes neuronales continuas aprenden a memorizar superficialmente frases sin incorporar el soporte lógico de la verdad, sugiriendo que el conocimiento factual no debe inyectarse directamente en los pesos paramétricos.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Aporta evidencia empírica contundente de que los pesos paramétricos continuos no deben ser la base de almacenamiento del conocimiento factual. El conocimiento debe residir en una capa simbólica explícita y separable ($V_i, W_i^*$).
- **Cita Sugerida para el Paper:**
  > *"Gekhman et al. (2024) empirically prove that updating factual knowledge via continuous parametric fine-tuning inherently increases hallucination rates, supporting our argument for decoupled, deterministic logical stores."*
