# Tractatus As Logical Layer

## Preamble: An Inductive And Self-Contained Entry Point

We can begin from a very small and familiar case.

Suppose we are in a kitchen-vegetable context and we want to distinguish:

- `lechuga`
- `zanahoria`
- `apio`
- `espinaca`

If we only keep the words, we have names.
But the names alone do not yet tell us how those items are being represented.

The first genuinely useful step is to place them under a discriminative question such as:

```text
parte_comestible = {hoja, raiz, tallo}
```

Then the notation becomes:

```text
lechuga   -> hoja
zanahoria -> raiz
apio      -> tallo
espinaca  -> hoja
```

And this can be compiled as a matrix:

```text
           hoja  raiz  tallo
lechuga      1     0      0
zanahoria    0     1      0
apio         0     0      1
espinaca     1     0      0
```

This simple step already shows the core idea of our system.
We are not mainly representing isolated words.
We are placing stable anchors inside a structured space of possible distinctions.

That is why the important unit is not just `"lechuga"` as a sign.
The important unit is an articulated placement such as:

```text
D_PARTE_COMESTIBLE(C_LECHUGA) = hoja
```

At this point the connection with the *Tractatus* becomes easier to see.
Early Wittgenstein also insists that logic does not begin from isolated words.
It begins from articulation.
What matters is not the bare sign, but the sign in a structured use that projects a possible situation.

So the comparison is not mysterious.
It grows naturally from the notation itself:

1. we start with a stable anchor
2. we place it under a context
3. the context activates dimensions and admissible values
4. the resulting articulation places the anchor in a local logical space
5. the sign becomes meaningful only inside that articulated use

In that sense, our matrix is not just a storage device.
It is a local picture of possibilities.
It shows how a given anchor can be located under a specific dimension.

The same is true for the bit pattern.

```text
[1,0,0]
```

By itself, it means nothing.
It becomes operative only when a context, a dimension, and an ordering of values are already fixed.
Under `D_PARTE_COMESTIBLE = [hoja, raiz, tallo]`, it means `hoja`.
Under another dimension, the very same pattern would mean something else.

This is exactly the kind of distinction the *Tractatus* makes between sign and symbol.
The sign is the perceptible mark.
The symbol is the sign in its logical-syntactic use.

Our context therefore should not be read as vague background.
It is better understood as a local grammar of projection.
It determines:

- what counts as a candidate
- what dimensions are in force
- what values are admissible
- what articulations have sense there

This also explains why collisions matter.
If `lechuga` and `espinaca` both land in `hoja`, the world is not at fault.
What happens is that the current articulation is not yet rich enough for the distinction we want.
So we add another dimension, such as `estructura_hoja` or `grosor_hoja`.

This is the key inductive bridge to the tractarian reading.
Representation works when the notation has enough articulated multiplicity to project a possible arrangement.
When it does not, the remedy is not to reinterpret the word psychologically.
The remedy is to refine the logical articulation.

From this point of view, the *Tractatus* gives us a facts-first logical-semantic architecture, and our system gives a local computational notation that makes that architecture operational.

The rest of this document therefore does two things only:

- it states, in minimal form, the tractarian architecture we rely on
- it maps that architecture to anchors, contexts, dimensions, signatures, matrices, masks, and local worlds

## 1. Ultra-Short Description Of The Tractatus As A Logical-Semantic System

In the reading fixed by `03_1_computational_interpretation_of_tractatus.md`, the *Tractatus* describes a logical-semantic system with the following architecture:

- the world is the totality of facts, not of things (`1`, `1.1`, `1.13`)
- a fact is the obtaining of a state of affairs (`2`)
- a state of affairs is a possible combination of objects (`2.01`)
- objects contain the possibility of their occurrence in states of affairs (`2.012`, `2.013`, `2.0141`)
- a picture presents a possible situation in logical space (`2.11`, `2.201`, `2.202`)
- what a picture presents is its sense (`2.221`)
- truth and falsity arise only by comparing that sense with reality (`2.222`, `2.223`, `2.224`)
- the proposition is the proposition-sign in its projective relation to the world (`3.12`)
- only an articulated fact-like sign configuration can express sense; a mere class of names cannot (`3.142`)
- the proposition determines a place in logical space (`3.4`)
- logical form governs representation but cannot itself be said as one more fact; it can only be shown (`4.12`, `4.121`, `4.1212`)
- tautology and contradiction are `sinnlos`, not `unsinnig`; they belong to symbolism but do not depict a possible situation (`4.461`, `4.4611`, `4.462`)

In shorter and cleaner terms:

- the world is factual, not lexical
- the proposition is projective, not merely verbal
- sense is a possible articulated placement in logical space
- truth is the obtaining of that placement
- logical form is the condition of representability, not one more represented fact

