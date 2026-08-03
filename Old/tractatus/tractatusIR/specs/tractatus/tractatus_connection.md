# Tractatus Connection

## Summary
The system aligns surprisingly well with early Wittgenstein's Tractatus: context as logical syntax, dimensions as logical space, bits as signs within a notation. Not a psychological theory of meaning, but a logical notation for representation.

## Concepts
- Sign vs symbol (Wittgenstein: sign is sensible, symbol is logical usage)
- Logical space (dimensions as coordinate axes)
- Projection/form of representation (matrix as Bild/projection)
- Bit dictionary as logical syntax
- Discriminative dimension as formal variable with fixed values
- Collisions as lack of logical articulation
- Context as local grammar of use

## Content

### 1. Context as "Logical-Syntactic Use" of Sign

Wittgenstein: "Only the proposition has sense" and "the name has meaning only in the context of the proposition." He distinguishes the sensible sign from the logical symbol resulting from its use.

```
sign: "lechuga" (raw word)
symbol: lechuga under K_COCINA_VERDURAS with D_PARTE_COMESTIBLE = hoja
```
Your context is not psychological "background" — it's a **local grammar of use**.

From `tractatus_tree_de.json`: the sign acquires logical form through its syntactic use.

### 2. Discriminative Dimensions as "Logical Space"

Your dimension tree functions as a **local logical space**:
```
D_PARTE_COMESTIBLE: {hoja, raiz, tallo}
```
defines the possibilities within which a thing can be located. This resembles: a proposition determines a place in logical space; an object cannot be thought apart from the space of possibilities where it can appear.

```
"context cocina" = logical space
lechuga → hoja
zanahoria → raiz
apio → tallo
```
Your dimensions are **logical coordinate axes**. Bits are the coordinates.

### 3. Matrix as "Form of Projection" (Bild)

```
hoja  raiz  tallo
lechuga        1     0     0
zanahoria      0     1     0
apio           0     0     1
espinaca       1     0     0
```
Wittgenstein: we use sensible signs as a projection of a possible situation. The proposition stands in a projective relation to the world. The "picture" (Bild) represents a possible situation because it shares a **form of representation** with it.

Your matrix doesn't "contain" the thing — it contains the **form under which the thing can be represented** in that context. This is the Tractarian Bild: representation works because of structural correspondence between representation and domain.

### 4. Bits as Signs Within a Syntax (Not Pure Meaning)

```
[1,0,0] means nothing by itself.
```
Only with:
```yaml
context: K_COCINA_VERDURAS
dimension: D_PARTE_COMESTIBLE
bit_order: [hoja, raiz, tallo]
```
Does `[1,0,0] = hoja`. Under another dimension: `[1,0,0] = verde` or `[1,0,0] = vivo`.

This matches Wittgenstein's point: the same sign can belong to different symbols depending on use. Ambiguity (like "is/are" in German) causes philosophical confusion when sign/symbol/syntax aren't distinguished.

**Your bit dictionary fulfills the role of logical syntax**: it fixes how signs are used.

### 5. Context as Tractarian Variable

```
D_PARTE_COMESTIBLE(x) ∈ {hoja, raiz, tallo}
```
This is exactly the Tractarian idea: a variable is defined by fixing its possible values. In `tractatus_tree_de.json`: what a propositional variable can take as values must be fixed; that fixation constitutes the variable.

Your discriminative dimension IS a variable:
```
D_PARTE_COMESTIBLE(lechuga) = hoja
D_PARTE_COMESTIBLE(zanahoria) = raiz
```
Not a taxonomy — a **structure of variables with value domains**.

### 6. Collisions as Logical Ambiguity (Not Error)

```
bucket(hoja) = {lechuga, espinaca}
```
Wittgensteinian reading: the current form doesn't have enough logical articulation to say what you want to say. The world isn't wrong; your notation doesn't distinguish enough.

Solution: add dimension `D_ESTRUCTURA_HOJA` → more logical multiplicity.

Wittgenstein: a proposition must be articulated and have sufficient multiplicity to represent the situation. If it doesn't: add articulation.

### 7. Where It Fits Very Well

| Wittgenstein Point | System Equivalent |
|-------------------|-------------------|
| Meaning not in isolated sign | Concept + context = symbol |
| Representation = projection | Concept → matrix/bits under context |
| Logic not added content | Dimensions ARE the enabling form |
| Context not external noise | Context = space of possibilities |
| Good notation avoids confusion | Typed dimensions separate ontology/function/state |
| Collisions show lack of articulation | Not falsehood; needs more dimensions |

### 8. Where It Does NOT Fit Perfectly

**Tension**: Wittgenstein is NOT building a "concept ontology" or computational system. He's trying to show the logical form of the proposition and the **limits of what can be meaningfully said**.

Your system is more **pragmatic/computational**: indexing, searching, disambiguating, hashing, expanding dimensions, comparing concepts.

Closer to **logical engineering** than strict Tractarian metaphysics.

**Furthermore**: for Wittgenstein, the ultimate logical form cannot be said within the system — it **shows**. When you write:
```yaml
dimension: parte_comestible_principal
values: [hoja, raiz, tallo]
```
You're trying to make explicit part of the grammar. That's computationally useful, but Wittgenstein would say: logical form shows itself in the correct use of signs.

From `tractatus_tree_de.json`: the proposition can represent reality, but cannot represent that which it must share with reality to represent it; logical form shows itself.

### 9. Conceptual Mapping

