# Anexo B: Bit Representation Details

## B.1 Summary

The system can be represented using only bits, provided each bit is bound to a dimension and interpretable value via a bit dictionary.

## B.2 Concepts

- Bit vector (pure binary representation)
- Bit dictionary (maps position → dimension + value)
- One-hot encoding (exactly one active bit per dimension)
- Multi-hot encoding (zero, one, or many active bits per dimension)
- Validity mask (distinguish false vs unknown vs not-applicable)
- Two-bit encoding (00=unknown, 01=false, 10=true, 11=n/a)
- Closed-world assumption locally
- Bit operations for similarity (AND for shared, XOR for differences)

## B.3 Minimal Binary Representation

A concept in context becomes a bit vector:
```
lechuga   = [1,0,0]
zanahoria = [0,1,0]
apio      = [0,0,1]
```
With bit order: `[D_PARTE_COMESTIBLE.hoja, D_PARTE_COMESTIBLE.raiz, D_PARTE_COMESTIBLE.tallo]`

## B.4 Bit Dictionary (Mandatory)

Without a dictionary, bits lose meaning:
```yaml
bit_dictionary:
  0:
    dimension: D_PARTE_COMESTIBLE
    value: hoja
  1:
    dimension: D_PARTE_COMESTIBLE
    value: raiz
  2:
    dimension: D_PARTE_COMESTIBLE
    value: tallo
```
With dictionary: `[1,0,0] = hoja_comestible`

## B.5 Full Binary Representation

```yaml
signature:
  context: K_COCINA_VERDURAS
  bit_order:
    - D_PARTE_COMESTIBLE.hoja
    - D_PARTE_COMESTIBLE.raiz
    - D_PARTE_COMESTIBLE.tallo
  values:
    C_LECHUGA:   [1,0,0]
    C_ZANAHORIA: [0,1,0]
    C_APIO:      [0,0,1]
```

## B.6 Concatenated Dimensions

Multiple dimensions concatenated:
```
[
  parte.hoja, parte.raiz, parte.tallo,
  color.verde, color.naranja,
  forma.laminar, forma.alargada
]
```
```
lechuga = [1,0,0, 1,0, 1,0]
zanahoria = [0,1,0, 0,1, 0,1]
```

## B.7 One-Hot Encoding (Exclusive Dimensions)

Exactly one active bit per dimension:
```
D_PARTE_COMESTIBLE = {hoja, raiz, tallo}
lechuga   → [1,0,0]  (exactly one)
zanahoria → [0,1,0]  (exactly one)
```

## B.8 Multi-Hot Encoding (Non-Exclusive Dimensions)

Zero, one, or many active bits:
```yaml
D_USO_CULINARIO:
  - ensalada
  - sopa
  - sofrito
  - jugo
```
zanahoria = `[ensalada=1, sopa=1, sofrito=1, jugo=1]` (multi-hot)

## B.9 Representing Unknown / Not-Applicable

**Problem**: a single `0` can mean: false, unknown, or not-applicable.

### Option A: Validity Mask

Two vectors: `value_bits` + `validity_bits`
```
zanahoria.color.naranja = 1, valid = 1
zanahoria.es_mascota = 0, valid = 1
concepto_desconocido.color.naranja = 0, valid = 0
```
Representation: `values = [1,0,0,1], valid = [1,1,0,1]`

### Option B: Two Bits Per Predicate

```
00 = unknown
01 = false
10 = true
11 = not-applicable / reserved
```
Example: `hoja_comestible = 10, raiz_comestible = 01, tiene_motor = 11`

### Option C: Local Closed-World Assumption

In a controlled local universe: anything not marked `1` is interpreted as `0`.
Use: closed-world + validity mask when data is incomplete.

## B.10 Bits as Search Tree

Bits function as sequential questions:
```
¿parte.hoja?
├── sí:
│   ¿estructura.cabeza_compacta?
│   ├── sí → lechuga
│   └── no:
│       ¿estructura.hoja_suelta?
│       └── sí → espinaca
├── no:
│   ¿parte.raiz? → sí → zanahoria
└── ¿parte.tallo? → sí → apio
```
Bit vector: `lechuga = [1,0,0,1,0]`

## B.11 Bits as Index/Hash

```yaml
signature_index:
  "1-0-0-1-0": [C_LECHUGA]
  "1-0-0-0-1": [C_ESPINACA]
  "0-1-0-0-0": [C_ZANAHORIA]
  "0-0-1-0-0": [C_APIO]
```
Exact search: `1-0-0-1-0 → lechuga`
Partial search: `1-0-0-*-* → lechuga, espinaca`

## B.12 Horizontal Relations Using Bits

**Shared features (AND)**:
```
shared = lechuga AND espinaca = [1,0,0,0,0]
```
Both share `parte.hoja = 1`

**Differences (XOR)**:
```
diff = lechuga XOR espinaca = [0,0,0,1,1]
```
Differ in `cabeza_compacta` vs `hoja_suelta`

Result translates via bit dictionary: "similar because both are hoja; contrast because cabeza_compacta vs hoja_suelta"

## B.13 Recommended Final Representation

```yaml
context:
  id: K_COCINA_VERDURAS
  domain: cocina
  task: diferenciar
  local_universe: [C_LECHUGA, C_ZANAHORIA, C_APIO, C_ESPINACA]

bit_dictionary:
  0:
    dimension: D_PARTE_COMESTIBLE
    value: hoja
  1:
    dimension: D_PARTE_COMESTIBLE
    value: raiz
  2:
    dimension: D_PARTE_COMESTIBLE
    value: tallo
  3:
    dimension: D_ESTRUCTURA_HOJA
    value: cabeza_compacta
  4:
    dimension: D_ESTRUCTURA_HOJA
    value: hoja_suelta

signatures:
  C_LECHUGA:   [1,0,0,1,0]
  C_ESPINACA:  [1,0,0,0,1]
  C_ZANAHORIA: [0,1,0,0,0]
  C_APIO:      [0,0,1,0,0]
```

Three components:
1. **bit_vector**: compact representation
2. **bit_dictionary**: semantics of each position
3. **context**: why these bits matter

## B.14 Key Principle

> Bits represent responses to discriminative questions. They do not represent "the complete thing", but the useful projection of the thing in a context.