In one chain:

```text
objects
  -> possible states of affairs
  -> obtaining facts
  -> world
  -> proposition-sign used as projection
  -> sense
  -> truth or falsity by comparison with reality
```

The key distinction for what follows is this:

```text
sense is prior to truth
projection is prior to evaluation
logical form is prior to both, but cannot itself be said as another fact
```

## 2. Mapping To The Representation We Proposed

Our proposed representation can be read as a local computational notation built on that tractarian structure.

The mapping is not identity term by term.
It is a disciplined reinterpretation.

### 2.1 Stable Anchor

Our stable concept anchor is not identical to Wittgenstein's `Gegenstand` in a strict historical sense.
But it plays an analogous structural role: it is the persistent support across multiple possible articulations.

Examples:

- `C_ZANAHORIA`
- `C_LECHUGA`
- `C_AUTO`

These anchors are not yet the main logical units of interest.
They are the stable supports on which possible articulations are projected.

So the anchor is necessary, but it is not yet the main unit of sense.
Sense begins when the anchor enters a typed articulation.

### 2.2 Facts First, Signs Later

The tractarian order is facts-first.
This aligns with the central claim of our notation.

What matters is not primarily the isolated sign:

- `"zanahoria"`
- `"car"`
- `"carrot"`

What matters is the articulated logical-semantic position:

- `zanahoria : vegetal`
- `zanahoria : parte_comestible = raiz`
- `auto : color = rojo`

So the notation is not mainly a naming system.
It is a system for indexing stable anchors inside a space of possible properties, values, relations, and states.

This gives us the first explicit computational reading of `fact` in our notation.

### 2.2.1 Fact In Our Notation

A `fact` is not the isolated object and not the isolated value.
It is a typed atomic articulation of the form:

```text
dimension(subject) = value
```

or, more generally:

```text
relation(arg1, arg2, ...)
```

Examples:

- `D_PARTE_COMESTIBLE(C_LECHUGA) = hoja`
- `D_COLOR(C_AUTO) = rojo`
- `imports(MODULE_API, LIB_FASTAPI)`

This is the closest analogue, in our system, to the tractarian state-of-affairs or obtaining fact.

For the dimension-assignment case, the matrix view is:

```text
fact matrix = subject x property-value
```

That is, the matrix does not primarily store words.
It stores atomic projected facts.

This is where the tractarian layer fits strongly:

- the sign is only the perceptible entry point (`3.11`, `3.326`)
- the logical target is the articulated possible situation (`2.201`, `2.221`, `4.022`)

### 2.3 Context As Local Logical Space

In our representation, context is not mere thematic background.
It is the local regime that determines:

- which candidates belong to the current universe
- which dimensions are active
- which values are admissible
- which branches apply
- which distinctions are meaningful now

This maps well to the tractarian notion that the proposition determines a place in logical space (`3.4`) and that pictures represent possible situations in logical space (`2.11`, `2.202`).

So our context corresponds to a local logical space of admissible articulation.

### 2.3.1 Locality Of Welt

Once context is understood this way, a local `welt` can be defined as:

- a local universe of anchors
- plus the set of asserted or obtaining articulations valid under that context

In short:

```text
local welt = local universe + context-authorized obtaining facts
```

So the tensorial or matricial space does not float freely.
It defines localities of `welts` by fixing:

- which anchors are in play
- which dimensions count
- which values are admissible
- which branches apply
- which articulations can obtain there as meaningful facts

### 2.4 Dimensions As Structured Axes Of Possibility

Our discriminative dimensions play the role of structured local axes within that logical space.

Examples:

- `D_PARTE_COMESTIBLE`
- `D_ESTRUCTURA_HOJA`
- `D_COLOR`

Each dimension defines:

- a typed question
- a bounded set of admissible values
- a local field of possible placements for the anchor under the current context

This matches the tractarian idea that what matters is not a word by itself, but the possible configuration it enters.

And it lets different conceptual domains be composed without flattening them into a single lexical field.

### 2.5 Projection In Our System

In the *Tractatus*, the proposition is the proposition-sign in projective relation to the world (`3.12`).

In our notation, projection is the passage from:

- stable anchor
- under context
- through active dimensions
- into a typed indexed articulation

Formally:

```text
anchor + context + dimensions -> indexed articulation
```

Examples:

- `C_ZANAHORIA` under `K_COCINA` -> `D_PARTE_COMESTIBLE = raiz`
- `C_AUTO` under `K_PERCEPCION` -> `D_COLOR = rojo`

This is why our projection is not a lexical embedding.

An LLM-style embedding path can be caricatured as:

```text
natural language -> signs -> latent vector structure
```

The tractarian order behind our notation is different:

```text
possible fact
  -> projection
  -> articulated representation
  -> evaluation
```

