# Revisión de cierre — Anclaje KB→paper (Fase 3+4)

Fecha: 2026-08-03 · Revisor: subagente de revisión (READ-ONLY sobre artefactos) · Spec: `anchor/build/fase3_spec.md`

## Veredicto: **REQUIERE FIXES** (1 blocker)

El anclaje en sí (mapping, merge, extensión del pipeline, cobertura) es correcto y verificado.
Pero el guardrail central de no-invasividad **falla en disco**: el cuerpo del paper ya no coincide con el baseline.

---

## Blocker

### B1. `composed_hash_matches_baseline` FALLA — prosa reescrita tras el baseline

- `python3 anchor/verify_anchors.py` → **exit 1**:
  ```
  composed_hash_matches_baseline     FAIL   78eaefc65450 vs 38070c46a2ae
  ```
- Causa raíz con evidencia:
  - `anchor/build/pre_change_hashes.txt` (snapshot 00:40:23) espera `38070c46…` para `build/paper.composed.md`; el actual es `78eaefc6…`.
  - `Neurips_peiper/sections/04_discussion.md` tiene mtime **01:05:45** (post-baseline), ~40 s antes del último run del pipeline (01:06:24–27). Es la **única** fuente de sección modificada tras el snapshot.
  - Diff contra `paper/main.md` (00:09, pre-baseline): el párrafo "Relationship with LLM" sobre la sense mask fue **reescrito** ("neural network-based language models … play in attention mechanisms … during training" → "neural network language models … play across both training and inference pipelines … at train time"). Ese párrafo es **`04_discussion-p08`, que está anclado** (fase2_review; el verdict lo describe como "Atención + definición formal de S" — texto viejo).
- Consecuencias:
  1. Guardrail Paso 3.2 de la spec (hash compuesto IDÉNTICO al baseline) incumplido.
  2. Non-goal de la spec violado ("No traducir ni reescribir prosa", "No editar secciones del paper").
  3. El anclaje de p08 se computó sobre prosa distinta a la actual.
- A favor del resto del trabajo: `manuscript/paper.md` == baseline (`791fedee…` ✔, el manuscrito solo incrusta abstract/título/refs) y la recomposición en memoria desde los docs en disco == composed en disco (`78eaefc6…` ✔). O sea: el pipeline no introdujo el drift; lo introdujo la edición manual de la sección.
- Fix requerido (decisión del orquestador): **revertir** `sections/04_discussion.md` al texto pre-baseline y re-correr el pipeline (verificar que el hash vuelva a `38070c46…`), o **re-baselinear explícitamente** justificando la edición y re-validando los anclas de `04_discussion-p08`.

## Menores

- **M1. Guardrail 4 de la spec literalmente incumplido** (`grep -c "kb-atom" notes/*.md` = 0). La sección `## Source Digest` de TODAS las notas (con y sin kb) renderiza vacía: `render_model_markdown` no resuelve la composición `source_digest` (verificado por simulación directa del render con refs kb). Es comportamiento **pre-existente** del runtime SLDB (las notas baseline con 1 source ya tenían el digest vacío), no una regresión del anclaje. `verify_anchors.py` sustituye el check por "nota contiene ref `kb/`" (55/55 ✔), que es el chequeo sustantivo correcto. Spec y realidad difieren; conviene corregir la spec o arreglar el render del digest upstream.
- **M2. Wipe idempotente condicionado** (`build_pipeline.py:264-267`): `shutil.rmtree(KB_SOURCES_DIR)` solo ocurre `if kb_paragraphs:`. La spec dice "borrar `sources/kb/` al inicio de cada run". Si `mapping.yaml` se elimina o queda con `paragraphs: {}`, los kb sources stale quedan huérfanos en disco. Caso borde, pero desviación de la spec.
- **M3. `anchor/build/worker_fase34.md` está vacío (0 líneas)** — la spec exige reporte final del worker (archivos, comandos, evidencia de guardrails). `coverage.md` existe y es correcto, pero el reporte del worker falta. Dado B1, cualquier evidencia de "hash == baseline" que se haya reportado verbalmente queda contradicha por el disco.

## Correcto (verificado con evidencia)

