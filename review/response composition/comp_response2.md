# Composition for `review/response2.md` — Reviewer `ZHLy`

## Reviewer profile
- Reviewer: `ZHLy`
- Rating: `3`
- Main stance: interesting philosophical framing, but unclear implementation and unclear mathematical necessity

## Core objections

### 1. Sense mask during attention is unclear
Reviewer says Section 6 does not provide an implementation or algorithm, and asks what actually happens during training or generation.

**Paper-facing support:**
- `Neurips_peiper/sections/04_discussion.md`
- `Neurips_peiper/sections/09_conclusion.md`

**Atom support:**
- [[Mascara_Sentido_en_Mecanismos_Atencion]]
- [[Integracion_Teorica_con_LLMs_y_Trabajo_Futuro]]
- [[Integracion_LLM_en_Training_e_Inferencia_Aun_No_Demostrada]]
- [[Interrupcion_Decodificacion_Si_Cero]]

**Response stance:**
- Concede this point.
- State clearly:
  - no validated training-time integration is presented;
  - no validated internal inference coupling is presented;
  - Section 6 should be read as future integration work, not as implemented contribution.

### 2. “Functional implementation exists” but details are missing
Reviewer says this matters because Section 6 is otherwise too vague.

**Paper-facing support:**
- `Neurips_peiper/sections/09_conclusion.md`

**Spec support:**
- `atoms/composiciones_spec/atom-spec-canonical-hypertensor.md`
- `atoms/composiciones_spec/atom-spec-meel-engine.md`
- `atoms/composiciones_spec/atom-spec-rule-matrix-compiler.md`

**Response stance:**
- Because of blind-review constraints, do not expose repository-level details.
- Instead anchor the response in:
  - the paper's architecture;
  - the three component specs;
  - the logical roles of feeder/compiler, hypertensor, and engine.
- Do not promise benchmarks or unpublished engineering evidence.

### 3. Why are discrete primitives necessary?
Reviewer asks for mathematical justification and questions whether the argument is only philosophical.

**Paper-facing support:**
- `Neurips_peiper/sections/00_abstract.md`
- `Neurips_peiper/sections/01_introduction.md`
- `Neurips_peiper/sections/02_philosophical_foundation.md`
- `Neurips_peiper/sections/03_proposed_representation.md`

**Atom support:**
- [[Representacion_Continua_vs_Implementacion_Discreta]]
- [[Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable]]
- [[Teorema_Aproximacion_Universal_Hornik]]
- [[Fenomeno_de_Gibbs_en_Funciones_Indicadoras]]
- [[Geometria_de_Politopos_y_Ancho_Acotado_Hanin]]
- [[Fundamento_Logico_aRb]]
- [[Signo_vs_Simbolo]]

**Response stance:**
- Correct the framing.
- The claim is not:
  - “continuity implies hallucination”.
- The claim is:
  - sign-only continuous embeddings do not guarantee auditable logical operations over propositional relations such as `aRb`.
- Discrete primitives matter because the paper's object is logical admissibility, not just semantic similarity.

### 4. Questions about stochasticity, argmax, and probabilistic language
Reviewer questions the meaning of “probabilistic distances”, “probabilistic weights”, and whether deterministic decoding solves the issue.

**Atom support:**
- [[Arquitectura_Neuro_Estocastica]]
- [[Discretizacion_Logica_vs_Continuo]]
- [[Representacion_Continua_vs_Implementacion_Discreta]]
- [[Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable]]

**Response stance:**
- Clarify that the issue is not hardware discreteness.
- Clarify that deterministic decoding does not itself produce logical coordinates.
- Avoid claiming that training is “not stochastic”.

### 5. “Having demonstrated that LLMs can be utilized…”
Reviewer correctly asks where this is demonstrated.

**Paper-facing support:**
- `Neurips_peiper/sections/09_conclusion.md`

**Response stance:**
- Concede that this sentence overstates the evidence.
- Replace with weaker language:
  - the paper sketches a possible lowering interface;
  - it does not demonstrate a general mapping from NL to logic.

## What we should not claim
- No internal Transformer integration is demonstrated.
- No training loss is demonstrated.
- No benchmark on hallucination reduction is demonstrated.
- No code details should be exposed under blind review.

## Safe answer in one paragraph
The reviewer is right that Section 6 currently overreaches relative to what is actually established. Our revised position should separate the core contribution from speculative extensions: the paper contributes a discrete, context-bounded logical substrate with explicit truth and sense evaluation, but it does not yet demonstrate validated integration with LLM training or internal inference. The necessity of discreteness is not a claim that continuity by itself causes hallucination; it is a claim that sign-only continuous embeddings do not by themselves guarantee auditable logical admissibility for relations such as `aRb`. Any stronger claim about training, attention masks, or general NL→logic mapping should be moved to future work.
