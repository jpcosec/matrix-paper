# Análisis de estructura y ruteo de átomos

## 1. Árbol con claims

### Introduction [4]
- **p01** The rapid advancement of Large Language Models (LLMs) has demonstrated an unprecedented capacity for fluent te…
  ⚓ symbol, source-pdf-harnad1990symbolgrounding
- **p02** To address this representational gap, this paper argues for the necessity of a discrete, locally scoped repres…
  ⚓ tractatus, triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig
- **p03** By treating the validity of assertions as a problem of representability within a strict grammar of sense, we p…
  ⚓ wigame-wi
- **p04** Ultimately, instead of attempting to teach models not to lie through continuous probabilistic weights, this wo…
  ⚓ matrices-y-tensores

### State of the Art: Hallucination Mitigation and Representational Geometries [8]
- **p01** The generation of factually incorrect or logically inconsistent statements in Large Language Models (LLMs)—com…
  ⚓ taxonomia-sota-alucinaciones
- **p02** **Epistemic Evaluation and Probabilistic Detection** A significant portion of the literature focuses on auditi…
  ⚓ source-pdf-factscore2023-pdf, evaluacion-epistemica-factscore-halueval, sicofancia-y-problemas-del-rlhf, source-pdf-halueval2023, source-pdf-semantic-entropy2024
- **p03** **Internal Representations and Latent Probing** Latent probing reveals a fundamental discrepancy between inter…
  ⚓ source-pdf-iclr2025-a712d4-pdf, dicotomia-hk-minus-vs-hk-plus, source-pdf-simhi2024distinguishing, incongruencia-decodificacion-estocastica-vs-conocimiento-latente, probing-latente-y-decodificacion
