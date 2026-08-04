# Appendix paragraph 18

Section: 10_appendix
Paragraph Index: 18

## Notes

- ../notes/10_appendix-p18.md

## Paragraph Text

`argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wrong *reproducibly*, with no sampling randomness to blame. This cuts both ways—stochastic decoding is not the culprit either; both inherit the substrate. The design conclusion is that the boundary must be imposed *before* decoding, at compile time, where a stored Boolean matrix $S_i$ provides an exact check in $O(1)$ per step instead of an approximate one distributed across the network.

## Note Digest
