# Mascara Sentido en Mecanismos Atencion

Kind: kb-atom
Origin: ../TractatusKnowledgeMachine/atoms/Computacion/Optimizacion_y_Seguridad/Mascara_Sentido_en_Mecanismos_Atencion.md
Anchor: atom-mascara-sentido-en-mecanismos-atencion

## Excerpt

Es la propuesta de integración de Fase 3 (Discusión del manuscrito NeurIPS) donde la Máscara de Sentido Booleana $S_i$ se inyecta directamente dentro de la matriz de atención del Transformer durante el entrenamiento o la inferencia:

$$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{QK^T}{\sqrt{d_k}} + \mathbf{M}_{S_i}\right) V$$

Donde $\mathbf{M}_{S_i}$ aplica una penalización $-\infty$ a las posiciones con $S_i = 0$, actuando como una **Función de Pérdida Lógica** que modula el gradiente durante el aprendizaje por refuerzo (RL).

## Relevance

bridge=fase5_review score=0.9 — sense masks en mecanismos de atención; propuesta exacta del párrafo
