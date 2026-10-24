# Logical and Semantic Guarantees in LLMs Require More Than Continuous Embeddings

## Abstract
**This position paper argues that continuous embeddings are insufficient as the sole semantic substrate for reliable LLM-based systems.** Embeddings support similarity, generalization, and retrieval, but they do not by themselves define what counts as a valid proposition, a category error, a contextual truth, or a recoverable explanation. We argue that future AI systems need an additional representational layer: locally scoped logical spaces in which linguistic signs are separated from logical structure, and propositions are compiled into typed, auditable, context-bound coordinates. To support this position, we define a representational and operational framework for world-local semantic validation. In this framework, each local world specifies its own universe of concepts, admissible relations, rules of sense, and signatures. Candidate propositions must pass through symbolic validation before being asserted as knowledge. Mathematically, the framework is grounded in a contextualized boolean algebra over typed binary signatures. Our central claim is that hallucination mitigation should not be treated only as a retrieval problem, but as a representability problem: systems should reject propositions that cannot be expressed within the local grammar of sense.

## 1. Introduction

The rapid advancement of Large Language Models (LLMs) has demonstrated an unprecedented ability to generate fluent text and perform complex reasoning tasks. However, these systems remain plagued by "hallucinations"—the generation of factually incorrect or logically nonsensical statements. Current research efforts primarily treat hallucinations as failures of retrieval (Retrieval-Augmented Generation) or calibration (Reinforcement Learning from Human Feedback). 

In this paper, we propose that the root of the problem lies deeper: in the representational nature of the continuous embeddings that serve as the foundation of modern AI. Continuous vector spaces excel at capturing statistical associations and fuzzy similarities, but they lack the structural primitives necessary to define the boundaries of sense. They cannot, by themselves, distinguish between a proposition that is merely "unlikely" and one that is "logically impossible" or "semantically nonsensical" within a given domain.

**This position paper argues that reliable AI systems require a discrete, locally scoped representational layer that separates linguistic signs from logical structure, treating the validity of assertions as a problem of representability within a grammar of sense.** We contend that instead of attempting to build a single, universal model of truth, we should build systems capable of managing a database of "local worlds." Each world defines its own logical coordinates, and propositions are only admissible if they can be projected into that local space.

## 2. The Limits of Continuous Representability

Modern LLMs represent meaning through points in high-dimensional continuous spaces. While this enables powerful generalization, it introduces three fundamental limitations that prevent formal semantic guarantees:

### 2.1 The Confusion of Similarity and Sense
In a continuous embedding space, "apple" and "orange" are near each other because they are fruits. However, "the square root of an apple" is also a point in that space. The geometry of the space does not forbid the construction of such a vector, nor does it provide a mechanism to identify it as a category error. Because every point in a continuous space is potentially "reachable," the system has no inherent "Grammar of Sense" to reject nonsensical combinations of valid signs.

### 2.2 Global Coverage vs. Local Validity
Language models are trained to capture global statistical patterns across vast datasets. This leads to a "flat" ontology where truth values are averaged over conflicting contexts. However, a proposition that is true in a "Cooking World" (e.g., "tomatoes are vegetables") may be false in a "Botany World." Continuous embeddings struggle to maintain these strict boundaries because their representational coordinates are globally shared, leading to leakage between contradictory discursive domains.

### 2.3 The Absence of Propositional Auditability
When an LLM asserts a fact, the justification is buried in trillions of parameters. Even with attention maps or probing, there is no discrete "logical coordinate" that can be audited to verify if the assertion conforms to the rules of a specific domain. To achieve reliability, we need a system where every asserted proposition can be decomposed into its constituent logical components—subject, predicate, context, and logical form—and validated against a symbolic grammar.

## 3. The Tractarian Alternative: World-Local Semantics

To address these limitations, we draw inspiration from the early work of Ludwig Wittgenstein. In the *Tractatus Logico-Philosophicus*, the world is not a collection of things, but a collection of facts (propositions) in logical space. Crucially, the "Grammar of Sense" (*Sinn*) precedes the "Truth" (*Wahrheit*) of a statement. A statement has sense if it represents a possible state of affairs within a logical space, regardless of whether it is currently true.

