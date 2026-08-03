# Perfil de anotación para semantic parsing

**Borrador técnico v0.2:** de texto natural a forma superficial, sintaxis, contexto y representación semántica

## Resumen

Este documento reemplaza el uso ambiguo de “SMG” por un perfil de anotación basado en distinciones ya existentes en lingüística formal, NLP y teoría de lenguajes: entrada textual, forma superficial, sintaxis concreta, sintaxis abstracta, roles semánticos, forma lógica/representación de significado y contexto pragmático-discursivo. La intención no es proponer una teoría nueva del lenguaje ni inventar una representación semántica desde cero, sino adoptar nombres y separaciones cercanas a la literatura para que el sistema pueda interoperar con prácticas conocidas de semantic parsing, Universal Dependencies, frame semantics, AMR y DRT.

## 1. Principio de diseño

La tesis operacional es conservadora: una entrada en lenguaje natural debe pasar por capas de análisis que ya son habituales en NLP y lingüística computacional. Una gramática formal caracteriza cadenas o estructuras bien formadas, pero no agota el significado; esta separación entre forma sintáctica y significado está en la tradición de las gramáticas formales y la lingüística generativa (Chomsky, 1957; Harman, 1972). En semántica formal, el significado se modela mediante herramientas lógicas, composicionales o modelo-teóricas; Montague es la referencia clásica para tratar fragmentos de lenguaje natural con la misma precisión que lenguajes formales (Montague, 1970; Janssen, 2011).

```text
NaturalText + DiscoursePragmaticContext
  => SurfaceForm + ConcreteSyntax + AbstractSyntax + MeaningExpression + Alignment
```

La separación de capas busca reproducir una expectativa estándar: dos enunciados pueden compartir representación semántica aunque difieran en realización superficial; pueden compartir un patrón sintáctico aunque difieran en registro o dialecto; y el contexto puede modular la interpretación sin confundirse con la representación semántica resultante.

## 2. Capas adoptadas

Las capas siguientes no deben leerse como una taxonomía original. Son nombres operativos para conceptos cercanos a los usados en NLP, compiladores, semántica formal y anotación lingüística. Cuando exista un estándar o práctica dominante, debe preferirse ese estándar antes que una convención propia.

### 2.1 NaturalText

`NaturalText` corresponde al *utterance* o entrada textual original. No debe contener análisis; solo identifica la cadena, idioma presumido, fuente y metadatos mínimos. En semantic parsing, el punto de partida es precisamente un enunciado en lenguaje natural que se mapea hacia una forma lógica, programa o representación ejecutable (Liang, 2016; Kamath & Das, 2018).

```clojure
{:id "utt-001"
 :text "El vinacho ta pulento."
 :source :user
 :language-hint :es}
```

### 2.2 SurfaceForm

`SurfaceForm` corresponde a la realización superficial: tokens, variantes, registro, normalizaciones y elecciones léxicas. Esta capa no decide el significado. Su tarea es preservar lo dicho/escrito de modo reversible o auditable. La distinción entre estructura superficial y niveles más abstractos es clásica en la tradición generativa, aunque aquí no se adopta la tesis fuerte de que exista una única “deep structure” equivalente al significado (Chomsky, 1957; Harman, 1972).

```clojure
{:text "El vinacho ta pulento."
 :tokens ["El" "vinacho" "ta" "pulento"]
 :variety :cl-es
 :register :informal
 :lexical-choices {:vino "vinacho" :estar "ta" :bueno "pulento"}}
```

### 2.3 ConcreteSyntax

`ConcreteSyntax` representa la organización gramatical cercana al texto. En una implementación práctica conviene usar directamente Universal Dependencies cuando sea posible: partes de habla, rasgos morfológicos y dependencias sintácticas consistentes entre lenguas (de Marneffe et al., 2021). También puede mapearse a un árbol de constituyentes si el parser usado produce ese formato.

```clojure
{:construction :copular-clause
 :subject {:span [0 2] :head "vinacho"}
 :copula {:span [2 3] :form "ta"}
 :predicate {:span [3 4] :head "pulento"}}
```

### 2.4 AbstractSyntax

