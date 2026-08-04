# Delta 3 — Literatura de causas de alucinación (7 papers de `review/related_papers/`)

**Responde a:** Eje A / `ppL8` ("does not cite literature on the cause of hallucinations: EMNLP 2023, ACL 2023, ICLR 2024…"). Los 7 papers tienen PDF + resumen MD en `review/related_papers/`; **ninguno está en `references.bib` ni se cita**.

## DESDE (átomos KB origen + fuentes nuevas)

| Paper | Átomo KB de contenido que lo absorbe |
|---|---|
| mckenna2023 (EMNLP, sources of hallucination) | `Antecedentes/Alucinaciones/Causas_Estructurales_y_de_Entrenamiento.md`, `Origen_Geometrico_y_Espacio_Vectorial.md` |
| yin2023 (ACL, do LLMs know what they don't know) | `Antecedentes/Alucinaciones/Diferenciacion_Factualidad_Conocimiento_Alucinacion.md` |
| marks2024 (COLM, geometry of truth) | `Matematica/Tensores_y_Matriz_Bloques/Geometria_de_Embeddings_y_Canales_Semanticos.md` |
| chen2024 (ICLR, INSIDE hallucination detection) | `Antecedentes/Limites_Espacio_Continuo/Barrera_Deteccion_AUROC_Error_Tipo_III.md`, `Probing_Latente_y_Decodificacion.md` |
| gekhman2024 (EMNLP, finetuning new knowledge) | `Antecedentes/Alucinaciones/Causas_Estructurales_y_de_Entrenamiento.md` |
| kang2025 (NAACL, unfamiliar finetuning) | `Antecedentes/Alucinaciones/Causas_Estructurales_y_de_Entrenamiento.md`, `Ilusion_de_la_Autocorreccion.md` |
| chuang2024 (ICLR, DoLa decoding) | `Antecedentes/Limites_Espacio_Continuo/Probing_Latente_y_Decodificacion.md`, `Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente.md` |

## DESDE+ ampliación KB (referencias adicionales)

| Átomo | Aporte (párrafo SOTA) |
|---|---|
| `Filosofia/Epistemologia_y_Contextos/Taxonomia_SOTA_Alucinaciones.md` | Marco taxonómico de toda la sección SOTA |
| `Filosofia/Epistemologia_y_Contextos/Refactorizacion_SOTA_Paper_NeurIPS.md` | Criterio de selección de fuentes citadas |
| `Antecedentes/Alucinaciones/Entropia_Semantica.md` | Línea de detección por incertidumbre (Farquhar et al.) |
| `Antecedentes/Alucinaciones/Evaluacion_Epistemica_FActScore_HaluEval.md` | Línea de benchmarks (FActScore/HaluEval) |
| `Antecedentes/Alucinaciones/Sicofancia_y_Problemas_del_RLHF.md` | Causas de entrenamiento (RLHF) |
| `Antecedentes/Alucinaciones/Alucinaciones_Inducidas_por_RAG_y_Conflicto_de_Conocimiento.md` | RAG no resuelve: conflicto de conocimiento |
| `Antecedentes/Alucinaciones/Alucinaciones_Multi_Agente_y_Context_Drift.md` | Deriva de contexto multi-agente |
| `Antecedentes/Alucinaciones/Falla_de_Representabilidad.md` | Falla de representabilidad como causa raíz |
| `Antecedentes/Limites_Espacio_Continuo/Infidelidad_del_Razonamiento_en_Prosa_y_la_Ilusion_de_Pensar.md` | Infidelidad del razonamiento en prosa (McKenna) |
| `Antecedentes/Limites_Espacio_Continuo/Semantica_Formal_Neuro_Simbolica_vs_Opacidad_Neuronal.md` | Marco neuro-simbólico del párrafo de cierre |
| `Antecedentes/Limites_Espacio_Continuo/Comparacion_Arquitecturas_JEPA.md` | Contraste con arquitecturas de world-model (JEPA) |
| `Filosofia/Epistemologia_y_Contextos/Modelos_Mundo_Continuo_Lyre.md` | Lyre et al.: world models continuos |
| `Computacion/Optimizacion_y_Seguridad/Matrix_vs_Verificacion_Formal.md` | Contraste con verificación formal clásica |

**Extensión mapping (bridge `delta3_review`):**
- `01_1_sota-p01`: `Taxonomia_SOTA_Alucinaciones` (0.9), `Refactorizacion_SOTA_Paper_NeurIPS` (0.85), `Evaluacion_Epistemica_FActScore_HaluEval` (0.8).
- `01_1_sota-p02`: `Sicofancia_y_Problemas_del_RLHF` (0.8), `Entropia_Semantica` (0.8), `Falla_de_Representabilidad` (0.8), `Infidelidad_del_Razonamiento_en_Prosa_y_la_Ilusion_de_Pensar` (0.8).
- `01_1_sota-p03`: `Alucinaciones_Multi_Agente_y_Context_Drift` (0.75).
- `01_1_sota-p05` (RAG/cierre): `Alucinaciones_Inducidas_por_RAG_y_Conflicto_de_Conocimiento` (0.85), `Semantica_Formal_Neuro_Simbolica_vs_Opacidad_Neuronal` (0.8), `Matrix_vs_Verificacion_Formal` (0.75), `Comparacion_Arquitecturas_JEPA` (0.7), `Modelos_Mundo_Continuo_Lyre` (0.7).

## HACIA (párrafos destino — todos en `01_1_sota.md`, sin párrafos nuevos)

| Párrafo (anchor hoy) | Papers a insertar |
|---|---|
| `Epistemic Evaluation and Probabilistic Detection` (p02) | mckenna2023, yin2023 |
| `Internal Representations and Latent Probing` (p03) | marks2024, chen2024, chuang2024 |
| `Behavioral Interventions and Model Collapse` (p04) | gekhman2024, kang2025 |

**No requiere anexo** (1 frase por párrafo).

## Propuesta de texto

**p02** — añadir tras `…to estimate when a model is confabulating [@semantic_entropy2024].`:
```markdown
Complementary work traces these errors to their origin: hallucinations are not random noise but follow from co-occurrence biases in pretraining data that continuous representations fail to bound deductively [@mckenna2023], and from a measurable gap between what models internally know and what they can reliably verbalize [@yin2023].
```

**p03** — añadir tras la frase insertada por delta 2 (o al final si delta 2 no se aplica):
```markdown
Linear probing indeed recovers emergent truth directions, though they degrade as logical structure grows complex [@marks2024]; internal-state scores such as EigenScore detect hallucination risk but only post-hoc [@chen2024]; and decoding-time corrections that contrast final against premature layers (DoLa) mitigate symptoms without altering the continuous substrate that produced them [@chuang2024].
```

**p04** — añadir tras `…known as model collapse [@shumailov2024; @kommers2025slop].`:
```markdown
The same fragility appears during adaptation: fine-tuning on knowledge unfamiliar to the pretrained model systematically induces hallucinated factual completions [@gekhman2024; @kang2025], suggesting that continuous weight updates cannot mark the boundary between acquired knowledge and confabulation.
```

## bib — 7 entradas nuevas para `references.bib`

```bibtex
@inproceedings{mckenna2023, title={Sources of Hallucination by Large Language Models on Inference Tasks}, author={McKenna, Nick and Li, Tianyi and Cheng, Liang and Hosseini, Mohammad Javad and Johnson, Mark and Steedman, Mark}, booktitle={Findings of EMNLP}, year={2023}}
@inproceedings{yin2023, title={Do Large Language Models Know What They Don't Know?}, author={Yin, Zhangyue and Sun, Qiushi and Guo, Qipeng and Wu, Jiawen and Qiu, Xipeng and Huang, Xuanjing}, booktitle={Findings of ACL}, year={2023}}
@inproceedings{marks2024, title={The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets}, author={Marks, Samuel and Tegmark, Max}, booktitle={COLM}, year={2024}}
@inproceedings{chen2024, title={INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection}, author={Chen, Chao and Liu, Kai and Chen, Ze and Gu, Yi and Wu, Yue and Tao, Mingyuan and Fu, Zhihang and Ye, Jieping}, booktitle={ICLR}, year={2024}}
@inproceedings{gekhman2024, title={Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?}, author={Gekhman, Zorik and Yona, Gal and Aharoni, Roee and Eyal, Matan and Feder, Amir and Reichart, Roi and Herzig, Jonathan}, booktitle={EMNLP}, year={2024}}
@inproceedings{kang2025, title={On Familiarity-Aware Fine-Tuning and Hallucination in LLMs}, author={Kang, Katie and Wallace, Eric and Tomlin, Claire and Kumar, Aviral and Levine, Sergey}, booktitle={NAACL}, year={2025}}
@inproceedings{chuang2024, title={DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models}, author={Chuang, Yung-Sung and Xie, Yujia and Luo, Hongyin and Kim, Yoon and Glass, James and He, Pengcheng}, booktitle={ICLR}, year={2024}}
```
⚠️ Verificar títulos exactos de kang2025 y chuang2024 contra los PDFs de `review/related_papers/` (tengo autores/venue de los resúmenes; el título de kang lo reconstruí del nombre de archivo).

## Átomos nuevos (7) vía `atomize_sources.py`
`Source_PDF_{mckenna2023,yin2023,marks2024,chen2024,gekhman2024,kang2025,chuang2024}_pdf.md`. Bonus: estos PDFs **sí están en el repo** (`review/related_papers/*.pdf`) → referenciarlos en el átomo con ruta real en vez de "PDF no presente".

## mapping.yaml (añadir)
- `01_1_sota-p02`: bib mckenna2023, bib yin2023 + `Causas_Estructurales_y_de_Entrenamiento` (0.85), `Diferenciacion_Factualidad_Conocimiento_Alucinacion` (0.8) — bridge `delta3_review`.
- `01_1_sota-p03`: bib marks2024, bib chen2024, bib chuang2024 + `Geometria_de_Embeddings_y_Canales_Semanticos` (0.8) — `Probing_Latente_y_Decodificacion` y `Barrera_Deteccion_AUROC` ya llegan por delta 2 / delta 1.
- `01_1_sota-p04`: bib gekhman2024, bib kang2025 + `Causas_Estructurales_y_de_Entrenamiento` (0.85), `Ilusion_de_la_Autocorreccion` (0.75).

## Riesgos
- Añade ~120 palabras a una sección ya larga → vigilar page budget (ver README).
