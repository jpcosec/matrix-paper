# 2. The Limits of Continuous Representability

Modern LLMs represent meaning through points in high-dimensional continuous spaces. While this enables powerful generalization, it introduces three fundamental limitations that prevent formal semantic guarantees:

## 2.1 The Confusion of Similarity and Sense
In a continuous embedding space, "apple" and "orange" are near each other because they are fruits. However, "the square root of an apple" is also a point in that space. The geometry of the space does not forbid the construction of such a vector, nor does it provide a mechanism to identify it as a category error. Because every point in a continuous space is potentially "reachable," the system has no inherent "Grammar of Sense" to reject nonsensical combinations of valid signs.

## 2.2 Global Coverage vs. Local Validity
Language models are trained to capture global statistical patterns across vast datasets. This leads to a "flat" ontology where truth values are averaged over conflicting contexts. However, a proposition that is true in a "Cooking World" (e.g., "tomatoes are vegetables") may be false in a "Botany World." Continuous embeddings struggle to maintain these strict boundaries because their representational coordinates are globally shared, leading to leakage between contradictory discursive domains.

## 2.3 The Absence of Propositional Auditability
When an LLM asserts a fact, the justification is buried in trillions of parameters. Even with attention maps or probing, there is no discrete "logical coordinate" that can be audited to verify if the assertion conforms to the rules of a specific domain. To achieve reliability, we need a system where every asserted proposition can be decomposed into its constituent logical components—subject, predicate, context, and logical form—and validated against a symbolic grammar.
