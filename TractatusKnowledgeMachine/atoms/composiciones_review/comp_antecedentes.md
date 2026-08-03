---
title: Necesidad ontológica de primitivos discretos — Antecedentes
folder: Antecedentes
question: ¿Por qué los primitivos discretos son fundamentalmente necesarios?
atom_count: 5
tags:
- system:matrix
- topic:necesidad-discreta
- layer:epistemology
---

# Necesidad ontológica de primitivos discretos — Antecedentes

## Carpeta Revisada

`atoms/Antecedentes/`

## Pregunta que responde esta composición

¿Por qué los primitivos discretos son *fundamentalmente* necesarios? ¿Qué fallas estructurales del paradigma continuo demuestran que la discreción no es un capricho arquitectónico sino una exigencia ontológica?

## Cadena argumentativa (átomos en orden de lectura)

1. **[[Arquitectura_Neuro_Estocastica]]** — Define el paradigma continuo ($\mathbb{R}^d$ + Softmax) y enuncia sus 4 límites estructurales: confunde verosimilitud con verdad, no puede representar saltos escalonados, produce $HK^+$, y no detecta lo absurdo.

2. **[[Prueba_Necesidad_Representacion_Simbolica_Discreta]]** — Demostración por reducción al absurdo con 5 pruebas empíricas mapeadas a fuentes ($HK^+$, ilusión de autocorrección, sicofancia RLHF, conflicto RAG, knowledge overshadowing). Cada falla exige un primitivo discreto específico ($V_i$, $S_i=0$, $V_i \odot S_i$, $WC_i$, equidad de bits).

3. **[[Falla_de_Representabilidad]]** — Redefine la alucinación no como error de recuperación sino como incapacidad estructural de representabilidad: el espacio continuo no puede restringir proposiciones *Unsinnig*.

4. **[[Dicotomia_HK_Minus_vs_HK_Plus]]** — Prueba experimental (Orgad ICLR 2025, Simhi 2024) de que el conocimiento verdadero *sí existe* en el espacio latente pero la decodificación estocástica lo degrada.

5. **[[Origen_Geometrico_y_Espacio_Vectorial]]** — Demuestra la **barrera AUROC ≈ 0.478** para el Error Fáctico Tipo III: los embeddings codifican coocurrencia estadística, no verdad factual.

## Síntesis

Los átomos de Antecedentes prueban que la discreción es necesidad ontológica, no preferencia arquitectónica:
- $HK^+$ demuestra que el conocimiento está ahí pero el canal continuo no lo extrae fielmente.
- La barrera AUROC ≈ 0.48 demuestra que la distancia vectorial es azar puro para distinguir verdad de mentira dentro del canal semántico correcto.
- La alucinación es una **falla de representabilidad**, no de recuperación: el espacio continuo no puede delimitar *Unsinnig*.
- Cada una de las 5 patologías exige un primitivo discreto específico e insustituible.

## Gaps detectados
