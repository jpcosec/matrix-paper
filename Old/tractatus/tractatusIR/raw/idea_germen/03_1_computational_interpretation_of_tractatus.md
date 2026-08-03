# Computational Interpretation Of Tractatus

## Purpose

This document defines a computational interpretation of the *Tractatus Logico-Philosophicus* based as directly as possible on the proposition structure preserved in `tractatus_tree_de.json`.

The aim is not to summarize the whole book.
The aim is to isolate the parts that describe a formal architecture of:

- objects
- possible combinations
- facts
- worlds
- pictures
- proposition-signs
- propositions
- truth-functions
- the distinction between sense, truth, and what can only be shown

Primary textual basis: `truth_machine/tractatus_tree_de.json`

Main proposition groups used here:

- world and facts: `1`, `1.1`, `1.11`, `1.12`, `1.13`, `1.21`, `2`
- objects and possibility: `2.01`, `2.011`, `2.012`, `2.0121`, `2.0123`, `2.013`, `2.014`, `2.0141`
- picture and sense: `2.1`, `2.11`, `2.12`, `2.15`, `2.18`, `2.201`, `2.202`, `2.203`, `2.21`, `2.221`, `2.222`, `2.223`, `2.224`, `2.225`
- proposition-sign and projection: `3.1`, `3.11`, `3.12`, `3.13`, `3.14`, `3.141`, `3.142`, `3.143`, `3.1431`, `3.1432`, `3.144`
- names, symbols, logical syntax: `3.2`, `3.202`, `3.203`, `3.22`, `3.26`, `3.261`, `3.3`, `3.31`, `3.313`, `3.314`, `3.32`, `3.323`, `3.326`, `3.327`, `3.328`, `3.33`, `3.334`
- logical space and proposition: `3.4`, `3.42`, `4.021`, `4.022`, `4.023`, `4.024`, `4.03`, `4.031`, `4.0311`, `4.0312`
- saying and showing: `4.12`, `4.121`, `4.1211`, `4.1212`, `4.122`, `4.124`, `4.125`, `4.126`
- tautology, contradiction, nonsense: `4.46`, `4.461`, `4.4611`, `4.462`, `4.463`, `7`

## Core Thesis

The *Tractatus* can be read computationally because it describes a layered system in which:

1. simple objects define a space of possible combinations
2. possible combinations are states of affairs
3. obtaining states of affairs are facts
4. the world is the totality of facts
5. a picture or proposition projects a possible state of affairs
6. truth is determined by comparison with reality
7. logical form governs representability but cannot itself be said as one more fact

This is not an arbitrary modernization.
It is already suggested by the text itself.

References: `1-2`, `2.1-2.225`, `3.1-3.328`, `4.021-4.1212`, `4.46-4.463`, `7`

## 1. Ontological Base: Object, Possibility, State Of Affairs, Fact, World

The architecture begins from the bottom.

At 2.01, a `Sachverhalt` is a combination of objects:

```text
"Der Sachverhalt ist eine Verbindung von Gegenständen."
```

At 2.012, 2.0121, 2.0123, 2.013, and 2.0141, the possibility of occurring in states of affairs belongs to the object itself.
The object is inseparable from the space of its possible combinations.

This means that the ontology is already computationally constrained.
Objects are not bare names first and only later related.
Their form is the totality of their possible occurrences.

References: `2.01`, `2.011`, `2.012`, `2.0121`, `2.0123`, `2.013`, `2.014`, `2.0141`

At 2, the fact is the obtaining of a state of affairs:

```text
"Was der Fall ist, die Tatsache, ist das Bestehen von Sachverhalten."
```

At 1, 1.1, and 1.13, the world is not the totality of things but the totality of facts in logical space:

```text
1   Die Welt ist alles, was der Fall ist.
1.1 Die Welt ist die Gesamtheit der Tatsachen, nicht der Dinge.
1.13 Die Tatsachen im logischen Raum sind die Welt.
```

So the primary architecture is:

```text
object
  -> possible state of affairs
  -> obtaining fact
  -> world as totality of facts
```

This is already enough to justify a computational reading.
The system begins not from words but from a typed distinction between possibility, obtaining, and total world-description.

References: `1`, `1.1`, `1.11`, `1.12`, `1.13`, `2`, `2.01`

## 2. Picture And Proposition: Projection Of Possible Situations

The next layer is pictorial.

At 2.1 through 2.203, the picture is not a decorative image but a fact whose elements stand for objects and whose structure depicts a possible arrangement of them.

At 2.11, 2.12, and 2.201:

- the picture presents a situation in logical space
- it is a model of reality
- it depicts a possible state of affairs

At 2.221 through 2.225, the distinction between sense and truth becomes explicit:

