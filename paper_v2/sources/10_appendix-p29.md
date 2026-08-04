# Appendix source 29

Kind: current-paper-block
Origin: sections/10_appendix.md
Anchor: 10_appendix-p29

## Excerpt

1. **Decomposition into standard form.** The utterance is decomposed into its meaning plus syntactic sugar, and the meaning is expressed in a standardized representation—S-expressions, RDF/Turtle, or OWL. We propose small LLMs as surface decomposers: they absorb sign variability (including sign-to-symbol resolution and alias folding) but make no logical decisions.
2. **Reduction to candidate propositions.** The standard form is lowered to homogeneous candidate propositions `(R a b)`—e.g., `(sound dog barks)`, `(sound cat meows)`. Nothing here is asserted yet; candidates have no truth status.
3. **Two-step sense check.** (a) *Context indexing:* the candidate is routed to the context(s) that index its cross; if no context admits the (domain, relation) combination, the candidate is rejected as *Unsinnig*—absurdity is avoided by construction, before any truth evaluation. (b) *Contradiction check:* admissible candidates are checked against the existing facts $V_i$ of their context; a conflict with what is already asserted yields an explicit contradiction signal rather than silent overwrite.
4. **Matrix computation.** Only candidates passing both checks update or consult $V_i$; inference proceeds by boolean matrix multiplication and bitwise dimensional collapse, yielding $W_i^{*} = V_i \odot S_i$.

## Relevance

Bootstrap source block 29 extracted from the current Appendix draft.
