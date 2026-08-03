# Resumen de Artículo Relacionado #5

**Título:** *Unfamiliar Finetuning Examples Control How Language Models Hallucinate*  
**Autores:** Katie Kang, Eric Wallace, Claire Tomlin, Aviral Kumar, Sergey Levine (UC Berkeley, Google DeepMind)  
**Publicado en:** NAACL 2025  
**Archivo PDF Local:** `paper5_naacl2025_2403_05612.pdf`

---

## 1. Resumen Ejecutivo
Investiga cómo los datos de ajuste fino (*finetuning*) que contienen conceptos desconocidos para el modelo base influyen en el comportamiento de alucinación. Los autores descubren que forzar al modelo a aprender datos fuera de su ámbito de conocimiento preentrenado induce patrones sistemáticos de alucinación.

---

## 2. Hallazgos Principales
- **Origen de la Alucinación por Extrapolación:** Cuando se entrena un LLM con ejemplos desconocidos sin un límite ontológico explícito, el modelo aprende a asociar patrones sintácticos con respuestas ficticias confiadas.
- **Falta de Rechazo Activo:** El modelo no posee un mecanismo de rechazo predeterminado para proposiciones que trascienden su frontera de aplicabilidad semántica.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Justifica directamente la necesidad de la categoría *Unsinnig* ($\emptyset$) de Wittgenstein. En lugar de forzar a la red a extrapolar vectores sobre conceptos desconocidos, el sistema debe rechazar la proposición por falta de aplicabilidad semántica en $S_i$.
- **Cita Sugerida para el Paper:**
  > *"Kang et al. (2025) find that finetuning on unfamiliar concepts triggers systematic hallucinations, underscoring the necessity of a formal sense mask ($S_i$) to explicitly reject out-of-scope propositions."*