| System Element | Tractatus Equivalent |
|---------------|---------------------|
| Base concept | Object/name (not strictly Tractarian) |
| Context | Logical space + syntactic rules |
| Discriminative dimension | Formal variable with value domain |
| Dimension value | Possibility within logical space |
| Bit | Elementary sign within notation |
| Bit dictionary | Local logical grammar |
| Matrix | Projection form / logical picture (Bild) |
| Collision | Lack of logical articulation / multiplicity |
| Dimension expansion | Refinement of representation form |
| Index | Operative use of logical form for search |

### 10. Key Formulation

> Your system builds a **Begriffsschrift** (conceptual notation) where each binary sign only has meaning by its position in a contextual grammar of discrimination.

Wittgensteinian formulation:
> The bit does not signify by itself. The bit signifies in the matrix. The matrix signifies by its form of projection. The form of projection belongs to the context.

## References
- turn-26.md (full comparison: context as logical syntax, dimensions as logical space, matrix as Bild, bits as signs, collisions as lack of articulation)

## Version Notes
- Turn 26: comprehensive mapping of the system to early Wittgenstein/Tractatus concepts, with points of alignment and tension
- Turn 28: defined logical system: sinnvoll (sense), sinnlos (nonsense but valid), unsinnig (ill-formed/absurd)

## Logical System: sinnvoll / sinnlos / unsinnig

### Three Categories (Wittgensteinian)

| Category | System Equivalent | Description |
|----------|-------------------|-------------|
| **sinnvoll** | `sinnvoll(E, K)` | Well-formed + projects a possibility within logical space + reduces candidates properly |
| **sinnlos** | `sinnlos(E, K)` | Well-formed but tautological/contradictory/vacuous — valid in symbolism but doesn't discriminate |
| **unsinnig** | `unsinnig(E, K)` | Ill-formed — violates grammar, uses values outside domain, applies dimension where not applicable |

### Formal Definition

Let:
- `U_K` = local universe of context K
- `E` = expression selecting candidates ⟦E⟧_K ⊆ U_K

```
sinnvoll(E, K) iff:
  E is grammatical (well_formed)
  AND 0 < |⟦E⟧_K| < |U_K|
```

```
sinnlos(E, K) iff:
  E is grammatical (well_formed)
  AND (|⟦E⟧_K| = 0  [contradiction]
       OR |⟦E⟧_K| = |U_K|  [tautology])
```

```
unsinnig(E, K) iff:
  NOT well_formed(E, K)
  OR mixes incompatible dimensions
  OR uses values outside domain
  OR applies dimension where not applicable
```

### Examples

**sinnvoll** (true discrimination):
```
E = D_PARTE_COMESTIBLE = hoja
⟦E⟧ = {lechuga, espinaca}
0 < 2 < 4 (U_K size)
→ sinnvoll
```

**sinnlos** (tautological/vacuous):
```
E = D_PARTE_COMESTIBLE ∈ {hoja, raiz, tallo}
⟦E⟧ = {lechuga, zanahoria, apio, espinaca} = U_K
→ sinnlos (tautology, doesn't inform)
```

**sinnlos** (contradictory):
```
E = [1,1,0] on one-hot dimension
→ violates one-hot constraint
→ sinnlos-contradiction (well-formed but impossible)
```

**unsinnig** (ill-formed):
```
E = D_PARTE_COMESTIBLE = mamífero
→ mamífero ∉ {hoja, raiz, tallo}
→ unsinnig (value outside domain)
```

```
E = D_ESTADO_VITAL(martillo) where applies_when: organismo=1
→ martillo.organismo = 0
→ unsinnig (dimension not applicable)
```

### Four States in System

| State | Description |
|-------|-------------|
| **verdadero / matching** | Selects actual candidates |
| **falso local** | Well-formed, but doesn't match evaluated concept |
| **sinnlos** | Well-formed, but doesn't inform / doesn't discriminate |
| **unsinnig** | Ill-formed or outside grammar |

### Bit-Level Rules

For signature `sig(c) = [b0, b1, b2,...]` with dictionary:
```
well_formed(sig, D):
  if D is one-hot: sum(bits_D) = 1
  if D is multi-hot: sum(bits_D) >= 0
  if D not applicable: valid_mask(bits_D) = 0
```

```
sinnvoll(sig, K):
  well_formed(sig, K)
  AND signature reduces candidates
```

```
sinnlos(sig, K):
  well_formed(sig, K)
  AND (reduces to empty [contradiction]
       OR reduces to all [tautology])
```

```
unsinnig(sig, K):
  NOT well_formed(sig, K)
```

### Key Wittgensteinian Formulation

> **sinnvoll** = projects a possibility
> **sinnlos** = valid form without discriminative power
> **unsinnig** = violates grammatical form, appears to say something but fails to constitute a symbol

From `tractatus_tree_de.json`: tautologies and contradictions are **sinnlos** but NOT **unsinnig** — they belong to the symbolism. Pseudo-statements mixing categories fall into **unsinnig**.

### Central Rule for the System

> An expression has sense in this system if and only if it can be projected as a valid selection within the space of possibilities defined by the context.

Compact:
- **sinnvoll** = valid bit + valid dimension + valid value + valid context + reduces ambiguity
- **sinnlos** = valid bit/dimension/context, but doesn't reduce or reduces to empty
- **unsinnig** = incompatible bit/dimension/context

## References
- turn-26.md (full comparison: context as logical syntax, dimensions as logical space, matrix as Bild, bits as signs, collisions as lack of articulation)
- turn-28.md (complete logical system: sinnvoll/sinnlos/unsinnig with formal definitions and bit-level rules)
- turn-30.md (computational proposition: project(E,K) → signature → denote → semantic status)
