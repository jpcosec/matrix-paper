---
title: Eje A — Embeddings continuos como causa de alucinación
folder: Eje_A
question: ¿Por qué los primitivos discretos son necesarios, qué impide la distancia
  vectorial, y dónde está la demostración rigurosa?
atom_count: 10
tags:
- system:matrix
- eje:a
- topic:embeddings-continuos
---

# Eje A — Embeddings continuos como causa de alucinación

## Carpeta Revisada

Cruz-carpeta (Antecedentes + Filosofia + Matematica)

## Pregunta que responde esta composición

Tres preguntas:
1. ¿Por qué los primitivos discretos son *fundamentalmente* necesarios para evitar alucinaciones?
2. ¿Qué impide que una distancia vectorial continua aproxime lógica formal?
3. ¿Dónde está la demostración matemática rigurosa de que los embeddings continuos son intrínsecamente incapaces de garantizar verdad o consistencia lógica?

## Cadena argumentativa (átomos en orden de lectura)

**P1 — Necesidad fundamental de discreción:**

1. [[Arquitectura_Neuro_Estocastica]] — Define el paradigma continuo ($\mathbb{R}^d$ + Softmax) y enuncia sus 4 límites estructurales: confunde verosimilitud con verdad, no puede representar saltos escalonados, produce $HK^+$, y no detecta lo absurdo.
2. [[Prueba_Necesidad_Representacion_Simbolica_Discreta]] — **Núcleo.** Reducción al absurdo con 5 pruebas empíricas ($HK^+$, ilusión autocorrección, sicofancia RLHF, conflicto RAG, knowledge overshadowing), cada una exigiendo un primitivo discreto.
3. [[Falla_de_Representabilidad]] — Redefine alucinación como incapacidad estructural de representabilidad: el espacio continuo no puede restringir proposiciones *Unsinnig*.
4. [[Dicotomia_HK_Minus_vs_HK_Plus]] — Prueba experimental (Orgad ICLR 2025, Simhi 2024): el conocimiento verdadero *existe* en el espacio latente pero la decodificación estocástica lo degrada.
5. [[Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente]] — Extiende la prueba $HK^+$: maximizar $P(w_t|w_{<t})$ es infiel a la verdad latente; sesgos de prompt desvían la decodificación.

**P2 — Qué impide la distancia vectorial:**

6. [[Origen_Geometrico_y_Espacio_Vectorial]] — **Barrera AUROC ≈ 0.478**: los embeddings miden coocurrencia estadística, no verdad. Error Tipo III es geométricamente indistinguible del azar.
7. [[Eje_A_Justificacion_Matematica_Limites_Continuos]] — Síntesis de 4 teoremas: discontinuidad de indicadoras, Hornik 1991, Hanin 2017, barrera AUROC 0.48.

**P3 — Demostración rigurosa:**

8. [[Fenomeno_de_Gibbs_en_Funciones_Indicadoras]] — Sobrepaso de Gibbs ≈ 0.0895 *en el límite* $n \to \infty$ al aproximar $\mathbb{I}_A(x)$ con funciones continuas. Irreducible.
9. [[Geometria_de_Politopos_y_Ancho_Acotado_Hanin]] — Red ReLU con ancho acotado genera $\mathcal{N}$ politopos polinomial; fronteras no convexas requieren neuronas exponenciales.
10. [[Medida_y_Semianillos_Booleanos_vs_Probabilistas]] — El espacio probabilístico interpola suavemente ($P \in [0,1]$); el semianillo Booleano colapsa determinísticamente ($\{0,1\}$). La lógica exige fronteras rígidas.

## Síntesis

Los 5 fenómenos $HK^+$ (Prueba_Necesidad) prueban que lo discreto es **necesario**; Gibbs + Hanin + AUROC 0.48 prueban que lo continuo es **insuficiente**. La barrera AUROC 0.478 demuestra que la distancia vectorial es literalmente azar para distinguir verdad de falsedad dentro de un canal semántico correcto. El sobrepaso de Gibbs demuestra que el error es irreducible incluso con parámetros infinitos. Hanin demuestra que las fronteras no convexas requieren explosión exponencial de neuronas.

## Gaps detectados

**⚠️ GAP 1 — No existe átomo dedicado al Teorema de Hornik (1991).**
Eje_A lo referencia como "aproximadores universales de funciones continuas" pero no hay átomo que desarrolle la demostración formal ni la distinción exacta entre aproximar funciones continuas vs. discontinuas. El contenido vive implícito en Fenomeno_de_Gibbs pero no está separado.

**⚠️ GAP 2 — No existe átomo que formalice la barrera AUROC 0.478 como teorema.**
Origen_Geometrico enuncia el resultado empírico de Wei et al. 2024 pero no desarrolla la demostración formal de por qué la coocurrencia estadística es necesariamente incapaz de distinguir verdad factual (Error Tipo III). Falta una demostración topológica o informática, no solo un resultado experimental.

**✅ Cobertura adicional — [[Representacion_Continua_vs_Implementacion_Discreta]].**
Responde la objeción de que "el silicio ya es discreto" distinguiendo entre implementación numérica discreta y representación semántica continua en $\mathbb{R}^d$, y mostrando por qué `argmax` no elimina la interpolación semántica.