```text
2.221 Was das Bild darstellt, ist sein Sinn.
2.222 In der Übereinstimmung oder Nichtübereinstimmung seines Sinnes mit der Wirklichkeit, besteht seine Wahrheit oder Falschheit.
2.223 Um zu erkennen, ob das Bild wahr oder falsch ist, müssen wir es mit der Wirklichkeit vergleichen.
2.224 Aus dem Bild allein ist nicht zu erkennen, ob es wahr oder falsch ist.
2.225 Ein a priori wahres Bild gibt es nicht.
```

This is one of the most important computational distinctions in the book.

### Sense is not truth

`Sinn` is the possible state of affairs a picture or proposition presents.

Truth is a second step.
It is the agreement or non-agreement of that sense with reality.

So the basic evaluation sequence is:

```text
projection of a possible situation
  -> sense
  -> comparison with reality
  -> truth or falsity
```

This means that representability and truth-value are distinct.
A proposition must first determine a possible place in logical space before it can be true or false.

References: `2.201`, `2.202`, `2.203`, `2.21`, `2.221`, `2.222`, `2.223`, `2.224`, `2.225`

## 3. Proposition-Sign And Projection

The strongest computational turn comes in 3.11 to 3.13.

```text
3.11  Wir benützen das sinnlich wahrnehmbare Zeichen des Satzes als Projektion der möglichen Sachlage.
3.12  Der Satz ist das Satzzeichen in seiner projektiven Beziehung zur Welt.
3.13  Im Satz ist die Form seines Sinnes enthalten, aber nicht dessen Inhalt.
```

This gives a precise architecture.

The proposition is not the sign alone.
It is the proposition-sign in projective relation to the world.

That implies three distinct layers:

1. the perceptible sign
2. the projective method
3. the possible situation projected

And 3.14 to 3.1432 sharpen the point further:

- the proposition-sign is a fact
- its elements stand in determinate relations
- only facts can express sense
- a mere class of names cannot do so

In 3.142:

```text
"Nur Tatsachen können einen Sinn ausdrücken, eine Klasse von Namen kann es nicht."
```

This is decisive.
The logical unit is not the isolated word.
The logical unit is an articulated fact-like sign-configuration.

References: `3.11`, `3.12`, `3.13`, `3.14`, `3.141`, `3.142`, `3.143`, `3.1431`, `3.1432`, `3.144`

## 4. Why This Is Not A Sign-First Model

At this point a contrast can be drawn.

An LLM-style path can be glossed as:

```text
natural language
  -> signs
  -> latent statistical structure
```

The tractarian path is different.
It runs the other way around:

```text
possible facts and logical form
  -> projection
  -> proposition-sign
```

In the tractarian order, signs are not primary bearers of logic.
They are perceptible vehicles used as projections of possible situations.

The logical center therefore lies not in surface language as such, but in:

- `Sachverhalt`
- `Tatsache`
- `Bild`
- `Sinn`
- `logischer Raum`

This is why the book is much closer to a facts-first representational theory than to a signs-first semantic theory.

References: `2`, `2.01`, `2.221`, `3.11`, `3.12`, `3.142`, `4.021`, `4.022`

## 5. Name, Symbol, Logical Syntax

The next step appears in 3.2 through 3.263.

At 3.202 and 3.203, the simple signs used in the proposition are names and the name means the object.

But 3.3 through 3.326 insist that signs alone are not enough.

At 3.313, 3.314, 3.315, 3.32, 3.323, and especially 3.326, the distinction between sign and symbol is made through use.

The crucial propositions are:

```text
3.326 Das Zeichen ist das sinnlich Wahrnehmbare am Symbol.
3.327 Um das Symbol am Zeichen zu erkennen, muss man auf den sinnvollen Gebrauch achten.
3.328 Das Zeichen bestimmt erst mit seiner logisch-syntaktischen Verwendung zusammen eine logische Form.
```

And 3.33 and 3.334 make the requirement even sharper:

```text
3.33  In der logischen Syntax darf nie die Bedeutung eines Zeichens eine Rolle spielen.
3.334 Die Regeln der logischen Syntax müssen sich von selbst verstehen, wenn man nur weiss, wie ein jedes Zeichen bezeichnet.
```

So the computational order is not:

```text
word -> lexical meaning -> logic
```

but rather:

```text
sign
  -> logical-syntactic use
  -> symbol
  -> projected sense
```

Logic does not arise from the ornamental surface of language.
It arises from articulated symbolic use governed by syntax.

References: `3.202`, `3.203`, `3.22`, `3.26`, `3.261`, `3.326`, `3.327`, `3.328`, `3.33`, `3.334`

## 6. The Proposition Determines A Place In Logical Space

At 3.4 and 3.42, the proposition determines a place in logical space:

```text
3.4  Der Satz bestimmt einen Ort im logischen Raum.
```

And at 4.023:

```text
"Der Satz konstruiert eine Welt mit Hilfe eines logischen Gerüstes."
```

This is a profoundly computational claim.

