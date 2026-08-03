Official Review of Submission986 by Reviewer FJpU
Official Reviewby Reviewer FJpU24 Jun 2026, 10:44 (modified: 23 Jul 2026, 07:50)Program Chairs, Area Chairs, Reviewer FJpU, Authors, Reviewers SubmittedRevisions
Ethics: NO or VERY MINOR ethics concerns only
Position: Yes the paper is clearly a fit for the Position Paper Track
Summary:
Observing that the hallucination exhibited by large models cannot be completely resolved through retrieval or calibration, this paper argues that propositions expressed in local grammars should be rejected directly before the large model outputs. This is something that cannot be achieved through embedding natural language. Then, the authors propose adding an additional representation layer to define a logical space to separate language symbols from logical structure. Specifically, such approach is supposed to be implemented through a series of Boolean operations. This overall idea originates from Ludwig Wittgenstein’s ractatus Logico Philosophicus. In this architecture, while propositions are evaluated based on truth values, they also need to be evaluated based on the current state (environment), categorized into three types: Sinnvoll (meaningful), Sinnlos (tautological or contradictory), and Unsinning (absurd or structurally inapplicable).

Author Identification: No.
Support: 2: fair
Significance: 2: fair
Presentation: 2: fair
Context: 2: fair
Discussion: 3: possibly
Alternative Position: No
Strengths:
The topic is valuable, and interesting, investigating hallucination as a question of whether a proposition can be represented in the current semantic space.

The paper emphasizes rejecting the construction of a universal logical universe and stressing that bounded contexts are more realistic than attempting a global. The author's framework may be more suitable for structured text scenarios such as reports, technical documentation, code, and dictionaries.

Weaknesses:
The authors propose that solving hallucinations cannot rely solely on embeddings, RAGs, etc., but requires the addition of a representation. However, the paper does not provide a clearer or deeper distinction from existing technologies. Such as RAG, Knowledge Graph etc..

As a position paper, this paper does not need to provide complete training objectives or empirical evaluations. However, several of its core arguments rely on the feasibility of constructing and applying semantic masks in an LLM system. It would be more persuasive if this paper could provide at least one concrete operational path, such as how to extract candidate propositions, type-label them, check them against S_i, and ultimately decide whether to adopt or reject them as knowledge.

A major drawback of this framework lies in its scalability and schema construction. It relies on constructing W_i over a local logical space L_i, but the paper fails to explain how to select relevant entities, attributes, and acceptable relationships in the real world domain. Enumerating all attributes of an entity is impractical, while extracting only those mentioned in the input text makes it difficult to distinguish between spurious information, unknown information, and genuine semantic inapplicability. Therefore, the proposed semantic mask may confuse missing representations with meaningless representations. Unless concrete steps for constructing and updating L_i, V_i, and S_i are provided, the framework's practicality will be severely limited.

The paper contains obvious spelling and grammar errors, requiring substantial presentation improvement.

Questions:
Pls refer to W1-W3.
Agreement: 4: agree
Rating: 4: Borderline reject: The paper presents a position, but the reasons to reject, e.g., unclear reasoning or limited support for the claims, outweigh reasons to accept.
Confidence: 5: You are absolutely certain about your assessment. You are very familiar with the related work.
Thoroughness: 4: You read the paper and appendices and checked most of the details, including references..
Code Of Conduct Acknowledgement: Yes
LLM Policy Acknowledgement: Yes
