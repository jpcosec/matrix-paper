# Appendix



To understand why continuous semantic spaces struggle with factual accuracy, we can look at how the literature maps hallucinations to their geometric origins in the embedding space $\mathbb{R}^d$. Recent evaluation frameworks classify structural generation errors into three geometric types based on their spatial behavior within semantic submanifolds [@wei2024measuring; @sansford2024grapheval]:

**Type I: Infidelity (Contextual Deviation)**
This occurs when the generation strays from the provided context or the required semantic channel. Geometrically, the output vector drifts away from the target submanifold. Because this represents a significant spatial deviation, Type I errors are readily detectable using standard continuous distance metrics (e.g., cosine distance) or entropy measurements, typically yielding an AUROC $> 0.80$ [@wei2024measuring].

**Type II: Confabulation (Domain Mismatch)**
This happens when the model hallucinates a completely unrelated topic or bizarre assertion. Geometrically, these outputs fall far outside the expected distribution. Like Type I errors, Type II errors are easily flagged as out-of-distribution anomalies using continuous metrics (AUROC $> 0.75$).

**Type III: Factual Error (In-Channel Falsehood)**
This is the most pernicious error: the model generates an incorrect fact while staying perfectly within the correct conceptual framework. Because semantically related truths and falsehoods share the same geometrical neighborhood, Type III errors reside *inside* the typical channel of the representation. As demonstrated by Wei et al., linear discrimination for these in-channel errors performs close to chance (AUROC $\approx 0.478$) [@wei2024measuring].

The geometric detectability of Types I and II often creates the "Self-Correction Illusion" [@symcode2025]—the belief that scaling or better continuous monitoring will eventually solve all hallucinations. However, the AUROC barrier of Type III errors demonstrates a structural limit of current spatial paradigms: continuous distance encodes statistical co-occurrence, not factual truth. Resolving Type III errors therefore requires stepping outside the continuous spatial paradigm and introducing a discrete verification step.



This appendix details the three observations from Section 2. The first two establish inescapable mathematical limits when using continuous functions and bounded-width architectures to approximate discrete logic. The third observation highlights an empirical failure specific to current embedding methodologies rather than an absolute impossibility result for neural networks.

### Indicator boundaries and inescapable oscillation

Let $f: \mathbb{R}^d \to \{0,1\}$ indicate logical validity, discontinuous at the boundary of its support. Universal approximation results [@hornik1991approximation] guarantee convergence in $L^1$ / in measure: the *mass* of the error region can be made arbitrarily small. Convergence is not uniform, however: near a jump, any smooth or piecewise-smooth approximator exhibits a transition band with overshoot—the Gibbs phenomenon, whose classical overshoot is $\approx 8.95\%$ of the jump magnitude. Narrowing the band requires steeper activations and more units, but the band does not vanish with more data or training; it is a fundamental mathematical property of approximating a jump with continuous functions. In semantic terms, this inescapable limit means there is always a region where *Unsinn* receives an intermediate score instead of a strict exclusion.

### Polytope tiling at bounded width

A ReLU network is piecewise affine: each neuron's activation boundary is a hyperplane, and their arrangement partitions $\mathbb{R}^d$ into convex polytopes on which the network is linear. For width $w \le d$ and depth $L$, the number of regions is bounded by

$$\mathcal{N}(w, L) \le \sum_{j=0}^{d} \binom{wL}{j},$$

which grows polynomially in $L$ [@hanin2017universal]. Sense boundaries, by contrast, are typically non-convex and disconnected: type constraints over symbols combine combinatorially, so the set of _sinnvoll_ propositions scatters across many disconnected regions. Tiling such a set with convex cells requires a number of regions exponential in the number of constraints. While unbounded networks could theoretically escape this limit, any bounded-width network inevitably suffers from a structural deficit. This inescapably forces logical interference at categorical frontiers, making it an absolute limit within practical architectural constraints.

### The soft boundary of current embedding techniques

If factual errors were outliers in embedding space, post-hoc detection would be easy. However, probing studies find that factual errors—incorrect facts within the correct conceptual framework—reside inside the typical channel of the representation. Here, linear discrimination performs close to chance (AUROC $\approx 0.478$) [@wei2024measuring]. Unlike the first two mathematical limits, this represents a soft boundary of current spatial methodologies: distance metrics in embedding spaces encode statistical co-occurrence, not factual correspondence. Because semantically related truths and falsehoods share the same geometrical neighborhood, current continuous scalar reads fail to reliably separate valid from invalid generations—motivating a check that lives outside the continuous substrate.

### On deterministic decoding

`argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wrong *reproducibly*, with no sampling randomness to blame. This cuts both ways—stochastic decoding is not the culprit either; both inherit the substrate. The design conclusion is that the boundary must be imposed *before* decoding, at compile time, where a stored Boolean matrix $S_i$ provides an exact check in $O(1)$ per step instead of an approximate one distributed across the network.



### Formal backbone: logical form as a matrix

In the Tractarian reading that structures our substrate, logical form—"the possibility of structure" (2.033)—is instantiated as the syntax matrix $S_i$: an adjacency operator over the object layer $V_i$ that restricts which combinations are structurally possible *before* any truth evaluation, $\text{PossibleStructure} = \sigma(V_i \times S_i)$. Atomic facts are minterms—exhaustive boolean conjunctions over the base variables, stored operatively as (concept, dimension, discriminative value) tuples, e.g., `(lettuce, edible_part, leaf)`—so the world is the tensor region of active minterms. A proposition has *sense* (Sinn) iff it partitions minterm space properly (neither the all-ones tautology nor the all-zeros contradiction; those are *sinnlos*, senseless); it is *unsinnig* when it falls outside the span of $S_i$ altogether—a type violation, rejected at compilation, not a falsehood. Figure~\ref{fig:signsymbol} pictures the sign/symbol periphery (\S2) and the semantic index $L_i(C_i,R_i)$ that assigns integer coordinates; the two boolean layers $S_i$, $V_i$ and their queryable product are Figure~\ref{fig:layers} (\S1).

![From signs to coordinates. Perceptible signs—the word *perro*, the word *dog*, a dog pictogram—converge through the decomposition stage (sign$\to$symbol resolution and alias folding) onto a single symbol: one position in logical space, independent of language. The semantic index $L_i(C_i,R_i)$ then fixes its integer coordinate on an axis of the context grid. The system computes over coordinates, never over signs. \label{fig:signsymbol}](../figures/fig_sign_symbol.png){width=100%}

### Closed representations

A context $w_i$ is *closed* when its axes are typed locally: objects on each axis belong to the same local type and the context's rules range only over its own symbols. Within a closed context $S_i$ is near-trivial—almost all coordinates are admissible, and the real question is factual ($V_i \in \{\text{true}, \text{false}, \emptyset\}$). Sense structure becomes necessary exactly when contexts are *crossed*: objects of one domain with properties of another. Crossings then fall into three classes—*sinnvoll* (admissible), *don't care* (outside the subcontext, not evaluated), and *unsinnig* (violates categorial structure). A type layer $T_i$ validates that relational signatures align before any composition $W_1 \otimes p \otimes W_2$ is allowed, so $S_i=0$ cannot arise from accidental context incongruence: it is structurally emergent, and therefore derivable from the schemas rather than hand-listed.

### The omnirepresentation

Composition is realized in a single block matrix, the *omnirepresentation*, laid out in four quadrants: the top-left $m \times m$ quadrant ($WC_i$) routes and activates contexts; the top-right and bottom-left $m \times n$ quadrants hold don't-care membership blocks routing which facts belong to which context—this routing *is* the sense mask at composition level; and the bottom-right $n \times n$ quadrant holds the empirical truth matrix. Globally, knowledge exists as one canonical hypertensor $N \times |R| \times N$; operationally it materializes as a graph of dense 2D sub-matrices extracted by tensorial projection, alternating between the flat empirical view ($V_i, S_i$) and the hierarchical tensorial view in which global attributes are promoted to routing hyperdimensions. This form provides the flexibility the internal "pure matrix" engine deliberately lacks: $S_i$ can be applied over *unions of contexts* by activating several routing entries; the whole structure is a flat, ingestible view a stochastic model can read and write (massive I/O interface for LLMs); and any external computation—an LLM's candidate facts, a matrix calculation over embeddings—can be checked against the same blocks without format conversion.

### Operational ingestion pathway \label{app:ingestion}

From natural language to an audited proposition, four stages:

1. **Decomposition into standard form.** The utterance is decomposed into its meaning plus syntactic sugar, and the meaning is expressed in a standardized representation—S-expressions, RDF/Turtle, or OWL. We propose small LLMs as surface decomposers: they absorb sign variability (including sign-to-symbol resolution and alias folding) but make no logical decisions.
2. **Reduction to candidate propositions.** The standard form is lowered to homogeneous candidate propositions `(R a b)`—e.g., `(sound dog barks)`, `(sound cat meows)`. Nothing here is asserted yet; candidates have no truth status.
3. **Two-step sense check.** (a) *Context indexing:* the candidate is routed to the context(s) that index its cross; if no context admits the (domain, relation) combination, the candidate is rejected as *Unsinnig*—absurdity is avoided by construction, before any truth evaluation. (b) *Contradiction check:* admissible candidates are checked against the existing facts $V_i$ of their context; a conflict with what is already asserted yields an explicit contradiction signal rather than silent overwrite.
4. **Matrix computation.** Only candidates passing both checks update or consult $V_i$; inference proceeds by boolean matrix multiplication and bitwise dimensional collapse, yielding $W_i^{*} = V_i \odot S_i$.

*Worked example.* *"The edible part of lettuce is the leaf"* is decomposed and reduced to the candidate `(edible_part lettuce leaf)`. Context indexing routes it to the food context, which admits the cross (3a passes); no conflicting fact exists in $V_i$ (3b passes); the tuple is asserted and participates in closure. By contrast, `(has_color electron red)` fails step 3a in any closed physical-entity context—the (particle, color) cross violates categorial structure—and is rejected as *unsinnig* before a truth value can attach. Finally, `(sound cat barks)` submitted after `(sound cat meows)` was asserted passes 3a (the cross is admissible) but fails 3b: the system reports an explicit contradiction instead of silently overwriting the earlier fact.

### Self-optimization: $E(R)$ minimization and the hierarchical tensor \label{app:er}

Construction is not manual $\mathcal{O}(N^2)$—and a purely diagonal index is provably suboptimal, collapsing asymptotically to $E(R) \to 0.5$. Two deterministic mechanisms keep the substrate compact:

- **Information-energy minimization.** The engine scores each logical space with $E(R) = \frac{1}{4}(c + i + o + d)$—sense density, facticity, observed-fact rate, and discriminative power—and applies mutations only when $\Delta E(R) > 0$: constant (tautological) columns are promoted to tensor gates, contexts whose sense density drops are split into clean sub-contexts, and collisions in $W_i \otimes W_i^{T} - \mathbb{I}$ trigger injection of a minimal separating dimension. This is a deterministic analogue of training, run as maintenance after bulk ingestion.
- **Hierarchical tensor construction.** A common attribute (e.g., `is_vegetal`) becomes a partition dimension $C_k$; entities are factored into child sub-tensors linked by routing projections $WC_k$, and multi-hop queries navigate $P = WC_1 \otimes \dots \otimes WC_k$, reducing spatial complexity toward $\mathcal{O}(N \log N)$.

### Sense-mask integration with stochastic models \label{app:mask}

The mask enters at two levels. *At runtime*, the engine rejects deterministically at three checkpoints—`ingest`, `check`, `assert`: a proposition with $S_i = 0$ never enters the veritative system, and the caller receives an explicit `reject (unsinnig)` signal; generation whose continuations all fail is halted and reported as unanswerable in the context. *Inside a Transformer* (proposed integration), the mask is injected additively into attention,

$$\text{Attention}(Q, K, V) = \text{Softmax}\Big(\frac{QK^T}{\sqrt{d_k}} + \mathbf{M}_{S_i}\Big) V,$$

with $\mathbf{M}_{S_i} = -\infty$ at positions with $S_i = 0$, acting as a logical loss that modulates gradients during reinforcement learning. A decode-time variant restricts the sampling support to continuations whose lowered proposition passes the sense check. The attention-level integration is a proposal, not a validated result: we have not yet trained with it, and we state it as the concrete integration point for future work.

Section ID: 10_appendix
Source Section File: sections/10_appendix.md

## Paragraph Refs

- ../paragraphs/10_appendix-p01.md
- ../paragraphs/10_appendix-p02.md
- ../paragraphs/10_appendix-p03.md
- ../paragraphs/10_appendix-p04.md
- ../paragraphs/10_appendix-p05.md
- ../paragraphs/10_appendix-p06.md
- ../paragraphs/10_appendix-p07.md
- ../paragraphs/10_appendix-p08.md
- ../paragraphs/10_appendix-p09.md
- ../paragraphs/10_appendix-p10.md
- ../paragraphs/10_appendix-p11.md
- ../paragraphs/10_appendix-p12.md
- ../paragraphs/10_appendix-p13.md
- ../paragraphs/10_appendix-p14.md
- ../paragraphs/10_appendix-p15.md
- ../paragraphs/10_appendix-p16.md
- ../paragraphs/10_appendix-p17.md
- ../paragraphs/10_appendix-p18.md
- ../paragraphs/10_appendix-p19.md
- ../paragraphs/10_appendix-p20.md
- ../paragraphs/10_appendix-p21.md
- ../paragraphs/10_appendix-p22.md
- ../paragraphs/10_appendix-p23.md
- ../paragraphs/10_appendix-p24.md
- ../paragraphs/10_appendix-p25.md
- ../paragraphs/10_appendix-p26.md
- ../paragraphs/10_appendix-p27.md
- ../paragraphs/10_appendix-p28.md
- ../paragraphs/10_appendix-p29.md
- ../paragraphs/10_appendix-p30.md
- ../paragraphs/10_appendix-p31.md
- ../paragraphs/10_appendix-p32.md
- ../paragraphs/10_appendix-p33.md
- ../paragraphs/10_appendix-p34.md
- ../paragraphs/10_appendix-p35.md
- ../paragraphs/10_appendix-p36.md
- ../paragraphs/10_appendix-p37.md

## Paragraph Digest
