# Source Atomization Strategy

Current migration rule:

1. treat the current `specs/` tree as the most coherent working base
2. atomize existing specs first
3. only create new atoms when overlap or contradiction proves they are needed
4. treat missing atoms at the end as either:
   - necessary new canonical pieces
   - or real gaps to be filled deliberately later

This avoids filling `atomos/` in the abstract before the current spec corpus has been decomposed.
