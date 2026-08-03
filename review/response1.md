Official Review of Submission986 by Reviewer ppL8
Official Reviewby Reviewer ppL826 Jun 2026, 02:20 (modified: 23 Jul 2026, 07:50)Program Chairs, Area Chairs, Reviewer ppL8, Authors, Reviewers SubmittedRevisions
Ethics: NO or VERY MINOR ethics concerns only
Position: Yes the paper is clearly a fit for the Position Paper Track
Summary:
This paper takes the position that hallucinations in LLMs are a result of the representation choice as they represent concepts using continuous vectors. Therefore, the current mitigations of using RAG or RLHF which treat the hallucination problem from an informational standpoint are misguided. As a result, the paper argues that embeddings are structurally incapable of guaranteeing truth or logical consistency, leading to hallucinations. The proposed solution is that LLMs should move towards neuro-symbolic representations which can model facts and relationships in a logical manner. The paper derives its reasoning from Ludwig Wittgenstein's Tractatus Logico-Philosophicus and proposes a symbolic formulation that can structurally prevent / reject concepts which are not possible.

Author Identification: No.
Support: 2: fair
Significance: 2: fair
Presentation: 3: good
Context: 2: fair
Discussion: 2: unlikely
Alternative Position: No
Strengths:
The paper offers a unique and intellectually stimulating perspective on the hallucination problem.
The manuscript is well-structured and clear. The paper uses an illustrative example to explain the proposed approach, and it significantly helps the reader to understand what such a logic based formulation might look like.
Weaknesses:
The paper does not cite and discuss quite a bit of literature focused on understanding the cause of hallucinations. The paper is based on the claim that hallucinations are a representation problem, but this claim isn't backed up. The rest of the paper is focused on proposing a solution assuming the claim to be true. There are several papers which have studied hallucination [e.g. 1-7], and the paper should cite and discuss them.

The paper proposes this approach of building a World and a Scene matrix to build the symbolic representation. However, how these matrices could be created at scale is not discussed. Modern LLMs are trained on huge amounts of data and it is unclear how such a formulation could be applied there. Manually building such a matrix is clearly not feasible. Furthermore, concepts can mean different things in varying contexts. It is unclear how these problems would be tackled.

One of the requirements of the position paper track is that the paper should highlight the importance of their position. However, the paper only briefly touches upon the importance of solving hallucinations in the introduction. Section 2 is focused on methods to tackle this, but the overall argument on why this problem is important is missing. While I personally agree with the importance of the topic, this is something that should be covered within the paper as well as highlighted in the instructions due to the broad audience.

References:

https://aclanthology.org/2023.findings-emnlp.182.pdf, EMNLP 2023
https://aclanthology.org/2023.findings-acl.551.pdf, ACL 2023
https://arxiv.org/abs/2310.06824, CoLM 2024
https://arxiv.org/pdf/2402.03744, ICLR 2024
https://arxiv.org/pdf/2403.05612, NAACL 2025
https://aclanthology.org/2024.emnlp-main.444.pdf, EMNLP 2024
https://arxiv.org/pdf/2309.03883, ICLR 2024
Questions:
Can the authors please discuss how they think the sense and world matrices could be created in a real world setup?
Agreement: 3: neither agree nor disagree
Rating: 3: Reject: The paper has a weakly stated position, technical or logical flaws, inadequate support for claims, or addresses an issue of limited scope.
Confidence: 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.
Thoroughness: 3: You read the paper carefully but did not check all of the details.
Code Of Conduct Acknowledgement: Yes
LLM Policy Acknowledgement: Yes