`AbstractSyntax` es una normalización sintáctica que remueve detalles superficiales no necesarios para el análisis posterior. La analogía viene de teoría de lenguajes y compiladores: la sintaxis concreta es la forma parseable; la abstracta conserva la estructura relevante para análisis y traducción (Aho et al., 2006; Krahn et al., 2014). Esta capa sigue siendo sintáctica, no semántica.

```clojure
(copular-evaluation NP AdjP)
```

### 2.5 MeaningExpression

`MeaningExpression` corresponde a una *logical form*, *semantic representation*, *meaning representation* o programa semántico ejecutable/interpretable. La decisión local es serializarla como s-expression legible por humanos y herramientas, sin pretender que sea el AST del texto. Esta capa debe poder mapearse a formalismos existentes cuando convenga: AMR/PENMAN para grafos semánticos, RDF/OWL para publicación ontológica, SQL/SPARQL para consultas o lambda calculus/lambda-DCS para semantic parsing (Banarescu et al., 2013; Liang, 2016; Kamath & Das, 2018).

```clojure
(es vino calidad:buena)
(ser lechuga parte_comestible:hoja textura:lisa)
(dar libro agente:juan destinatario:maria)
```

### 2.6 SemanticFrame

`SemanticFrame` corresponde a una estructura predicado-argumento con roles semánticos nombrados. No debe inventar roles arbitrarios si existe un inventario aplicable: conviene alinearlo con FrameNet, PropBank, VerbNet, AMR roles o una ontología de eventos del dominio. La decisión de usar etiquetas como `agente`, `destinatario`, `tema`, `paciente` o `instrumento` se apoya en case grammar, thematic roles y semantic role labeling (Fillmore, 1968; Gildea & Jurafsky, 2002).

```clojure
{:predicate :dar
 :theme :libro
 :roles {:agent :juan
         :recipient :maria}}
```

### 2.7 DiscoursePragmaticContext

`DiscoursePragmaticContext` reúne condiciones de interpretación: dominio, situación, historia discursiva, registro, variedad lingüística, intención del hablante y supuestos activos. Esta capa es una operacionalización práctica de nociones existentes, no una teoría nueva del contexto. En pragmática, el contexto contribuye al significado de los enunciados; en DRT y semánticas dinámicas, las oraciones actualizan representaciones discursivas que permiten resolver referencia, anáfora y dependencia contextual (Grice, 1975; Levinson, 1983; Kamp, 1981; Kamp & Reyle, 1993).

```clojure
{:domain :wine
 :locale :cl
 :speaker-intent :positive-evaluation
 :target-dimension :quality
 :discourse-state {:referents [] :assumptions [:informal-register]}}
```

### 2.8 Alignment

`Alignment` registra la trazabilidad entre spans/tokens, análisis sintáctico y nodos de la representación semántica. No es significado, sino evidencia de anotación. Debe parecerse a las prácticas de corpus anotados: spans sobre tokens, referencias a nodos sintácticos y referencias a nodos/aristas semánticas. AMR justifica la capa de grafo semántico y UD la capa sintáctica multilingüe; el alineamiento es la relación técnica que permite auditar el paso entre ambas (Banarescu et al., 2013; de Marneffe et al., 2021).

```clojure
[{:surface-span [1 2] :surface "vinacho" :meaning-node :vino}
 {:surface-span [3 4] :surface "pulento" :meaning-edge [:calidad :buena]}]
```

## 3. Ejemplos de separación de capas

Ejemplo A y B comparten `MeaningExpression`, pero no `SurfaceForm`. Pueden compartir una `AbstractSyntax` aproximada, aunque difieren en registro, variante y lexicalización.

```text
Input A: "El vino está bueno."
MeaningExpression: (es vino calidad:buena)
SurfaceForm: {:register :neutral :lexical-choices {:vino "vino" :bueno "bueno"}}
ConcreteSyntax: {:construction :copular-clause :copula "está"}
Context: {:locale :generic-es :domain :wine}
```

```text
Input B: "El vinacho ta pulento."
MeaningExpression: (es vino calidad:buena)
SurfaceForm: {:register :informal :variety :cl-es :lexical-choices {:vino "vinacho" :bueno "pulento"}}
ConcreteSyntax: {:construction :copular-clause :copula "ta"}
Context: {:locale :cl :domain :wine :speaker-intent :positive-evaluation}
```

