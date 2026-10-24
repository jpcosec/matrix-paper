# Apéndice

## Sobre el origen geométrico de las alucinaciones \label{app:hallucinations}

Para comprender por qué los espacios semánticos continuos tienen dificultades con la exactitud factual, podemos examinar cómo la literatura asocia las alucinaciones con sus orígenes geométricos en el espacio de embeddings $\mathbb{R}^d$. Marcos de evaluación recientes clasifican los errores estructurales de generación en tres tipos geométricos según su comportamiento espacial dentro de subvariedades semánticas [@wei2024measuring; @sansford2024grapheval]:

**Tipo I: Infidelidad (desviación contextual)**
Ocurre cuando la generación se aparta del contexto provisto o del canal semántico requerido. Geométricamente, el vector de salida se aleja de la subvariedad objetivo. Dado que esto representa una desviación espacial significativa, los errores de Tipo I son fácilmente detectables mediante métricas de distancia continua estándar (p. ej., distancia coseno) o mediciones de entropía, con un AUROC típicamente $> 0.80$ [@wei2024measuring].

**Tipo II: Confabulación (incongruencia de dominio)**
Sucede cuando el modelo alucina un tema completamente ajeno o una afirmación extravagante. Geométricamente, estas salidas caen muy fuera de la distribución esperada. Al igual que los errores de Tipo I, los de Tipo II se señalan con facilidad como anomalías fuera de distribución mediante métricas continuas (AUROC $> 0.75$).

**Tipo III: Error factual (falsedad dentro del canal)**
Este es el error más pernicioso: el modelo genera un hecho incorrecto permaneciendo perfectamente dentro del marco conceptual correcto. Como las verdades y falsedades semánticamente relacionadas comparten la misma vecindad geométrica, los errores de Tipo III residen *dentro* del canal típico de la representación. Como demuestran Wei et al., la discriminación lineal de estos errores dentro del canal se desempeña cerca del azar (AUROC $\approx 0.478$) [@wei2024measuring]. 

La detectabilidad geométrica de los Tipos I y II suele crear la "Ilusión de Autocorrección" [@symcode2025] —la creencia de que escalar los modelos o contar con un mejor monitoreo continuo acabará resolviendo todas las alucinaciones—. Sin embargo, la barrera del AUROC en los errores de Tipo III demuestra un límite estructural de los paradigmas espaciales actuales: la distancia continua codifica la coocurrencia estadística, no la verdad factual. Por lo tanto, resolver los errores de Tipo III exige salir del paradigma espacial continuo e introducir un paso de verificación discreto.

## Sobre los límites de la aproximación continua \label{app:continuous}

Este apéndice detalla las tres observaciones de la Sección 2. Las dos primeras establecen límites matemáticos ineludibles al emplear funciones continuas y arquitecturas de ancho acotado para aproximar lógica discreta. La tercera observación destaca una falla empírica específica de las metodologías de embeddings actuales, y no un resultado de imposibilidad absoluta para las redes neuronales.

### Fronteras de indicador y oscilación ineludible

Sea $f: \mathbb{R}^d \to \{0,1\}$ un indicador de validez lógica, discontinuo en la frontera de su soporte. Los resultados de aproximación universal [@hornik1991approximation] garantizan convergencia en $L^1$ / en medida: la *masa* de la región de error puede hacerse arbitrariamente pequeña. Sin embargo, la convergencia no es uniforme: cerca de un salto, cualquier aproximador suave o suave por tramos exhibe una banda de transición con sobreimpulso —el fenómeno de Gibbs, cuyo sobreimpulso clásico es $\approx 8.95\%$ de la magnitud del salto—. Estrechar la banda requiere activaciones más empinadas y más unidades, pero la banda no desaparece con más datos ni más entrenamiento; es una propiedad matemática fundamental de aproximar un salto con funciones continuas. En términos semánticos, este límite ineludible significa que siempre existe una región donde el *Unsinn* recibe un puntaje intermedio en lugar de una exclusión estricta.

### Teselación por politopos con ancho acotado

