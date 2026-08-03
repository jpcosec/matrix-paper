---
title: Preguntas adicionales de revisores (ZHLy, FJpU)
folder: Reviewer_Qs
question: Estocasticidad en silicio discreto, conexión con arquitectura real, demostración
  de mapping NL→lógica, pipeline operacional completo
atom_count: 8
tags:
- system:matrix
- eje:reviewer
- topic:revisor-objeciones
---

# Preguntas adicionales de revisores (ZHLy, FJpU)

## Carpeta Revisada

Cruz-carpeta (Filosofia + Computacion)

## Pregunta que responde esta composición

Cuatro preguntas de revisores:
14. (ZHLy) ¿Qué significa "estocasticidad" si las redes corren sobre silicio discreto y la decodificación puede ser determinista vía argmax?
15. (ZHLy) ¿Cómo se conecta la representación de la Sección 3 con la arquitectura real de redes neuronales?
16. (ZHLy) ¿Dónde está la demostración de la afirmación "demostramos que los LLMs se pueden usar para mapear lenguaje..."?
17. (FJpU) ¿Cuál es el pipeline operacional paso a paso para extraer proposiciones, etiquetar tipos, verificar $S_i$ y decidir aceptar o rechazar una proposición?

## Cadena argumentativa (átomos en orden de lectura)

**P14 — Estocasticidad en silicio discreto:**

1. [[Arquitectura_Neuro_Estocastica]] — Define "estocasticidad" como el paradigma de muestreo de Softmax sobre $\mathbb{R}^d$, no como ruido físico del silicio.
2. [[Discretizacion_Logica_vs_Continuo]] — Distingue entre dominio continuo/estocástico (superficie $S$) y dominio Booleano discreto (espacio lógico $L_i$).
3. [[Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable]] — Corrige el framing: el problema no es que continuidad implique alucinación, sino que los signos embebidos no garantizan lógica auditable.

**P15 — Conexión con arquitectura real de redes:**

4. [[Mascara_Sentido_en_Mecanismos_Atencion]] — Fórmula de inyección $\mathbf{M}_{S_i}$ en attention.
5. [[Acoplamiento_Neuro_Estocastico_Simbolico]] — Pipeline de 5 etapas LLM ↔ MEEL.
6. [[Eje_C_Mecanismo_Conexion_LLM_y_SHRDLU]] — Lowering como mecanismo de interfaz.
7. [[Integracion_LLM_en_Training_e_Inferencia_Aun_No_Demostrada]] — Delimita explícitamente que no hay integración validada con training/inference.

**P16 — Demostración de mapping NL→lógica:**

6. [[Demostracion_Mundo_Bloques_SHRDLU]] — Prototipo SHRDLU como prueba de concepto.
7. [[Anclaje_Simbolos_Grounding]] — Proceso de mapeo signo → símbolo.

**P17 — Pipeline operacional paso a paso:**

8. [[Pipeline_Ingesta_Lenguaje_Matrix]] — 5 estadios: anclaje → parseo → S-Expr → validación $S_i$ → cómputo $V_i \odot S_i$.
[[Operacion_Assert]], [[Operacion_Evaluar_Sentido]], [[Operacion_Evaluar_Verdad]], [[Operacion_Validar_Formulacion]] — Operaciones individuales del pipeline.

## Síntesis

La "estocasticidad" se refiere al muestreo probabilístico (Softmax) sobre representaciones continuas, no al ruido del hardware. La conexión actual con la red neuronal es por lowering y auditoría post-generación, no por modificación interna del Transformer. SHRDLU es una prueba de concepto de mapping NL→lógica en dominio restringido. El pipeline operacional ya tiene walkthrough concreto, pero la validación empírica general del lowering sigue abierta.

## Gaps detectados

**✅ P14 cubierto por [[Representacion_Continua_vs_Implementacion_Discreta]].**
Distingue entre discretización numérica del hardware y continuidad topológica del espacio semántico $\mathbb{R}^d$, y explica por qué `argmax` no elimina la interpolación semántica ni corrige las fronteras lógicas.

**⚠️ GAP CRÍTICO 2 (P15) — No existe átomo que conecte la arquitectura de Matrix con capas específicas del Transformer.**
Mascara_Sentido da la fórmula pero no especifica: ¿se inyecta en todas las capas? ¿Solo en la última? ¿Cómo se alinean las coordenadas de $S_i$ (basadas en símbolos lógicos) con las posiciones de la secuencia de tokens del Transformer? Falta un "mapping de coordenadas" entre el espacio $L_i$ y la secuencia de entrada.

**🔴 GAP CRÍTICO 3 (P16) — Sigue abierto.**
SHRDLU es un prototipo en un dominio restringido (mundo de bloques). No hay evaluación de: tasa de éxito del parseo, dominios cubiertos, robustez ante ambigüedad, ni comparación con parsers existentes (SPICE en CLEVR, etc.). La afirmación "demostramos" no está respaldada por un experimento con métricas.

**✅ P17 cubierto por [[Walkthrough_Pipeline_con_Ejemplo]].**
Ya existe un átomo paso a paso con ejemplo concreto desde texto natural hasta decisión aceptar/rechazar.