## 4. Perfil de datos

El objeto principal se denomina aquí `SemanticParsingAnnotation`. El nombre es deliberadamente descriptivo: no pretende introducir un estándar nuevo, sino agrupar salidas que ya aparecen en pipelines de NLP y semantic parsing. Si se adopta un formato externo concreto, este registro debe poder funcionar como perfil de intercambio o adaptador.

```clojure
{:annotation-id "spa-001"
 :natural-text NaturalText
 :surface-form SurfaceForm
 :concrete-syntax ConcreteSyntax
 :abstract-syntax AbstractSyntax
 :meaning-expression MeaningExpression
 :semantic-frame SemanticFrame
 :context DiscoursePragmaticContext
 :alignment [Alignment]
 :confidence {:meaning 0.82 :syntax 0.76}
 :provenance {:parser :manual-v0 :created-at "2026-06-09"}}
```

| Campo local                 | Nombre cercano en literatura                                    | Función                                                                                 | Referencia base                                                                                               |
| --------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `NaturalText`               | utterance / sentence / natural-language input                   | Entrada textual humana antes de analizar.                                               | NLP como análisis y representación de textos naturales: Liddy (2001); semantic parsing: Kamath & Das (2018).  |
| `SurfaceForm`               | surface form / realization                                      | Realización textual concreta: tokens, grafía, variante, registro, elección léxica.      | Distinción forma superficial vs estructura subyacente: Chomsky (1957); Harman (1972).                         |
| `ConcreteSyntax`            | parse tree / dependency syntax / Universal Dependencies         | Estructura sintáctica próxima al texto y preservadora de detalles gramaticales.         | Universal Dependencies: de Marneffe et al. (2021).                                                            |
| `AbstractSyntax`            | abstract syntax / AST-like syntactic structure                  | Estructura sintáctica normalizada, sin detalles superficiales no esenciales.            | Abstract syntax trees: Aho et al. (2006); Krahn et al. (2014).                                                |
| `MeaningExpression`         | logical form / semantic representation / executable program     | Representación semántica operable, serializable como s-expression.                      | AMR: Banarescu et al. (2013); semantic parsing: Liang (2016), Kamath & Das (2018).                            |
| `SemanticFrame`             | predicate-argument structure / semantic roles / case frame      | Predicado/evento/estado con participantes y atributos nombrados.                        | Case grammar and roles: Fillmore (1968); SRL: Gildea & Jurafsky (2002).                                       |
| `DiscoursePragmaticContext` | pragmatic context / discourse context / DRT context             | Información de uso, dominio, situación, registro, discurso y supuestos interpretativos. | Pragmatics: Grice (1975), Levinson (1983); DRT: Kamp (1981), Kamp & Reyle (1993).                             |
| `Alignment`                 | annotation links / token-node alignment                         | Vínculos entre spans/tokens, nodos sintácticos y nodos semánticos para trazabilidad.    | AMR and sembanking: Banarescu et al. (2013); UD annotations: de Marneffe et al. (2021).                       |

## 5. Reglas de interoperabilidad

* `SurfaceForm` no puede introducir nodos semánticos por sí sola; solo preserva realización textual y rasgos de forma.
* `ConcreteSyntax` y `AbstractSyntax` describen organización gramatical, no verdad, referencia ni inferencia.
* `MeaningExpression` debe poder mantenerse estable a través de paráfrasis, cambios de registro y traducción parcial.
* `DiscoursePragmaticContext` puede seleccionar o restringir interpretaciones, pero no debe reemplazar a `MeaningExpression`.
* `Alignment` es evidencia trazable, no una capa ontológica.
* Toda conversión hacia s-expressions debe distinguir roles semánticos de posiciones gramaticales como sujeto/objeto.
* Siempre que un formato establecido cubra la necesidad, debe preferirse el formato establecido antes que una etiqueta local.
* Las etiquetas locales (`agente`, `destinatario`, `tema`) deben mantener una tabla de equivalencias hacia roles externos cuando exista un recurso aplicable.

## 6. Justificación bibliográfica por estructura de dato

