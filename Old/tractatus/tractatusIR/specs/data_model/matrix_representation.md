# Matrix Representation Model

## Summary
The spec uses multiple matrix representations to encode concepts, discriminative dimensions, and inverted indices for efficient lookup and collision detection.

## Concepts
- M0: Concept × Feature matrix (base properties)
- M1: Concept × DiscriminantValue matrix (response to discriminative question)
- M1ᵀ: DiscriminantValue × Concept matrix (search buckets / inverted index)
- Recursive submatrix expansion on collisions
- One-hot encoding of dimension values

## Content

### M0: Concept × Feature Matrix
The base matrix mapping concepts to their features.
```
           vegetal alimento hoja raiz tallo
lechuga         1       1      1    0    0
espinaca        1       1      1    0    0
zanahoria       1       1      0    1    0
apio            1       1      0    0    1
```
Represents **properties** of concepts as binary vectors.

### M1: Concept × DiscriminantValue Matrix
Maps concepts to their values within a discriminative dimension.
```
           hoja   raiz   tallo
lechuga      1      0      0
zanahoria    0      1      0
apio         0      0      1
espinaca     1      0      0
```
Represents **responses to discriminative questions**. More semantically meaningful than M0.

### M1ᵀ: DiscriminantValue × Concept Matrix (Inverted Index)
The transpose of M1, functioning as search buckets.
```
          lechuga zanahoria apio espinaca
hoja         1        0      0        1
raiz         0        1      0        0
tallo        0        0      1        0
```
Directly gives:
- `bucket(hoja) = {lechuga, espinaca}`
- `bucket(raiz) = {zanahoria}`
- `bucket(tallo) = {apio}`

### Collision Detection
When `|bucket(v)| > 1`, a collision exists requiring dimension expansion:
```
bucket(hoja) = {lechuga, espinaca} → collision detected
```
Add secondary dimension: `estructura_de_hoja`

### Recursive Submatrix Expansion
On collision, build a submatrix for the colliding subgroup:
```
D1: parte_comestible_principal
├── hoja
│   └── D2: estructura_de_hoja
│       ├── hoja_en_cabeza → lechuga
│       └── hoja_suelta
│           └── D3: grosor_hoja
│               ├── delgada → espinaca
│               └── gruesa → acelga
├── raiz → zanahoria
└── tallo → apio
```
This is literally a **search tree built from matrices**.

### M1 × M1ᵀ: Horizontal Similarity
Computes concept similarity by shared discriminant values.
```
       lechuga zanahoria apio espinaca
lechuga      1        0      0      1
zanahoria    0        1      0      0
apio         0        0      1      0
espinaca     1        0      0      1
```
Tells us: lechuga and espinaca share the same discriminant value (hoja).

### Formal Definition
```
D: C → V
where:
  C = set of concepts
  V = set of possible dimension values
```
One-hot encoding:
```
M_D[c, v] = 1  if D(c) = v
```
Transpose (inverted index):
```
M_Dᵀ[v, c] = 1  if c belongs to bucket v
```
Collisions: values v where `|bucket(v)| > 1`

### M_D × M_Dᵀ: Horizontal Relations
Computes co-membership or collision structure:
- Concepts sharing values → horizontal similarity
- Values with multiple concepts → collision points needing expansion

## Summary of Matrix Roles

| Matrix  | Represents                  | Use                                |
| ------- | --------------------------- | ---------------------------------- |
| M0      | Concept × Feature           | Base properties                    |
| M1      | Concept × DiscriminantValue | Discriminative response            |
| M1ᵀ     | DiscriminantValue × Concept | Buckets / inverted index           |
| M1  M1ᵀ | Concept × Concept           | Horizontal similarity / collisions |

## References
- turn-14.md (M0 concept × feature matrix example)
- turn-18.md (M1, M1ᵀ definitions, recursive expansion, formalization)

## Version Notes
- Turn 14: introduced M0 (concept × feature) matrix
- Turn 18: extended to M1 (concept × discriminant value) and M1ᵀ (inverted index), formalization with D: C → V
