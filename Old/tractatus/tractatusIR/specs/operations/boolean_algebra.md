# Boolean Algebra Operations

## Summary
Pseudocode implementing the complete boolean algebra over signatures: project, denote, sinnvoll/sinnlos/unsinnig classification, similarity, contrast, collisions, and tree building.

## Concepts
- `project(c, K)` → signature (bits + valid mask)
- `denote(q, K)` → subset of local universe
- `well_formed(s, K)` → syntax validation
- `applicable(c, D)` → applicability check
- `status(E, K)` → sinnvoll / sinnlos / unsinnig
- Boolean ops: AND, OR, XOR, NOT, SUM, MASK
- Matrix construction and transpose
- Collision detection and dimension expansion
- Decision tree building from matrices
- **sense_mask**: what bits/dimensions participate in sense for current context
- **discriminative_mask**: what effectively separates candidates now
- **observed_mask**: what has been measured/observed

## Core Structures

```pseudo
Context K:
  universe: Set[Concept]
  dimensions: List[Dimension]
  bit_dictionary: Dict[BitIndex, BitSpec]
  sense_mask: BitVector        # what has sense in this context/task
  discriminative_mask: BitVector  # what effectively separates candidates now
  observed_mask: BitVector       # what has been measured/observed

Dimension D:
  id: String
  type: "one_hot" | "multi_hot" | "boolean"
  values: Set[Value]
  applies_when: Predicate[Concept]
  bit_indices: List[BitIndex]

BitSpec:
  dimension: DimensionID
  value: Value
  applies_when: Predicate[Concept]

Signature:
  bits: BitVector        # 0/1
  valid: BitVector       # 0/1, indicates if that bit applies
```

## Boolean Operations Base

```pseudo
AND(a, b):    return bitwise_and(a, b)
OR(a, b):     return bitwise_or(a, b)
XOR(a, b):    return bitwise_xor(a, b)
NOT(a):       return bitwise_not(a)
SUM(a):        return count_bits_equal_to_1(a)
ANY(a):        return SUM(a) > 0
ALL(a):        return SUM(a) == length(a)
MASK(bits, mask): return bits AND mask
```

## Projection: `project(c, K)` → Signature

Transforms a concept into a binary signature within context K:

```pseudo
project(concept c, context K) -> Signature:
  bits  = zeros(length(K.bit_dictionary))
  valid = zeros(length(K.bit_dictionary))

  for each bit_index i in K.bit_dictionary:
    spec = K.bit_dictionary[i]
    D = K.dimensions[spec.dimension]

    if D.applies_when(c) == false:
      valid[i] = 0
      bits[i] = 0
      continue

    valid[i] = 1
    value_of_c = get_value(c, D)

    if D.type == "one_hot":
      bits[i] = 1 if value_of_c == spec.value else 0

    if D.type == "multi_hot":
      bits[i] = 1 if spec.value in value_of_c else 0

    if D.type == "boolean":
      bits[i] = 1 if value_of_c == true else 0

  return Signature(bits, valid)
```

Example: `project(lechuga, K_COCINA) → bits=[1,0,0,1,0], valid=[1,1,1,1,1]`

## Syntax Validation: `well_formed(s, K)`

Checks if signature respects the boolean grammar of context:

```pseudo
well_formed(signature s, context K) -> Bool:
  for each dimension D in K.dimensions:
    indices = D.bit_indices
    local_bits  = s.bits[indices]
    local_valid = s.valid[indices]

    if SUM(local_valid) == 0:
      continue

    active_bits = MASK(local_bits, local_valid)

    if D.type == "one_hot":
      if SUM(active_bits) != 1:
        return false

    if D.type == "multi_hot":
      continue  # any combination is valid

    if D.type == "boolean":
      if length(indices) != 1:
        return false
      if active_bits[0] not in {0, 1}:
        return false

  return true
```

## Applicability: `applicable(c, D)`

```pseudo
applicable(concept c, dimension D) -> Bool:
  return D.applies_when(c)
```

