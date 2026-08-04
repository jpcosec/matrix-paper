# Deltas pendientes — respuesta a reviewers sobre paper_v2

Formato de cada delta: **DESDE** (átomos KB origen) → **HACIA** (párrafos destino, o anexo si es largo) → **propuesta de texto** (lista para pegar) + bib/átomos/mapping. **Ninguno está aplicado.**

| # | Delta | Eje | Destino prosa | bib nuevas | Átomos KB nuevos |
|---|-------|-----|---------------|-----------|------------------|
| 1 | [Pruebas de insuficiencia del continuo](delta_01_pruebas_continuo.md) | A | `01_1_sota.md`, párrafo nuevo pre-cierre + **anexo** (subsección formal, tono no categórico) | 0 | 0 (ya creados) |
| 2 | [Dicotomía HK⁺/HK⁻](delta_02_hk_dichotomy.md) | A | `01_1_sota.md` p03, extensión | 0 | 0 (ya creado) |
| 3 | [Literatura de causas (7 papers)](delta_03_related_papers.md) | A | `01_1_sota.md` p02/p03/p04, extensiones | 7 (ya en bib) | 0 (ya creados) |
| 4 | [Repr. cerrada + omnirrepresentación + pipeline + máscara](delta_04_representaciones_pipeline_mascara.md) | B+C | **documento largo directo a anexo** + puntero de 2 frases en `04_discussion.md` | 0 | 0 |
| 6 | [Diferenciación RAG/KGs vs OWL/redes causales](delta_06_diferenciacion_kgs.md) | D | `04_discussion.md`, párrafo nuevo tras p03 | 0 | 0 (ya creados) |

**Nota:** los antiguos deltas 4 (pipeline) y 5 (máscara) fueron fusionados en el nuevo delta 4 por decisión del autor: ninguno tiene sentido sin introducir primero la representación cerrada y la omnirrepresentación.

## Orden de aplicación recomendado

1 → 2 → 3 (SOTA juntos; 3 asume 2 aplicado en p03) → 4 → 6.
El anexo `10_appendix.md` lo crea el primero que se aplique entre 1/4 (encabezado `# Appendix` + registro en `paper/paper.yaml`).
Cada delta indica su punto de inserción **por cita textual**, robusto a reediciones.

## Aplicación (por delta)

1. Pegar prosa en `Neurips_peiper/sections/<archivo>`.
2. bibkeys nuevas → `Neurips_peiper/references.bib` (ya hecho para delta 3).
3. Átomos nuevos → `anchor/atomize_sources.py` (ya hecho: 32 Source_PDF bib).
4. Anclas → `anchor/mapping.yaml`.
5. Regenerar y verificar:
   ```bash
   cd paper_v2
   python3 anchor/build_index.py && python3 build_pipeline.py
   python3 anchor/verify_anchors.py && python3 anchor/build_coverage.py
   ```
6. Deltas 1, 4 y 6 crean párrafos nuevos → los anchors posteriores de esa sección se renumeran: re-mapear esas entradas de mapping **por contenido**, no por índice viejo.

## Riesgos transversales

- **Page budget:** 1+2+3 suman ~300 palabras a SOTA; 6 suma ~150 a Discussion; delta 4 solo 2 frases en cuerpo. El grueso va al anexo (fuera del límite). Probable recorte compensatorio: repeticiones en `04_discussion` (p08/p09 solapan máscara/loss).
- **Edición en vivo:** verificar el anclaje textual del punto de inserción antes de pegar.
- **Blind review:** sin repo/tests/benchmarks (`review/summary_response_current_state.md`).
- **Duplicado bib:** `orgad2025apple` vs `orgad2025iclr` → resolver en delta 2.
- **Eje F (typos):** "plant"/línea 171 eran de la versión ICML — en v2 no existen. Minucias v2: doble espacio en `02_philosophical_foundation.md`, doble espacio final en `00_abstract.md:6`, contracción "It's worth noting" en `04_discussion.md`. Recomendado proofread completo.
