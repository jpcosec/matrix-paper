# paper_v2

Pipeline SLDB para modelar el paper actual como una cadena de composición editorial.

## Flujo

- `sources/`: átomo documental o bloque fuente.
- `notes/`: nota de redacción derivada de una o varias fuentes.
- `paragraphs/`: párrafo de sección derivado de una o varias notas.
- `sections/`: sección compuesta por transclusiones de párrafos.
- `manuscript/paper.md`: paper completo compuesto por transclusiones de secciones.
- `build/paper.composed.md`: materialización final expandida.

## Modelo

Los modelos viven en `models.py`:

- `PaperSourceDoc`
- `WritingNoteDoc`
- `SectionParagraphDoc`
- `PaperSectionDoc`
- `PaperManuscriptDoc`

La composición final usa dos mecanismos distintos:

- `__compositions__`: para digests legibles de referencias hijas.
- `![[transclusions]]`: para materializar cuerpo de secciones y paper con `sldb docs compose` o con `build_pipeline.py`.

## Bootstrap desde el paper actual

Este directorio se alimenta desde:

- `../Neurips_peiper/sections/*.md`
- `../Neurips_peiper/paper/paper.yaml`
- `../Neurips_peiper/references.bib`

Ejecuta:

```bash
cd paper_v2
python3 build_pipeline.py
```

Eso regenera:

- `sources/*.md`
- `notes/*.md`
- `paragraphs/*.md`
- `sections/*.md`
- `manuscript/paper.md`
- `build/paper.composed.md`
- `build/validation_report.json`
- `build/compose_report.json`

## Uso con SLDB CLI

Con SLDB en el `PYTHONPATH`:

```bash
export PYTHONPATH=../../../hum-ecosystem/tools/sldb/src
cd paper_v2
python -m sldb validate models:PaperSectionDoc --input sections/01_introduction.md --pythonpath .
python -m sldb validate models:PaperManuscriptDoc --input manuscript/paper.md --pythonpath .
python -m sldb docs compose manuscript/paper.md --format markdown -o -
```

## Idea de trabajo

La estructura ya permite reemplazar el bootstrap automático por edición real:

- una fuente nueva entra en `sources/`
- se redacta su nota en `notes/`
- la nota alimenta un párrafo en `paragraphs/`
- los párrafos componen la sección
- las secciones componen el manuscrito completo
