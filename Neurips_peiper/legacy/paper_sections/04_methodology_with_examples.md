# Methodology: A Tractarian Framework for Semantic Validation

Our methodology for semantic representation and validation is structured in three layers: the philosophical foundation, the bit-and-matrix representation model, and the algebraic operational logic.

## 1. Philosophical Foundation: The Tractarian Influence

Our framework operationalizes key insights from Ludwig Wittgenstein’s *Tractatus Logico-Philosophicus* to create a computable "Grammar of Sense":

- **The World as a Totality of Facts:** We represent knowledge not as a flat list of objects, but as a collection of asserted propositions (facts) within a logical space.
- **Sense ($Sinn$) vs. Truth ($Wahrheit$):** We treat *sense* as a structural property. An expression is senseful if it represents a possible configuration in logical space. Truth is the subsequent correspondence of that senseful expression with the actual state of the world.
- **Logical Space and Coordinates:** Every concept exists within a "space of possible atomic facts." We implement this by projecting concepts onto coordinates in locally scoped worlds. If a concept cannot be projected into a world's coordinates (e.g., because of a category error), it is outside the "limits of that world" and thus *unsinnig* (senseless).

### Example: Sense Before Truth

Consider the local world `K_CULINARY_VEGETABLES`, whose task is to discriminate vegetables according to their culinary use.

The proposition:

```text
lettuce has edible_part = leaf
```

is senseful because `edible_part` is a valid coordinate in this world and `leaf` is one of its allowed values.

By contrast:

```text
lettuce has engine_type = diesel
```

is not false in the same way that a mistaken empirical claim is false. Rather, it is outside the coordinate system of the culinary vegetable world. The predicate `engine_type` does not belong to the local logical space, so the expression is treated as structurally senseless within this context.

## 2. Representation Model: Bits and Matrices

We transform linguistic signs into discrete logical coordinates using a dual representation system.

### 2.1 Bit-Level Representation: Signatures and Masks

Every concept in a context is compiled into a **Typed Binary Signature**. To preserve meaning, we use a **Bit Dictionary** that maps every bit position to a specific `(Dimension, Value)` pair.

- **Encoding Schemes:** We use **one-hot encoding** for exclusive dimensions, such as `edible_part = leaf`, and **multi-hot encoding** for non-exclusive properties, such as `culinary_usage = salad, soup`.
- **The Four-Mask System:** To handle incomplete or inapplicable data, we employ a masking architecture:
    - `valid_mask`: what applies to the concept, i.e. its ontological boundary.
    - `sense_mask`: what is relevant in the current context or task.
    - `observed_mask`: what has been measured or asserted.
    - `discriminative_mask`: what effectively separates concepts in the current local universe.

#### Example: Bit Dictionary and Typed Signature

Suppose the context is:

```yaml
context:
  id: K_CULINARY_VEGETABLES
  task: discriminate
  local_universe:
    - C_LETTUCE
    - C_CARROT
    - C_CELERY
    - C_SPINACH
  active_dimensions:
    - D_EDIBLE_PART
    - D_CULINARY_USAGE
```

The context defines the following bit dictionary:

```yaml
bit_dictionary:
  0:
    dimension: D_EDIBLE_PART
    value: leaf
    encoding: one_hot
  1:
    dimension: D_EDIBLE_PART
    value: root
    encoding: one_hot
  2:
    dimension: D_EDIBLE_PART
    value: stem
    encoding: one_hot
  3:
    dimension: D_CULINARY_USAGE
    value: salad
    encoding: multi_hot
  4:
    dimension: D_CULINARY_USAGE
    value: soup
    encoding: multi_hot
```

The concept `C_LETTUCE` may then be encoded as:

```yaml
concept: C_LETTUCE
context: K_CULINARY_VEGETABLES
values:
  D_EDIBLE_PART: leaf
  D_CULINARY_USAGE:
    - salad
signature:
  bit_order:
    - D_EDIBLE_PART.leaf
    - D_EDIBLE_PART.root
    - D_EDIBLE_PART.stem
    - D_CULINARY_USAGE.salad
    - D_CULINARY_USAGE.soup
  values: [1, 0, 0, 1, 0]
```

Here, the first three bits form a one-hot block, because a vegetable has only one main edible part in this context. The last two bits form a multi-hot block, because a vegetable may be used in more than one culinary role.

#### Example: Masks

The four-mask system allows the signature to distinguish `false`, `unknown`, and `not applicable`.

