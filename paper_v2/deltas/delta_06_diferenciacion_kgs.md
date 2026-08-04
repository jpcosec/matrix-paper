# Delta 6 — Diferenciación explícita vs RAG/KGs y cercanía a OWL/redes causales

**Responde a:** Eje D (AC, `ppL8`, `FJpU`).
**Encuadre (según comentario del autor):** la diferencia mayor con RAG es la **ausencia de la categoría *Unsinnig***: RAG/KGs modelan **coocurrencia semántica** pero no **caminos lógicos**. Nuestra propuesta se acerca más a lo que permiten las **redes causales y OWL**, añadiendo la frontera de sentido explícita.

## DESDE (átomos KB origen)

| Átomo | Aporta |
|---|---|
| `Computacion/Optimizacion_y_Seguridad/Matrix_vs_RAG.md` | RAG recupera texto por coocurrencia, sin garantía lógica |
| `Computacion/Optimizacion_y_Seguridad/Matrix_vs_Neuro_Simbolicos_Previos.md` | Contraste con neuro-simbólico previo |
| `Computacion/Bitwise_Hardware/Eje_D_Diferenciacion_OWL_KGs_y_Vectorizacion_Bitwise.md` | OWL/KGs: sin categoría de inaplicabilidad semántica |
| `Aplicaciones/Demostracion_Ontologias_OWL_Semantic_Web.md` | OWL como vecino cercano y fuente de ingesta |
| `Computacion/Estructuras_Matriciales/Emergencia_Estructural_de_Si_en_Cruces_de_Contexto.md` | *Unsinnig* como categoría estructural (lo que falta en KGs) |
| `Antecedentes/Limites_Espacio_Continuo/Semantica_Formal_Neuro_Simbolica_vs_Opacidad_Neuronal.md` | Semántica formal vs opacidad neuronal |

## DESDE+ ampliación KB (referencias adicionales)

| Átomo | Aporte |
|---|---|
| `Computacion/Optimizacion_y_Seguridad/Matrix_vs_Neuro_Simbolicos_Previos.md` | Tabla comparativa vs NeSy: desacoplamiento estricto + semianillo booleano nativo |
| `Matematica/Algebra_Booleana_y_Silicio/Medida_y_Semianillos_Booleanos_vs_Probabilistas.md` | Medida booleana vs probabilista — formaliza "co-occurrence, not paths" |
| `Computacion/Optimizacion_y_Seguridad/Matrix_vs_Verificacion_Formal.md` | Contraste con verificación formal (vecino distinto de KGs) |
| `Antecedentes/Alucinaciones/Alucinaciones_Inducidas_por_RAG_y_Conflicto_de_Conocimiento.md` | RAG/KGs no eliminan alucinación: conflicto de conocimiento |
| `Computacion/Parsers_y_Runtimes/Parser_OWL2Matrix.md` | OWL/RDF = formato de ingesta, no rival |
| `Computacion/Optimizacion_y_Seguridad/Manejo_de_Contradicciones.md` | Manejo explícito de contradicciones (ausente en KGs) |
| `Teoria_de_Bases_de_Datos/03_acid_y_consistencia_logica.md` | Consistencia lógica como propiedad del store |
| `Filosofia/Tractatus_y_Ontologia/Triparticion_Wittgensteiniana_Sinnvoll_Sinnlos_Unsinnig.md` | Categoría Unsinnig: la diferencia categorial que falta en KGs |
| `Filosofia/Tractatus_y_Ontologia/Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable.md` | Embeddings insuficientes para lógica auditable |

**Extensión mapping (mismo párrafo nuevo, bridge `delta6_review`):**
```yaml
   - {atom_id: atom-matrix-vs-neuro-simbolicos-previos, atom_path: Computacion/Optimizacion_y_Seguridad/Matrix_vs_Neuro_Simbolicos_Previos.md, bridge: delta6_review, score: 0.9, detail: "strict decoupling + native boolean semiring vs NeSy"}
   - {atom_id: atom-medida-y-semianillos-booleanos-vs-probabilistas, atom_path: Matematica/Algebra_Booleana_y_Silicio/Medida_y_Semianillos_Booleanos_vs_Probabilistas.md, bridge: delta6_review, score: 0.85, detail: "boolean vs probabilistic measure"}
   - {atom_id: atom-matrix-vs-verificacion-formal, atom_path: Computacion/Optimizacion_y_Seguridad/Matrix_vs_Verificacion_Formal.md, bridge: delta6_review, score: 0.8, detail: "contrast with formal verification"}
   - {atom_id: atom-alucinaciones-inducidas-por-rag-y-conflicto-de-conocimiento, atom_path: Antecedentes/Alucinaciones/Alucinaciones_Inducidas_por_RAG_y_Conflicto_de_Conocimiento.md, bridge: delta6_review, score: 0.8, detail: "RAG/KGs do not remove hallucination"}
   - {atom_id: atom-parser-owl2matrix, atom_path: Computacion/Parsers_y_Runtimes/Parser_OWL2Matrix.md, bridge: delta6_review, score: 0.85, detail: "OWL/RDF as ingestion format"}
   - {atom_id: atom-manejo-de-contradicciones, atom_path: Computacion/Optimizacion_y_Seguridad/Manejo_de_Contradicciones.md, bridge: delta6_review, score: 0.75, detail: "explicit contradiction handling"}
   - {atom_id: atom-03-acid-y-consistencia-logica, atom_path: Teoria_de_Bases_de_Datos/03_acid_y_consistencia_logica.md, bridge: delta6_review, score: 0.75, detail: "logical consistency of the store"}
   - {atom_id: atom-triparticion-wittgensteiniana-sinnvoll-sinnlos-unsinnig, atom_path: Filosofia/Tractatus_y_Ontologia/Triparticion_Wittgensteiniana_Sinnvoll_Sinnlos_Unsinnig.md, bridge: delta6_review, score: 0.85, detail: "Unsinnig categorial difference"}
   - {atom_id: atom-insuficiencia-de-embeddings-de-signos-para-logica-auditable, atom_path: Filosofia/Tractatus_y_Ontologia/Insuficiencia_de_Embeddings_de_Signos_para_Logica_Auditable.md, bridge: delta6_review, score: 0.75, detail: "auditable logic beyond embeddings"}
```

