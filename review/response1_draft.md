# Draft Author Response to Reviewer `ppL8`

We thank the reviewer for the careful reading and for identifying three places where the manuscript needed to be clearer: (i) the representational claim must be situated more carefully within the hallucination literature, (ii) the paper should explain more concretely how local logical worlds could be built, and (iii) the practical importance of the proposal should be stated more directly. We agree on all three points.

## 1. On the claim that hallucination is a representational problem

We agree that the original phrasing could be read too strongly. The paper should not claim that “continuity causes hallucination” in any monocausal or universal sense. That would require evidence far beyond what this position paper provides.

The narrower claim we intend to defend is this:

> continuous embeddings are insufficient as the **only** representational substrate for systems that must decide, in an auditable way, whether a proposition is admissible in a domain, meaningful in context, and true.

This is closer to the abstract and introduction than to a global theory of hallucination. The point is not only that a model may output false statements, but that a sign-based continuous representation does not by itself define: (a) what counts as a valid proposition in a local logical space, (b) what counts as a category error, and (c) what should be rejected before factual evaluation.

That is why the paper distinguishes truth (`V_i`) from sense/applicability (`S_i`). In the representational section, the logic is: define a local logical space `L_i`, then define truth and sense separately over that space, and only then define the bounded world `W_i`. This is a claim about representability, not a dismissal of retrieval, calibration, or latent probing.

We should also connect this more clearly to prior work. The revision should explicitly position the paper relative to factuality evaluation, latent probing, behavioral mitigation, and neuro-symbolic work. The paper accepts that hallucination has many causes and many observable forms. What it adds is a more specific claim: even when a model retrieves relevant evidence or encodes useful knowledge latently, a sign-only substrate still does not explicitly encode whether a candidate relation is admissible in the first place.

That is why the distinction between falsehood and inapplicability matters so much here. A system may fail because it lacks knowledge, because it decodes poorly, or because it builds a proposition that never belonged to the grammar of the active domain. Our claim is that the third case deserves its own representational treatment.

## 2. On how local worlds could be created in practice

We agree that the paper should not leave the impression that `W_i`, `V_i`, or `S_i` are handcrafted globally. That would be infeasible. The intended path is local, context-bounded, and staged.

The direct answer is simple: the matrices are not meant to be universal or manually authored; they are meant to be built for bounded domains from a schema, ontology, or indexed document family, then populated through a lowering and validation pipeline.

A toy example makes the point. In a clinical medication domain, `(patient has-medication drug)` may be an admissible relation. “Patient X is taking aspirin” is therefore admissible and can then be checked for truth. By contrast, “aspirin is blue on Tuesdays” may be grammatical English but does not belong to that domain relation system and should be rejected as inadmissible rather than treated as an ordinary factual claim.

The stronger answer is that the worlds are not only local; they are composable. A realistic system would not be one monolithic `W_i`, but many bounded worlds connected by routing/projection structures. Each local world captures one bounded context; projections between them allow the system to reuse entities and constraints without collapsing everything into one universal table.

Read computationally, the mathematical objects are quite simple:
- `L_i`: typed coordinate system for a bounded domain;
- `S_i`: boolean admissibility mask over those coordinates;
- `V_i`: factual state over admissible coordinates;
- `W_i`: bounded world obtained when truth is evaluated under those admissibility constraints.

So the construction problem has two layers: one layer builds or routes the local logical spaces in which relations are admissible; another populates those spaces with current truth values.

### 2.1. Operational database view

A concise way to present the formalization is with the concrete database operations already associated with the framework:

| Operation | Formal expression | Role |
|---|---|---|
| `Partition` | `H = ⋃ W_i` | partition the global tensor into bounded local worlds |
| `Project` | `Π_{C,R}(H)` | extract a `W_i` as a slice of the global substrate |
| `ValidateFormulation` | `F = is_valid(L_i)` | check well-formedness in the active logical space |
| `EvalSense` | `S_{x,y} = e_x^T S_i e_y` | test whether a coordinate is admissible in context |
| `EvalTruth` | `f(a,b) = V_{a,b}` | read the factual value at an admissible coordinate |
| `Assert` | `V_new = V_old ∨ (ΔV ∧ S_i)` | write only through the sense mask |
| `IdentifyUnknowns` | `U = I_req ∧ ¬V` | distinguish missing information from stored fact |
| `QueryProposition` | `f(aRb) = M_{aRb}` | treat propositions as tensor coordinates, including cross-context routing |

This table makes two things clear. First, a proposition does not go directly from text to truth. It is validated structurally, then tested for admissibility through `S_i`, and only then evaluated factually through `V_i`. Second, the database is not one flat universal table. It is partitioned into `W_i` and accessed by projection.

### 2.2. Dense local representation vs. omnirepresentation

The paper should also explain the storage geometry more clearly. A local `W_i` is not an isolated database with its own private facts. It is a projection of a canonical global substrate, materialized as a dense local block for fast evaluation. In other words, the dense layer is the operational unit for inference.

By contrast, omnirepresentation is the larger block-structured topology in which multiple `W_i`, their routing masks, and the global truth store coexist. This is what allows one proposition in `W_i` to be routed or indexed in `W_j` rather than forcing all knowledge into one undifferentiated matrix.

This is why the paper favors hierarchical tensor construction over a naive diagonal index. The current argument is that a purely diagonal scheme is both space-inefficient and information-suboptimal: in the idealized analysis it tends toward `E(R) -> 0.5`, requires `O(N^2)` storage, and drives entropy per dimension toward zero, whereas hierarchical factorization yields `O(N log_2 N)` storage and a higher information regime (`E(R) = 0.75`).

### 2.3. What remains open

We also want to be explicit about what the current paper does **not** solve. It does not yet provide a large-scale empirical study showing how local worlds should be induced automatically across arbitrary domains. It does not claim that schema construction is solved universally. It also does not claim that natural-language-to-logic lowering is robust enough for unrestricted deployment.

What it does provide is a formal motivation for separating truth from sense and an operational picture of how candidate propositions can be lowered and validated.

## 3. On why this matters

We agree that the manuscript should make the importance of the problem more explicit. The issue is not only that LLMs sometimes say false things. In many structured or high-stakes settings, a system must distinguish at least three cases:
- propositions that are true in a bounded domain;
- propositions that are false but meaningful;
- propositions that are not admissible in the domain at all.

Retrieval, ranking, and confidence estimation can help with factual support, but they do not by themselves encode the third case. A system can still combine correct fragments into an ill-typed proposition if the representation never explicitly marks that the relation itself is out of scope.

That is why we believe the problem matters beyond philosophical interest. In technical documentation, code, controlled reporting, and other bounded specialist domains, the cost of conflating falsehood with inadmissibility is high.

## 4. Direct answer to the reviewer’s question

> Can the authors please discuss how they think the sense and world matrices could be created in a real world setup?

Yes. They should not be understood as manually authored universal tables. They should be understood as local representations built from bounded domains. In practice, the input artifacts could be a domain ontology, a controlled schema, or an indexed document family. A lowering stage converts candidate statements into symbolic propositions over that schema. Those propositions are then validated in `L_i`, filtered through `S_i`, and only then evaluated for truth through `V_i`. If a proposition requires moving between contexts, it is routed across linked local worlds rather than forced into one global flat matrix.

## 5. Changes we would make in revision

To address this review, we would:
1. restate the main thesis as a representability claim, not as “continuity causes hallucination”;
2. strengthen the discussion of related work on factuality, probing, mitigation, and neuro-symbolic systems;
3. explain local-world construction more concretely in terms of partition, projection, admissibility, and truth;
4. add a short operational excerpt on the database formalization;
5. state more clearly that the practical target is bounded specialist domains;
6. explicitly mark large-scale schema induction and broad empirical validation as open work.

We thank the reviewer again. We believe these clarifications strengthen the paper without changing its core contribution.
