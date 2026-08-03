# Context, Representation, And Expansion

## Starting Point

Once the discrimination game is accepted as the base heuristic, the next question is:

```text
How do we represent the context that makes one articulation relevant rather than another?
```

The early discussion converges on a strong answer:

context is not just free text or thematic background.
It is a structured local regime of interpretation and discrimination.

## Context As Selection Structure

Several equivalent views appear early on.

Context can be described as:

- frame
- axis selector
- preferred relation selector
- binary mask
- local discriminative program

These are not separate theories so much as progressively stronger descriptions of the same thing.

In the weakest form, context says which reading wins.

Example:

- in `cocina`, `zanahoria` is read functionally as food or ingredient
- in `biologia`, `zanahoria` is read ontologically as plant or organism
- in `estado vital`, `zanahoria` is read through a state axis

In the stronger form, context says not only which reading wins, but which relation, axis, or question is active.

## Context As Projection Rule

This leads to the formula:

```text
interpretacion = proyectar(concepto, contexto)
```

Projection does not create a new object.
It selects the dimension of articulation that matters now.

So the same concept can support multiple projections without losing stability.

## Local Versus Global Representation

The discussion then sharpens into a two-level model.

### Global representation

What the thing is in general, across many possible contexts.

Example:

```text
lechuga:
  planta
  organismo
  vegetal
  alimento posible
```

### Local representation

What matters to distinguish it from the current competitors.

Example:

```text
lechuga vs zanahoria in cocina
```

Shared:

- vegetal
- planta
- alimento

Discriminative:

- `lechuga -> hoja`
- `zanahoria -> raiz`

The system therefore refuses the idea that the most complete representation is always the most useful one.

## Representation As Search Structure

The breakthrough of the early formulation is that the same local projection can do several jobs at once.

The projection can function simultaneously as:

- representation
- contextual hash
- search path
- index key
- basis for local horizontal relations

This is why the discussion repeatedly insists that the system is not hashing the word itself, but its contextual projection.

## Bit Signatures And Typed Meaning

The first usable encoding is binary, but only under a strict condition:

bits must be typed.

A flat code like:

```text
perro = 010101
```

is semantically useless by itself.

The meaningful structure is instead:

```text
bit_0 = D_PARTE_COMESTIBLE.hoja
bit_1 = D_PARTE_COMESTIBLE.raiz
bit_2 = D_PARTE_COMESTIBLE.tallo
```

So the minimal complete binary representation is not just a vector, but:

- bit vector
- bit dictionary
- context

This is already enough for exact match, partial match, search path construction, and contrast.

## From Dimensions To Matrices

The next major step is recognizing that a discriminative dimension is not merely a set of isolated bits.
It is a semantic question with a finite set of admissible values.

Example:

```text
D_PARTE_COMESTIBLE: {hoja, raiz, tallo}
```

This allows three increasingly rich structures.

### M0: concept x feature

The earlier, flatter matrix of base properties.

```text
           vegetal alimento hoja raiz tallo
lechuga         1       1    1    0    0
espinaca        1       1    1    0    0
zanahoria       1       1    0    1    0
apio            1       1    0    0    1
```

This is useful because it makes visible a base descriptive surface.
But it still mixes two different things:

- shared background properties
- truly discriminative answers

### M1: concept x value-of-dimension

The one-hot or multi-hot codification of responses to a discriminative question.

If the active question is:

```text
D_PARTE_COMESTIBLE: {hoja, raiz, tallo}
```

then the same local universe becomes:

```text
           hoja raiz tallo
lechuga       1    0     0
espinaca      1    0     0
zanahoria     0    1     0
apio          0    0     1
```

This matrix is already much closer to the real computational object.
It is not listing generic traits.
It is encoding the response to one active discriminative question.

### M1^T: value-of-dimension x concept

The inverted view that yields buckets directly.

```text
         lechuga espinaca zanahoria apio
hoja           1        1         0    0
raiz           0        0         1    0
tallo          0        0         0    1
```

This is where lookup and collision become immediately visible:

- `bucket(hoja) = {lechuga, espinaca}`
- `bucket(raiz) = {zanahoria}`
- `bucket(tallo) = {apio}`

At this point the system becomes more than a feature table.
It becomes a machine for inducing partitions over a local universe.