So the notation begins from possible fact-like structure, not from surface language as such.

This is also why our projection differs from the dominant LLM pattern.

In a simplified contrast:

```text
LLM-style path:
natural language -> signs -> latent vector regularities

tractarian path used here:
possible facts -> projection -> articulated representation -> evaluation
```

Our notation therefore treats embeddings, signatures, and matrices as compiled coordinates of possible fact-like articulation, not as primary semantic objects.

### 2.6 Bit Signatures As Proposition-Signs In A Restricted Notation

Once projected, our articulations can be compiled into typed signatures.

Example:

```text
D_PARTE_COMESTIBLE = {hoja, raiz, tallo}
lechuga   -> [1,0,0]
zanahoria -> [0,1,0]
apio      -> [0,0,1]
```

These signatures are meaningful only because they belong to:

- a bit dictionary
- a context
- a typed dimension system

So a bit vector by itself is only a sign-pattern.
It becomes symbolically operative only through its projective role inside a local notation.

That is the direct analogue of:

- sign vs symbol (`3.326`, `3.327`, `3.328`)
- proposition-sign vs proposition (`3.12`)

### 2.7 Matrices As Local Pictures Of Possibility

Our matrices can then be read as local pictures in the tractarian sense.

For a dimension `D`, the matrix:

```text
M_D : concept x value
```

does not merely store labels.
It presents how candidates are placed across a bounded field of possible values.

Example:

```text
hoja  raiz  tallo
lechuga        1     0     0
zanahoria      0     1     0
apio           0     0     1
espinaca       1     0     0
```

This is a local picture because it presents a possible arrangement inside a structured possibility space.

Its transposed index gives buckets, and its collisions indicate under-articulation.

More strictly:

- the row is a compiled local fact-profile of a stable anchor
- the columns are typed property-values
- the occupied cells are projected atomic articulations

So the matrix is not just `concept x value`.
It is a compact factual surface over a restricted logical space.

### 2.8 Collision As Lack Of Sufficient Articulation

If two anchors occupy the same bucket under the same dimension, the notation has not yet articulated enough to distinguish them.

Example:

- `lechuga -> hoja`
- `espinaca -> hoja`

This is not merely retrieval ambiguity.
Under the tractarian reading, it means the current symbolic multiplicity is insufficient.

So collision triggers another dimension:

- `D_ESTRUCTURA_HOJA`
- then maybe `D_GROSOR_HOJA`

This is how our notation grows by further articulation of possible fact-like placement.

In tensorial terms, each new dimension adds a sparse axis of possible articulation, but only where the current local world requires that further distinction.

### 2.9 Sense, Truth, And Logical Status In Our System

The tractarian distinction between sense and truth maps directly onto our system.

In our notation:

- an articulation has `sense` if it determines a valid possible position in the local logical space
- it is `true` or `matched` when that articulated position obtains for the anchor in the relevant world, context, or fact base

So:

```text
sense = valid projected possibility
truth = obtaining of that possibility
```

### 2.9.1 Sinn As Masked Admissible Space

In our notation, `Sinn` should not be reduced to a bare denotation result.
It is better understood as the admissible space of projected articulation once the relevant masks are applied.

At minimum, those masks separate:

- what applies to the anchor at all
- what has sense in the current context or task
- what is currently discriminative
- what is actually observed

So the practical reading is:

```text
Sinn in our notation = the region of logical-semantic space left open by the active masks
```

And the projected articulation is `sinnvoll` when it occupies a valid non-trivial region of that masked space.

This is why masks are not auxiliary metadata.
They are the computational boundary of sense.

This is why our later logical statuses can be grounded tractarianly:

- `sinnvoll`: valid articulated possibility
- `sinnlos`: formally valid but non-depictive or non-informative limiting case
- `unsinnig`: failure of admissible projection or grammar

The exact computational treatment comes later.
The tractarian layer only gives the structural basis.

### 2.10 What The Mapping Preserves

This mapping preserves the following tractarian commitments:

1. logic does not arise from isolated words
2. signs become operative only in structured use
3. projection is the central relation between notation and possible fact
4. representability is prior to truth-value
5. logical space constrains what can be meaningfully articulated
6. further articulation is needed when the current notation does not distinguish enough
7. a fact is an obtaining typed articulation, not a bare symbol
8. local worlds are factual localities defined by contextual admissibility

### 2.11 Compact Formula

The shortest statement of the mapping is:

```text
The Tractatus gives a facts-first logical-semantic architecture.
Our notation reinterprets that architecture locally:
stable anchors are projected through context and dimensions into indexed articulations,
compiled into typed signatures and factual matrices,
restricted by masks that define the active space of sense,
and evaluated according to the local worlds those articulations determine.
```