```yaml
concept: C_LETTUCE
signature:           [1, 0, 0, 1, 0]
valid_mask:          [1, 1, 1, 1, 1]
sense_mask:          [1, 1, 1, 0, 0]
observed_mask:       [1, 1, 1, 1, 0]
discriminative_mask: [1, 1, 1, 0, 0]
```

In this example, the task is to discriminate vegetables by edible part, so only the first three coordinates are relevant to sense and discrimination. The `soup` value is not observed, but it is still a valid coordinate for the concept.

For a non-vegetable object in the same context, such as `C_CAR_ENGINE`, the signature behaves differently:

```yaml
concept: C_CAR_ENGINE
signature:     [0, 0, 0, 0, 0]
valid_mask:    [0, 0, 0, 0, 0]
sense_mask:    [1, 1, 1, 0, 0]
observed_mask: [0, 0, 0, 0, 0]
```

The zeros in the signature do not mean that the engine empirically lacks leaves, roots, or stems. They mean that those coordinates do not apply to the object in this local world. This distinction prevents category errors from being treated as ordinary negative facts.

### 2.2 Encoding Procedure

Given a concept `c` and a context `K`, the encoder constructs a typed binary signature by projecting `c` onto the context's discriminative dimensions. The context specifies the local universe, the active dimensions, the allowed values for each dimension, and the applicability conditions of each dimension.

Algorithmically, the encoder:

1. retrieves the active dimensions of `K`;
2. maps each `(dimension, value)` pair to a stable bit position;
3. evaluates whether each dimension applies to `c`;
4. encodes applicable categorical dimensions using one-hot vectors;
5. encodes non-exclusive properties using multi-hot vectors;
6. records inapplicable coordinates in the `valid_mask`;
7. records unobserved coordinates in the `observed_mask`;
8. filters task-relevant coordinates using the `sense_mask`;
9. returns the effective signature `σ_eff = σ ∧ mask_sense`;
10. inserts `σ_eff` as the row corresponding to `c` in `M_1`.

#### Example: Encoding One Concept

For `C_CARROT`, the context provides:

```yaml
input:
  concept: C_CARROT
  context: K_CULINARY_VEGETABLES
assertions:
  D_EDIBLE_PART: root
  D_CULINARY_USAGE:
    - soup
```

Using the same bit order:

```text
[D_EDIBLE_PART.leaf,
 D_EDIBLE_PART.root,
 D_EDIBLE_PART.stem,
 D_CULINARY_USAGE.salad,
 D_CULINARY_USAGE.soup]
```

The encoder returns:

```yaml
encoded_output:
  concept: C_CARROT
  raw_signature:       [0, 1, 0, 0, 1]
  valid_mask:          [1, 1, 1, 1, 1]
  sense_mask:          [1, 1, 1, 0, 0]
  observed_mask:       [1, 1, 1, 0, 1]
  discriminative_mask: [1, 1, 1, 0, 0]
  effective_signature: [0, 1, 0, 0, 0]
```

The raw signature stores all asserted information. The effective signature keeps only the bits relevant to the current discrimination task. Therefore, `soup` remains available as knowledge, but it is ignored for this particular local distinction.

### 2.3 Matrix-Level Representation: $M_1$ and $M_1^\intercal$

We organize these signatures into a multi-layered matrix model:

- **$M_1$ (Concept × DiscriminantValue):** A sparse matrix where $M_1[i, j] = 1$ if concept `i` satisfies discriminant value `j`.
- **$M_1^\intercal$ (DiscriminantValue × Concept):** The transpose matrix, which functions as a set of **Search Buckets** or an inverted index. This allows direct lookup for all concepts sharing a specific property.

#### Example: Concept × DiscriminantValue Matrix

For the discriminative dimension `D_EDIBLE_PART`, the local universe is:

```text
U_K = {C_LETTUCE, C_CARROT, C_CELERY, C_SPINACH}
```

The matrix $M_1$ is:

| Concept | leaf | root | stem |
| :--- | ---: | ---: | ---: |
| C_LETTUCE | 1 | 0 | 0 |
| C_CARROT | 0 | 1 | 0 |
| C_CELERY | 0 | 0 | 1 |
| C_SPINACH | 1 | 0 | 0 |

Each row is the encoding of one concept with respect to the active discriminative dimension.

The transposed matrix $M_1^\intercal$ is:

| Discriminant value | C_LETTUCE | C_CARROT | C_CELERY | C_SPINACH |
| :--- | ---: | ---: | ---: | ---: |
| leaf | 1 | 0 | 0 | 1 |
| root | 0 | 1 | 0 | 0 |
| stem | 0 | 0 | 1 | 0 |

