# Appendix source 18

Kind: current-paper-block
Origin: sections/10_appendix.md
Anchor: 10_appendix-p18

## Excerpt

`argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wrong *reproducibly*, with no sampling randomness to blame. This cuts both ways—stochastic decoding is not the culprit either; both inherit the substrate. The design conclusion is that the boundary must be imposed *before* decoding, at compile time, where a stored Boolean matrix $S_i$ provides an exact check in $O(1)$ per step instead of an approximate one distributed across the network.

## Relevance

Bootstrap source block 18 extracted from the current Appendix draft.