- **p04** **Behavioral Interventions and Model Collapse** The recursive ingestion of synthetic, AI-generated content (of…
  ⚓ source-pdf-nature-shumailov2024-pdf, causas-estructurales-y-de-entrenamiento, Source_PDF_nature_shumailov2024_pdf, source-pdf-kommers2025slop
- **p05** **Semantic Grounding and Continuous World Models** From a philosophical and cognitive perspective, recent lite…
  ⚓ modelos-mundo-continuo-lyre, source-pdf-bender2020, source-pdf-lyre2024understanding
- **p06** **Neuro-Symbolic Approaches and Knowledge Graphs** Recognizing the limits of purely probabilistic reasoning, t…
  ⚓ source-pdf-symcode2025-pdf, source-pdf-vossel2025advancing-pdf, Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva, Matrix_vs_Neuro_Simbolicos_Previos, falla-de-representabilidad, ilusion-de-la-autocorreccion, source-pdf-ibrahim2026, source-pdf-ferrone2019, source-pdf-liu2025code4logic, source-pdf-choi2025knowledge, source-pdf-bian2025llm
- **p07** **Why Continuous Spaces Offer No Guarantee of Logical Validity** The case for discrete primitives rests on thr…
  ⚓ fenomeno-de-gibbs-en-funciones-indicadoras, geometria-de-politopos-y-ancho-acotado-hanin, barrera-deteccion-auroc-error-tipo-iii, representacion-continua-vs-implementacion-discreta
- **p08** While these current methodologies offer significant advancements, they fundamentally rely on continuous vector…
  ⚓ wigame-wi, source-pdf-wittgenstein1922

### 02 Philosophical Foundation [7]
- **p01** Wittgenstein's Tractatus opens with an interesting phrase: **the world is composed of all facts, not things**.…
  ⚓ thing, tractatus
- **p02** A proposition is a description of a fact in relation to reality; a fact that is expressed perceptibly through …
  ⚓ fact, proposition
- **p03** * *Sinnvoll*: propositions that are meaningful and capable of representing a possible situation in the world. …
  ⚓ triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig, categorias-sentido
- **p04** * *Sinnlos*: propositions that say nothing about the world but legitimately belong to logical symbolism, such …
  ⚓ triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig, categorias-sentido
- **p05** * *Unsinnig*: formulations without logical meaning, where the symbols have not been given a significant functi…
  ⚓ 06_Absurdo_Unsinnig_como_Violacion_Sintactica, triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig
- **p06** A sign is the perceptible medium that allows the mapping and transmission of a fact, an object, or their relat…
  ⚓ fact
- **p07** A symbol is a sign and a structure within a logical space, used within a context; that is, within a sufficient…
  ⚓ context-ci, symbol

### Proposed representation [27]
- **p01** Consider the logical structure of a partition of the world $W_i$ by the following symbolic set:
  ⚓ wigame-wi
- **p02** 1. A context, that is, a partition over the world $W$ that limits what belongs into $W_i$. 2. A logical space …
  ⚓ context-ci, relation-ri, logicalspace-li, wigame-wi
- **p03** [FIGURE fig_anatomy]
  ⚓ signo-vs-simbolo, logicalspace-li, context-ci, relation-ri, capa-sentido-si, capa-verdad-vi, w-operativo, wigame-wi
- **p04** Then, we can define $W_i$ as the boolean AND operation between $V_i$ and $S_i$ (see Figure~\ref{fig:anatomy}).…
  ⚓ wigame-wi
- **p05** | | vegetable | food | leaf | root | stem | | ------- | --------- | ---: | ---: | ---: | ---: | | lettuce | 1 …
  ⚓ capa-verdad-vi, tabla-de-verdad
- **p06** It is important to note that within this logical space, the properties "vegetable" and "food" are true for all…
  ⚓ tractatus, wigame-wi
- **p07** | | lettuce | spinach | carrot | celery | | ---- | ------: | ------: | -----: | -----: | | leaf | 1 | 1 | 0 | …
  ⚓ proyeccion-tensorial, capa-verdad-vi
- **p08** If we designate a Boolean semiring AND/OR over this space, we can verify some useful results.
  ⚓ semianillo-booleano
- **p09** * If we perform matrix multiplication of $W^T_i \otimes W_i$, we can obtain a map of property co-occurrences. …
  ⚓ wigame-wi
- **p10** We return to Wittgenstein for a moment; what are the logical restrictions of this system? They are those given…
  ⚓ Triparticion_Wittgensteiniana_Sinnvoll_Sinnlos_Unsinnig
- **p11** * Tautology, when the property returns a positive result in all cases, like the properties food and vegetable …
  ⚓ triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig
- **p12** * Contradiction, when the search vector yields a combination of properties that returns no object, as would be…
  ⚓ triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig
- **p13** On the other hand, the category of *unsinnig*, in our case, would correspond to operations that are not possib…
  ⚓ logicalspace-li
- **p14** Up to this point, the proposed system aligns with standard Boolean logic without offering anything new to the …
  ⚓ logicalspace-li, inferencia-deductiva-matricial
- **p15** We first address its extensibility. Extending $W_i$ to contain new facts is a straightforward operation. If th…
  ⚓ fact, proposition, logicalspace-li, wigame-wi
- **p16** Regarding ambiguity in $W_i$, the proposed system allows the detection of it through an elementary algebraic o…
  ⚓ wigame-wi
- **p17** * $W_i \otimes W^T_i$ yields a matrix of objects against objects, containing all the facts that denote some tr…
  ⚓ wigame-wi
- **p18** * $(W_i \otimes W^T_i) - \mathbb{I}$ clears the diagonal, which contains only tautological results.
  ⚓ wigame-wi
- **p19** * Finally, by dimensionally collapsing this matrix by multiplying it by a vector of ones, we can detect those …
  ⚓ Colapso_Dimensional
- **p20** Then, to disambiguate these objects, we introduce a new property to $L_i$ that will allow differentiating them…
  ⚓ logicalspace-li
- **p21** | | leaf | root | stem | (leaf) rough | (leaf) smooth | | ------- | ---: | ---: | ---: | -----------: | ------…
  ⚓ Distincion_Ausencia_vs_Unsinnig, diccionario-bits-y-codificacion, capa-verdad-vi
- **p22** Another detail becomes apparent: if we make a partition defined by the objects lettuce and spinach, and the pr…
  ⚓ operacion-particionar, triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig, Distincion_Ausencia_vs_Unsinnig
- **p23** * Use a sense mask $S_i$ around the facts that are indexable by these objects and properties, setting the resu…
  ⚓ capa-sentido-si, mascaras-estructurales
- **p24** * Create another matrix $W_i'$ that indexes only leafy vegetables. Then, the operation to search for vegetable…
  ⚓ Matrices_Puras
- **p25** This yields some interesting results:
  ⚓ —
- **p26** - $W_i$ is basically a hierarchical routing space that partitions $W_i \cup W'_i$, in other words, a context i…
  ⚓ context-ci, relation-ri, logicalspace-li
- **p27** In Wittgenstein's words, we have defined a direct projection between thought and its logical image, represente…
  ⚓ diccionario-bits-y-codificacion, algebra-booleana, proyeccion-tensorial

### Discussion [12]
- **p01** The task of processing text and extracting semantic logic from it has no novelty. Mapping facts and relations …
  ⚓ tractatus, matrices-y-tensores
- **p02** # Relationship with Language
  ⚓ —
- **p03** Existing works often translate language into logical forms, graphs, or inference tasks; however, they do not a…
  ⚓ source-pdf-vossel2025advancing-pdf, context-ci, Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva, Matrix_vs_Neuro_Simbolicos_Previos, infidelidad-del-razonamiento-en-prosa-y-la-ilusion-de-pensar, source-pdf-liu2025code4logic, source-pdf-lee2025entailment, source-pdf-choi2025knowledge, source-pdf-cheng2025empowering, source-pdf-bian2025llm, source-pdf-liang2025survey
- **p04** Two families of neighboring work clarify what is new here. Retrieval pipelines and knowledge graphs capture *s…
  ⚓ context-ci, gramatica-universal-unl
- **p05** An interesting first approach to semantics in language is that the formalization proposed in this work would a…
  ⚓ signo-vs-simbolo, anclaje-simbolos-grounding, representacion-flotante
- **p06** An important limitation to note at this point is that, as the treatise anticipates, the distinction between th…
  ⚓ algebra-booleana, algebra-de-boole
- **p07** Furthermore, a little-explored feature of language is that, by defining a closed set of signs and facts, the m…
  ⚓ —
- **p08** # Relationship with LLM
  ⚓ mascara-sentido-en-mecanismos-atencion, capa-sentido-si
- **p09** An interesting approach to how this proposal relates to the burgeoning field of neural network language models…
  ⚓ context-ci
- **p10** On the other hand, by introducing context as a limit to the family of texts we can unite in a logically *sinnv…
  ⚓ source-pdf-lecun-jepa2023-pdf, comparacion-arquitecturas-jepa, source-pdf-dawid2024latent, source-pdf-assran2023ijepa
- **p11** This last point aligns directly with what LeCun and colleagues have been proposing in JEPA and H-JEPA [@lecun2…
  ⚓ context-ci, fact
- **p12** Finally, one might ask whether a logic machine with sufficient "knowledge" could replace what LLMs can do toda…
  ⚓ —

### Conclusion [3]
- **p01** In conclusion, this paper has presented a formal framework to bridge the relationship between natural language…
  ⚓ algebra-booleana, algebra-de-boole
- **p02** While the body of this work has focused on establishing the theoretical and algebraic foundations of this mode…
  ⚓ algebra-booleana, wigame-wi
- **p03** Future work will focus on closing this computational loop. Having demonstrated that LLMs can be utilized to ma…
  ⚓ mascara-sentido-en-mecanismos-atencion, categorias-sentido

### Appendix [18]
- **p01** ## On the Geometric Origin of Hallucinations \label{app:hallucinations}
  ⚓ —
- **p02** To understand why continuous semantic spaces struggle with factual accuracy, we can look at how the literature…
  ⚓ —
- **p03** **Type I: Infidelity (Contextual Deviation)** This occurs when the generation strays from the provided context…
  ⚓ —
- **p04** **Type II: Confabulation (Domain Mismatch)** This happens when the model hallucinates a completely unrelated t…
  ⚓ —
- **p05** **Type III: Factual Error (In-Channel Falsehood)** This is the most pernicious error: the model generates an i…
  ⚓ —
- **p06** The geometric detectability of Types I and II often creates the "Self-Correction Illusion" [@symcode2025]—the …
  ⚓ —
- **p07** ## On the Limits of Continuous Approximation \label{app:continuous}
  ⚓ —
- **p08** This appendix details the three observations from Section 2. The first two establish inescapable mathematical …
  ⚓ —
- **p09** ### Indicator boundaries and inescapable oscillation
  ⚓ —
- **p10** Let $f: \mathbb{R}^d \to \{0,1\}$ indicate logical validity, discontinuous at the boundary of its support. Uni…
  ⚓ —
- **p11** ### Polytope tiling at bounded width
  ⚓ —
- **p12** A ReLU network is piecewise affine: each neuron's activation boundary is a hyperplane, and their arrangement p…
  ⚓ —
- **p13** $$\mathcal{N}(w, L) \le \sum_{j=0}^{d} \binom{wL}{j},$$
  ⚓ —
- **p14** which grows polynomially in $L$ [@hanin2017universal]. Sense boundaries, by contrast, are typically non-convex…
  ⚓ —
- **p15** ### The soft boundary of current embedding techniques
  ⚓ —
- **p16** If factual errors were outliers in embedding space, post-hoc detection would be easy. However, probing studies…
  ⚓ —
- **p17** ### On deterministic decoding
  ⚓ —
- **p18** `argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wron…
  ⚓ —


## 2. Ruteo de átomos (átomo → párrafos)

### 2a. Átomos dispersos (aparecen en >1 sección)

- `wigame-wi` (Computacion) → 01·p03, 01·p08, 03·p01, 03·p02, 03·p03, 03·p04, 03·p06, 03·p09, 03·p15, 03·p16, 03·p17, 03·p18, 09·p02
- `context-ci` (Computacion) → 02·p07, 03·p02, 03·p03, 03·p26, 04·p03, 04·p04, 04·p09, 04·p11
- `triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig` (Filosofia) → 01·p02, 02·p03, 02·p04, 02·p05, 03·p11, 03·p12, 03·p22
- `tractatus` (Filosofia) → 01·p02, 02·p01, 03·p06, 04·p01
- `fact` (Computacion) → 02·p02, 02·p06, 03·p15, 04·p11
- `algebra-booleana` (Matematica) → 03·p27, 04·p06, 09·p01, 09·p02
- `categorias-sentido` (Filosofia) → 02·p03, 02·p04, 09·p03
- `capa-sentido-si` (Computacion) → 03·p03, 03·p23, 04·p08
- `symbol` (Computacion) → 01·p01, 02·p07
- `matrices-y-tensores` (Matematica) → 01·p04, 04·p01
- `source-pdf-vossel2025advancing-pdf` (Fuentes) → 01·p06, 04·p03
- `Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva` (Computacion) → 01·p06, 04·p03
- `Matrix_vs_Neuro_Simbolicos_Previos` (Computacion) → 01·p06, 04·p03
- `source-pdf-liu2025code4logic` (Fuentes) → 01·p06, 04·p03
- `source-pdf-choi2025knowledge` (Fuentes) → 01·p06, 04·p03
- `source-pdf-bian2025llm` (Fuentes) → 01·p06, 04·p03
- `proposition` (Computacion) → 02·p02, 03·p15
- `signo-vs-simbolo` (Filosofia) → 03·p03, 04·p05
- `algebra-de-boole` (Matematica) → 04·p06, 09·p01
- `mascara-sentido-en-mecanismos-atencion` (Computacion) → 04·p08, 09·p03

### 2b. Átomos muy repetidos (≥3 párrafos)

- `wigame-wi` → 01·p03, 01·p08, 03·p01, 03·p02, 03·p03, 03·p04, 03·p06, 03·p09, 03·p15, 03·p16, 03·p17, 03·p18, 09·p02
- `context-ci` → 02·p07, 03·p02, 03·p03, 03·p26, 04·p03, 04·p04, 04·p09, 04·p11
- `triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig` → 01·p02, 02·p03, 02·p04, 02·p05, 03·p11, 03·p12, 03·p22
- `logicalspace-li` → 03·p02, 03·p03, 03·p13, 03·p14, 03·p15, 03·p20, 03·p26
- `tractatus` → 01·p02, 02·p01, 03·p06, 04·p01
- `fact` → 02·p02, 02·p06, 03·p15, 04·p11
- `capa-verdad-vi` → 03·p03, 03·p05, 03·p07, 03·p21
- `algebra-booleana` → 03·p27, 04·p06, 09·p01, 09·p02
- `categorias-sentido` → 02·p03, 02·p04, 09·p03
- `relation-ri` → 03·p02, 03·p03, 03·p26
- `capa-sentido-si` → 03·p03, 03·p23, 04·p08

## 3. Perfil de familias por sección (nº anclas)

| sección | Antecedentes | Computacion | Filosofia | Fuentes | Isomorfismo_Tractatus_Algebra | Matematica |
|---|---|---|---|---|---|---|
| Introduction |  | 2 | 2 | 1 |  | 1 |
| State of the Art: Ha | 9 | 3 | 3 | 18 |  | 2 |
| 02 Philosophical Fou |  | 6 | 6 |  | 1 |  |
| Proposed representat |  | 40 | 6 |  |  | 6 |
| Discussion | 2 | 11 | 3 | 10 |  | 3 |
| Conclusion |  | 2 | 1 |  |  | 3 |

## 4. Solapamiento de átomos entre secciones (Jaccard)

- Introduction ↔ 02 Philosophical Foundat: J=0.25 comparten: symbol, tractatus, triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig
- 02 Philosophical Foundat ↔ Proposed representation: J=0.18 comparten: context-ci, fact, proposition, tractatus, triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig
- Proposed representation ↔ Discussion: J=0.14 comparten: algebra-booleana, capa-sentido-si, context-ci, fact, signo-vs-simbolo, tractatus
- Introduction ↔ Proposed representation: J=0.11 comparten: tractatus, triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig, wigame-wi
- State of the Art: Halluc ↔ Discussion: J=0.11 comparten: Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva, Matrix_vs_Neuro_Simbolicos_Previos, source-pdf-bian2025llm, source-pdf-choi2025knowledge, source-pdf-liu2025code4logic, source-pdf-vossel2025advancing-pdf
- Discussion ↔ Conclusion: J=0.11 comparten: algebra-booleana, algebra-de-boole, mascara-sentido-en-mecanismos-atencion
- Introduction ↔ Conclusion: J=0.10 comparten: wigame-wi
- 02 Philosophical Foundat ↔ Discussion: J=0.09 comparten: context-ci, fact, tractatus