- **`build_pipeline.py`** (única modificación permitida): carga automática de `anchor/mapping.yaml` sin flag (`load_kb_mapping`, :77-83, llamada en `main` :258); wipe+regen de `sources/kb/` (:264-267); `PaperSourceDoc` con `kind: kb-atom`, `origin` = relpath desde `paper_v2/` (`../../TractatusKnowledgeMachine/atoms/...`, resuelve ✔), `anchor` = atom_id, excerpt de `## Qué es` con fallback al primer párrafo post-H1 y corte a 1200 chars (:96-114), relevance `bridge=… score=… — detail` (:187-191); refs kb añadidos **después** del ref actual en la nota (:197). No toca `paragraph_text`/`section_body`/`manuscript` (inspección de código + recomposición en memoria idéntica). `models.py` intacto (0 referencias a kb).
- **`anchor/mapping.yaml`**: schema conforme (`version: 1`, `generated_by`, `paragraphs`, `sections`); 58 párrafos, 121 entradas, 55 anclados; bridges ∈ {bib, bib_transitive, lexical, fase2_review}; scores ∈ [0.5, 1.0]; sin violaciones de cap 6; sin duplicados por `atom_path`; `sections` == `mapping_draft.section_compositions` (copia verbatim ✔); 0 lexical <0.5; 0 fase2 <0.6.
- **`anchor/build/merge_mapping.py`**: reglas 1-4 coinciden con la spec (bib+bib_transitive siempre; lexical ≥0.5; fase2 ≥0.6 con bridge `fase2_review`; dedupe por atom_path gana mayor score; cap 6 descartando menor score). Única ausencia vs draft: 1 candidato bib_transitive en `01_1_sota-p06` descartado legítimamente por cap 6 (empate 0.8 entre 5, desempate determinista por atom_id). Los 3 párrafos sin ancla (`03_proposed_representation-p24`, `04_discussion-p02`, `04_discussion-p07`) son 1 frase transicional + 2 encabezados — justificación de coverage.md confirmada contra los verdicts de fase 2.
- **`sources/kb/*.md`** (muestreo + chequeo exhaustivo de los 121): formato PaperSourceDoc correcto; los 121 origin resuelven a átomos existentes; excerpts no vacíos, máx 855 chars (≤1200 ✔); títulos == `atoms_index.json` (0 mismatches); relevance con bridge+score ✔; 14/51 átomos usan el fallback permitido (mayoría `Fuentes/*` sin `## Qué es`).
- **`anchor/build/coverage.md`**: todos los números recomputados independientemente y coinciden — 55/58 anclados, 121 entradas, distribución bridges lexical 72 / fase2_review 30 / bib_transitive 12 / bib 7 (=121), tabla por sección exacta, 43/182 átomos usados (139 sin usar; filtro de `build_coverage.py` reproducido: excluye Fuentes/composiciones/Propuesta_Indice), 17 bibkeys sin Source_PDF == `summary.md`, 11 wikilinks rotos == Fase 1.
- **Evidencia conocida confirmada**: 302 validaciones `valid: true` ✔; 121 entradas == 121 archivos ✔; 55 notas con kb ✔. La afirmación "composed hash == baseline" queda **contradicha** (ver B1).

## Observaciones

- **O1.** `merge_mapping.py:31` desempata `bib > bib_transitive > fase2_review > lexical`; la spec nombra solo "bib > fase2_review > lexical". Desviación documentada en comentario del código, razonable (bib_transitive deriva de bib), sin impacto en el resultado.
- **O2.** `verify_anchors.py` cubre: existencia de artefactos, hash baseline, validation all-true, conteo kb==mapping, notas↔anclados, origins. NO cubre: exit code del pipeline, cap 6, dedupe, rango de scores, excerpt ≤1200 (los verifiqué manualmente: todos OK). Sería deseable añadirlos para futuras regresiones.
- **O3.** El desempate por cap usa `atom_id` como criterio final (determinista pero arbitrario alfabéticamente); en p06 dejó fuera `Infidelidad_del_Razonamiento_en_Prosa_y_la_Ilusion_de_Pensar` (0.8) conservando átomos de igual score. Aceptable; si se quiere precisión semántica, el criterio de corte del cap es mejorable.
- **O4.** El pipeline genera "párrafos" a partir de bloques que son encabezados (`# Relationship with …`) — comportamiento pre-existente, ajeno al anclaje, pero explica 2 de los 3 párrafos sin ancla.

## Comandos ejecutados (solo lectura)

- `python3 anchor/verify_anchors.py` → **exit 1** (5 PASS / 1 FAIL: `composed_hash_matches_baseline`).
- Verificaciones puntuales con python3 (yaml/json/hash/difflib) sobre mapping vs draft+verdicts, kb sources, coverage, recomposición en memoria del composed, y simulación del render del digest — todas reportadas arriba.
- `stat`/`sha256sum` para cronología y hashes; sin git en el directorio (confirmado).
