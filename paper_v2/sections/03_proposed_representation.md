# Proposed representation

Consider the logical structure of a partition of the world $W_i$ by the following symbolic set:

1. A context, that is, a partition over the world $W$ that limits what belongs into $W_i$.
2. A logical space $L_i$ that describes the admissible mapping coordinates, for example objects and their properties.
3. A Boolean matrix $V_i$ that describes all the relationships that map the facts in relation to their truth.
4. A Boolean matrix $S_i$ that describes all the relationships that map the facts in relation to their meaning; that is, their applicability within the logical space.

![A context $W_i=(C_i,R_i)$ instantiates two boolean layers over the same $L_i$ grid: the sense mask $S_i$ (admissible crosses) and the truth layer $V_i$ (asserted facts). Queries see only the operative projection $W_i^{*}=V_i\odot S_i$: an injected fact outside the mask is structurally invisible. \label{fig:layers}](../figures/fig_layers.png){width=100%}

Then, we can define $W_i$ as the boolean AND operation between $V_i$ and $S_i$ (see Figure~\ref{fig:layers}). Consider this small example;

Table: Matrix $W_i$ mapping objects to their properties.

|         | vegetable | food | leaf | root | stem |
| ------- | --------- | ---: | ---: | ---: | ---: |
| lettuce | 1         |    1 |    1 |    0 |    0 |
| spinach | 1         |    1 |    1 |    0 |    0 |
| carrot  | 1         |    1 |    0 |    1 |    0 |
| celery  | 1         |    1 |    0 |    0 |    1 |

It is important to note that within this logical space, the properties "vegetable" and "food" are true for all objects containing our $W_i$, that is, they are tautological under the Tractatus definition and are therefore meaningless (*sinnlos*). We begin by removing them to facilitate further analysis. $W^{T}_i$, the transversal of this would essentially be an index of properties and which object they belong to.

Table: Matrix $W^{T}_i$, the transversal index of properties and their corresponding objects.

|      | lettuce | spinach | carrot | celery |
| ---- | ------: | ------: | -----: | -----: |
| leaf |       1 |       1 |      0 |      0 |
| root |       0 |       0 |      1 |      0 |
| stem |       0 |       0 |      0 |      1 |

If we designate a Boolean semiring AND/OR over this space, we can verify some useful results.

* If we perform matrix multiplication of $W^T_i \otimes W_i$, we can obtain a map of property co-occurrences.
* The matrix $W$ serves as an indexing space, meaning we can take a one-hot-encoded vector of properties $v_q$ that denotes the objects we want to find. And by vector multiplication $W_i \otimes v_q$ find those vegetables that meet these properties.

