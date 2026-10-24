# Evidence: Graphlang Collision Detection

In the `graphlang` prototype, we demonstrate that local worlds can detect "Semantic Collisions." When a world is defined with insufficient discriminative dimensions (e.g., trying to distinguish types of tea using only the dimension "color"), the system generates identical bit-signatures for distinct concepts. 

The framework detects this as a "Representational Failure," forcing the operator (or the model) to either:
1. Add a new discriminative dimension.
2. Admit that the world is logically underspecified for that task.

This behavior contrasts with LLMs, which would simply "choose" one concept or conflate them without notifying the user of the logical ambiguity.
