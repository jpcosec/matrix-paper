# Discussion note 04

Stage: writing-note

## Sources

- ../sources/04_discussion-p04.md
- ../sources/kb/04_discussion-p04__atom-context-ci.md
- ../sources/kb/04_discussion-p04__atom-gramatica-universal-unl.md

## Intent

Bridge source block 04 into section-ready prose for Discussion.

## Claim

Two families of neighboring work clarify what is new here.

## Notes

Two families of neighboring work clarify what is new here. Retrieval pipelines and knowledge graphs capture *semantic co-occurrence*—which entities and phrases appear together—but not *logical paths*: a KG edge records that two nodes are related, with no category for combinations that are ill-formed in the first place, and recent benchmarks show LLM-based graph construction still produces unfaithful structures [@sansford2024grapheval]. Our proposal is closer in spirit to description logics and causal networks (KL-ONE, CLASSIC, conceptual graphs), which do constrain what can be consistently asserted [@brachman1990; @lehmann1992; @sowa1991; @kruse2022causal]; indeed, OWL ontologies enter our framework directly as input to the ingestion pathway. What we add to that lineage is an explicit, operable category of semantic inapplicability: sense is stored as a matrix layer $S_i$, and *Unsinnig* is rejected at compile time inside the substrate. Crucially, whereas traditional OWL ontologies and KGs rely on iterative graph traversals ($\mathcal{O}(V+E)$) or external deductive theorem provers to diagnose consistency after the fact, our framework evaluates both transitive closure and semantic applicability via dense bitwise matrix multiplication. This pushes logical verification down to $\mathcal{O}(1)$ operations on native silicon registers, bypassing the bottleneck of traditional logical inference.

## Source Digest
