# Fase 3+4 — Especificación para worker: materialización del anclaje KB→paper

## Contexto
- Pipeline SLDB en `Neurips_peiper/paper_v2/build_pipeline.py`: regenera `sources/`, `notes/`, `paragraphs/`, `sections/`, `manuscript/` desde `paper/paper.yaml` + `paper/sections/*.md`. Cada doc se escribe con `write_doc(model, path, payload)` que renderiza y valida roundtrip.
- `WritingNoteDoc.sources` alimenta la composición `source_digest` (renderiza `- {title} [{kind}] :: {anchor}` por cada PaperSourceDoc referenciado). Hoy cada nota tiene exactamente 1 source `current-paper-block`.
- Modelos en `Neurips_peiper/paper_v2/models.py` (NO modificarlos).
- Átomos KB en `TractatusKnowledgeMachine/atoms/` (NO modificarlos). Índice ya construido: `anchor/build/atoms_index.json`.

## Inputs
- `anchor/build/mapping_draft.yaml` — candidatos Fase 1 (bib, bib_transitive, lexical, composition) + `confidence` + `section_compositions` (ya bendecido por el orquestador, copiar verbatim).
- `anchor/build/fase2_verdicts.json` — verdicts LLM del residual (19 párrafos): `{verdicts: [{anchor, accepted: [{atom_id, atom_path, confidence, reason}], note}]}`.

## Paso 1 — Merge → `anchor/mapping.yaml`
Por párrafo (anchor), átomos aceptados:
1. De mapping_draft: TODOS los candidatos `bib` y `bib_transitive`; candidatos `lexical` con score ≥ 0.5.
2. De fase2_verdicts: aceptados con confidence ≥ 0.6, bridge = `fase2_review` (score = confidence).
3. Dedupe por `atom_path` (gana mayor score; en empate gana bib > fase2_review > lexical).
4. Cap final de 6 átomos por párrafo (precisión: descarta el excedente de menor score).

Schema mapping.yaml:
```yaml
version: 1
generated_by: anchor merge (fases 1+2)
paragraphs:
  <anchor>:
    - atom_id: ...
      atom_path: ...        # relativo a TractatusKnowledgeMachine/atoms/
      bridge: bib|bib_transitive|lexical|fase2_review
      score: 0.0-1.0
      detail: ...           # razón corta
sections:
  <section_id>:
    - composition: comp_x
      path: composiciones_review/comp_x.md
```

## Paso 2 — Extensión de `build_pipeline.py` (única modificación permitida a archivo existente)
1. Cargar `anchor/mapping.yaml` si existe (comportamiento automático; sin flag).
2. Al generar cada párrafo con átomos KB: crear `PaperSourceDoc` en `sources/kb/<stem>__<atom_id>.md`:
   - `title`: title del átomo (atoms_index.json o frontmatter).
   - `kind`: `kb-atom`.
   - `origin`: path relativo desde `paper_v2/` al .md del átomo (`../../TractatusKnowledgeMachine/atoms/<atom_path>`).
   - `anchor`: atom_id.
   - `excerpt`: sección `## Qué es` del átomo (fallback: primer párrafo tras el H1), recortado a ≤1200 chars.
   - `relevance`: `bridge={bridge} score={score} — {detail}`.
3. Añadir los refs kb a la lista `sources` de la nota correspondiente (después del ref actual), con `relpath` correcto.
4. Idempotente: borrar `sources/kb/` al inicio de cada run y regenerar desde mapping.yaml. Ningún archivo se edita a mano.
5. NO tocar `paragraph_text`, `section_body`, `manuscript`, ni `models.py`.

## Paso 3 — Guardrails (obligatorios, reportar evidencia)
1. `python3 build_pipeline.py` exit 0.
2. `sha256sum build/paper.composed.md` IDÉNTICO a `anchor/build/pre_change_hashes.txt` (el anclaje no altera el cuerpo del paper).
3. Todo `build/validation_report.json` con `valid: true` (incluye los nuevos kb sources).
4. `grep -c "kb-atom" notes/*.md` > 0 y conteo de fuentes kb generadas.

## Paso 4 — Reporte de cobertura → `anchor/build/coverage.md`
- Párrafos con/sin ancla KB, por sección.
- Distribución por bridge.
- Gap inverso: átomos KB nunca referenciados por el paper (top por carpeta).
- Bibkeys citadas sin Source_PDF (17, de Fase 1).
- Wikilinks rotos en la KB (11, de Fase 1) como apéndice de calidad KB.

## Non-goals
- No editar átomos, secciones del paper, models.py, ni `paper/`.
- No traducir ni reescribir prosa.

## Reporte final del worker
Archivos creados/modificados, comandos con exit codes, evidencia de guardrails (hashes, conteos), resumen de cobertura, sorpresas. Conciso.
