# Worker — Fase 0+1: Anclaje determinista KB→paper

Fecha: 2026-08-03 · Ejecutado desde `Neurips_peiper/paper_v2/` · Python 3.13.5 + pyyaml 6.0.3

## Archivos creados (todos nuevos, bajo `Neurips_peiper/paper_v2/anchor/`)

- `anchor/build_index.py` — generador determinista (stdlib + pyyaml), ~430 líneas
- `anchor/build/atoms_index.json` — índice de átomos (240 entradas)
- `anchor/build/candidates.json` — candidatos por párrafo con bridge/score/detail
- `anchor/build/mapping_draft.yaml` — draft + section_compositions + confidence
- `anchor/build/summary.md` — conteos, residual, bibkeys sin match, anomalías
- `anchor/build/worker_fase01.md` — este reporte

No se modificó ningún archivo existente (verificado con `sha256sum` contra `build/pre_change_hashes.txt`: `paper.composed.md` y `manuscript/paper.md` intactos). Átomos KB solo leídos.

## Ejecución y validación

`python3 anchor/build_index.py` → **exit code 0**, corre limpio a la primera.

| Métrica | Valor | Meta | Estado |
|---|---|---|---|
| Átomos indexados | **240** .md | 241 | ⚠ ver nota |
| Párrafos parseados | **58** | 58 | ✓ |
| Párrafos con ≥1 candidato bib o lexical ≥0.5 | **39** | ≥30 | ✓ |
| Bibkeys citadas / matcheadas | 23 / **6** | — | ✓ (17 sin match reportadas) |
| Confianza: high / medium / low | 39 / 7 / 12 | — | ✓ |

Nota átomos: el conteo real de `.md` bajo `atoms/` es **240** (19 Antecedentes + 5 Aplicaciones + 17 composiciones_review + 4 composiciones_spec + 90 Computacion + 22 Filosofia + 36 Fuentes + 6 Isomorfismo + 36 Matematica + 1 Propuesta_Indice + 4 Teoria_de_Bases_de_Datos). La cifra "241" del briefing probablemente incluía `predicates-5w1h.yaml` (no es .md). Sin duplicados de stem ni de id.

## Conteos por bridge (candidatos / párrafos con ≥1)

| bridge | candidatos | párrafos |
|---|---|---|
| bib | 7 | 6 |
| bib_transitive (grounded_by→Source_PDF) | 13 | 6 |
| lexical (top-5, solape términos distintivos) | 229 | 50 |
| composition (cadenas comp_* por sección, cap 10) | 569 | 58 |

Bibkeys matcheadas (Apellido+año vía comp_fuentes.md): `orgad2025apple`→iclr2025_a712d4 (exacto), `factscore2023`→factscore2023 (exacto), `shumailov2024`→nature_shumailov2024 (exacto), `symcode2025`→symcode2025 (exacto), `vossel2025advancing`→vossel2025advancing (exacto), `lecun2022path`→lecun_jepa2023 (**solo-apellido**: bib 2022 vs átomo "LeCun (2023, JEPA)").

## Set residual Fase 2 (19 párrafos low/medium) — primeras 5 líneas

```
- 01_1_sota-p01 (01_1_sota) conf=medium lex_max=0.33 bibkeys=—
- 01_1_sota-p05 (01_1_sota) conf=medium lex_max=0.33 bibkeys=['bender2020', 'lyre2024understanding']
- 02_philosophical_foundation-p03 (02_philosophical_foundation) conf=low lex_max=0.20 bibkeys=—
- 02_philosophical_foundation-p04 (02_philosophical_foundation) conf=low lex_max=0.20 bibkeys=—
- 02_philosophical_foundation-p05 (02_philosophical_foundation) conf=medium lex_max=0.40 bibkeys=—
```