## HACIA (párrafo destino)

- **`Neurips_peiper/sections/04_discussion.md`**, párrafo nuevo en `# Relationship with Language`, insertado **después del párrafo que cita traducciones a formas lógicas** (hoy `04_discussion-p03`) y **antes del de "document families"**.
- **No requiere anexo** (~150 palabras).

## Propuesta de texto

```markdown
Two families of neighboring work clarify what is new here. Retrieval pipelines and knowledge graphs capture *semantic co-occurrence*—which entities and phrases appear together—but not *logical paths*: a KG edge records that two nodes are related, with no category for combinations that are ill-formed in the first place, and recent benchmarks show LLM-based graph construction still produces unfaithful structures [@sansford2024grapheval]. Our proposal is closer in spirit to description logics and causal networks (KL-ONE, CLASSIC, conceptual graphs), which do constrain what can be consistently asserted [@brachman1990; @lehmann1992; @sowa1991; @kruse2022causal]; indeed, OWL ontologies enter our framework directly as input to the ingestion pathway. What we add to that lineage is an explicit, operable category of semantic inapplicability: sense is stored as a matrix layer $S_i$, and _Unsinnig_ is rejected at compile time inside the substrate rather than diagnosed by an external reasoner after the fact.
```

## bib / átomos / mapping

- **bib:** `kruse2022causal` añadida (capítulo Springer 2022); las otras 4 ya estaban (huérfanas resueltas).
- **Átomos:** ya creados (`Source_PDF_{brachman1990,lehmann1992,sowa1991,sansford2024grapheval,kruse2022causal}_pdf.md`).
- **mapping.yaml** (párrafo nuevo, p.ej. `04_discussion-p04` tras renumeración):
```yaml
   - {atom_id: atom-source-pdf-brachman1990, atom_path: Fuentes/Source_PDF_brachman1990_pdf.md, bridge: bib, score: 1.0, detail: "[@brachman1990] KL-ONE"}
   - {atom_id: atom-source-pdf-lehmann1992, atom_path: Fuentes/Source_PDF_lehmann1992_pdf.md, bridge: bib, score: 1.0, detail: "[@lehmann1992] CLASSIC"}
   - {atom_id: atom-source-pdf-sowa1991, atom_path: Fuentes/Source_PDF_sowa1991_pdf.md, bridge: bib, score: 1.0, detail: "[@sowa1991] conceptual graphs"}
   - {atom_id: atom-source-pdf-sansford2024grapheval, atom_path: Fuentes/Source_PDF_sansford2024grapheval_pdf.md, bridge: bib, score: 1.0, detail: "[@sansford2024grapheval]"}
   - {atom_id: atom-matrix-vs-rag, atom_path: Computacion/Optimizacion_y_Seguridad/Matrix_vs_RAG.md, bridge: delta6_review, score: 0.9, detail: "coocurrencia sin caminos lógicos"}
   - {atom_id: atom-eje-d-diferenciacion-owl-kgs-y-vectorizacion-bitwise, atom_path: Computacion/Bitwise_Hardware/Eje_D_Diferenciacion_OWL_KGs_y_Vectorizacion_Bitwise.md, bridge: delta6_review, score: 0.9, detail: "KG sin categoría Unsinnig"}
   - {atom_id: atom-emergencia-estructural-de-si-en-cruces-de-contexto, atom_path: Computacion/Estructuras_Matriciales/Emergencia_Estructural_de_Si_en_Cruces_de_Contexto.md, bridge: delta6_review, score: 0.85, detail: "Unsinnig como categoría estructural"}
   - {atom_id: atom-demostracion-ontologias-owl-semantic-web, atom_path: Aplicaciones/Demostracion_Ontologias_OWL_Semantic_Web.md, bridge: delta6_review, score: 0.8, detail: "OWL como ingesta/vecino cercano"}
```

- **mapping.yaml** (añadir a la lista del párrafo): `{atom_id: atom-source-pdf-kruse2022causal, atom_path: Fuentes/Source_PDF_kruse2022causal_pdf.md, bridge: bib, score: 1.0, detail: "[@kruse2022causal] causal networks"}`

## Riesgos
- Renumeración de anchors en `04_discussion` (p04+ se desplazan): re-mapear por contenido.
- `kruse2022causal` ya está en bib + átomo creado (cap. "Causal Networks", Kruse et al., *Computational Intelligence*, Springer 2022, pp. 617-625).
