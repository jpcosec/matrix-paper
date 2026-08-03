# Draft Author Response to Reviewer `ZHLy`

We thank the reviewer for pressing on exactly the places where the manuscript overreaches. We agree that the relationship with LLMs, especially in Section 6, must be delimited more carefully. We also agree that the paper must separate what is already established from what remains a future architectural direction.

## 1. On the sense mask in attention, generation, and training

We agree that Section 6 is too speculative relative to the evidence presented. The reviewer is correct on three counts:
- the paper does not provide a concrete algorithm for injecting a sense mask into Transformer attention;
- the paper does not define a validated intermediate loss;
- the paper does not show that such a mechanism reduces hallucination during training or generation.

So Section 6 should be read as future integration work, not as part of the paper’s current demonstrated contribution.

The actual contribution is earlier and narrower. The abstract frames the problem as one of semantic representability, the introduction motivates a second layer separating stochastic signs from logical structure, and Section 3 defines a local logical space `L_i`, a truth layer `V_i`, and a sense/applicability layer `S_i`, from which the bounded world `W_i` is formed. That is what the manuscript establishes.

Accordingly, the safer and more accurate answer to the reviewer’s question about generation is not that the paper already demonstrates token-level intervention, but that it motivates a post-lowering symbolic validation stage. A model may produce a candidate statement; that statement may be converted into a symbolic proposition; that proposition may then be checked against the local admissibility mask and only then treated as a valid knowledge candidate. That is a post-generation validation story, not a demonstrated decoding-control algorithm.

## 2. On the statement that a “functional implementation exists”

We understand the concern. If the paper claims a functional implementation while the relationship with LLMs remains vague, then the implementation statement can carry too much weight.

Two clarifications are needed.

First, under blind-review constraints, we should not rely on unpublished repository details, private benchmarks, or engineering evidence not already contained in the manuscript.

Second, the implementation statement should be interpreted much more narrowly than “the LLM integration problem has been solved.” What the manuscript supports is an architectural substrate built around:
- a bounded logical space `L_i`;
- a truth layer `V_i`;
- a sense/applicability layer `S_i`;
- boolean operations over those layers;
- a lowering step from signs into symbolic propositions.

That architectural story is what Sections 3, 4, and 9 can safely support. What the paper does **not** support is a claim that it already provides all the machinery required for production-grade coupling with contemporary Transformer training or inference.

## 3. On whether discrete primitives are necessary

We agree that the strongest version of the claim would be unjustified if it said that continuity itself directly explains hallucination in general. That is not the right claim.

The claim we intend to defend is narrower:

> a representation based only on signs embedded in continuous spaces is insufficient as the sole substrate for auditable logical validation.

Why? Because the paper’s object is not merely semantic similarity or fluent continuation. It is logical admissibility inside a bounded context. The system must answer questions such as:
- is this proposition meaningful in the active logical space?
- is it false, or is it inapplicable?
- does this sign sequence map to a relation that is even licensed in the domain?

These are boundary questions about whether a relation of the form `aRb` is admissible, not just whether two signs are geometrically close. That is why the distinction between sign and symbol matters. Continuous embeddings may be useful for similarity, retrieval, clustering, and candidate lowering, but they do not by themselves define the local grammar that determines whether a proposition is admissible in the first place.

So the use of boolean structure is motivated by the kind of judgment the paper wants to make. `S_i` and `V_i` are not added because “all useful cognition must be discrete,” but because admissibility, contradiction, tautology, and contextual truth benefit from explicit logical boundaries if they are to be audited.

## 4. On the sentence about stochastic algorithms running on digital systems

The reviewer is right that this sentence is confusing and should be rewritten.

We are **not** claiming that neural training is “not stochastic,” nor that decoding randomness is irrelevant. The intended point is narrower: digital discreteness at the hardware level does not, by itself, provide a logical grammar of admissibility at the representational level. A model can run on binary hardware and still organize its semantic behavior in a distributed continuous geometry that does not explicitly encode whether a proposition is licensed in the active domain.

