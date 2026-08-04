# Introduction

The rapid advancement of Large Language Models (LLMs) has demonstrated an unprecedented capacity for fluent text generation and complex pattern matching. However, these systems remain plagued by a fundamental structural unreliability that predates them and is the cause of drift, unpredictable behaviour and hallucinations, the symbol grounding problem [@harnad1990symbolgrounding]. Current research efforts primarily address this issue through epistemic improvements, such as Retrieval-Augmented Generation or Reinforcement Learning from Human Feedback. We argue, however, that the root of this unreliability is representational rather than purely informational. The reliance on continuous vector spaces as the sole substrate for semantic encoding excels at capturing fuzzy similarities but lacks the discrete primitives necessary to define the rigorous boundaries of logical sense. Consequently, current architectures often conflate falsehood with fundamental inapplicability.

To address this representational gap, this paper argues for the necessity of a discrete, locally scoped representational layer that explicitly separates the stochastic nature of linguistic signs from their underlying deterministic logical structure. Drawing upon the logical atomism of Ludwig Wittgenstein’s Tractatus Logico-Philosophicus—specifically the premise that the logical structure of the world is determined by facts rather than isolated things — **we propose a transition from probabilistic distances to verifiable, algebraic logical coordinates.** Under this framework, propositions must be evaluated not only by their truth value but by their state of meaning: *Sinnvoll* (meaningful), *Sinnlos* (tautological or contradictory), and *Unsinnig* (absurd or structurally inapplicable).

By treating the validity of assertions as a problem of representability within a strict grammar of sense, we propose decoupling language processing into two parallel dimensions. We define a partition of the world $W_i$ through a Boolean matrix evaluating Truth $V_i$ and a secondary matrix evaluating Sense or applicability $S_i$. This separation provides a mathematical mechanism—a "sense mask"—that filters out *Unsinnig* (absurd) propositions before they can perturb the logical evaluation of a system.

Ultimately, instead of attempting to teach models not to lie through continuous probabilistic weights, this work formally defines an algebraic architecture that is structurally incapable of representing nonsense. By mapping structured knowledge into these Boolean matrices, we present a direct projection between thought and its logical image, providing a deterministic anchor that could redefine how neural reasoning and knowledge verification operate in specialized domains.

Section ID: 01_introduction
Source Section File: sections/01_introduction.md

## Paragraph Refs

- ../paragraphs/01_introduction-p01.md
- ../paragraphs/01_introduction-p02.md
- ../paragraphs/01_introduction-p03.md
- ../paragraphs/01_introduction-p04.md

## Paragraph Digest
