# Re-baseline del guardrail de hash — 2026-08-03

## Qué pasó
- El baseline original (`pre_change_hashes.txt`, snapshot 00:40) quedó invalidado por una **edición externa al anclaje** en `Neurips_peiper/sections/04_discussion.md` (mtime 01:05:45), detectada por el reviewer de cierre (blocker B1).
- La edición reescribió el párrafo "Relationship with LLM" (04_discussion-p08): amplía la propuesta de la sense mask $S$ a **training E inference** (antes solo training). Es una mejora de contenido coherente con el paper; `paper/main.md` ya venía regenerado con el mismo texto.
- Ningún proceso del anclaje (workers, pipeline, orquestador) editó prosa del paper: el pipeline solo regenera desde `sections/`, y el drift entró por edición manual de la fuente.

## Decisión del orquestador
**Adoptar la edición y re-baselinear** (la alternativa, revertir, destruiría una edición deliberada ajena al anclaje).

## Re-validación de los anclas de `04_discussion-p08`
Anclas aceptadas en Fase 2: `Mascara_Sentido_en_Mecanismos_Atencion` (0.95) + `Capa_Sentido_Si` (0.8).
El nuevo texto trata exactamente la misma propuesta (máscara $S$ en atención, detección de sentido en texto generado, RL, ahora también en train time) → **ambas anclas siguen siendo semánticamente correctas**. Las fuentes kb derivan de los átomos, no de la prosa del paper, por lo que no requieren regeneración de contenido.

## Nuevo baseline
`pre_change_hashes.txt` regenerado el 2026-08-03 tras la re-verificación completa del pipeline (exit 0, 302 validaciones `valid: true`).
Hash anterior del composed: `38070c46a2ae…` → nuevo: `78eaefc65450…`.

## Fix asociado (M2 del review)
`build_pipeline.py`: el wipe de `sources/kb/` ahora es incondicional (antes solo ocurría si había mapping), evitando kb sources huérfanos si mapping.yaml desaparece.