Example: `D_ESTADO_VITAL.applies_when(c) = c.features["organismo"] == 1`
- `applicable(perro, D_ESTADO_VITAL)` → true
- `applicable(martillo, D_ESTADO_VITAL)` → false

## Matching: `matches(c, q, K)`

A concept satisfies a query if its bits coincide on valid positions:

```pseudo
matches(concept c, query_signature q, context K) -> Bool:
  s = project(c, K)
  common_valid = q.valid AND s.valid
  q_bits = MASK(q.bits, common_valid)
  s_bits = MASK(s.bits, common_valid)
  return q_bits == s_bits
```

## Denotation: `denote(q, K)`

The subset of local universe selected by a signature:

```pseudo
denote(query_signature q, context K) -> Set[Concept]:
  result = empty_set()
  for each concept c in K.universe:
    if matches(c, q, K):
      result.add(c)
  return result
```

Example: `denote(D_PARTE.hoja, K) → {lechuga, espinaca, acelga}`

## Logical Status: `status(E, K)`

Classifies expression into sinnvoll / sinnlos / unsinnig:

```pseudo
status(expression E, context K) -> Status:
  q = project_expression(E, K)

  if q == ERROR:
    return UNSINNIG

  if not well_formed(q, K):
    return UNSINNIG

  S = denote(q, K)
  U = K.universe

  if size(S) == 0:
    return SINNLOS_CONTRADICTION

  if size(S) == size(U):
    return SINNLOS_TAUTOLOGY

  return SINNVOLL
```

Formal:
```
sinnvoll(E, K)  ⇔ well_formed(q, K) ∧ 0 < |denote(q, K)| < |U|
sinnlos(E, K)   ⇔ well_formed(q, K) ∧ (|denote(q, K)| = 0 ∨ |denote(q, K)| = |U|)
unsinnig(E, K)  ⇔ ¬well_formed(q, K) ∨ ¬applicable(q, K)
```

## Truth: `truth_of(E, c, K)`

```pseudo
truth_of(expression E, concept c, context K) -> TruthValue:
  q = project_expression(E, K)
  if q == ERROR:
    return UNDEFINED
  if not well_formed(q, K):
    return UNDEFINED
  if matches(c, q, K):
    return TRUE
  return FALSE
```

## Tautology Detection: `is_tautology(E, K)`

```pseudo
is_tautology(expression E, context K) -> Bool:
  q = project_expression(E, K)
  if not well_formed(q, K):
    return false
  S = denote(q, K)
  return S == K.universe
```

Boolean equivalent: `E = hoja OR raiz OR tallo` → TRUE over universe.

## Contradiction Detection: `is_contradiction(E, K)`

```pseudo
is_contradiction(expression E, context K) -> Bool:
  q = project_expression(E, K)
  if not well_formed(q, K):
    return false
  S = denote(q, K)
  return size(S) == 0
```

## Collision Detection

```pseudo
bucket(dimension D, value v, context K) -> Set[Concept]:
  result = empty_set()
  bit = bit_for(D, v)
  for each concept c in K.universe:
    s = project(c, K)
    if s.bits[bit] == 1:
      result.add(c)
  return result

is_collision(D, v, K) -> Bool:
  return size(bucket(D, v, K)) > 1

detect_collisions(D, K) -> Dict[Value, Set[Concept]]:
  collisions = {}
  for each value v in D.values:
    B = bucket(D, v, K)
    if size(B) > 1:
      collisions[v] = B
  return collisions
```

Example: `bucket(D_PARTE, hoja, K) = {lechuga, espinaca} → collision!`

## Similarity: `similarity(c1, c2, K)`

```pseudo
shared_bits(c1, c2, K) -> BitVector:
  s1 = project(c1, K)
  s2 = project(c2, K)
  common_valid = s1.valid AND s2.valid
  return MASK(s1.bits AND s2.bits, common_valid)

similarity(c1, c2, K) -> Float:
  s1 = project(c1, K)
  s2 = project(c2, K)
  common_valid = s1.valid AND s2.valid
  a = MASK(s1.bits, common_valid)
  b = MASK(s2.bits, common_valid)
  shared = SUM(a AND b)
  union  = SUM(a OR b)
  if union == 0:
    return 0
  return shared / union
```

