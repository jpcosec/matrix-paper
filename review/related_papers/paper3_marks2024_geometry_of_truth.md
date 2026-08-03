# Resumen de Artículo Relacionado #3

**Título:** *The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets*  
**Autores:** Samuel Marks, Max Tegmark (Northeastern University, MIT)  
**Publicado en:** COLM 2024 (Conference on Language Modeling)  
**Archivo PDF Local:** `paper3_colm2024_2310_06824.pdf`

---

## 1. Resumen Ejecutivo
Este trabajo investiga si los LLMs construyen representaciones internas lineales del valor de verdad (Verdadero/Falso). Entrenando sondas lineales (*linear probes*) sobre las activaciones de los modelos, los autores descubren direcciones emergentes de verdad, pero revelan límites críticos cuando las estructuras lógicas se vuelven complejas.

---

## 2. Hallazgos Principales
- **Estructura Lineal Emergente:** En datasets simples de afirmaciones factuales, existe una dirección lineal en el espacio de activaciones que separa enunciados verdaderos de falsos.
- **Falla de Generalización en Lógica Compleja:** Las sondas lineales formadas en un dominio no generalizan ante negaciones, disyunciones o estructuras lógicas complejas, porque la geometría continua difumina las discontinuidades de la lógica formal.

---

## 3. Relevancia Directa para `tractatusBIt` (Eje A)
- **Conexión con el Eje A:** Aporta la prueba geométrica exacta que pedía el Revisor `ZHLy`. Aunque el espacio de embeddings continuos desarrolla aproximaciones lineales de verdad, no puede sostener la consistencia deductiva sobre operaciones compuestas sin primitivos discretos matriciales.
- **Cita Sugerida para el Paper:**
  > *"Marks & Tegmark (2024) show that while linear probes can identify truth directions in simple activation spaces, continuous geometry fails to generalize across complex logical compositions, confirming the need for explicit discrete boolean structures."*
