# Delta 4 — Representación cerrada, omnirrepresentación, pipeline, escalabilidad E(R) y máscara $S_i$ (documento largo → anexo)

**Responde a:** Ejes B y C (`FJpU`, `ZHLy`, `ppL8` escalabilidad).
**Decisión del autor:** pipeline y máscara no tienen sentido sin introducir antes la **representación cerrada** y la **omnirrepresentación** → documento único directo a anexos. Reemplaza los antiguos deltas 4 y 5.
**v2 (tras lectura profunda de átomos):** corrige 3 desalineamientos con el KB — (1) el orden real del pipeline es **grounding → parseo/frames → forma canónica → validación $S_i$ → cómputo $V_i$**; (2) la respuesta de escalabilidad es el algoritmo $E(R)$ + tensor jerárquico, no solo "parsing masivo"; (3) la máscara es **inyección aditiva en atención** ($-\infty$) + **rechazo determinista en 3 checkpoints** (ingest/check/assert) — sí hay interrupción.

## DESDE (átomos KB origen)

| Átomo | Aporta |
|---|---|
| `Isomorfismo_Tractatus_Algebra/04_Forma_Logica_como_Matriz_Si.md` | $S_i$ = forma lógica; $Estructura\_Posible = \sigma(V_i \times S_i)$ |
| `Isomorfismo_Tractatus_Algebra/05_Sentido_Sinn_como_Region_Tensorial.md` | Sinn = partición propia de mintermos (ni tautología ni contradicción) |
| `Isomorfismo_Tractatus_Algebra/06_Absurdo_Unsinnig_como_Violacion_Sintactica.md` | $P_{unsinnig} \notin Span(S_i)$; distinción Sinnlos/Unsinnig |
| `Isomorfismo_Tractatus_Algebra/01_El_Mundo_como_Espacio_Tensor.md` + `02_Hecho_Atomico_como_Mintermo.md` | Backbone mintermos: $\Omega = \sum m_k$ |
| `Computacion/Estructuras_Matriciales/Emergencia_Estructural_de_Si_en_Cruces_de_Contexto.md` | $S_i$ casi trivial en contexto cerrado; 3 clases al cruzar (Sinnvoll / don't care / Unsinnig) |
| `Computacion/Optimizacion_y_Seguridad/Sistema_Tipos_Ti.md` | Validación de firma relacional **antes** de componer contextos ($W_1 \otimes p \otimes W_2$) |
| `Computacion/Optimizacion_y_Seguridad/Omnirepresentacion.md` + `Computacion/Estructuras_Matriciales/Enrutamiento_Jerarquico.md` | Block matrix: diagonal $WC_i$ + cruces + verdad |
| `Matematica/Tensores_y_Matriz_Bloques/Matriz_por_Bloques.md` | Estructura formal de 4 cuadrantes (base de la omnirrepresentación) |
| `Matematica/Tensores_y_Matriz_Bloques/Dualidad_del_Hipertensor.md` + `Proyeccion_Tensorial.md` + `Representacion_Plana_vs_Tensorial.md` | Dualidad: hipertensor canónico $N\times|R|\times N$ ⇔ grafo de sub-matrices densas proyectadas |
| `Matematica/Tensores_y_Matriz_Bloques/Hecho_Atomico_CDV.md` | Hecho atómico = tupla (Concepto, Dimensión, Valor); ejemplo canónico lechuga |
| `Matematica/Tensores_y_Matriz_Bloques/Teorema_Suboptimizabilidad_Diagonal.md` | Índice diagonal colapsa a $E(R)\to0.5$ → motiva la auto-optimización |
| `Computacion/Optimizacion_y_Seguridad/Eje_B_Escalabilidad_Minimizacion_ER_y_Tensor_Jerarquico.md` | Respuesta de escalabilidad: $E(R)$ + tensor $N\log N$ |
| `Computacion/Optimizacion_y_Seguridad/Algoritmo_Minimizacion_ER.md` | $E(R)=\frac14(c+i+o+d)$; poda tautologías, escisión, inyección; aceptar si $\Delta E>0$ |
| `Computacion/Estructuras_Matriciales/Construccion_Tensor_Jerarquico.md` | Dimensión de partición $C_k$, ruteo $WC_i$, multihop $\bigotimes WC_k$ |
| `Matematica/Optimizacion_y_Desambiguacion/Colapso_Dimensional.md` | Colapso bitwise (etapa 5 de Eje B) |
| `Computacion/Parsers_y_Runtimes/Pipeline_Ingesta_Lenguaje_Matrix.md` + `Walkthrough_Pipeline_con_Ejemplo.md` + `S_Expressions.md` + `Parser_OWL2Matrix.md` + `RuleMatrixCompiler.md` + `Anclaje_Simbolos_Grounding.md` | Pipeline oficial de 4 etapas (descomposición → candidatos → chequeo de sentido en dos pasos → cómputo) |
| `Filosofia/Tractatus_y_Ontologia/Signo_vs_Simbolo.md` + `Computacion/Estructuras_Matriciales/LogicalSpace_Li.md` + `Context_Ci.md` + `Relation_Ri.md` | Fig. `fig:signsymbol` (anexo): signo→símbolo→coordenada $L_i$; $W_i=(C_i,R_i)$ |
| `Computacion/Estructuras_Matriciales/Capa_Sentido_Si.md` + `Capa_Verdad_Vi.md` + `W_Operativo.md` + `WiGame_Wi.md` | Fig. `fig:layers` (§1): capas $S_i$, $V_i$, producto $W_i=V_i\odot S_i$ |
| `Computacion/Optimizacion_y_Seguridad/Mascara_Sentido_en_Mecanismos_Atencion.md` | $\text{Softmax}(QK^T/\sqrt{d_k} + \mathbf{M}_{S_i})V$, penalización $-\infty$, loss lógica en RL |
| `Computacion/Parsers_y_Runtimes/Interrupcion_Decodificacion_Si_Cero.md` | Rechazo determinista en 3 checkpoints vía `wigame.accepts()` |
| `Computacion/Parsers_y_Runtimes/Integracion_LLM_en_Training_e_Inferencia_Aun_No_Demostrada.md` | Delimitación honesta |

## DESDE+ ampliación KB (referencias adicionales, por subsección del anexo)

**Backbone formal (álgebra booleana canónica):**

| Átomo | Aporte |
|---|---|
| `Matematica/Algebra_Booleana_y_Canonica/Algebra_de_Boole.md` + `Axiomas_Huntington.md` + `Semianillo_Booleano.md` | Base algebraica del cálculo $\{0,1\}$ |
| `Matematica/Algebra_Booleana_y_Canonica/Mintermo.md` + `Formas_Canonicas_y_Mintermos.md` + `Suma_de_Productos_SOP.md` + `Tabla_de_Verdad.md` + `Maxtermo.md` | Minterms/formas canónicas: soporte formal del backbone |
| `Matematica/Algebra_Booleana_y_Silicio/Multiplicacion_Matricial_Booleana_y_Clausura_Transitiva.md` | Multiplicación booleana = mecanismo de clausura/inferencia |
| `Matematica/Algebra_Booleana_y_Silicio/Regla_Dont_Care.md` | Don't cares: fundamento de los bloques cruzados |
| `Matematica/Algebra_Booleana_y_Silicio/Medida_y_Semianillos_Booleanos_vs_Probabilistas.md` | Por qué semianillo booleano y no probabilidad |
| `Matematica/Gramatica_y_Sentido/Alfabeto_Sigma.md` + `Gramatica_Formal.md` + `Reglas_de_Produccion_Sintactica.md` | Unsinnig como violación sintáctica (gramática formal) |
| `Filosofia/Tractatus_y_Ontologia/Triparticion_Wittgensteiniana_Sinnvoll_Sinnlos_Unsinnig.md` + `Categorias_Sentido.md` + `Fundamento_Logico_aRb.md` + `Tractatus.md` | Tripartición TLP y fundamento $aRb$ |

**Representación cerrada / contextos:**

| Átomo | Aporte |
|---|---|
| `Computacion/Estructuras_Matriciales/Context_Ci.md` + `LogicalSpace_Li.md` + `Relation_Ri.md` + `WiGame_Wi.md` + `W_Operativo.md` | Primitivas: contexto, espacio lógico, relación, WiGame |
| `Computacion/Estructuras_Matriciales/Capa_Sentido_Si.md` + `Capa_Verdad_Vi.md` + `Distincion_Ausencia_vs_Unsinnig.md` | Capas $S_i$/$V_i$ y tres estados |
| `Matematica/Teoria_de_Reticulos_Contextuales/Poset_Conjunto_Parcialmente_Ordenado.md` + `Reticulo_Matematico_Lattice.md` + `Supremo_e_Infimo.md` | Retículo de contextos (sub/super-contexto) |
| `Filosofia/Epistemologia_y_Contextos/Estados_Verdad_Epistemicos_Semanticos.md` + `Triparticion_Contextual.md` | Separación semántico/epistémico/veritativo |
| `Filosofia/Tractatus_y_Ontologia/Signo_vs_Simbolo.md` | Signo vs símbolo (grounding) |

**Omnirrepresentación:**

| Átomo | Aporte |
|---|---|
| `Computacion/Estructuras_Matriciales/Mascaras_Estructurales.md` + `Matrices_Puras.md` + `Ruteo_Como_Relacion.md` + `Grafo_Indice_G.md` + `Evolucion_y_Versionado_Contextos.md` | Máscaras estructurales, matrices puras, ruteo, índice |
| `Computacion/Modelos_Datos_MEEL/Hipertensor_Canonico.md` + `WiGame.md` + `Fact.md` + `Proposition.md` + `Symbol.md` + `Thing.md` + `Relation.md` + `LogicalSystem.md` | Modelo de datos MEEL (8 primitivas) |
| `Teoria_de_Bases_de_Datos/02_query_como_proyeccion_tensorial.md` + `04_vista_materializada_clausura.md` + `01_indice_como_coordenada.md` | Omnirrepresentación como vista materializada; query = proyección |

**Pipeline de ingesta:**

| Átomo | Aporte |
|---|---|
| `Computacion/Optimizacion_y_Seguridad/Gramatica_Universal_UNL.md` | **Sí existe átomo dedicado UNL** (etapa 2) |
| `Computacion/Parsers_y_Runtimes/OWLFeeder.md` + `SExprFeeder.md` + `AtomFeeder.md` + `MatrixFeeder.md` + `S_Expressions.md` | Feeders y runtime S-expr |
| `Computacion/Parsers_y_Runtimes/Eje_C_Mecanismo_Conexion_LLM_y_SHRDLU.md` + `Integracion_Teorica_con_LLMs_y_Trabajo_Futuro.md` + `Prototipo_SHRDLU.md` | Mecanismo de conexión LLM (Eje C) |
| `Computacion/Kernel_MEEL/MEEL.md` + `Operaciones_MEEL.md` + `Clausura_Transitiva_Matricial.md` + `Inferencia_Deductiva_Matricial.md` + `Compilador_Matricial_Reglas.md` | Kernel: clausura, deducción, compilador |
| `Computacion/Operaciones_DB_Logica/Operacion_Deducir.md` + `Operacion_Auditar_Consistencia.md` + `Operacion_Contrafactual.md` + `Operacion_Validar_Formulacion.md` + `Operacion_Identificar_Faltantes.md` + `Operacion_Justificar.md` | API de operaciones del anexo |
| `Computacion/Bitwise_Hardware/Vectorizacion_Bitwise_Densa.md` + `Diccionario_Bits_y_Codificacion.md` + `Tipado_Typestate.md` | Colapso dimensional bitwise en silicio |
| `Aplicaciones/Demostracion_Ontologias_OWL_Semantic_Web.md` + `Demostracion_Mundo_Bloques_SHRDLU.md` + `Demostracion_Compilacion_Reglas_y_Modus_Ponens.md` + `Dominio_Culinario/Demostracion_Dominio_Culinario_Ragout.md` | Demostraciones ejecutables (walkthrough) |

**E(R) y escalabilidad:**

| Átomo | Aporte |
|---|---|
| `Computacion/Optimizacion_y_Seguridad/Energia_Informacion.md` | **Átomo dedicado de $E(R)$** (definición formal) |
| `Computacion/Estructuras_Matriciales/Optimizador_de_Contextos.md` + `Tensor_Jerarquico_NxNxC.md` | Optimizador y tensor $N\times N\times C$ |
| `Matematica/Optimizacion_y_Desambiguacion/Funcion_Objetivo_Seleccion_Dimensiones.md` + `Expansion_Submatricial_Recursiva.md` + `Juego_de_Desambiguacion.md` | Selección de dimensiones, expansión recursiva |
| `Computacion/Optimizacion_y_Seguridad/Manejo_de_Contradicciones.md` + `Reduccion_Descriptiva.md` + `Seguridad_Pseudo_Proposicional.md` + `Representacion_AST_y_Algebra_Booleana.md` | Contradicciones, reducción descriptiva, seguridad |

**Máscara / acoplamiento:**

| Átomo | Aporte |
|---|---|
| `Matematica/Optimizacion_y_Desambiguacion/Fenomeno_de_Gibbs_en_Funciones_Indicadoras.md` | Gibbs: por qué el margen $-\infty$ y no pesos blandos |
| `Antecedentes/Limites_Espacio_Continuo/Ausencia_de_Senal_de_Fallo_Determinista.md` | El LLM por sí solo no emite señal de fallo |
| `Fuentes/Source_Code_src_operational_model_language_s_expressions_py.md` + `.../matrices_si_matrix_py.md` + `.../matrices_vi_matrix_py.md` + `.../matrices_block_matrix_py.md` + `.../optimization_information_energy_py.md` + `.../optimization_dimensional_collapse_py.md` + `.../language_owl2matrix_py.md` + `.../engine_meel_engine_py.md` + `.../game_wi_game_py.md` + `.../inference_transitive_closure_py.md` + `.../inference_propositional_inference_py.md` + `.../hardware_bool_mult_py.md` | Proveniencia de código: cada afirmación del anexo tiene módulo |

**Extensión mapping (bridge `delta4_review`, añadir a las listas existentes):**
- Backbone formal: `Mintermo` (0.9), `Formas_Canonicas_y_Mintermos` (0.9), `Algebra_de_Boole` (0.85), `Semianillo_Booleano` (0.85), `Suma_de_Productos_SOP` (0.8), `Tabla_de_Verdad` (0.8), `Axiomas_Huntington` (0.75), `Maxtermo` (0.7), `Multiplicacion_Matricial_Booleana_y_Clausura_Transitiva` (0.9), `Regla_Dont_Care` (0.85), `Medida_y_Semianillos_Booleanos_vs_Probabilistas` (0.8), `Alfabeto_Sigma`/`Gramatica_Formal`/`Reglas_de_Produccion_Sintactica` (0.8), `Triparticion_Wittgensteiniana` (0.9), `Categorias_Sentido` (0.85), `Fundamento_Logico_aRb` (0.85), `Tractatus` (0.75).
- Repr. cerrada: `Context_Ci` (0.85), `LogicalSpace_Li` (0.85), `Relation_Ri` (0.8), `WiGame_Wi` (0.85), `W_Operativo` (0.8), `Capa_Sentido_Si` (0.9), `Capa_Verdad_Vi` (0.9), `Distincion_Ausencia_vs_Unsinnig` (0.85), `Poset` (0.75), `Reticulo_Matematico_Lattice` (0.8), `Supremo_e_Infimo` (0.7), `Estados_Verdad_Epistemicos_Semanticos` (0.85), `Triparticion_Contextual` (0.75), `Signo_vs_Simbolo` (0.85).
- Omnirrepresentación: `Mascaras_Estructurales` (0.8), `Matrices_Puras` (0.8), `Ruteo_Como_Relacion` (0.8), `Grafo_Indice_G` (0.75), `Evolucion_y_Versionado_Contextos` (0.7), `Hipertensor_Canonico` (0.85), `Fact`/`Proposition`/`Symbol`/`Thing`/`Relation`/`WiGame`/`LogicalSystem` (0.75), `02_query_como_proyeccion_tensorial` (0.85), `04_vista_materializada_clausura` (0.85), `01_indice_como_coordenada` (0.75).
- Pipeline: `Gramatica_Universal_UNL` (0.9), `OWLFeeder`/`SExprFeeder`/`AtomFeeder`/`MatrixFeeder` (0.8), `Eje_C_Mecanismo_Conexion_LLM_y_SHRDLU` (0.85), `Integracion_Teorica_con_LLMs_y_Trabajo_Futuro` (0.8), `Prototipo_SHRDLU` (0.7), `MEEL` (0.85), `Operaciones_MEEL` (0.8), `Clausura_Transitiva_Matricial` (0.9), `Inferencia_Deductiva_Matricial` (0.85), `Compilador_Matricial_Reglas` (0.85), `Operacion_Deducir`/`Auditar_Consistencia`/`Contrafactual`/`Validar_Formulacion`/`Identificar_Faltantes`/`Justificar` (0.8), `Vectorizacion_Bitwise_Densa` (0.85), `Diccionario_Bits_y_Codificacion` (0.75), `Tipado_Typestate` (0.75), 4 `Demostracion_*` (0.75).
- E(R): `Energia_Informacion` (0.95), `Optimizador_de_Contextos` (0.85), `Tensor_Jerarquico_NxNxC` (0.85), `Funcion_Objetivo_Seleccion_Dimensiones` (0.8), `Expansion_Submatricial_Recursiva` (0.75), `Juego_de_Desambiguacion` (0.7), `Manejo_de_Contradicciones` (0.75), `Reduccion_Descriptiva` (0.7), `Seguridad_Pseudo_Proposicional` (0.7), `Representacion_AST_y_Algebra_Booleana` (0.7).
- Máscara: `Fenomeno_de_Gibbs_en_Funciones_Indicadoras` (0.85), `Ausencia_de_Senal_de_Fallo_Determinista` (0.8), 12 `Fuentes/Source_Code_*` (0.8).

## HACIA (destino)

1. **Anexo (principal):** sección completa nueva en `Neurips_peiper/sections/10_appendix.md` (compartido con delta 1; el primero que se aplique crea el archivo con `# Appendix` + registro en `paper/paper.yaml`).
2. **Cuerpo (mínimo, 2 frases):** puntero en `04_discussion.md`, **antes del encabezado `# Relationship with LLM`**:

```markdown
Two design notions make this operational at scale: *closed representations*, within which sense is near-trivial and violations emerge only at structurally inadmissible context crossings, and the *omnirepresentation*, a block-matrix form exposing contexts, routing and facts jointly to stochastic models. The formal construction, the ingestion pathway, the self-optimization algorithm and the sense-mask integration are given in Appendix~\ref{app:repr}.
```

## Propuesta de texto (anexo completo)

```markdown
## Closed Representations, Omnirepresentation, and the Operational Pathway {#app:repr}

### Formal backbone: logical form as a matrix

In the Tractarian reading that structures our substrate, logical form—"the possibility of structure" (2.033)—is instantiated as the syntax matrix $S_i$: an adjacency operator over the object layer $V_i$ that restricts which combinations are structurally possible *before* any truth evaluation, $\text{PossibleStructure} = \sigma(V_i \times S_i)$. Atomic facts are minterms—exhaustive boolean conjunctions over the base variables, stored operatively as (concept, dimension, discriminative value) tuples, e.g., `(lettuce, edible_part, leaf)`—so the world is the tensor region of active minterms. A proposition has *sense* (Sinn) iff it partitions minterm space properly (neither the all-ones tautology nor the all-zeros contradiction; those are *sinnlos*, senseless); it is *unsinnig* when it falls outside the span of $S_i$ altogether—a type violation, rejected at compilation, not a falsehood. Figure~\ref{fig:signsymbol} pictures the sign/symbol periphery (\S2) and the semantic index $L_i(C_i,R_i)$ that assigns integer coordinates; the two boolean layers $S_i$, $V_i$ and their queryable product are Figure~\ref{fig:layers} (\S1).

\begin{figure}[t]
\centering
\begin{tikzpicture}[font=\small]
  \node[draw=gray!70, rounded corners=2pt, inner sep=2.5pt, fill=gray!8] (s1) at (-1.7,0) {\emph{``perro''}};
  \node[draw=gray!70, rounded corners=2pt, inner sep=2.5pt, fill=gray!8] (s2) at (0,0) {\emph{``dog''}};
  \node[draw=gray!70, rounded corners=2pt, inner sep=2.5pt, fill=gray!8] (s3) at (1.7,0) {\emoji{dog}};
  \node[font=\scriptsize\itshape] at (0,0.62) {signs: pure perceptible medium};
  \node[draw, rounded corners=3pt, inner sep=4pt, align=center] (dec) at (0,-1.4) {decomposition (stage 1)\\[-1pt]{\scriptsize sign$\to$symbol resolution, alias folding}};
  \draw[-{Latex[length=2mm]}, thick] (s1.south) -- (dec.150);
  \draw[-{Latex[length=2mm]}, thick] (s2.south) -- (dec.north);
  \draw[-{Latex[length=2mm]}, thick] (s3.south) -- (dec.30);
  \node[draw, circle, inner sep=2pt, fill=purple!12, font=\small\bfseries] (sym) at (0,-3.0) {\textsc{dog}};
  \node[font=\scriptsize, anchor=west] at (0.65,-3.0) {one position in logical space};
  \draw[-{Latex[length=2mm]}, thick] (dec) -- (sym);
  \node[draw, rounded corners=3pt, inner sep=4pt, align=center, fill=teal!8] (coord) at (0,-4.35) {coordinate $(i,j)$\\[-1pt]{\scriptsize row of \emph{dog} on axis $a$}};
  \draw[-{Latex[length=2mm]}, thick] (sym) -- (coord) node[midway, right, font=\scriptsize] {$L_i(C_i,R_i)$};
  % mini grid preview (axis a)
  \foreach \r in {0,1,2,3} \foreach \c in {0,1,2} \draw[gray!60, line width=0.3pt] ({2.3+0.5*\c},{-3.9-0.5*\r}) rectangle ++(0.5,-0.5);
  \foreach \c in {0,1,2} \fill[teal!28] ({2.3+0.5*\c},-3.9) rectangle ++(0.5,-0.5);
  \foreach \c in {0,1,2} \draw[gray!60, line width=0.3pt] ({2.3+0.5*\c},-3.9) rectangle ++(0.5,-0.5);
  \foreach \r/\n in {0/dog, 1/cat, 2/cow, 3/stone} \node[font=\scriptsize, anchor=east] at (2.22,{-4.15-0.5*\r}) {\n};
  \node[font=\scriptsize, align=center] at (3.05,-6.25) {grid over $L_i$};
  \draw[purple, dashed, thick, -{Latex[length=2mm]}] (coord.east) .. controls (1.7,-4.35) .. (2.24,-4.18);
\end{tikzpicture}
\caption{From signs to coordinates. Perceptible signs---the word \emph{perro}, the word \emph{dog}, a dog pictogram---converge through the decomposition stage (sign$\to$symbol resolution and alias folding) onto a single symbol: one position in logical space, independent of language. The semantic index $L_i(C_i,R_i)$ then fixes its integer coordinate on an axis of the context grid. The system computes over coordinates, never over signs.}
\label{fig:signsymbol}
\end{figure}

### Closed representations

A context $w_i$ is *closed* when its axes are typed locally: objects on each axis belong to the same local type and the context's rules range only over its own symbols. Within a closed context $S_i$ is near-trivial—almost all coordinates are admissible, and the real question is factual ($V_i \in \{\text{true}, \text{false}, \emptyset\}$). Sense structure becomes necessary exactly when contexts are *crossed*: objects of one domain with properties of another. Crossings then fall into three classes—*sinnvoll* (admissible), *don't care* (outside the subcontext, not evaluated), and *unsinnig* (violates categorial structure). A type layer $T_i$ validates that relational signatures align before any composition $W_1 \otimes p \otimes W_2$ is allowed, so $S_i=0$ cannot arise from accidental context incongruence: it is structurally emergent, and therefore derivable from the schemas rather than hand-listed.

### The omnirepresentation

Composition is realized in a single block matrix, the *omnirepresentation*, laid out in four quadrants: the top-left $m \times m$ quadrant ($WC_i$) routes and activates contexts; the top-right and bottom-left $m \times n$ quadrants hold don't-care membership blocks routing which facts belong to which context—this routing *is* the sense mask at composition level; and the bottom-right $n \times n$ quadrant holds the empirical truth matrix. Globally, knowledge exists as one canonical hypertensor $N \times |R| \times N$; operationally it materializes as a graph of dense 2D sub-matrices extracted by tensorial projection, alternating between the flat empirical view ($V_i, S_i$) and the hierarchical tensorial view in which global attributes are promoted to routing hyperdimensions. This form provides the flexibility the internal "pure matrix" engine deliberately lacks: $S_i$ can be applied over *unions of contexts* by activating several routing entries; the whole structure is a flat, ingestible view a stochastic model can read and write (massive I/O interface for LLMs); and any external computation—an LLM's candidate facts, a matrix calculation over embeddings—can be checked against the same blocks without format conversion.

### Operational ingestion pathway {#app:ingestion}

From natural language to an audited proposition, four stages:

1. **Decomposition into standard form.** The utterance is decomposed into its meaning plus syntactic sugar, and the meaning is expressed in a standardized representation—S-expressions, RDF/Turtle, or OWL. We propose small LLMs as surface decomposers: they absorb sign variability (including sign-to-symbol resolution and alias folding) but make no logical decisions.
2. **Reduction to candidate propositions.** The standard form is lowered to homogeneous candidate propositions `(R a b)`—e.g., \texttt{(sound dog barks)}, \texttt{(sound cat meows)}. Nothing here is asserted yet; candidates have no truth status.
3. **Two-step sense check.** (a) *Context indexing:* the candidate is routed to the context(s) that index its cross; if no context admits the (domain, relation) combination, the candidate is rejected as *Unsinnig*—absurdity is avoided by construction, before any truth evaluation. (b) *Contradiction check:* admissible candidates are checked against the existing facts $V_i$ of their context; a conflict with what is already asserted yields an explicit contradiction signal rather than silent overwrite.
4. **Matrix computation.** Only candidates passing both checks update or consult $V_i$; inference proceeds by boolean matrix multiplication and bitwise dimensional collapse, yielding $W_i^{*} = V_i \odot S_i$.

Figure~\ref{fig:ingestion} summarizes the pathway; the two-step sense check is the only decision point, and it precedes any contact with the veritative store.

\begin{figure}[t]
\centering
\begin{tikzpicture}[
  font=\small,
  stage/.style={draw, rounded corners, align=center, minimum width=4.6cm, minimum height=0.9cm, fill=blue!4},
  decision/.style={draw, diamond, aspect=2.1, align=center, fill=orange!10, inner sep=1pt},
  reject/.style={draw, rounded corners, align=center, minimum width=3.4cm, fill=red!8},
  lab/.style={align=left, text width=3.6cm, font=\footnotesize, color=black!70},
  arr/.style={-{Stealth[length=2.5mm]}, thick},
  node distance=0.55cm and 1.1cm]
\node (in) {natural language};
\node[stage, below=of in] (s1) {\textbf{1. Decomposition} \\ meaning + syntactic sugar $\to$ standard form \\ {\footnotesize (S-expressions, RDF/Turtle, OWL)}};
\node[stage, below=of s1] (s2) {\textbf{2. Reduction to candidates} \\ \texttt{(sound dog barks)}, \texttt{(sound cat meows)}};
\node[decision, below=of s2] (d1) {\textbf{3a. Context indexing} \\ admissible cross? ($S_i$)};
\node[reject, right=of d1] (rej1) {\texttt{reject (unsinnig)} \\ absurdity avoided by construction};
\node[decision, below=of d1] (d2) {\textbf{3b. Contradiction check} \\ conflicts with $V_i$?};
\node[reject, right=of d2] (rej2) {\texttt{reject (contradiction)} \\ explicit signal};
\node[stage, below=of d2] (s4) {\textbf{4. Matrix computation} \\ $V_i$ update; $W_i^{*} = V_i \odot S_i$};
\node[below=of s4] (out) {inference: boolean closure, bitwise collapse};
\node[lab, right=of s1] (llm) {proposal: small LLMs as surface decomposers; sign variability only, no logical decisions};
\draw[arr] (in) -- (s1);
\draw[arr] (s1) -- (s2);
\draw[arr] (s2) -- (d1);
\draw[arr] (d1) -- node[above]{no ($S_i{=}0$)} (rej1);
\draw[arr] (d1) -- node[right]{admissible} (d2);
\draw[arr] (d2) -- node[above]{conflict} (rej2);
\draw[arr] (d2) -- node[right]{clean} (s4);
\draw[arr] (s4) -- (out);
\draw[-{Stealth[length=2.5mm]}, densely dashed, color=black!60] (llm.west) -- (s1);
\end{tikzpicture}
\caption{Ingestion pathway. Natural language is decomposed into a standardized representation and reduced to candidate propositions; a two-step sense check---context indexing, which rejects \texttt{unsinnig} crosses before any truth evaluation, and a contradiction check against $V_i$---gates all contact with the veritative store.}
\label{fig:ingestion}
\end{figure}

\paragraph{Worked example.} \emph{``The edible part of lettuce is the leaf''} is decomposed and reduced to the candidate \texttt{(edible\_part lettuce leaf)}. Context indexing routes it to the food context, which admits the cross (3a passes); no conflicting fact exists in $V_i$ (3b passes); the tuple is asserted and participates in closure. By contrast, \texttt{(has\_color electron red)} fails step 3a in any closed physical-entity context---the (particle, color) cross violates categorial structure---and is rejected as \texttt{unsinnig} before a truth value can attach. Finally, \texttt{(sound cat barks)} submitted after \texttt{(sound cat meows)} was asserted passes 3a (the cross is admissible) but fails 3b: the system reports an explicit contradiction instead of silently overwriting the earlier fact.

### Self-optimization: $E(R)$ minimization and the hierarchical tensor {#app:er}

Construction is not manual $\mathcal{O}(N^2)$—and a purely diagonal index is provably suboptimal, collapsing asymptotically to $E(R) \to 0.5$. Two deterministic mechanisms keep the substrate compact:

- **Information-energy minimization.** The engine scores each logical space with $E(R) = \frac{1}{4}(c + i + o + d)$—sense density, facticity, observed-fact rate, and discriminative power—and applies mutations only when $\Delta E(R) > 0$: constant (tautological) columns are promoted to tensor gates, contexts whose sense density drops are split into clean sub-contexts, and collisions in $W_i \otimes W_i^{T} - \mathbb{I}$ trigger injection of a minimal separating dimension. This is a deterministic analogue of training, run as maintenance after bulk ingestion.
- **Hierarchical tensor construction.** A common attribute (e.g., `is_vegetal`) becomes a partition dimension $C_k$; entities are factored into child sub-tensors linked by routing projections $WC_k$, and multi-hop queries navigate $P = WC_1 \otimes \dots \otimes WC_k$, reducing spatial complexity toward $\mathcal{O}(N \log N)$.

### Sense-mask integration with stochastic models {#app:mask}

The mask enters at two levels. *At runtime*, the engine rejects deterministically at three checkpoints—`ingest`, `check`, `assert`: a proposition with $S_i = 0$ never enters the veritative system, and the caller receives an explicit `reject (unsinnig)` signal; generation whose continuations all fail is halted and reported as unanswerable in the context. *Inside a Transformer* (proposed integration), the mask is injected additively into attention,

$$\text{Attention}(Q, K, V) = \text{Softmax}\Big(\frac{QK^T}{\sqrt{d_k}} + \mathbf{M}_{S_i}\Big) V,$$

with $\mathbf{M}_{S_i} = -\infty$ at positions with $S_i = 0$, acting as a logical loss that modulates gradients during reinforcement learning. A decode-time variant restricts the sampling support to continuations whose lowered proposition passes the sense check. The attention-level integration is a proposal, not a validated result: we have not yet trained with it, and we state it as the concrete integration point for future work.
```

## bib / átomos / mapping

- **bib:** nada. **Átomos nuevos:** ninguno.
- **mapping.yaml:**
  - Puntero cuerpo (`04_discussion`, p. nuevo): `Omnirepresentacion` (0.95), `Emergencia_Estructural_de_Si_en_Cruces_de_Contexto` (0.9), `Eje_B_Escalabilidad_Minimizacion_ER_y_Tensor_Jerarquico` (0.85) — bridge `delta4_review`.
  - `10_appendix` subsección backbone formal: `04_Forma_Logica_como_Matriz_Si` (0.95), `05_Sentido_Sinn` (0.9), `06_Absurdo_Unsinnig` (0.95), `01_El_Mundo` (0.8), `02_Hecho_Atomico` (0.8).
  - Subsección repr. cerrada: `Emergencia_Estructural_de_Si_en_Cruces_de_Contexto` (0.95), `Sistema_Tipos_Ti` (0.9), `Bootstrapping_Contextos_Cerrados_y_Poblacion_Masiva` (0.8).
  - Subsección omnirrepresentación: `Omnirepresentacion` (0.95), `Matriz_por_Bloques` (0.95), `Dualidad_del_Hipertensor` (0.9), `Proyeccion_Tensorial` (0.85), `Representacion_Plana_vs_Tensorial` (0.85), `Enrutamiento_Jerarquico` (0.8), `Acoplamiento_Neuro_Estocastico_Simbolico` (0.8).
  - Subsección backbone formal (añadir): `Hecho_Atomico_CDV` (0.85).
  - Subsección E(R) (añadir): `Teorema_Suboptimizabilidad_Diagonal` (0.9).
  - Subsección pipeline: `Pipeline_Ingesta_Lenguaje_Matrix` (0.95), `Anclaje_Simbolos_Grounding` (0.9), `S_Expressions` (0.9), `Parser_OWL2Matrix` (0.85), `RuleMatrixCompiler` (0.8), `Walkthrough_Pipeline_con_Ejemplo` (0.8), `Operacion_Assert`/`Operacion_Evaluar_Sentido`/`Operacion_Evaluar_Verdad` (0.85), `Colapso_Dimensional` (0.75).
  - Subsección E(R): `Algoritmo_Minimizacion_ER` (0.95), `Construccion_Tensor_Jerarquico` (0.9), `Eje_B_Escalabilidad_Minimizacion_ER_y_Tensor_Jerarquico` (0.95), `Filosofia/Tractatus_y_Ontologia/Principio_de_Minimalidad` (0.75).
  - Subsección máscara: `Mascara_Sentido_en_Mecanismos_Atencion` (0.95), `Interrupcion_Decodificacion_Si_Cero` (0.95), `Integracion_LLM_en_Training_e_Inferencia_Aun_No_Demostrada` (0.9).

## Riesgos
- El diagrama requiere `\usepackage{tikz}` + `\usetikzlibrary{positioning,arrows.meta,shapes.geometric}` en el preámbulo de la plantilla NeurIPS — verificar que la clase lo permite; si no, fallback: misma figura como lista numerada con flechas Unicode.
- `fig:signsymbol` además requiere `\usepackage{emoji}` + compilación con LuaLaTeX (fuente Noto Color Emoji) para el pictograma del signo; fallback pdflatex: sustituir `\emoji{dog}` por un recuadro con la palabra ``pictogram''.
- Frase de honestidad final ("not a validated result") **obligatoria**.
- "near-trivial" en repr. cerrada es fiel al átomo (`Emergencia_Estructural`: "$S_i=1$ suele ser casi trivial"); si suena débil ante reviewers, reformular como "mostly admissible by construction".
- Todas las rutas de átomos del mapping verificadas en disco (incl. `Matematica/Tensores_y_Matriz_Bloques/*` y `Matematica/Optimizacion_y_Desambiguacion/Colapso_Dimensional`).
- Depende de `10_appendix.md` compartido con delta 1.