Distribución del residual: 2× 01_1_sota, 3× 02_philosophical_foundation, **11× 03_proposed_representation**, 3× 04_discussion. La sección 03 concentra el residual (11/19): prosa matemática formal con poco solape léxico directo con títulos de átomos en español. Ningún párrafo quedó sin candidatos (composition cubre 58/58).

## Bibkeys citadas sin match Source_PDF (17)

`harnad1990symbolgrounding`, `wittgenstein1922`, `bender2020`, `lyre2024understanding`, `halueval2023`, `semantic_entropy2024`, `kommers2025slop`, `dawid2024latent`, `assran2023ijepa`, `ibrahim2026`, `ferrone2019`, `liu2025code4logic`, `lee2025entailment`, `choi2025knowledge`, `cheng2025empowering`, `bian2025llm`, `liang2025survey`. Causa: no existe línea Apellido+año para ellos en comp_fuentes.md (la KB solo registra 13 Source_PDF). Es un hallazgo de cobertura KB, no un error del script.

## section_compositions (draft YAML, 1–3 por sección, justificación incluida)

- 01_introduction → comp_antecedentes (5 átomos), comp_isomorfismo (6)
- 01_1_sota → comp_eje_d (6), comp_fuentes (34), comp_antecedentes (5)
- 02_philosophical_foundation → comp_filosofia (5), comp_isomorfismo (6)
- 03_proposed_representation → comp_computacion (5), comp_matematica (5), comp_eje_b (11)
- 04_discussion → comp_eje_a (11), comp_gaps (0*), comp_aplicaciones (4)
- 09_conclusion → comp_eje_e (35), comp_aplicaciones (4)

(*) comp_gaps tiene `atom_count: 0` legítimo: el documento declara "No hay cadena argumentativa — este documento registra lo que **falta**". El draft apunta al documento, no a una cadena.

## Anomalías (en summary.md)

- **Wikilinks rotos: 11 distintos** (top: `[[BlockMatrix]]` ×12, `[[BooleanMatrix]]` ×3, `[[Dimension_Hipertensor]]` ×2, `[[Source_PDF_hornik1991approximation_pdf]]`, `[[Source_PDF_arxiv2306_06085_pdf]]` — los dos últimos son átomos Source_PDF referenciados por `grounded_by` que no existen en `Fuentes/`).
- Stems/IDs duplicados: ninguno.
- Frontmatter heterogéneo: dos esquemas (`id/title/five_wh_one_plus/tags` y `system/layer/domain/topic`); el indexer usa fallback id=stem, title=H1|stem.

## Sorpresas / riesgos

1. **240 ≠ 241**: el briefing contaba 241 átomos; hay 240 .md. No falta ningún archivo según el desglose por carpeta.
2. **Gap idiomático ES→EN**: la KB está en español y el paper en inglés; el puente léxico solo engancha cognados, nombres propios (tractatus, wittgenstein, gibbs…) y símbolos ($V_i$,$S_i$,$W_i$,HK±). Matches de un solo término genérico (p.ej. `symbol`→atom-symbol 1.00, `nature`→Source_PDF_nature_* 0.50) son correctos pero débiles: revisar en Fase 2.
3. **Cobertura bib baja (6/23)**: esperada — la KB solo mapea 13 fuentes primarias; los 17 sin match son literatura SotA no atomizada. Dato útil para priorizar atomización.
4. `lecun2022path` vs átomo "LeCun (2023, JEPA)": discrepancia de año KB↔bib; el script lo reporta como match "solo-apellido" en `detail`.
5. Score lexical = coeficiente de solape |∩|/|términos átomo| (contención del átomo), 0–1, determinista; df-cap 10% + stopwords EN/ES/corpus.

## Próximo paso recomendado

Fase 2 sobre el residual de 19 párrafos (prioridad: 11 de 03_proposed_representation): revisión asistida de candidatos `composition` ya propuestos + alias bilingües (p.ej. "sense mask"↔Capa_Sentido_Si) antes de promover `mapping_draft.yaml` a mapping definitivo.