Una red ReLU es afín por tramos: la frontera de activación de cada neurona es un hiperplano, y su disposición particiona $\mathbb{R}^d$ en politopos convexos sobre los cuales la red es lineal. Para un ancho $w \le d$ y una profundidad $L$, el número de regiones está acotado por

$$\mathcal{N}(w, L) \le \sum_{j=0}^{d} \binom{wL}{j},$$

que crece polinomialmente en $L$ [@hanin2017universal]. Las fronteras del sentido, en cambio, son típicamente no convexas y disconexas: las restricciones de tipo sobre los símbolos se combinan de manera combinatoria, de modo que el conjunto de proposiciones _sinnvoll_ se dispersa en numerosas regiones disconexas. Teselar un conjunto así con celdas convexas requiere un número de regiones exponencial en el número de restricciones. Si bien redes no acotadas podrían en teoría escapar de este límite, toda red de ancho acotado sufre inevitablemente un déficit estructural. Esto fuerza ineludiblemente interferencia lógica en las fronteras categoriales, lo que lo convierte en un límite absoluto dentro de las restricciones arquitectónicas prácticas.

### La frontera blanda de las técnicas actuales de embeddings

Si los errores factuales fueran valores atípicos en el espacio de embeddings, la detección a posteriori sería sencilla. Sin embargo, los estudios de sondeo encuentran que los errores factuales —hechos incorrectos dentro del marco conceptual correcto— residen dentro del canal típico de la representación. Aquí, la discriminación lineal se desempeña cerca del azar (AUROC $\approx 0.478$) [@wei2024measuring]. A diferencia de los dos primeros límites matemáticos, este representa una frontera blanda de las metodologías espaciales actuales: las métricas de distancia en espacios de embeddings codifican coocurrencia estadística, no correspondencia factual. Como las verdades y falsedades semánticamente relacionadas comparten la misma vecindad geométrica, las lecturas escalares continuas actuales no logran separar de manera confiable las generaciones válidas de las inválidas, lo que motiva una verificación que viva fuera del sustrato continuo.

### Sobre la decodificación determinista

`argmax` es una función determinista de la superficie de puntajes: dondequiera que la superficie esté distorsionada, la decodificación es errónea de forma *reproducible*, sin aleatoriedad de muestreo a la cual culpar. Esto opera en ambos sentidos: la decodificación estocástica tampoco es la culpable; ambas heredan el sustrato. La conclusión de diseño es que la frontera debe imponerse *antes* de la decodificación, en tiempo de compilación, donde una matriz booleana almacenada $S_i$ proporciona una verificación exacta en $O(1)$ por paso, en lugar de una aproximada distribuida a lo largo de la red.

## Representaciones cerradas, omnirrepresentación y la vía operativa \label{app:repr}

### Esqueleto formal: la forma lógica como matriz

En la lectura tractariana que estructura nuestro sustrato, la forma lógica —"la posibilidad de la estructura" (2.033)— se instancia como la matriz de sintaxis $S_i$: un operador de adyacencia sobre la capa de objetos $V_i$ que restringe qué combinaciones son estructuralmente posibles *antes* de toda evaluación de verdad, $\text{PossibleStructure} = \sigma(V_i \times S_i)$. Los hechos atómicos son minitérminos —conjunciones booleanas exhaustivas sobre las variables base—, almacenados operativamente como tuplas (concepto, dimensión, valor discriminativo), p. ej., `(lettuce, edible_part, leaf)`, de modo que el mundo es la región tensorial de los minitérminos activos. Una proposición tiene *sentido* (Sinn) si y solo si particiona adecuadamente el espacio de minitérminos (ni la tautología de todos unos ni la contradicción de todos ceros; esas son *sinnlos*, carentes de sentido); es *unsinnig* cuando cae por completo fuera del espacio generado por $S_i$ —una violación de tipo, rechazada en compilación, no una falsedad—. La Figura~\ref{fig:signsymbol} ilustra la periferia signo/símbolo (\S2) y el índice semántico $L_i(C_i,R_i)$ que asigna coordenadas enteras; las dos capas booleanas $S_i$, $V_i$ y su producto consultable corresponden a la Figura~\ref{fig:layers} (\S1).

