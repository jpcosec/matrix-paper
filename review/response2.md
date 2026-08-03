fficial Review of Submission986 by Reviewer ZHLy
Official Reviewby Reviewer ZHLy25 Jun 2026, 14:15 (modified: 23 Jul 2026, 07:50)Program Chairs, Area Chairs, Reviewer ZHLy, Authors, Reviewers SubmittedRevisions
Ethics: NO or VERY MINOR ethics concerns only
Position: Yes the paper is clearly a fit for the Position Paper Track
Summary:
The paper argues that the current state of neural language modeling with continuous embeddings is insufficient to fully remove hallucinations, and that a logical layer, which detects sensibility and truthfulness, is necessary. The authors draw on concepts from Ludwig Wittgenstein’s Tractatus Logico-Philosophicus to derive a boolean representation of world partitions. Practically, the authors argue that a sense mask can be incorporated into the attention mechanism and that "highly precise" synthetic datasets can be curated.

Author Identification: No.
Support: 2: fair
Significance: 2: fair
Presentation: 2: fair
Context: 3: good
Discussion: 2: unlikely
Alternative Position: Yes, and alternative positions are well-considered and addressed by the argument
Strengths:
The paper provides a good description of logical atomism and a vision via boolean matrices. It offers a perspective on how we can diagnose hallucinations, via both truth and sensibility.
The paper gives a good discussion of related work in Section 2.
Weaknesses:
Section 6 - the described sense mask during attention is unclear. The paper does not propose an implementation or algorithm. During training, this simply appears to be a form of filtering (and there is no evidence to suggest that this would actually help with hallucinations), and it is unclear what the paper proposes during generation - does generation simply stop if some sense mask is activated? It is also unclear what the proposed intermediate loss would be.
The paper states that “Currently, a functional implementation exists” + “This implementation is actively used” but provides no details on the implementation. While I understand that this is a position paper and this “functional implementation” may be under review, I feel it is a critical piece to the argument, as Section 6 (Relationship with LLM) is vague and I do not see the authors' direct vision for how this can be implemented.
The paper's general perspective is that continuous embeddings are in some fundamentally insufficient, but only argues this from a philosophical perspective. Is there a rigorous mathematical justification for this? Why are discrete primitives fundamentally necessary?
147 - “plant” does not appear in the table 171 - incomplete sentence

Questions:
“However, given that actual stochastic algorithms are based on digital systems that also operate on boolean logic at the bit level, it is worth asking how stochastic the training and operation of the neural networks that make up LLMs really are.” What does this mean? Are the authors suggesting that NN training is not stochastic? Are the authors suggesting that we cannot (and have never) measured any functions of this randomness or the sensitivity of training? Does this argue against the main perspective of the paper that LLMs are currently too "probabilistic" for logical guarantees?
How does the proposed representation in Section 3 connect with any neural network architecture?
“Having demonstrated that LLMs can be utilized to map language onto these deterministic knowledge base” - where is this demonstrated in the paper?
What do "probabilistic distances", "probabilistic weights", and "probabilistic geometries" mean? The weights of a language model are frozen after training, and the source of randomness afterwards is from the decoding algorithm, but one is free to decode deterministically via argmax.
Agreement: 2: disagree
Rating: 3: Reject: The paper has a weakly stated position, technical or logical flaws, inadequate support for claims, or addresses an issue of limited scope.
Confidence: 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.
Thoroughness: 3: You read the paper carefully but did not check all of the details.
Code Of Conduct Acknowledgement: Yes
LLM Policy Acknowledgement: Yes