| Estructura                  | Justificación                                                                       | Citas mínimas                                      |
| --------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------- |
| `NaturalText`               | Entrada natural previa a semantic parsing.                                          | Liang (2016); Kamath & Das (2018)                  |
| `SurfaceForm`               | Realización concreta y rasgos superficiales distinguibles de niveles abstractos.    | Chomsky (1957); Harman (1972)                      |
| `ConcreteSyntax`            | Árbol/dependencias cercanas al texto.                                               | de Marneffe et al. (2021)                          |
| `AbstractSyntax`            | Normalización sintáctica útil para análisis posterior, distinta de concrete syntax. | Aho et al. (2006); Krahn et al. (2014)             |
| `MeaningExpression`         | Forma lógica/representación semántica operable.                                     | Banarescu et al. (2013); Liang (2016); Kamath & Das (2018) |
| `SemanticFrame`             | Predicado con roles semánticos.                                                     | Fillmore (1968); Gildea & Jurafsky (2002)          |
| `DiscoursePragmaticContext` | Contexto de uso y estado discursivo.                                                | Grice (1975); Levinson (1983); Kamp (1981)         |
| `Alignment`                 | Trazabilidad entre forma y significado en anotación semántica.                      | Banarescu et al. (2013); de Marneffe et al. (2021) |

## Referencias

Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools* (2nd ed.). Pearson.

Banarescu, L., Bonial, C., Cai, S., Georgescu, M., Griffitt, K., Hermjakob, U., Knight, K., Koehn, P., Palmer, M., & Schneider, N. (2013). Abstract Meaning Representation for sembanking. *Proceedings of the 7th Linguistic Annotation Workshop and Interoperability with Discourse*, 178–186. https://aclanthology.org/W13-2322/

Chomsky, N. (1957). *Syntactic Structures*. Mouton.

de Marneffe, M.-C., Manning, C. D., Nivre, J., & Zeman, D. (2021). Universal Dependencies. *Computational Linguistics, 47*(2), 255–308. https://doi.org/10.1162/coli_a_00402

Fillmore, C. J. (1968). The Case for Case. In E. Bach & R. T. Harms (Eds.), *Universals in Linguistic Theory* (pp. 1–88). Holt, Rinehart and Winston.

Gildea, D., & Jurafsky, D. (2002). Automatic labeling of semantic roles. *Computational Linguistics, 28*(3), 245–288. https://doi.org/10.1162/089120102760275983

Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics, Vol. 3: Speech Acts* (pp. 41–58). Academic Press.

Harman, G. (1972). Deep Structure as Logical Form. In D. Davidson & G. Harman (Eds.), *Semantics of Natural Language* (pp. 25–47). D. Reidel.

Janssen, T. M. V. (2011). Montague Semantics. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/montague-semantics/

Kamath, A., & Das, R. (2018). A Survey on Semantic Parsing. *arXiv:1812.00978*. https://arxiv.org/abs/1812.00978

Kamp, H. (1981). A theory of truth and semantic representation. In J. Groenendijk, T. Janssen, & M. Stokhof (Eds.), *Formal Methods in the Study of Language* (pp. 277–322). Mathematical Centre.

Kamp, H., & Reyle, U. (1993). *From Discourse to Logic: Introduction to Modeltheoretic Semantics of Natural Language, Formal Logic and Discourse Representation Theory*. Kluwer.

Krahn, H., Rumpe, B., & Völkel, S. (2014). Integrated Definition of Abstract and Concrete Syntax for Textual Languages. *arXiv:1409.6624*. https://arxiv.org/abs/1409.6624

Levinson, S. C. (1983). *Pragmatics*. Cambridge University Press.

Liang, P. (2016). Learning executable semantic parsers for natural language understanding. *Communications of the ACM, 59*(9), 68–76. https://doi.org/10.1145/286656 executable version available at https://cs.stanford.edu/~pliang/papers/executable-cacm2016.pdf

Liddy, E. D. (2001). Natural Language Processing. In *Encyclopedia of Library and Information Science* (2nd ed.). Marcel Decker.

Montague, R. (1970). Universal grammar. *Theoria, 36*(3), 373–398.