![De los signos a las coordenadas. Signos perceptibles —la palabra *perro*, la palabra *dog*, un pictograma de perro— convergen, a través de la etapa de descomposición (resolución signo$\to$símbolo y plegado de alias), en un único símbolo: una posición en el espacio lógico, independiente del idioma. El índice semántico $L_i(C_i,R_i)$ fija entonces su coordenada entera sobre un eje de la grilla de contextos. El sistema calcula sobre coordenadas, nunca sobre signos. \label{fig:signsymbol}](../figures/fig_sign_symbol.pdf){width=55%}

### Representaciones cerradas

Un contexto $w_i$ es *cerrado* cuando sus ejes están tipados localmente: los objetos de cada eje pertenecen al mismo tipo local y las reglas del contexto abarcan únicamente sus propios símbolos. Dentro de un contexto cerrado, $S_i$ es casi trivial —casi todas las coordenadas son admisibles, y la pregunta real es factual ($V_i \in \{\text{true}, \text{false}, \emptyset\}$)—. La estructura de sentido se vuelve necesaria precisamente cuando los contextos se *cruzan*: objetos de un dominio con propiedades de otro. Los cruces se dividen entonces en tres clases: *sinnvoll* (admisible), *don't care* (fuera del subcontexto, no evaluado) y *unsinnig* (viola la estructura categorial). Una capa de tipos $T_i$ valida que las firmas relacionales se alineen antes de permitir cualquier composición $W_1 \otimes p \otimes W_2$, de modo que $S_i=0$ no puede surgir por una incongruencia accidental de contextos: es estructuralmente emergente y, por lo tanto, derivable de los esquemas en lugar de enumerarse a mano.

### La omnirrepresentación

La composición se realiza en una única matriz por bloques, la *omnirrepresentación*, dispuesta en cuatro cuadrantes: el cuadrante superior izquierdo $m \times m$ ($WC_i$) enruta y activa contextos; los cuadrantes superior derecho e inferior izquierdo, de $m \times n$, contienen bloques de pertenencia *don't care* que enrutan qué hechos pertenecen a qué contexto —este enrutamiento *es* la máscara de sentido a nivel de composición—; y el cuadrante inferior derecho $n \times n$ contiene la matriz de verdad empírica. Globalmente, el conocimiento existe como un único hipertensor canónico $N \times |R| \times N$; operativamente se materializa como un grafo de submatrices 2D densas extraídas mediante proyección tensorial, alternando entre la vista empírica plana ($V_i, S_i$) y la vista tensorial jerárquica en la que los atributos globales se promueven a hiperdimensiones de enrutamiento. Esta forma aporta la flexibilidad de la que el motor interno de "matriz pura" carece deliberadamente: $S_i$ puede aplicarse sobre *uniones de contextos* activando varias entradas de enrutamiento; toda la estructura es una vista plana e ingerible que un modelo estocástico puede leer y escribir (interfaz de E/S masiva para LLM); y cualquier cómputo externo —los hechos candidatos de un LLM, un cálculo matricial sobre embeddings— puede verificarse contra los mismos bloques sin conversión de formato.

### Vía operativa de ingesta \label{app:ingestion}

Del lenguaje natural a una proposición auditada, en cuatro etapas:

1. **Descomposición a forma estándar.** El enunciado se descompone en su significado más el azúcar sintáctico, y el significado se expresa en una representación estandarizada: S-expresiones, RDF/Turtle u OWL. Proponemos LLM pequeños como descomponedores de superficie: absorben la variabilidad de los signos (incluida la resolución de signo a símbolo y el plegado de alias) pero no toman decisiones lógicas.
2. **Reducción a proposiciones candidatas.** La forma estándar se reduce a proposiciones candidatas homogéneas `(R a b)` —p. ej., `(sound dog barks)`, `(sound cat meows)`—. Aquí aún no se afirma nada; las candidatas no tienen estatus de verdad.
3. **Verificación de sentido en dos pasos.** (a) *Indexación de contexto:* la candidata se enruta al o los contextos que indexan su cruce; si ningún contexto admite la combinación (dominio, relación), la candidata se rechaza como *Unsinnig*: el absurdo se evita por construcción, antes de cualquier evaluación de verdad. (b) *Verificación de contradicción:* las candidatas admisibles se contrastan con los hechos existentes $V_i$ de su contexto; un conflicto con lo ya afirmado produce una señal explícita de contradicción en lugar de una sobrescritura silenciosa.
4. **Cómputo matricial.** Solo las candidatas que superan ambas verificaciones actualizan o consultan $V_i$; la inferencia procede por multiplicación matricial booleana y colapso dimensional bit a bit, produciendo $W_i^{*} = V_i \odot S_i$.

