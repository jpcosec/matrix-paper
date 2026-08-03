# Composition for `review/response1.md` — Reviewer `ppL8`

## Reviewer profile
- Reviewer: `ppL8`
- Rating: `3`
- Main stance: interesting position, but weak support and unclear scalability

## Core objections

### 1. Missing literature on causes of hallucination
Reviewer says the paper makes a representational claim without enough engagement with existing literature.

**Paper-facing support:**
- `Neurips_peiper/sections/01_1_sota.md`
- `Neurips_peiper/sections/01_introduction.md`

**Atom support:**
- [[Dicotomia_HK_Minus_vs_HK_Plus]]
- [[Probing_Latente_y_Decodificacion]]
- [[Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente]]
- [[Barrera_Deteccion_AUROC_Error_Tipo_III]]
- [[Alucinaciones_Inducidas_por_RAG_y_Conflicto_de_Conocimiento]]

**Response stance:**
- Accept the criticism.
- Reframe the paper's claim as narrower:
  - not “continuity causes hallucination”;
  - but “continuous sign embeddings are insufficient as the sole substrate for auditable logical validation”.

### 2. How are `W_i` / `V_i` / `S_i` built at scale?
Reviewer asks how the matrices are created in practice and notes that manual construction is infeasible.

**Paper-facing support:**
- `Neurips_peiper/sections/03_proposed_representation.md`
- `Neurips_peiper/sections/04_discussion.md`
- `Neurips_peiper/sections/09_conclusion.md`

**Atom support:**
- [[Pipeline_Ingesta_Lenguaje_Matrix]]
- [[Anclaje_Simbolos_Grounding]]
- [[Construccion_Tensor_Jerarquico]]
- [[Capa_Verdad_Vi]]
- [[Capa_Sentido_Si]]
- [[Operacion_Validar_Formulacion]]
- [[Operacion_Evaluar_Sentido]]
- [[Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva]]
- [[Emergencia_Estructural_de_Si_en_Cruces_de_Contexto]]

**Spec support:**
- `atoms/composiciones_spec/atom-spec-rule-matrix-compiler.md`
- `atoms/composiciones_spec/atom-spec-canonical-hypertensor.md`
- `atoms/composiciones_spec/atom-spec-meel-engine.md`

**Response stance:**
- Say the paper does **not** assume manual construction.
- Say the intended path is:
  - lowering / feeder stage,
  - compilation into logical coordinates,
  - separate truth and sense evaluation,
  - bounded contexts rather than a universal world-model.
- Also concede that large-scale empirical validation is still pending.

### 3. Why is the problem important?
Reviewer says the paper does not sufficiently motivate the importance of hallucination as a problem for a broad audience.

**Paper-facing support:**
- `Neurips_peiper/sections/00_abstract.md`
- `Neurips_peiper/sections/01_introduction.md`
- `Neurips_peiper/sections/04_discussion.md`

**Atom support:**
- [[Falla_de_Representabilidad]]
- [[Distincion_Ausencia_vs_Unsinnig]]
- [[Benchmarks_y_Metricas_Cuantitativas]]
- [[Matrix_vs_RAG]]

**Response stance:**
- Strengthen the motivation around:
  - factual reliability;
  - category errors;
  - inability of retrieval-only fixes to reject `unsinnig` propositions;
  - need for auditable logic in closed domains.

## What we should not claim
- Do not claim that hallucination is universally explained by continuity alone.
- Do not rely on unpublished repository details.
- Do not promise mature large-scale construction already demonstrated.

## Safe answer in one paragraph
The reviewer is right that the representational claim must be narrower and better situated in the hallucination literature. Our revised position is not that continuity alone explains all hallucination, but that embeddings of signs in continuous spaces do not by themselves provide auditable logical boundaries for validity, truth, and inapplicability. The paper's contribution is therefore a bounded logical substrate with separate truth (`V_i`) and sense (`S_i`) evaluation, together with an intended feeder/compiler pipeline for constructing local worlds rather than a universal semantic universe. We agree that large-scale empirical validation remains future work.
