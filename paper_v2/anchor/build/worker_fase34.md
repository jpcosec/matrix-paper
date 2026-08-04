# Reporte final — Fase 3+4: materialización del anclaje KB→paper

Fecha: 2026-08-03 · Cerrado por el orquestador tras muerte del worker (0243025b) y review de cierre.

## Archivos creados/modificados

**Creados**
- `anchor/mapping.yaml` — 58 párrafos, 121 entradas (lexical 72, fase2_review 30, bib_transitive 12, bib 7); sections = section_compositions bendecido.
- `anchor/build/merge_mapping.py` — merge Fase 1 + Fase 2 según reglas de la spec.
- `anchor/verify_anchors.py` — test ejecutable de guardrails (6 checks).
- `anchor/build_coverage.py` + `anchor/build/coverage.md` — reporte Fase 4.
- `anchor/build/rebaseline_note.md` — decisión de re-baseline + re-validación de anclas p08.
- `sources/kb/*.md` — 121 `PaperSourceDoc kind: kb-atom` generados por el pipeline.

**Modificados**
- `build_pipeline.py` — carga automática de mapping, generación kb sources, refs en notas, wipe incondicional de `sources/kb/` (fix M2 del review).

## Evidencia de guardrails (final)

- `python3 build_pipeline.py` → exit 0.
- `python3 anchor/verify_anchors.py` → **6/6 PASS** (hash composed == baseline, 302 validaciones `valid: true`, 121 archivos == 121 entradas, 55 notas con kb, origins resuelven).
- Cuerpo del paper sin cambios por el anclaje: el único drift de hash vino de una edición externa en `sections/04_discussion.md`, adoptada vía re-baseline documentado.

## Review de cierre (ver `review_cierre.md`)

- Blocker B1 (hash ≠ baseline por edición externa) → resuelto: re-baseline + re-validación de anclas de p08 (siguen siendo correctas).
- M1 (digest de fuentes renderiza vacío — comportamiento pre-existente del runtime SLDB) → documentado; no es regresión del anclaje.
- M2 (wipe condicionado) → corregido.
- M3 (reporte de worker ausente) → este documento.
- Verificado por el reviewer: merge conforme a spec, schema conforme, 121 kb sources correctos (origin resuelve, excerpt ≤1200, títulos == índice), coverage recomputado y exacto.

## Cobertura final

- 55/58 párrafos anclados (3 vacíos justificados: 2 encabezados, 1 transición).
- 43/182 átomos de contenido usados; gap inverso top: `Computacion/Parsers_y_Runtimes` (16), `Operaciones_DB_Logica` (14), `Optimizacion_y_Seguridad` (13).
- 17 bibkeys citadas sin Source_PDF en la KB (candidatas a atomización).
- 11 wikilinks rotos en la KB (apéndice de calidad).