Likewise, deterministic decoding via `argmax` does not resolve the problem. It removes one source of output variability, but it does not transform a sign-level representation into an auditable logical system.

## 5. On the sentence “Having demonstrated that LLMs can be utilized…”

We agree that this sentence overstates the evidence. The paper does not demonstrate, in a general empirical sense, that LLMs can reliably map natural language into deterministic knowledge bases across open domains. At most, it motivates a possible interface in which language can be lowered into a symbolic substrate and then audited within bounded contexts.

That sentence should be weakened.

## 6. Small excerpt on the mathematical formalization of the database

Because this reviewer presses on implementation claims, the paper should also include one short operational table on what is already formalized at the database level:

| Operation | Formal expression | What it supports |
|---|---|---|
| `Partition` | `H = ⋃ W_i` | context-bounded storage rather than one flat universal table |
| `Project` | `Π_{C,R}(H)` | local `W_i` worlds as slices of a global substrate |
| `ValidateFormulation` | `F = is_valid(L_i)` | formulation validity separated from neural generation |
| `EvalSense` | `S_{x,y} = e_x^T S_i e_y` | explicit symbolic test for admissibility |
| `EvalTruth` | `f(a,b) = V_{a,b}` | truth evaluation separate from sense evaluation |
| `Assert` | `V_new = V_old ∨ (ΔV ∧ S_i)` | updates constrained by admissibility |
| `IdentifyUnknowns` | `U = I_req ∧ ¬V` | unknown distinguished from falsehood |
| `QueryProposition` | `f(aRb) = M_{aRb}` | propositions treated as tensor coordinates |

This table clarifies what is and is not currently supported. What is supported is a symbolic database substrate with explicit operations over truth, admissibility, partition, projection, and missingness. What is **not** supported is a validated method for injecting these operations into Transformer training or inference.

The same table also explains the dense-versus-omnirepresentational distinction. A `W_i` is a local language game materialized as a dense slice of the canonical hypertensor; it is not an isolated store with private facts. Omnirepresentation is the larger block-structured organization in which contexts, routing masks, and the global truth store coexist in one topological space.

Finally, the indexing argument should be stated concretely. The current mathematical case against a purely diagonal scheme is that it is both space-inefficient and information-suboptimal: in the idealized analysis, diagonal indexing tends toward `E(R) -> 0.5`, requires `O(N^2)` storage, and yields vanishing entropy per dimension, whereas hierarchical factorization yields `O(N log_2 N)` storage and a higher information regime (`E(R) = 0.75`).

## 7. Direct answers to the reviewer’s questions

**Q1. What does the sentence about stochastic algorithms on digital systems mean?**
It should not be read as a denial of stochasticity. The intended point is only that hardware discreteness does not automatically provide logical admissibility at the representational level.

**Q2. How does Section 3 connect to neural network architecture?**
In the current manuscript, not through a validated implementation. Section 3 defines the logical substrate; Section 6 sketches future interfaces with neural architectures.

**Q3. Where is it demonstrated that LLMs can map language onto deterministic knowledge bases?**
It is not demonstrated in the strong empirical sense implied by the current wording. The sentence should be weakened.

**Q4. What do “probabilistic distances,” “probabilistic weights,” and “probabilistic geometries” mean?**
These expressions are currently too loose. The intended meaning is that present systems rely on distributed continuous representational spaces and decoding procedures that do not themselves encode explicit logical admissibility constraints.

## 8. Changes we would make in revision

To address this review, we would:
1. explicitly mark Section 6 as future integration work rather than current demonstrated contribution;
2. remove or weaken overstatements about demonstrated LLM lowering;
3. restate the main thesis as a representability claim about the insufficiency of sign-only continuous embeddings as the sole substrate for auditable logic;
4. clarify the distinction between hardware discreteness and logical/semantic discreteness;
5. add a short operational excerpt on the database formalization;
6. tighten ambiguous terminology around probability, weights, and geometry;
7. fix the local textual errors.

We thank the reviewer again. We believe these revisions preserve the paper’s core contribution while aligning its claims more closely with what the manuscript actually establishes.
