We sincerely thank the reviewers for their insightful and constructive feedback. While the rebuttal system does not allow us to upload a revised PDF, we want to assure the reviewers that all stylistic, formatting, and typo-related issues—including the correct italicization of Tractarian terminology (sinnvoll, sinnlos, unsinnig), heading hierarchies, and figure boundary adjustments—have been fully resolved locally and will be reflected in the camera-ready version.

Below, we address the core theoretical and technical points raised during the review process, which have now been explicitly expanded upon in our revised manuscript:

1. Differentiation from OWL and Traditional Knowledge Graphs (KGs)
To better position our contribution, we have made the contrast with existing symbolic systems (like OWL and KGs) computationally explicit. Traditional KGs capture semantic co-occurrence, but they rely on iterative graph traversals or external deductive theorem provers to diagnose logical consistency after a claim is generated. This incurs an inherent O(V+E) bottleneck per evaluation. 

By contrast, our architecture introduces an operable category of semantic inapplicability (the "sense mask"). Our framework evaluates both transitive closure and semantic applicability via dense bitwise matrix multiplication. This pushes logical verification down to native silicon registers, executing in O(1) operations. We bypass the combinatorial bottleneck of traditional logical inference by rejecting structurally absurd (unsinnig) propositions at compile time, completely outside the veritative system.

2. The Geometric Origin of Hallucinations in Continuous Spaces
We have refined our argument regarding why current LLMs hallucinate. We clarify that factual errors are not mere statistical anomalies to be solved by scaling, but rather an inescapable geometric and structural deficit of continuous embedding spaces. 

Because semantically related truths and falsehoods share the same geometrical neighborhood, continuous scalar reads fail to reliably separate valid from invalid generations. Tiling such a set with convex cells requires a number of regions exponential in the number of constraints, inevitably forcing logical interference at categorical frontiers in any bounded-width network. Our matrix approach resolves this by decoupling the stochastic nature of linguistic signs from their deterministic logical structure prior to decoding.

3. Scalability and the Operational Pathway
To address concerns regarding practical implementation, we have formally documented the system's "Operational Pathway" and "Omnirepresentation" in the Appendix. We detail how natural language is ingested by small LLMs acting strictly as surface decomposers (handling sign-to-symbol resolution and alias folding) without making logical decisions. 

Candidates are routed to their respective context grids; if a relational signature crosses incorrectly, it is rejected immediately. This hierarchical tensor construction reduces spatial complexity toward O(N log N) and prevents the state-space explosion typical of unbounded symbolic systems.

We believe these clarifications significantly strengthen the theoretical foundations of the paper and directly address the concerns regarding computational complexity and the fundamental limits of continuous embeddings.
