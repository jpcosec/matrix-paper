# Delta 1 — Pruebas de insuficiencia de representaciones continuas

**Responde a:** Eje A (AC `7v48`, `ZHLy`). El rebuttal prometió 3 demostraciones; no están en v2.
**Tono:** deliberadamente NO categórico — los argumentos motivan el diseño, no pretenden imposibilidad absoluta. Los pasos interpretativos van marcados como tales.

## DESDE (átomos KB origen)

| Átomo | Aporta |
|---|---|
| `Matematica/Optimizacion_y_Desambiguacion/Fenomeno_de_Gibbs_en_Funciones_Indicadoras.md` | Prueba 1: oscilación de Gibbs al aproximar indicadoras discontinuas |
| `Matematica/Optimizacion_y_Desambiguacion/Geometria_de_Politopos_y_Ancho_Acotado_Hanin.md` | Prueba 2: cota de regiones ReLU con ancho acotado |
| `Matematica/Tensores_y_Matriz_Bloques/Geometria_de_Embeddings_y_Canales_Semanticos.md` | Prueba 3: error fáctico dentro del canal típico |
| `Antecedentes/Limites_Espacio_Continuo/Barrera_Deteccion_AUROC_Error_Tipo_III.md` | AUROC ≈ 0.478 (barrera de detección) |
| `Filosofia/Epistemologia_y_Contextos/Eje_A_Justificacion_Matematica_Limites_Continuos.md` | Hilo argumental del eje |
| `Filosofia/Epistemologia_y_Contextos/Representacion_Continua_vs_Implementacion_Discreta.md` | Respuesta al punto argmax/silicio de ZHLy |

## DESDE+ ampliación KB (referencias adicionales)

| Átomo | Aporte al argumento |
|---|---|
| `Antecedentes/Limites_Espacio_Continuo/Ausencia_de_Senal_de_Fallo_Determinista.md` | "No compile error": ausencia estructural de fallo determinista |
| `Antecedentes/Alucinaciones/Origen_Geometrico_y_Espacio_Vectorial.md` | Indistinguibilidad geométrica del error en $\mathbb{R}^d$ |
| `Matematica/Optimizacion_y_Desambiguacion/Teorema_Aproximacion_Universal_Hornik.md` | Hornik: universal solo para funciones *continuas* |
| `Filosofia/Epistemologia_y_Contextos/Discretizacion_Logica_vs_Continuo.md` | Discretización lógica vs sustrato continuo |
| `Filosofia/Epistemologia_y_Contextos/Prueba_Necesidad_Representacion_Simbolica_Discreta.md` | Necesidad de representación simbólica discreta |
| `Filosofia/Tractatus_y_Ontologia/Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable.md` | Embeddings de signos insuficientes para lógica auditable |
| `Antecedentes/Limites_Espacio_Continuo/Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente.md` | Subsección argmax: incongruencia decodificación/latente |
| `Antecedentes/Limites_Espacio_Continuo/Semantica_Formal_Neuro_Simbolica_vs_Opacidad_Neuronal.md` | Cierre del anexo: semántica formal vs opacidad |