## From Disambiguation To Domain Hierarchy

The matrix sequence matters because it mirrors the conceptual movement of the system.

### Step 1: disambiguation pressure

We begin with a local ambiguity.

Example:

```text
lechuga, espinaca, zanahoria, apio
```

We need a question that separates them.

### Step 2: domain hierarchy selection

To choose a useful question, we usually move through a domain hierarchy.

For example:

```text
entidad fisica
  -> organismo
    -> planta
      -> alimento vegetal
```

This hierarchy does not yet solve the local discrimination problem by itself.
But it tells us which family of dimensions is appropriate.

Once we know that the local universe lives under a food-plant regime, a dimension like `parte_comestible_principal` becomes natural.

So the hierarchy does not end the process.
It orients the choice of discriminative dimension.

### Step 3: discriminative matrix

The chosen dimension then produces `M1`, which induces the first real partition of the local universe.

At that moment, the system passes from:

- domain understanding

to:

- operational discrimination

This is the point where semantic organization becomes a search structure.

## Why M0 Is Not Enough

The examples matter because they show why a simple property table is not yet the right final representation.

In `M0`, both `lechuga` and `espinaca` remain effectively collapsed:

```text
lechuga   = [1,1,1,0,0]
espinaca  = [1,1,1,0,0]
```

`M0` tells us they are similar, but not how to continue the discrimination process.

`M1` improves the situation by making the active question explicit.
But it also reveals the unresolved bucket:

```text
hoja -> {lechuga, espinaca}
```

That unresolved bucket is the computational signal that the current representational depth is insufficient.

So the examples are not illustrative decoration.
They show where the representational pressure comes from.

## Dimensions As Recursive Object:Property Indices

The previous description is still not strong enough unless we make one point explicit.

A discriminative dimension is not just a convenient question.
It is an index of the form:

```text
object : property
```

For example:

```text
lechuga : parte_comestible = hoja
zanahoria : parte_comestible = raiz
apio : parte_comestible = tallo
```

But once this is made explicit, a second step appears.
The value reached by one index can itself open a new indexed representational space.

For example:

```text
lechuga : parte_comestible = hoja
espinaca : parte_comestible = hoja
```

The shared value `hoja` does not end the representation.
It becomes the object-domain for a new layer of properties:

```text
hoja : estructura = cabeza_compacta
hoja : estructura = hoja_suelta
```

Operationally, this means that we move from:

```text
concept -> value under dimension D1
```

to:

```text
value reached under D1 -> further values under dimension D2
```

And that second layer is not external to the first.
It is indexed by it.

So the representation grows as a succession of indexed object:property spaces.

## Representation Of Representations

This is the key consequence.

The system is not only representing objects by properties.
It is also allowing one representation to become the object of a further representation.

That is why the discussion naturally moves toward trees, submatrices, and branch-local dimensions.

The structure is closer to this:

```text
concept
  -> represented by a first discriminative property
  -> whose attained value opens a second representational space
  -> whose attained value may open a third representational space
```

Example:

```text
lechuga
  : parte_comestible = hoja
  : estructura_hoja = cabeza_compacta

espinaca
  : parte_comestible = hoja
  : estructura_hoja = hoja_suelta
  : grosor_hoja = delgada
```

This means the system supports indexed representations of indexed representations.

In other words, the dimensions are compositional.

## The Disambiguation Tensor

We can now state more clearly what the tensorial idea amounts to.

The system does not begin with a single giant tensor fully populated in advance.
It grows a tensorial structure as disambiguation requires further articulation.

Starting from the first matrix:

```text
M1(parte_comestible)
```

we detect the unresolved branch:

```text
hoja -> {lechuga, espinaca}
```

Then we activate a second matrix only on that branch:

```text
M2(estructura_hoja | parte_comestible = hoja)
```

Example:

```text
                  cabeza_compacta hoja_suelta
lechuga                        1           0
espinaca                       0           1
acelga                         0           1
```

If `espinaca` and `acelga` still collide, we introduce:

```text
M3(grosor_hoja | parte_comestible = hoja, estructura_hoja = hoja_suelta)
```

Example:

```text
           delgada gruesa
espinaca         1      0
acelga           0      1
```

This produces the sequence:

```text
M1 -> M2 -> M3 -> ...
```