We propose an architecture where knowledge is stored in **locally scoped logical worlds** ($W$). A world is not a mini-Wikipedia; it is a **coordinate system** defined by its dimensions of discrimination. In this view:
1.  **Sense is local:** A proposition is only meaningful if it can be projected onto the dimensions defined by the local world.
2.  **Representability is the filter:** If a candidate proposition (generated by an LLM) does not fit the local coordinates, it is rejected as "senseless" (*unsinnig*) before it can even be evaluated for truth.
3.  **Signs are separated from Structure:** We use LLMs to map natural language to "Names" (signs), but the "Logical Form" (the way those names can connect) is governed by a hard-coded symbolic layer.

## 4. Formal Framework for Semantic Validation

We formalize this position through a representational framework based on **Contextualized Boolean Algebra** and **Typed Binary Signatures**.

### 4.1 The Logical World ($W$)
A logical world is defined as a tuple $W = \langle C, \Delta, \Gamma, \Psi \rangle$, where:
- $C$ is the set of stable names (concepts).
- $\Delta$ is a set of discriminative dimensions (e.g., `Color`, `Function`).
- $\Gamma$ is the **Grammar of Sense**, a set of constraints defining which concepts can be projected onto which dimensions.
- $\Psi$ is the projection function that maps concepts to coordinates.

### 4.2 Propositions as Coordinates
An atomic proposition $P$ is represented not as a vector, but as a **coordinate set** within the world's dimensions. For a concept $c \in C$ and a dimension $d \in \Delta$, the projection $\Psi(c, d) = v$ produces a typed binary signature $\sigma$. 

This signature acts as a **mask of possibility**. If the grammar $\Gamma$ forbids the connection between $c$ and $d$, the projection returns a null-mask ($\emptyset$), effectively making the proposition unrepresentable.

### 4.3 Operational Logic
Instead of cosine similarity, our framework uses boolean operations over binary signatures to perform reasoning:
- **Contrast ($\oplus$):** The difference between two concepts is their XOR signature. This shows exactly which dimensions differentiate them.
- **Filtering ($\wedge$):** Queries are boolean masks that select concepts that satisfy specific logical forms.
- **Inclusion ($\subseteq$):** Logical entailment is verified through bitwise inclusion in the boolean semiring.

By compiling knowledge into these auditable bit-vectors, we create a **Symbolic Validation Layer** that sits between the LLM and the database. The LLM proposes a state of affairs, but the World ($W$) authorizes its representation.

## 5. Evidence from Prototype Implementation

To demonstrate the operational viability of this position, we have implemented a prototype system, `graphlang`, in Common Lisp. The system provides a microkernel for managing world-local semantics, including:

- **Contextual Discrimination Engines:** Instead of global embeddings, the system constructs local discrimination trees that compile concepts into bit-signatures based on the available dimensions of a specific "world."
- **Collision Detection:** The system automatically identifies when a world lacks the discriminative power to distinguish between two distinct concepts, marking the state as logically "underspecified."
- **Semantic Masking:** Operations on signatures are governed by validity masks. This ensures that operations like XOR-based contrasts only occur between concepts that belong to the same logical domain, preventing the "category errors" common in continuous spaces.

This implementation proves that the Tractarian requirement of "representability as a condition for sense" can be achieved with low computational overhead and high formal rigor, providing a scalable path for hybrid AI architectures.

## 6. Objections and Counterarguments

The position that AI requires a symbolic, world-local representational layer faces several viable counterarguments:

**Objection 1: The Scaling Hypothesis.**
*Argument:* One could argue that as LLMs scale, they will implicitly learn the boundaries of sense and logic from data, making an explicit symbolic layer redundant.
*Response:* While scaling improves statistical performance, it does not change the underlying representational geometry. A continuous space remains inherently "open" and lack the discrete boundaries required for formal validation. Implicit logic is not the same as explicit auditability.

**Objection 2: The Knowledge Bottleneck.**
*Argument:* Defining local worlds and grammars of sense is labor-intensive and creates a "knowledge bottleneck" reminiscent of classical symbolic AI.
*Response:* Unlike classical AI, which attempted to model the *entire* world, our approach focuses on *locally scoped* worlds. We argue that LLMs themselves can be used as "assimilation engines" to help human operators bootstrap these local structures, combining the flexibility of neural models with the safety of symbolic coordinates.

## 7. Conclusion

The current trajectory of LLM development focuses on making models "smarter" through more data and better retrieval. However, we argue that the most critical frontier for reliable AI is not the quantity of knowledge, but the **structure of representability**. 

By adopting a world-local, Tractarian approach to semantics, we can move beyond the "black box" of continuous embeddings and towards systems that can formally guarantee the sense and auditability of their assertions. A system that cannot represent nonsense is inherently more reliable than one that must be taught, through endless calibration, not to speak it.
