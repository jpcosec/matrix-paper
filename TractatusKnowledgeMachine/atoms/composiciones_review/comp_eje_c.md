---
title: Eje C — Mecanismo de conexión con LLMs
folder: Eje_C
question: ¿Cómo se integra S_i en atención, en entrenamiento, en generación, y cómo
  se calcula la pérdida intermedia?
atom_count: 5
tags:
- system:matrix
- eje:c
- topic:conexion-llm
---

# Eje C — Mecanismo de conexión con LLMs

## Carpeta Revisada

Cruz-carpeta (Computacion + Filosofia)

## Pregunta que responde esta composición

Cuatro preguntas:
6. ¿Cuál es el algoritmo concreto para integrar las máscaras de sentido en el mecanismo de atención?
7. Durante el entrenamiento: ¿la máscara actúa como mero filtrado de datos? ¿Hay prueba de que mitigue alucinaciones?
8. Durante la generación: ¿se interrumpe la decodificación si $S_i = 0$? ¿Cómo funciona ese mecanismo?
9. ¿Cómo se calcula la pérdida intermedia (intermediate loss)?

## Cadena argumentativa (átomos en orden de lectura)

**P6 — Algoritmo en atención:**

1. [[Mascara_Sentido_en_Mecanismos_Atencion]] — **Único átomo que aborda la inyección directa.** Fórmula: $\text{Attention}(Q,K,V) = \text{Softmax}(\frac{QK^T}{\sqrt{d_k}} + \mathbf{M}_{S_i})V$ donde $\mathbf{M}_{S_i}$ aplica $-\infty$ a posiciones con $S_i=0$. Actúa como "Función de Pérdida Lógica" que modula el gradiente en RL.
2. [[Acoplamiento_Neuro_Estocastico_Simbolico]] — Pipeline de 5 etapas con secuencia completa: usuario → LLM → lowering → MEEL → Matrix $V_i \odot S_i$ → LLM → usuario. Define la arquitectura de desacoplamiento.
3. [[Eje_C_Mecanismo_Conexion_LLM_y_SHRDLU]] — Eje temático que conecta LLM con SHRDLU como mecanismo de lowering.

**P7 — Entrenamiento:**

Sin átomo dedicado. Mascara_Sentido_en_Mecanismos_Atencion menciona que $\mathbf{M}_{S_i}$ modula el gradiente durante RL, pero no hay átomo que demuestre que esto mitiga alucinaciones durante entrenamiento.

**P8 — Generación con interrupción:**

4. [[Capa_Sentido_Si]] — $S_{xy}=1$ permite paso; $S_{xy}=0$ bloquea. Funciona como "guardián ontológico".
5. [[Pipeline_Ingesta_Lenguaje_Matrix]] — Etapa 4: si $S_i=1$ aprueba; si $S_i=0$ (*Unsinnig*) rechaza la proposición. Acoplamiento muestra el rejection signal.

**P9 — Pérdida intermedia:**

Sin átomo dedicado.

## Síntesis

La conexión actual con LLMs es débil a propósito: el LLM propone texto o parsing, y Matrix audita después del lowering. [[Integracion_LLM_en_Training_e_Inferencia_Aun_No_Demostrada]] fija explícitamente que no existe hoy integración validada con training ni con inferencia interna de Transformers. Durante inferencia sí existe rechazo post-lowering de proposiciones Unsinnig; durante entrenamiento no existe hoy mecanismo probado.

## Gaps detectados

**🟡 Cobertura editorial — [[Integracion_Teorica_con_LLMs_y_Trabajo_Futuro]].**
Ya existe un átomo que delimita correctamente el alcance actual: Matrix hoy usa LLMs como parsers/proponentes y actúa como auditor lógico post-generación. No implementa cruce profundo con Transformers ni entrenamiento conjunto.

**🔴 GAP CRÍTICO 1 (P6) — Sigue abierto.**
La proyección de $S_i$ en atención queda como hipótesis arquitectónica razonable, pero **no está claro** el algoritmo concreto: capa, heads, alineación símbolo-token y tratamiento de tokens sin mapeo simbólico.

**🔴 GAP CRÍTICO 2 (P7) — Sigue abierto.**
$S_i$ no tiene hoy rol demostrado en entrenamiento. No hay experimento, regularizador, ni definición de pérdida. Lo único claro es su rol como auditor post-generación para detectar inconsistencias lógicas.

**✅ P8 cubierto por [[Interrupcion_Decodificacion_Si_Cero]].**
Ya existe un átomo específico sobre el mecanismo de rechazo en runtime cuando la proposición resulta `unsinnig`.

**🔴 GAP CRÍTICO 4 (P9) — Sigue abierto.**
La pérdida intermedia no existe aún. Además, $E(R)$ optimiza la representación de la base de datos y **no** debe presentarse como loss de entrenamiento neuronal.

**Resumen: Este eje sigue siendo principalmente trabajo futuro.**