*Ejemplo resuelto.* *"La parte comestible de la lechuga es la hoja"* se descompone y se reduce a la candidata `(edible_part lettuce leaf)`. La indexación de contexto la enruta al contexto de alimentos, que admite el cruce (3a se cumple); no existe en $V_i$ ningún hecho conflictivo (3b se cumple); la tupla se afirma y participa en la clausura. En contraste, `(has_color electron red)` falla el paso 3a en cualquier contexto cerrado de entidades físicas —el cruce (partícula, color) viola la estructura categorial— y se rechaza como *unsinnig* antes de que pueda asignársele un valor de verdad. Finalmente, `(sound cat barks)`, presentada después de haberse afirmado `(sound cat meows)`, supera 3a (el cruce es admisible) pero falla 3b: el sistema informa una contradicción explícita en lugar de sobrescribir silenciosamente el hecho anterior.

### Autooptimización: minimización de $E(R)$ y el tensor jerárquico \label{app:er}

La construcción no es manual $\mathcal{O}(N^2)$, y un índice puramente diagonal es demostrablemente subóptimo, pues colapsa asintóticamente a $E(R) \to 0.5$. Dos mecanismos deterministas mantienen compacto el sustrato:

- **Minimización de energía de información.** El motor puntúa cada espacio lógico con $E(R) = \frac{1}{4}(c + i + o + d)$ —densidad de sentido, facticidad, tasa de hechos observados y poder discriminativo— y aplica mutaciones solo cuando $\Delta E(R) > 0$: las columnas constantes (tautológicas) se promueven a compuertas tensoriales, los contextos cuya densidad de sentido decae se dividen en subcontextos limpios, y las colisiones en $W_i \otimes W_i^{T} - \mathbb{I}$ desencadenan la inyección de una dimensión separadora mínima. Esto es un análogo determinista del entrenamiento, ejecutado como mantenimiento tras una ingesta masiva.
- **Construcción jerárquica del tensor.** Un atributo común (p. ej., `is_vegetal`) se convierte en una dimensión de partición $C_k$; las entidades se factorizan en subtensores hijos vinculados mediante proyecciones de enrutamiento $WC_k$, y las consultas de múltiples saltos navegan $P = WC_1 \otimes \dots \otimes WC_k$, reduciendo la complejidad espacial hacia $\mathcal{O}(N \log N)$.

### Integración de la máscara de sentido con modelos estocásticos \label{app:mask}

La máscara interviene en dos niveles. *En tiempo de ejecución*, el motor rechaza de manera determinista en tres puntos de control —`ingest`, `check`, `assert`—: una proposición con $S_i = 0$ nunca ingresa al sistema veritativo, y quien invoca recibe una señal explícita `reject (unsinnig)`; la generación cuyas continuaciones fallan todas se detiene y se informa como no respondible en el contexto. *Dentro de un Transformer* (integración propuesta), la máscara se inyecta aditivamente en la atención,

$$\text{Attention}(Q, K, V) = \text{Softmax}\Big(\frac{QK^T}{\sqrt{d_k}} + \mathbf{M}_{S_i}\Big) V,$$

con $\mathbf{M}_{S_i} = -\infty$ en las posiciones con $S_i = 0$, actuando como una pérdida lógica que modula los gradientes durante el aprendizaje por refuerzo. Una variante en tiempo de decodificación restringe el soporte de muestreo a las continuaciones cuya proposición reducida supera la verificación de sentido. La integración a nivel de atención es una propuesta, no un resultado validado: aún no hemos entrenado con ella, y la planteamos como el punto concreto de integración para trabajos futuros.