Jaccard-like over active bits. Example:
```
lechuga  = [1,0,0,1,0]
espinaca = [1,0,0,0,1]
shared = [1,0,0,0,0] → share parte=hoja
diff   = [0,0,0,1,1] → cabeza_compacta vs hoja_suelta
```

## Contrast: `contrast_by_dimension(c1, c2, K)`

```pseudo
contrast_by_dimension(c1, c2, K) -> List[Contrast]:
  contrasts = []
  s1 = project(c1, K)
  s2 = project(c2, K)

  for each dimension D in K.dimensions:
    indices = D.bit_indices
    b1 = s1.bits[indices]
    b2 = s2.bits[indices]
    v1 = s1.valid[indices]
    v2 = s2.valid[indices]
    common_valid = v1 AND v2

    if SUM(common_valid) == 0:
      continue

    diff = MASK(b1 XOR b2, common_valid)
    if ANY(diff):
      contrasts.add({
        dimension: D.id,
        c1_value: decode_value(b1, D),
        c2_value: decode_value(b2, D)
      })

  return contrasts
```

## Matrix Construction: `build_matrix(D, K)`

```pseudo
build_matrix(dimension D, context K) -> Matrix:
  rows = K.universe
  cols = D.values
  M = zeros(rows=len(rows), cols=len(cols))

  for i, concept c in enumerate(rows):
    if not D.applies_when(c):
      continue
    value = get_value(c, D)

    if D.type == "one_hot":
      j = index_of(value, D.values)
      M[i][j] = 1

    if D.type == "multi_hot":
      for each v in value:
        j = index_of(v, D.values)
        M[i][j] = 1

  return M
```

Result:
```
           hoja  raiz  tallo
lechuga        1     0     0
zanahoria      0     1     0
apio           0     0     1
espinaca       1     0     0
```

## Transpose Index: `transpose_index(M, D, K)`

```pseudo
transpose_index(M, D, K) -> Dict[Value, Set[Concept]]:
  index = {}
  for each value v in D.values:
    index[v] = empty_set()

  for i, concept c in enumerate(K.universe):
    for j, value v in enumerate(D.values):
      if M[i][j] == 1:
        index[v].add(c)

  return index
```

Result: `hoja → {lechuga, espinaca}, raiz → {zanahoria}, tallo → {apio}`

## Horizontal Co-membership: `co_membership(M)`

```pseudo
co_membership(M) -> Matrix:
  return M * transpose(M)   # boolean matrix multiplication
```

Where `boolean_matmul(A, B)`: `C[i][j] = OR_over_k(A[i][k] AND B[k][j])`

Result: `S[lechuga][espinaca] = 1` (share hoja value).

## Dimension Expansion: `expand_collision(K, D, v, D2)`

```pseudo
expand_collision(context K, dimension D, value v, next_dimension D2) -> Context:
  B = bucket(D, v, K)
  K_sub = Context()
  K_sub.universe = B
  K_sub.dimensions = [D2]
  K_sub.parent = K
  K_sub.condition = (D == v)
  M_sub = build_matrix(D2, K_sub)
  collisions = detect_collisions(D2, K_sub)
  return K_sub
```

## Next Dimension Selection

```pseudo
score_dimension(D, concepts B, K) -> Float:
  M = build_matrix(D, context_with_universe(B))
  index = transpose_index(M, D, B)
  bucket_sizes = [size(index[v]) for v in D.values if size(index[v]) > 0]
  max_bucket = max(bucket_sizes)
  num_buckets = length(bucket_sizes)
  return num_buckets / max_bucket   # want many small buckets

choose_next_dimension(B, candidate_dimensions, K) -> Dimension:
  best_D = null
  best_score = -infinity
  for each D in candidate_dimensions:
    score = score_dimension(D, B, K)
    if score > best_score:
      best_score = score
      best_D = D
  return best_D
```