A proposition is not merely about the world.
It fixes a structured possibility inside a logical field.

References: `3.4`, `3.42`, `4.022`, `4.023`, `4.031`, `4.0311`

That is why the proposition can be understood as something like a structured coordinate or placement mechanism in logical space.

## 7. Sense As An Independent Property

The distinction between `Sinn` and truth must remain explicit.

At 4.022:

```text
"Der Satz zeigt seinen Sinn. Der Satz zeigt, wie es sich verhält, wenn er wahr ist. Und er sagt, dass es sich so verhält."
```

At 4.024:

```text
"Einen Satz verstehen, heisst, wissen was der Fall ist, wenn er wahr ist."
```

So `Sinn` is not identical to actual truth.
It is the articulated possible situation that is grasped when the proposition is understood.

This means:

- a proposition can have sense even if false
- a proposition can be understood without knowing whether it is true
- truth requires comparison with reality
- sense is therefore a property of articulated representability prior to truth-value

Computationally:

```text
sense = the possible state of affairs fixed by the proposition
truth = whether that sense obtains in the world
```

References: `2.221`, `2.222`, `2.223`, `4.022`, `4.024`

## 8. What Can Be Represented, Said, And Only Shown

The boundary condition appears at 4.12 through 4.1212.

```text
4.12   The proposition can represent the whole of reality, but not what it must have in common with reality in order to represent it: logical form.
4.121  What reflects itself in language, language cannot represent.
4.1212 Was gezeigt werden kann, kann nicht gesagt werden.
```

This forces a sharp distinction.

### What can be represented and said

- possible states of affairs
- obtaining or non-obtaining configurations
- the sense of a proposition
- the truth or falsity of a proposition by comparison with reality

### What cannot be said in the same way

- logical form itself
- formal properties as if they were ordinary external facts
- the representational condition shared by proposition and world

What belongs to the possibility of representation can show itself in the proposition, but cannot be added as one more proposition of the same kind.

This is crucial because it prevents collapsing:

- fact
- form
- syntax
- condition of representation

into a single level.

References: `4.12`, `4.121`, `4.1211`, `4.1212`, `4.122`, `4.124`, `4.125`, `4.126`, `7`

## 9. Tautology, Contradiction, Sinnlos, Unsinnig

At 4.46 to 4.463 the *Tractatus* distinguishes tautology and contradiction as limiting truth-functional cases.

At 4.461:

```text
"Tautologie und Kontradiktion sind sinnlos."
```

But 4.4611 immediately adds:

```text
"Tautologie und Kontradiktion sind aber nicht unsinnig; sie gehören zum Symbolismus."
```

And 4.462 says that they are not pictures of reality and do not represent a possible situation.

This yields a precise triad.

### Sinnvoll

A proposition has sense if it presents a possible state of affairs.

### Sinnlos

A tautology or contradiction belongs to symbolism and to logic, but does not determine a possible situation in the world.

### Unsinnig

At 4.003 and 7, the truly nonsensical is what fails to belong to meaningful logical articulation and must ultimately be exposed rather than answered.

So the system does not collapse all failure into one bucket.
It distinguishes:

- sense-bearing proposition
- truth-functionally valid but world-empty form
- genuine nonsense

References: `4.46`, `4.461`, `4.4611`, `4.462`, `4.463`, `7`

## 10. Final Computational Reading

Taken together, the computational interpretation can be stated as follows.

```text
The Tractatus describes a formal architecture in which
simple objects determine a space of possible combinations,
possible combinations are states of affairs,
obtaining states are facts,
the world is the totality of facts in logical space,
the proposition-sign is used as a projection of a possible situation,
the proposition therefore has sense before truth,
truth is comparison of that sense with reality,
logical form governs this whole structure,
but logical form itself can only show itself and cannot be said as one more fact.
```

And in the narrow contrastive gloss requested here:

```text
LLM-style order:
natural language -> signs

Tractarian order:
logical form -> possible fact -> projection -> proposition-sign
```

The important consequence is that the tractarian system is not grounded in surface language first.
It is grounded in the articulable structure of possible facts.

## Proposition Reference Summary

For quick reuse, the core claims of this document rely on the following proposition clusters:

- ontological base: `1`, `1.1`, `1.11`, `1.12`, `1.13`, `2`, `2.01`, `2.011`, `2.012`, `2.013`, `2.0141`
- picture and sense: `2.1`, `2.11`, `2.12`, `2.18`, `2.201-2.225`
- projection and proposition-sign: `3.11-3.14`, `3.142-3.144`
- names, symbols, syntax: `3.202`, `3.203`, `3.22`, `3.26`, `3.261`, `3.326-3.334`
- logical space and proposition: `3.4`, `3.42`, `4.021-4.0312`
- saying vs showing: `4.12-4.126`
- tautology, contradiction, nonsense: `4.46-4.463`, `7`
