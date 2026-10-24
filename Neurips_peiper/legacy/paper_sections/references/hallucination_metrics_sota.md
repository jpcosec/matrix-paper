# The Hallucination Landscape: Metrics, Benchmarks, and Gaps

Current research in Large Language Models (LLMs) has developed a comprehensive taxonomy for evaluating and mitigating hallucinations. However, these metrics primarily focus on the *output* of the model rather than the *representational validity* of the underlying propositions.

## 1. Evaluation Taxonomy

| Family | Objective | Common Benchmarks |
| :--- | :--- | :--- |
| **Factuality** | Correspondence with external world truth | TruthfulQA, FActScore, SimpleQA, PopQA |
| **Faithfulness / Grounding** | Support by the provided context | HaluEval, QAGS, FactCC, NLI entailment |
| **Self-consistency** | Agreement across multiple samples | SelfCheckGPT, Semantic Entropy |
| **Reasoning Accuracy** | Correctness in formal/mathematical tasks | GSM8K, MATH, BBH, GPQA |
| **Calibration** | Model's awareness of its own ignorance | ECE, Brier score, refusal rate |

## 2. Key Metrics and Their Limitations

- **FActScore (EMNLP 2023):** Decomposes long-form generation into "atomic facts" to calculate precision against reliable sources. *Gap:* It measures the truth of a claim but cannot detect if the claim is a category error within a specific domain.
- **HaluEval (ACL 2023):** A large-scale collection of generated and human-annotated hallucinated samples. *Gap:* It treats hallucinations as content that "conflicts" with a source, but not as a failure of logical representability.
- **SelfCheckGPT (ACL 2023):** Detects hallucinations by measuring consistency across stochastic samples. *Gap:* It identifies uncertainty but lacks a formal logical space to audit *why* the responses diverge.
- **Semantic Entropy (Farquhar et al., Nature 2024):** Measures uncertainty over meanings rather than just token strings. *Gap:* While it moves toward semantic awareness, it remains a probabilistic measure rather than a structural guarantee.
- **TruthfulQA (arXiv 2021):** Specifically targets human-like misconceptions. *Gap:* It shows that scaling does not fix truthfulness but does not provide an alternative representational substrate.

## 3. Current Mitigation Strategies

1.  **Retrieval-Augmented Generation (RAG):** The dominant paradigm. It improves grounding by providing external evidence but does not guarantee the logical composition of the final answer.
2.  **Fact-checking Pipelines:** Using "LLM-as-a-judge" or NLI models to verify claims post-generation. These are reactive rather than preventive.
3.  **Knowledge Graph Integration:** Connecting LLMs to symbolic triplets (KGs). While close to our work, these usually focus on fact retrieval rather than the enforcement of a "Grammar of Sense" ($\Gamma$).

## 4. The "Representability Gap"

Existing hallucination metrics primarily evaluate factual support, faithfulness, consistency, or calibration. We argue that these do not fully capture **representability**: whether a candidate proposition is well-typed, contextually admissible, and assertable within a local grammar of sense.

This position paper addresses this gap by shifting the focus from "checking the output" to "constraining the representational coordinates" of the model's assertions.