## Tree Building: `build_tree(K, candidate_dimensions)`

```pseudo
build_tree(context K, candidate_dimensions) -> TreeNode:
  if size(K.universe) <= 1:
    return Leaf(K.universe)

  D = choose_next_dimension(K.universe, candidate_dimensions)
  M = build_matrix(D, K)
  index = transpose_index(M, D, K)
  node = TreeNode(dimension=D)

  for each value v in D.values:
    B = index[v]
    if size(B) == 0:
      continue
    if size(B) == 1:
      node.children[v] = Leaf(B)
      continue
    K_sub = Context()
    K_sub.universe = B
    K_sub.dimensions = remove(candidate_dimensions, D)
    K_sub.parent = K
    K_sub.condition = (D == v)
    node.children[v] = build_tree(K_sub, K_sub.dimensions)

  return node
```

Result:
```
D_PARTE
├── hoja
│   └── D_ESTRUCTURA_HOJA
│       ├── cabeza → lechuga
│       └── suelta
│           └── D_GROSOR_HOJA
│               ├── delgada → espinaca
│               └── gruesa → acelga
├── raiz → zanahoria
└── tallo → apio
```

## Algebraic Summary

```pseudo
# Projection
b_c = project(c, K).bits

# Effective bits (with sense mask applied)
effective = b_c AND valid AND K.sense_mask

# Shared features
shared(c1, c2) = b_c1 AND b_c2

# Differences
diff(c1, c2) = b_c1 XOR b_c2

# Query matching (with sense mask)
matches(c, q) = MASK(b_c, q.valid AND K.sense_mask) == MASK(q.bits, q.valid AND K.sense_mask)

# Denotation
denote(q, K) = {c ∈ U_K | matches(c, q)}

# sinvoll (now requires sense_mask participation)
sinvoll(q, K) =
  well_formed(q, K)
  AND applicable(q, K)
  AND SUM(q.bits AND q.valid AND K.sense_mask) > 0
  AND 0 < |denote(q, K)| < |U_K|

# sinnlos tautological
sinnlos_taut(q, K) =
  well_formed(q, K)
  AND applicable(q, K)
  AND (|denote(q, K)| = 0 ∨ |denote(q, K)| = |U_K|)

# unsinnig
unsinnig(q, K) =
  NOT well_formed(q, K)
  OR NOT applicable(q, K)

# Outside context (new!)
outside_context(q, K) =
  well_formed(q, K)
  AND SUM(q.bits AND q.valid AND K.sense_mask) = 0

# Collision
collision(D, v, K) = |bucket(D, v, K)| > 1

# Similarity
similar(c1, c2, K) = ANY(project(c1,K).bits AND project(c2,K).bits)

# Contrast
contrast(c1, c2, K) = project(c1,K).bits XOR project(c2,K).bits
```

## Four Masks Summary

| Mask | Purpose | Example |
|------|---------|---------|
| **valid_mask** | What applies to the concept (ontological) | `estado_vital` applies only to `organismo=1` |
| **sense_mask** | What has sense in this context/task | In "distinguish vegetables": `estado_vital=0, precio=0` |
| **discriminative_mask** | What effectively separates candidates now | `parte_comestible` when both are vegetables |
| **observed_mask** | What has been measured/observed | After measuring: `color` and `forma` bits = 1 |

Central rule with masks:
```pseudo
effective_mask = valid_mask AND sense_mask AND observed_mask
search_mask  = valid_mask AND sense_mask AND discriminative_mask AND observed_mask
```

> The sense mask defines which parts of the logical space are enabled as meaningful for the current context.

## References
- turn-32.md (complete boolean algebra pseudocode: project, denote, sinnvoll/sinnlos/unsinnig, similarity, contrast, matrix ops, tree building)
- turn-34.md (sense_mask: valid vs sense vs discriminative vs observed masks; outside_context status)

## Version Notes
- Turn 32: complete boolean algebra implementation with all operations needed for the logical system
- Turn 34: added sense_mask concept — 4 masks (valid, sense, discriminative, observed); new OUTSIDE_CONTEXT status
