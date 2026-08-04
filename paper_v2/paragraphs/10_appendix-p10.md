# Appendix paragraph 10

Section: 10_appendix
Paragraph Index: 10

## Notes

- ../notes/10_appendix-p10.md

## Paragraph Text

Let $f: \mathbb{R}^d \to \{0,1\}$ indicate logical validity, discontinuous at the boundary of its support. Universal approximation results [@hornik1991approximation] guarantee convergence in $L^1$ / in measure: the *mass* of the error region can be made arbitrarily small. Convergence is not uniform, however: near a jump, any smooth or piecewise-smooth approximator exhibits a transition band with overshoot—the Gibbs phenomenon, whose classical overshoot is $\approx 8.95\%$ of the jump magnitude. Narrowing the band requires steeper activations and more units, but the band does not vanish with more data or training; it is a fundamental mathematical property of approximating a jump with continuous functions. In semantic terms, this inescapable limit means there is always a region where *Unsinn* receives an intermediate score instead of a strict exclusion.

## Note Digest