**Extensión mapping (párrafo cuerpo + anexo, bridge `delta1_review`):**
```yaml
   - {atom_id: atom-ausencia-de-senal-de-fallo-determinista, atom_path: Antecedentes/Limites_Espacio_Continuo/Ausencia_de_Senal_de_Fallo_Determinista.md, bridge: delta1_review, score: 0.9, detail: "no deterministic failure signal in continuous nets"}
   - {atom_id: atom-origen-geometrico-y-espacio-vectorial, atom_path: Antecedentes/Alucinaciones/Origen_Geometrico_y_Espacio_Vectorial.md, bridge: delta1_review, score: 0.85, detail: "geometric origin: errors indistinguishable in R^d"}
   - {atom_id: atom-teorema-aproximacion-universal-hornik, atom_path: Matematica/Optimizacion_y_Desambiguacion/Teorema_Aproximacion_Universal_Hornik.md, bridge: delta1_review, score: 0.9, detail: "universal approximation limited to continuous functions"}
   - {atom_id: atom-discretizacion-logica-vs-continuo, atom_path: Filosofia/Epistemologia_y_Contextos/Discretizacion_Logica_vs_Continuo.md, bridge: delta1_review, score: 0.85, detail: "logical discretization vs continuous substrate"}
   - {atom_id: atom-prueba-necesidad-representacion-simbolica-discreta, atom_path: Filosofia/Epistemologia_y_Contextos/Prueba_Necesidad_Representacion_Simbolica_Discreta.md, bridge: delta1_review, score: 0.85, detail: "necessity of discrete symbolic representation"}
   - {atom_id: atom-insuficiencia-de-embeddings-de-signos-para-logica-auditable, atom_path: Filosofia/Tractatus_y_Ontologia/Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable.md, bridge: delta1_review, score: 0.8, detail: "sign embeddings insufficient for auditable logic"}
   - {atom_id: atom-semantica-formal-neuro-simbolica-vs-opacidad-neuronal, atom_path: Antecedentes/Limites_Espacio_Continuo/Semantica_Formal_Neuro_Simbolica_vs_Opacidad_Neuronal.md, bridge: delta1_review, score: 0.8, detail: "formal semantics vs neuronal opacity (anexo, cierre)"}
```
(`Incongruencia_Decodificacion...` ya anclada vía delta 2; reutilizar.)

## HACIA (párrafos destino + ANEXO)

1. **Cuerpo:** párrafo nuevo en `01_1_sota.md`, **antes del último** (`While these current methodologies offer significant advancements…`). ~140 palabras, con puntero al anexo.
2. **Anexo:** subsección `## On the Limits of Continuous Approximation {#app:continuous}` en `Neurips_peiper/sections/10_appendix.md` (mismo archivo que deltas 4/5; si no existe aún, crearlo con encabezado `# Appendix` y registrar en `paper/paper.yaml` tras `09_conclusion.md`).

## Propuesta de texto

**Cuerpo (`01_1_sota.md`):**
```markdown
**Why Continuous Spaces Offer No Guarantee of Logical Validity** The case for discrete primitives rests on three structural observations about continuous approximation, not on architectural preference. First, an indicator of logical validity $f(x) \in \{0, 1\}$ is discontinuous at its boundary; smooth approximators converge to such functions in measure but not uniformly, and boundary oscillations of the Gibbs type (classically $\approx 8.95\%$ of the jump) shrink in width without disappearing [@hornik1991approximation]. Second, a ReLU network partitions $\mathbb{R}^d$ into convex polytopes whose number grows only polynomially with depth at bounded width [@hanin2017universal]; carving non-convex or discontinuous regions of semantic invalidity (_Unsinnig_, $S_i = 0$) thus appears to demand exponentially many units, and forcing the fit tends to concentrate error precisely at categorical frontiers. Third, probing studies find factual-discrimination errors lying within the typical channel of the embedding submanifold, where linear separation is close to chance (AUROC $\approx 0.478$) [@wei2024measuring]. Deterministic decoding inherits rather than removes these distortions: `argmax` over a distorted score surface is reliably wrong wherever the surface is distorted. A discrete Boolean primitive ($S_i \in \{0, 1\}$) instead imposes a compile-time boundary *prior* to decoding—a guarantee that continuous approximation alone does not provide. Formal statements and caveats are given in Appendix~\ref{app:continuous}.
```

