# Reporte — Fase 5: revisión léxica + atomización de fuentes

Fecha: 2026-08-03 · Orquestado con 3+1 subagentes (shards A/B/C + revive de A) y scripts deterministas.

## 1. Revisión semántica de las 72 anclas léxicas (3 shards)
- **47 keep / 21 drop / 4 replace.** Drops típicos: cognados falsos (`nature`→Source_PDF_nature ×3, `formal`→Gramatica_Formal, `thing` genérico), stubs Source_Code redundantes, UNL donde el párrafo *rechaza* máquinas universales.
- Shard A murió sin emitir JSON (gate de aceptación); revivido (`resume`) y completó: 19 keep / 6 drop.
- Veredictos: `anchor/build/fase5_lexical_reviews.json` (36 párrafos, 72 entradas).

## 2. Atomización de las 17 fuentes faltantes (0 LLM)
- `anchor/atomize_sources.py` creó 17 átomos `Source_PDF_<key>_pdf.md` en `TractatusKnowledgeMachine/atoms/Fuentes/` desde `references.bib` (surname, year, title).
- `comp_fuentes.md`: nueva sección "Source Bib" (formato parseable por el bib bridge) + `atom_count: 52`.
- **20 anclas bib nuevas** añadidas al mapping (18 esperadas + `dawid2024latent` y `assran2023ijepa` en párrafo de latent probing).
- Cierra el loop de provenance: las 23 bibkeys citadas tienen ahora átomo registrado (antes 6/23).

## 3. Backfill orquestador (5 anclas)
- `04_discussion-p05` → Signo_vs_Simbolo (0.9), Anclaje_Simbolos_Grounding (0.85), Representacion_Flotante (0.75).
- `09_conclusion-p03` → Mascara_Sentido_en_Mecanismos_Atencion (0.9), Categorias_Sentido (0.8).
- Ambos párrafos habían quedado sin ancla tras drops correctos (sus únicos matches eran espurios).

## 4. Guardrail mejorado
- `verify_anchors.py`: el check de hash baseline se reemplazó por **invariante de no-invasividad** (composed con mapping == sin mapping) + idempotencia (rerun == rerun). Robusto ante las ediciones en vivo del usuario en `sections/` (04_discussion 01:05, 09_conclusion 01:21).

## Estado final (ALL PASS)
- **55/58 párrafos anclados** (los 3 sin ancla son: 2 encabezados de sección + 1 frase transicional).
- **126 entradas** (bib 27, bib_transitive 12, lexical 52, fase2_review 30, fase5_review 5).
- 307 validaciones SLDB `valid: true`; 126 archivos kb == 126 entradas; origins resuelven.
- `coverage.md` regenerado con los nuevos números.

## Notas
- Edición externa de `09_conclusion.md` (01:21) verificada: mismas afirmaciones, anclas siguen válidas.
- Los 17 átomos nuevos son provenance stubs (sin PDF en repo); `Propuesta_Indice.md` sigue desactualizado (dice 35 en Fuentes; hay 53) — pendiente menor de KB.
