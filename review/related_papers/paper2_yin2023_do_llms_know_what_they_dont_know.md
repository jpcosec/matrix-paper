# Resumen de Artículo Relacionado #2

**Título:** *Do Large Language Models Know What They Don’t Know?*  
**Autores:** Zhangyue Yin, Qiushi Sun, Qipeng Guo, Jiawen Wu, Xipeng Qiu, Xuanjing Huang (Fudan University, National University of Singapore)  
**Publicado en:** ACL 2023 (Findings)  
**Archivo PDF Local:** `paper2_acl2023_551.pdf`

---

## 1. Resumen Ejecutivo
El artículo analiza la capacidad de calibración y autoconocimiento de los LLMs. Examina si los modelos pueden identificar los límites de su propio conocimiento o si sobreestiman su certeza al responder preguntas fuera de su alcance.

---

## 2. Hallazgos Principales
- **Falta de Delimitación de Fronteras de Conocimiento:** Los LLMs carecen de un mecanismo interno explícito para marcar proposiciones fuera de su dominio como "desconocidas" o "inaplicables".
- **Sobre-confianza en Distribuciones Continuas:** Las distribuciones de probabilidad sobre tokens (softmax continuo) fuerzan al modelo a emitir una respuesta incluso cuando la certeza lógica es nula, generando alucinaciones confiadas.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Demuestra la necesidad de una máscara de aplicabilidad semántica ($S_i$). Sin una estructura discreta que marque proposiciones fuera de dominio como *Unsinnig* ($\emptyset$), las funciones continuas de probabilidad obligan a la red a generar texto estocástico.
- **Cita Sugerida para el Paper:**
  > *"Yin et al. (2023) demonstrate that LLMs lack self-knowledge regarding their epistemic boundaries, generating confident hallucinations due to unconstrained continuous logit distributions."*