Returning to the categories of sense defined in Section 2, the logical restrictions of this system become clear. *Sinnlos* denotes computable operations that yield no distinguishing information: either tautologies (e.g., searching for "food" returns all objects) or contradictions (e.g., searching for "leaf" and "stem" simultaneously). Conversely, *Unsinnig* corresponds to operations that are structurally inexpressible because no coordinate exists in $L_i$ (such as asking for a vegetable's "doors" or an unmapped property like "sweet taste").

Up to this point, the proposed system aligns with standard Boolean logic without offering anything new to the fundamental works of logic and computation. However, its true utility emerges once we introduce indexability and unambiguity, as restrictions that allow turning this into a kind of logical truth machine.

We first address its extensibility. Extending $W_i$ to contain new facts is a straightforward operation. If the fact has a defined coordinate (object, property) that is mappable to the current $L_i$, the mechanism is to find the coordinate and set its value to true. Otherwise, the operation will require adding a new object or property to the coordinates and check its truthfulness $W_i$ and sense $S_i$ for every other proposition that the dimensional addition generates.

Regarding ambiguity in $W_i$, the proposed system allows the detection of it through an elementary algebraic operation.

* $W_i \otimes W^T_i$ yields a matrix of objects against objects, containing all the facts that denote some truthfulness in the map. Note that, in this case, since we are interested only in the objects that share some property in reality, the sense layer $S_i$ can simply be ignored. Furthermore, the intersection of anything with ∅ can simply be considered 0.

* $(W_i \otimes W^T_i) - \mathbb{I}$ clears the diagonal, which contains only tautological results.

* Finally, by dimensionally collapsing this matrix by multiplying it by a vector of ones, we can detect those objects that are colliding in some property in $W_i$.

Then, to disambiguate these objects, we introduce a new property to $L_i$ that will allow differentiating them. In our case, since the collapse dimension is a leaf, the easiest thing to do is to add inherited properties to it, for example, rough and smooth.

Table: Extended matrix with inherited properties and sense mask ($\emptyset$) for invalid coordinates.

|         | leaf | root | stem | (leaf) rough | (leaf) smooth |
| ------- | ---: | ---: | ---: | -----------: | ------------: |
| lettuce |    1 |    0 |    0 |            0 |             1 |
| spinach |    1 |    0 |    0 |            1 |             0 |
| carrot  |    0 |    1 |    0 |            Ø |             Ø |
| celery  |    0 |    0 |    1 |            Ø |             Ø |

Another detail becomes apparent: if we partition by lettuce and spinach over leaf-related properties, "leaf" becomes a tautological (*sinnlos*) property. However, for carrot and celery, these newly introduced leaf properties are *unsinnig*: any truth value computed for them is structurally meaningless. The solution can be approached in two ways:

* Use a sense mask $S_i$ around the facts that are indexable by these objects and properties, setting the result to 0 for every possible case if querying about truth.

* Create another matrix $W_i'$ that indexes only leafy vegetables. Then, the operation to search for vegetables by the property about their leaves becomes $W_i \otimes p'_i \otimes W'_i \otimes p'_i$.

This yields some interesting results:

- $W_i$ is basically a hierarchical routing space that partitions $W_i \cup W'_i$, in other words, a context index over a tensorial logic space where we can identify objects by their properties without the need to use $S_i$.
- The tensorial expansion and collapsing are reversible: $S( W_i \cup W'_i)$ can be recovered by filling the facts that the properties of $L'_i$ do not map in $L_i$ with Ø.
- The process is infinitely recursive, enabling unions, intersections and every other set operations that a boolean ring allows. And as long as we correctly permute the dimensions, we can reorganize the tensorial routes as we want.
- The introduction of hierarchies of contexts enables the use of this logic as a tree search index. Or, to treat a tree search index as a combination of truth and sense matrices.
- In the proposed example, we worked with an $L_i$ that mapped objects to properties, but $L$ contains every relation expressible with boolean logic. State machines, s-expressions, if-else flows, among others, are just instances of what can be computed with the combination of sense and logic.
- Finally, by the usage of these results, we can obtain partitions of $S$, as a set of algebraically computable logical grammar rules for determined contexts.

In Wittgenstein's words, we have defined a direct projection between thought and its logical image, represented in bits and operable through Boolean logic.

Section ID: 03_proposed_representation
Source Section File: sections/03_proposed_representation.md

## Paragraph Refs

- ../paragraphs/03_proposed_representation-p01.md
- ../paragraphs/03_proposed_representation-p02.md
- ../paragraphs/03_proposed_representation-p03.md
- ../paragraphs/03_proposed_representation-p04.md
- ../paragraphs/03_proposed_representation-p05.md
- ../paragraphs/03_proposed_representation-p06.md
- ../paragraphs/03_proposed_representation-p07.md
- ../paragraphs/03_proposed_representation-p08.md
- ../paragraphs/03_proposed_representation-p09.md
- ../paragraphs/03_proposed_representation-p10.md
- ../paragraphs/03_proposed_representation-p11.md
- ../paragraphs/03_proposed_representation-p12.md
- ../paragraphs/03_proposed_representation-p13.md
- ../paragraphs/03_proposed_representation-p14.md
- ../paragraphs/03_proposed_representation-p15.md
- ../paragraphs/03_proposed_representation-p16.md
- ../paragraphs/03_proposed_representation-p17.md
- ../paragraphs/03_proposed_representation-p18.md
- ../paragraphs/03_proposed_representation-p19.md
- ../paragraphs/03_proposed_representation-p20.md
- ../paragraphs/03_proposed_representation-p21.md
- ../paragraphs/03_proposed_representation-p22.md
- ../paragraphs/03_proposed_representation-p23.md
- ../paragraphs/03_proposed_representation-p24.md
- ../paragraphs/03_proposed_representation-p25.md
- ../paragraphs/03_proposed_representation-p26.md
- ../paragraphs/03_proposed_representation-p27.md

## Paragraph Digest
