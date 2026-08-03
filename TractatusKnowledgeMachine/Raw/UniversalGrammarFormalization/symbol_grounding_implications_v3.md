# Implicaciones del symbol grounding para una v3

## Resumen

La publicación de Liu (2026) refuerza una intuición central del perfil: el significado no queda suficientemente estabilizado dentro de un sistema puramente simbólico, cerrado y autosuficiente. Si el grounding exige conexión externa, actualización dinámica y algún tipo de intervención meta-sistémica, entonces una v3 no debe presentar `MeaningExpression` como “el significado final”, sino como una representación operable, auditable y provisionalmente anclada por evidencia externa, contexto y validación.

Esto cambia el énfasis del perfil. La v2 separa capas para evitar mezclar superficie, sintaxis, contexto y representación semántica. La v3 debería añadir explícitamente una capa de grounding o evidencia referencial: no basta con producir `(es vino calidad:buena)` o `(dar libro agente:juan destinatario:maria)`. El sistema debe registrar por qué esa representación está autorizada: qué input la motivó, qué contexto la seleccionó, qué ontología o recurso externo la respalda, qué referente se asumió, qué confianza tiene y qué condiciones permitirían revisarla.

## Cambio conceptual

La distinción importante es esta: semantic parsing transforma lenguaje natural en una representación formal, pero symbol grounding pregunta por qué esa representación significa algo fuera del sistema. Una v3 debería conservar el pipeline de semantic parsing, pero no confundirlo con grounding. El parser puede producir una forma lógica; el grounding layer debe conectar esa forma con mundo, dominio, percepción, base de conocimiento, interacción humana o reglas institucionales.

En términos prácticos, esto implica que `MeaningExpression` no debería estar sola. Debe ir acompañada de una estructura como `GroundingEvidence`, `ReferenceBinding` o `GroundingState`. Esa estructura indicaría si el nodo semántico apunta a una entidad conocida, a una clase ontológica, a una hipótesis contextual, a una metáfora, a una convención lingüística o a un referente todavía no resuelto.

## Propuesta para v3

La v3 podría extender `SemanticParsingAnnotation` así:

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
 :grounding GroundingState
 :confidence {:meaning 0.82 :syntax 0.76 :grounding 0.64}
 :provenance {:parser :manual-v0 :created-at "2026-06-09"}}
```

Donde `GroundingState` podría ser:

```clojure
{:status :grounded
 :bindings [{:meaning-node :vino
             :binding-type :ontology-class
             :target :Wine
             :source :domain-ontology}
            {:meaning-node :buena
             :binding-type :contextual-value
             :target [:quality :good]
             :source :domain-policy}]
 :open-questions []
 :revision-policy :context-sensitive}
```

Para un caso ambiguo:

```clojure
{:status :partially-grounded
 :bindings [{:surface "sangre de cristo"
             :meaning-node :vino
             :binding-type :metaphorical-or-institutional-alias
             :source :religious-context}]
 :open-questions [:literal-reference? :domain-confirmation?]
 :revision-policy :requires-context}
```

## Ejemplo: “El vino está bueno”

La v2 permite representar:

```clojure
(es vino calidad:buena)
```

La v3 debería añadir qué autoriza esa normalización:

```clojure
{:meaning-expression '(es vino calidad:buena)
 :grounding {:status :grounded
             :bindings [{:meaning-node :vino
                         :target :Wine
                         :binding-type :ontology-class}
                        {:meaning-node :calidad:buena
                         :target [:sensory-quality :positive]
                         :binding-type :domain-value}]
             :context {:domain :wine :locale :generic-es}}}
```

Para “El vinacho ta pulento”, la `MeaningExpression` puede ser la misma, pero el grounding debe registrar que la equivalencia depende de variedad lingüística y contexto chileno informal:

```clojure
{:surface-form {:tokens ["El" "vinacho" "ta" "pulento"]
                :variety :cl-es
                :register :informal}
 :meaning-expression '(es vino calidad:buena)
 :grounding {:status :grounded
             :bindings [{:surface "vinacho"
                         :meaning-node :vino
                         :binding-type :lexical-normalization
                         :source :cl-es-lexicon}
                        {:surface "pulento"
                         :meaning-node :calidad:buena
                         :binding-type :lexical-normalization
                         :source :cl-es-lexicon}]}}
```

## Consecuencia para LLMs

Los embeddings y los LLMs pueden proponer equivalencias útiles, pero no deben ser la autoridad final de grounding. Pueden sugerir que “vinacho” está cerca de “vino”, o que “sangre de cristo” puede referir a vino en cierto contexto, pero la v3 debe exigir una etapa posterior de validación: recurso léxico, ontología, contexto discursivo, regla de dominio, interacción humana o evidencia externa.

La conclusión de diseño es que el LLM puede operar como generador de hipótesis entre `SurfaceForm` y `MeaningExpression`, mientras que `GroundingState` funciona como la capa que decide si esa hipótesis queda aceptada, parcialmente aceptada, rechazada o pendiente de contexto.

## Referencia clave

Liu, Z. (2026). *A Unified Formal Theory on the Logical Limits of Symbol Grounding*. Minds and Machines, 36(1), Article 11. https://doi.org/10.1007/s11023-026-09763-2
