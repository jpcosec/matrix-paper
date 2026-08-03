---
topic: comparacion-arquitecturas-jepa
use_when: Aplicable al contexto semantico y factual de Comparacion Arquitecturas JEPA.
do_not_use_when: No utilizar fuera del dominio formal de continuous-space-limits.
id: atom-comparacion-arquitecturas-jepa
title: Comparacion Arquitecturas JEPA
five_wh_one_plus: what
tags:
- system:matrix
---
# Comparación con Arquitecturas JEPA / H-JEPA (Yann LeCun)

**Categoría Padre:** [[Antecedentes/Limites_Espacio_Continuo]]
**Relaciones 5W1H+:**
* [grounded_by:: [[Source_PDF_lecun_jepa2023_pdf]]]
* [explains_failure_of:: [[Arquitectura_Neuro_Estocastica]]]
* [is_solved_by:: [[BlockMatrix]]]
* [explains_failure_of:: [[Discretizacion_Logica_vs_Continuo]]]
* [explains_failure_of:: [[Matriz_por_Bloques]]]
* [explains_failure_of:: [[Representacion_Plana_vs_Tensorial]]]

---

## Qué es
Es la comparación crítica entre la arquitectura de predicción conjunta en espacio abstracto **JEPA / H-JEPA** (LeCun et al.) y el marco neuro-simbólico **Matrix**.

---

## Similitudes y Diferencias

* **Similitud:** Ambas arquitecturas rechazan la predicción generativa autorregresiva token por token a nivel de superficie de texto.
* **Diferencia Fundamental:** JEPA utiliza funciones de energía escalar continuas e incrustaciones multidominio en espacios de representación continuos. *Matrix*, en cambio, impone una **separación lógica y de sentido Booleana discreta ($V_i \odot S_i$)**, garantizando verificabilidad e inmutabilidad estricta.