**Anexo (`10_appendix.md`, subsección nueva):**
```markdown
## On the Limits of Continuous Approximation {#app:continuous}

This appendix states the three observations of Section 2 more precisely, with their scope and caveats. They motivate the discrete substrate; we do not claim impossibility results for unbounded architectures.

### Indicator boundaries and oscillation

Let $f: \mathbb{R}^d \to \{0,1\}$ indicate logical validity, discontinuous at the boundary of its support. Universal approximation results [@hornik1991approximation] guarantee convergence in $L^1$ / in measure: the *mass* of the error region can be made arbitrarily small. Convergence is not uniform, however: near a jump, any smooth or piecewise-smooth approximator exhibits a transition band with overshoot—the Gibbs phenomenon, whose classical overshoot is $\approx 8.95\%$ of the jump magnitude. Narrowing the band requires steeper activations and more units, but the band does not vanish with more data or training; it is a property of approximating a jump with continuous functions. In semantic terms, there is always a region where *Unsinn* receives an intermediate score instead of an exclusion.

### Polytope tiling at bounded width

A ReLU network is piecewise affine: each neuron's activation boundary is a hyperplane, and their arrangement partitions $\mathbb{R}^d$ into convex polytopes on which the network is linear. For width $w \le d$ and depth $L$, the number of regions is bounded by

$$\mathcal{N}(w, L) \le \sum_{j=0}^{d} \binom{wL}{j},$$

which grows polynomially in $L$ [@hanin2017universal]. Sense boundaries, by contrast, are typically non-convex and disconnected: type constraints over symbols combine combinatorially, so the set of _sinnvoll_ propositions scatters across many disconnected regions. Tiling such a set with convex cells appears to require a number of regions exponential in the number of constraints, while a bounded-width network supplies only polynomially many. Two caveats keep this honest: (i) the deficit can in principle be escaped with exponentially growing width—the claim concerns bounded-width regimes; (ii) the step from the region bound to *interference at categorical frontiers* is our interpretation, consistent with empirical observations of representation interference, and we offer it as a hypothesis to test rather than as part of Hanin's theorem.

### Errors inside the typical channel

If factual errors were outliers in embedding space, post-hoc detection would be easy. Probing studies instead find them inside the typical channel of the representation, where linear discrimination performs close to chance (AUROC $\approx 0.478$) [@wei2024measuring]. This suggests no continuous scalar read from the substrate reliably separates valid from invalid generations—motivating a check that lives outside the continuous substrate.

### On deterministic decoding

`argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wrong *reproducibly*, with no sampling randomness to blame. This cuts both ways—stochastic decoding is not the culprit either; both inherit the substrate. The design conclusion is that the boundary must be imposed *before* decoding, at compile time, where a stored Boolean matrix $S_i$ provides an exact check in $O(1)$ per step instead of an approximate one distributed across the network.
```

## bib / átomos / mapping

- **bib:** nada — las 3 bibkeys ya están en `references.bib`.
- **Átomos nuevos:** ya creados (`Source_PDF_{hornik1991approximation,hanin2017universal,wei2024measuring}_pdf.md`).
- **mapping.yaml:**
  - Párrafo nuevo cuerpo (`01_1_sota-p07` tras renumeración): 3 bib + `Fenomeno_de_Gibbs` (0.95), `Geometria_de_Politopos_y_Ancho_Acotado_Hanin` (0.95), `Barrera_Deteccion_AUROC` (0.9), `Representacion_Continua_vs_Implementacion_Discreta` (0.8) — bridge `delta1_review`.
  - Párrafos del anexo (`10_appendix-pXX`): mismo set + `Eje_A_Justificacion_Matematica_Limites_Continuos` (0.9) + `Geometria_de_Embeddings_y_Canales_Semanticos` (0.85) — bridge `delta1_review`.

## Riesgos
- Verificar 8.95% y 0.478 contra los PDFs antes de someter.
- El paso "polytope overlap → interferencia" quedó explícitamente marcado como interpretación (caveat ii) — mantener esa honestidad si se edita.
- Renumeración de anchors de `01_1_sota` (cierre p07→p08): re-mapear por contenido tras regenerar.
- Depende de `10_appendix.md` (compartido con deltas 4/5): el primero que se aplique crea el archivo + la línea en `paper.yaml`.
