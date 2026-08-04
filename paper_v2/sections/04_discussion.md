# Discussion

The task of processing text and extracting semantic logic from it has no novelty. Mapping facts and relations to matrices is a technique with a long history in computing, as seen in what is commonly known as lookup tables. Also, handling non-informative bits in logical operations using the null state Ø is a standard practice in digital system design. Moreover, handling different ordered tables as relational databases has its own language and rules in SQL. However, it is the philosophical-logical substrate that Wittgenstein's Tractatus provides, which makes this approach useful.



While existing neuro-symbolic and parsing works often translate language into logical forms (as reviewed in Section 1), they generally fail to explicitly formalize the difference between truth, applicability/sense, and algebraic disambiguation of the sign. Furthermore, no current framework appears to use the triad of context, logic, and sense as extractable, operable properties across document domains.

Two families of neighboring work clarify what is new here. Retrieval pipelines and knowledge graphs capture *semantic co-occurrence*—which entities and phrases appear together—but not *logical paths*: a KG edge records that two nodes are related, with no category for combinations that are ill-formed in the first place, and recent benchmarks show LLM-based graph construction still produces unfaithful structures [@sansford2024grapheval]. Our proposal is closer in spirit to description logics and causal networks (KL-ONE, CLASSIC, conceptual graphs), which do constrain what can be consistently asserted [@brachman1990; @lehmann1992; @sowa1991; @kruse2022causal]; indeed, OWL ontologies enter our framework directly as input to the ingestion pathway. What we add to that lineage is an explicit, operable category of semantic inapplicability: sense is stored as a matrix layer $S_i$, and *Unsinnig* is rejected at compile time inside the substrate. Crucially, whereas traditional OWL ontologies and KGs rely on iterative graph traversals ($\mathcal{O}(V+E)$) or external deductive theorem provers to diagnose consistency after the fact, our framework evaluates both transitive closure and semantic applicability via dense bitwise matrix multiplication. This pushes logical verification down to $\mathcal{O}(1)$ operations on native silicon registers, bypassing the bottleneck of traditional logical inference.

An interesting first approach to semantics in language is that the formalization proposed in this work would allow the generation of document families where the shared logic can be audited not only by its degrees of truthfulness but also by its states of sense. In other words, the use of the proposed tools would enable the creation of curated knowledge graphs, prepared to operate on particular domains with explicit limits on the context they admit. Furthermore, the proposal presented in this work explicitly rejects the possibility of a complete mapping of universal and computable logical universes. The case of the UNL project, _Universal Network Language_, from the United Nations Institute for Advanced Studies, demonstrates the difficulty of encompassing a complete language that maintains both logical coherence and extensibility.

An important limitation to note at this point is that, as the treatise anticipates, the distinction between the concept represented in a knowledge graph and the textual sign that denotes it (token or word) does not belong to the realm of formal logic. The universe of possible contexts involved between natural language and its underlying logic makes the exact calculation of all of them intractable. In other words, there is a real possibility that the mapping of words to symbols is unequivocally stochastic in nature. Fortunately, recent advances in natural language processing models, and especially in neural network language models such as LLMs, make this task much more manageable than it was a few years ago.

Furthermore, a little-explored feature of language is that, by defining a closed set of signs and facts, the mapping of those signs and facts to language can shift from a stochastic process to a deterministic logical process, determined by two separate logical processes. First, structured knowledge, as presented in the previous section, and second, a "representation surface" layer, determined by the document structure and the grammar of the language to be represented. The combination of these would allow the representation of any type of "structured language" document by the combination of abstract syntax trees and the Boolean algebra described above. It is worth noting that while this type of representation would have serious problems representing certain regional dialects or more artistic and creative documents like poetry, it would be very well suited to other types of documents that, by nature, tend to be more structured, such as reports, dictionaries, technical documentation, or computer code.

Two design notions make this operational at scale: *closed representations*, within which sense is near-trivial and violations emerge only at structurally inadmissible context crossings, and the *omnirepresentation*, a block-matrix form exposing contexts, routing and facts jointly to stochastic models. The formal construction, the ingestion pathway, the self-optimization algorithm and the sense-mask integration are given in Appendix~\ref{app:repr}.



An interesting approach to how this proposal relates to the burgeoning field of neural network language models is the role that the sense mask $S$ can play across both training and inference pipelines. Given a sufficiently large knowledge base, built on the same body of documents used for training, obtaining a sense mask from the input text at train time would allow early control over which information is more or less important through sense detection. Similarly, sense detection in the generated text would enable a new, automated form of text loss detection, opening a new dimension within reinforcement learning, synthetic dataset generation, and even early prevention of outputs the model might generate during inference.

On the other hand, by introducing context as a limit to the family of texts we can unite in a logically *sinnvoll* universe, we are providing accurate tools for curating datasets, while also facilitating the training of models that function not as universal language machines, but as specialist machines for specific domains (something sought after today by SMLs). The effect of this would be greatly amplified if, in addition to the direct loss in text processing and generation, we introduced a logical loss in the intermediate layers, thus separating the processing of language as a sign, with all its inherent imprecisions and "grammatical sugar," from symbolic representation and sense.

This last point aligns directly with what LeCun and colleagues have been proposing in JEPA and H-JEPA [@lecun2022path; @dawid2024latent; @assran2023ijepa]. In their case, decoupling the abstract representation of the sign "token by token" is being attempted through a combination of two things: the use of scalar energy to measure compatibility between input and output, and the use of multidomain embeddings. In our case, this could be decoupled into two independent levels: the data as a sign and the representation of its logic and sense.

Finally, one might ask whether a logic machine with sufficient "knowledge" could replace what LLMs can do today. The answer is most likely no. The generalization capacity of a machine based solely on facts and logical operations on them is, by definition, null. While it is possible to represent a significant number of tasks and their solutions through the appropriate combination of algorithms and fact and context trees, a machine built this way will always struggle to handle novel situations if it lacks the "creative" capacity provided by stochastic algorithms. However, given that current stochastic algorithms are based on digital systems that also operate on boolean logic at the bit level, it is worth asking how stochastic the training and operation of the neural networks that make up LLMs really are.

Section ID: 04_discussion
Source Section File: sections/04_discussion.md

## Paragraph Refs

- ../paragraphs/04_discussion-p01.md
- ../paragraphs/04_discussion-p02.md
- ../paragraphs/04_discussion-p03.md
- ../paragraphs/04_discussion-p04.md
- ../paragraphs/04_discussion-p05.md
- ../paragraphs/04_discussion-p06.md
- ../paragraphs/04_discussion-p07.md
- ../paragraphs/04_discussion-p08.md
- ../paragraphs/04_discussion-p09.md
- ../paragraphs/04_discussion-p10.md
- ../paragraphs/04_discussion-p11.md
- ../paragraphs/04_discussion-p12.md
- ../paragraphs/04_discussion-p13.md

## Paragraph Digest