where each new matrix is activated only on a restricted branch determined by previous articulations.

This is the clearest sense in which the system builds a disambiguation tensor.

Not because everything is encoded in one dense tensor from the start,
but because each discriminative layer adds a new indexed axis over a restricted local subspace.

So the tensorial object is:

- hierarchical
- conditional
- branch-local
- sparse

and generated by unresolved ambiguity.

## The Real Target Is Not The Isolated Atom

At this point another clarification becomes necessary.

What matters in this notation is not primarily the representation of the isolated atom as such.

Not:

- `zanahoria` as a bare lexical unit
- `cebolla` as a bare lexical unit
- the surface sign in one language or another

What matters is the indexed position of that stable anchor inside a logical-semantic space.

That indexed position is given by articulations such as:

```text
zanahoria : vegetal
zanahoria : alimento
zanahoria : parte_comestible = raiz
auto : color = rojo
```

So the true representational target is not the atom alone, but its structured insertion into a field of properties, states, values, and contexts.

This is why the notation is better understood as an indexation system than as a naming system.

The stable concept anchor remains necessary, but mainly as the support on which indexed articulations can be attached, compared, composed, and refined.

## Facts Rather Than Semantic Sugar

This also explains why the system cannot begin from the surface richness of natural language alone.

Languages, dialects, and lexical variants provide signs.
They are important, but they are not where the logical force of the notation comes from.

The logical force comes from articulable facts such as:

- `el auto es rojo`
- `la zanahoria es vegetal`
- `la zanahoria tiene como parte comestible principal la raiz`

Or, in more abstract form:

- object-property
- object-state
- object-relation
- object-in-context

This means the notation is not trying first of all to preserve the semantic sugar of surface expressions.
It is trying to preserve the indexable logical articulation that surface expressions point toward.

In that sense, the surface sign is only the entry point.
The real work begins once the sign is compiled into a structured fact-like position in the logical-semantic space.

## Why This Matters More Than A Tree Metaphor

If we say only that the system builds a decision tree, we miss the deeper point.

The important fact is not merely the order of questions.
It is that each answered dimension produces a new representational surface on which further dimensions may be defined.

So the branch is not just a path in a classifier.
It is a local redefinition of the object-space under a previous articulation.

That is exactly what the matrix examples make visible:

- the tree is the readable shape
- the submatrices are the operative mechanism
- the tensorial reading is the abstract structure behind the growing family of submatrices

This is why the dimensions can be described as sparse tensorial expansions.

Each new dimension adds a new articulatory axis, but only where the previous structure makes it meaningful.
The full system is therefore not one dense universal tensor applied everywhere.
It is a compositional family of partially activated representational axes.

## Composing Conceptual Domains

Once dimensions are understood this way, a second consequence appears.

They allow the system to compose different conceptual domains without flattening them.

For instance, one domain may begin taxonomically:

```text
organismo -> planta -> vegetal
```

Another may begin functionally:

```text
alimento -> ingrediente -> uso_culinario
```

Another may begin morphologically:

```text
hoja -> estructura -> grosor -> textura
```

The system can connect these domains because each dimension defines a typed representational interface.

Examples:

- taxonomy can locate the candidate set
- functional dimensions can discriminate practical roles
- morphological dimensions can refine collisions inside a functional bucket

So different conceptual domains are not merely listed side by side.
They become composable because they can be activated sequentially and conditionally over the same stable concept anchors.

This is one of the strongest consequences of the model.

It means the system can move from one semantic regime to another without pretending they are the same regime.

## From Taxonomy And Semantics To Tensor And Boolean Space

This compositionality is what enables the bridge to a tensorial and boolean-operational reading.

On one side, we have a semantic-taxonomic space:

- concepts
- typed relations
- discriminative questions
- admissible values
- local universes

On the other side, we want a space where computation becomes tractable:

- vectors
- matrices
- sparse axes
- masks
- boolean operations

The dimensions are the bridge.

Because each dimension is typed and value-bounded, it can be compiled into:

- one-hot slices
- multi-hot slices
- matrix rows
- matrix columns
- bucket indices
- boolean expressions over active positions

So the model does not jump directly from semantics to raw linear algebra.

It passes through a structured layer of discriminative dimensions that preserves interpretation while enabling compilation.

This is why the mapping can be stated as:

```text
taxonomy and semantics
  -> typed discriminative dimensions
  -> sparse tensorial representation
  -> boolean and matrix operations
```

## Tensorial Reading

The word `tensorial` here should be understood carefully.

It does not mean that the whole system must begin as a pre-fixed high-order dense tensor.

It means:

- dimensions introduce structured axes
- compositions of dimensions introduce higher-order indexed structure
- branch-local activation makes the result sparse

So the representational object can be read as tensorial because it supports multiple indexed axes of articulation, but sparse because only a subset is active for any given local problem.

This lets the system preserve semantic traceability while still becoming computationally operable.

## Boolean Consequence

Once compiled into typed indexed positions, the representation enters a space where boolean operations become meaningful.

For example:

- `AND` can detect shared active articulation
- `XOR` can detect contrastive articulation
- `OR` can express widened admissible sets
- masks can restrict applicability, sense, and observation

The important point is that boolean operations are not applied to arbitrary opaque bits.
They are applied to positions obtained from typed semantic compilation.

That is why the bridge matters so much.

Without the discriminative dimension layer, the boolean space is semantically blind.
With it, boolean space becomes an operational shadow of semantic structure.

## Restated Consequence

The full consequence of the model is therefore stronger than "context selects dimensions".

It is this:

1. a context activates a local succession of discriminative dimensions
2. each dimension indexes objects by properties
3. attained values may open new representational subspaces
4. this yields a compositional family of sparse tensorial articulations
5. the resulting structure can be compiled into matrices, indices, and boolean operations

That is the deeper representational claim behind the early discussion.

## Partition, Bucket, Collision

Once a dimension is treated as a function:

```text
D: C -> V
```

it partitions the local universe into buckets.

Example:

- `hoja -> {lechuga, espinaca}`
- `raiz -> {zanahoria}`
- `tallo -> {apio}`

Now collision has a precise meaning.

It is not generic similarity.
It is multiplicity inside the same bucket under the same discriminative question.

## Expansion By New Matrices Or Sparse Tensorial Dimensions

The early discussion treats collision resolution as recursive matrix growth.

If `lechuga` and `espinaca` collide under `parte_comestible`, we introduce another dimension such as `estructura_hoja`.

This can be seen in two complementary ways.

### Recursive matrix view

- main discriminative matrix
- submatrix on the colliding bucket
- sub-submatrix if the collision persists

Concrete example:

```text
D1: parte_comestible_principal
  hoja  -> {lechuga, espinaca, acelga}
  raiz  -> {zanahoria}
  tallo -> {apio}

D2 on hoja: estructura_hoja
  cabeza_compacta -> {lechuga}
  hoja_suelta     -> {espinaca, acelga}

D3 on hoja_suelta: grosor_hoja
  delgada -> {espinaca}
  gruesa  -> {acelga}
```

### Sparse tensorial growth view

Each new dimension can be seen as a new sparse articulatory axis that only becomes active on part of the universe.

This is important.
The system does not require every concept to carry every deep dimension globally.

Instead, new dimensions can be branch-local and conditionally activated.

That is why this is better thought of as sparse discriminative expansion than as one giant dense universal tensor fixed in advance.

In short:

```text
disambiguation
  -> choose domain-relevant dimension
  -> compile local matrix
  -> detect unresolved bucket
  -> activate branch-local matrix
  -> grow sparse disambiguation tensor
```

## Context As Discriminative Program

The strongest early formulation arrives when context is no longer a flat set of active dimensions but a sequence or tree of dimension applications.

In that reading, context includes:

- local universe
- task
- dimension sequence or discriminative tree
- allowed values per dimension
- applicability conditions for each branch
- local interpretation rules

This means context becomes a local program of questions.

Example:

```text
parte_comestible
  hoja -> estructura_hoja
    hoja_suelta -> grosor_hoja
  raiz -> zanahoria
  tallo -> apio
```

The system can then be summarized as:

```text
concept
  -> context
  -> projection
  -> typed signature or matrix position
  -> bucket
  -> collision or discrimination
```

## Central Consequence

Context is not merely where interpretation happens.
It is the local architecture that determines:

- what can be asked
- in what order
- under what applicability conditions
- what counts as a valid answer
- when expansion is required

This is the representational and computational core of the system before any tractarian logical layer is added on top.
