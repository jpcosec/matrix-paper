# Appendix note 18

Stage: writing-note

## Sources

- ../sources/10_appendix-p18.md

## Intent

Bridge source block 18 into section-ready prose for Appendix.

## Claim

`argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wrong *reproducibly*, with no sampling randomness to blame.

## Notes

`argmax` is a deterministic function of the score surface: wherever the surface is distorted, decoding is wrong *reproducibly*, with no sampling randomness to blame. This cuts both ways—stochastic decoding is not the culprit either; both inherit the substrate. The design conclusion is that the boundary must be imposed *before* decoding, at compile time, where a stored Boolean matrix $S_i$ provides an exact check in $O(1)$ per step instead of an approximate one distributed across the network.

## Source Digest