This transpose can be read as an inverted index:

```yaml
index:
  D_EDIBLE_PART:
    leaf:
      - C_LETTUCE
      - C_SPINACH
    root:
      - C_CARROT
    stem:
      - C_CELERY
```

Therefore, the query:

```yaml
query:
  D_EDIBLE_PART: leaf
```

returns:

```yaml
result:
  - C_LETTUCE
  - C_SPINACH
```

This is also where semantic collisions become visible: more than one concept occupies the bucket `leaf`.

## 3. Operational Logic: Boolean Algebra and Dynamic Refinement

Validation and reasoning are implemented as bitwise and matrix operations over the Boolean semiring $(\mathbb{B}, \vee, \wedge, 0, 1)$.

### 3.1 Table of Core Operations

| Operation | Logical Intent | Formal Calculation | Example |
| :--- | :--- | :--- | :--- |
| **Projection** | Map concept to coordinates | $P(c, K) \to \sigma \in \{0, 1\}^n$ | $P(C\_CARROT, K) = [0,1,0,0,1]$ |
| **Sense Masking** | Filter context-relevant bits | $\sigma_{eff} = \sigma \wedge mask_{sense}$ | $[0,1,0,0,1] \wedge [1,1,1,0,0] = [0,1,0,0,0]$ |
| **Similarity** | Find shared features | $S(c_1, c_2) = \sigma_{c1} \wedge \sigma_{c2}$ | lettuce $\wedge$ spinach = `[1,0,0]` |
| **Contrast** | Identify discriminative differences | $C(c_1, c_2) = \sigma_{c1} \oplus \sigma_{c2}$ | lettuce $\oplus$ carrot = `[1,1,0]` |
| **Denotation** | Select universe subset | $\{c \in U \mid \sigma_c \wedge mask_{query} = mask_{query}\}$ | `leaf` returns lettuce and spinach |
| **Co-membership** | Identify concepts in same bucket | $M_1 \times M_1^\intercal$ (Boolean MatMul) | lettuce and spinach share the `leaf` bucket |
| **Collision** | Detect logical underspecification | $\exists v : \|M_1^\intercal[v, \cdot]\|_1 > 1$ | `leaf = {lettuce, spinach}` |

### 3.2 Dynamic Expansion: Collision and Refinement

If a local world cannot distinguish between two concepts ($|bucket(v)| > 1$), a **Semantic Collision** is triggered. The system then performs **Recursive Submatrix Expansion**, introducing a new discriminative dimension to split the logical space. This ensures that the system's "Grammar of Sense" is always as complex as the distinctions it is required to make, but no more.

#### Example: Collision and Recursive Submatrix Expansion

The first matrix detects the following collision:

```yaml
collision:
  context: K_CULINARY_VEGETABLES
  dimension: D_EDIBLE_PART
  value: leaf
  bucket:
    - C_LETTUCE
    - C_SPINACH
  status: unresolved
```

The system creates a subcontext whose universe is only the colliding bucket:

```yaml
subcontext:
  id: K_CULINARY_VEGETABLES__LEAF_BUCKET
  parent_context: K_CULINARY_VEGETABLES
  local_universe:
    - C_LETTUCE
    - C_SPINACH
  active_dimension:
    D_LEAF_STRUCTURE
```

A new discriminative dimension is introduced:

```yaml
dimension:
  id: D_LEAF_STRUCTURE
  question: How is the edible leaf organized?
  values:
    - compact_head
    - loose_leaf
```

The resulting submatrix is:

| Concept | compact_head | loose_leaf |
| :--- | ---: | ---: |
| C_LETTUCE | 1 | 0 |
| C_SPINACH | 0 | 1 |

The corresponding index is:

```yaml
index:
  D_LEAF_STRUCTURE:
    compact_head:
      - C_LETTUCE
    loose_leaf:
      - C_SPINACH
```

The collision is now resolved because every bucket contains exactly one concept:

```yaml
collision_status:
  D_LEAF_STRUCTURE.compact_head: resolved
  D_LEAF_STRUCTURE.loose_leaf: resolved
```

The recursive structure can be read as a decision tree:

```text
D_EDIBLE_PART
├── leaf
│   └── D_LEAF_STRUCTURE
│       ├── compact_head → C_LETTUCE
│       └── loose_leaf   → C_SPINACH
├── root → C_CARROT
└── stem → C_CELERY
```

The refinement process stops when the local task is satisfied, i.e. when the required concepts can be distinguished at the desired resolution.
