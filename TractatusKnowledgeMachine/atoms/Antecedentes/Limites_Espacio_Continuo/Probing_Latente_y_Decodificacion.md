---
topic: probing-latente-y-decodificacion
use_when: Aplicable al contexto semantico y factual de Probing Latente y Decodificacion.
do_not_use_when: No utilizar fuera del dominio formal de continuous-space-limits.
id: atom-probing-latente-y-decodificacion
title: Probing Latente y Decodificacion
five_wh_one_plus: what
tags:
- system:matrix
---
# Probing de Espacio Latente y Decodificación Infiel

**Categoría Padre:** [[Antecedentes/Limites_Espacio_Continuo]]
**Relaciones 5W1H+:**
* [explains_failure_of:: [[Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente]]]
* [grounded_by:: [[Dicotomia_HK_Minus_vs_HK_Plus]]]
* [explains_failure_of:: [[Matriz_por_Bloques]]]

---

## Qué es
Es la técnica de auditoría (*linear probing*) mediante la cual se entrenan clasificadores lineales sobre las activaciones de las capas ocultas intermedias de un LLM para comprobar si la verdad factual existe dentro del espacio latente antes de la decodificación.

---

## Hallazgo Científico
El *probing* demuestra que el espacio latente posee la veracidad de la proposición, pero la capa final de muestreo estocástico (Softmax) degrada la fidelidad, convirtiendo conocimiento latente verdadero en alucinación de superficie ($HK^+$).

---

## 📚 Fuentes Científicas y Archivos PDF en el Repositorio
* 📄 **Orgad et al. (ICLR 2025)**: *LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations*
  * PDF en Repositorio: [iclr2025_a712d4.pdf](file:///home/jp/proyectos/Matrix/limits_of_continuous_llm_training/pdf/iclr2025_a712d4.pdf)
