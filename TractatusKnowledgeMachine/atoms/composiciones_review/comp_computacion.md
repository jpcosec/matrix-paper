---
title: Qué impide que la distancia vectorial continua aproxime lógica formal — Computacion
folder: Computacion
question: ¿Qué impide que una distancia vectorial continua aproxime lógica formal?
atom_count: 4
tags:
- system:matrix
- topic:limites-continuo
- layer:computation
---

# Qué impide que la distancia vectorial continua aproxime lógica formal — Computacion

## Carpeta Revisada

`atoms/Computacion/`

## Pregunta que responde esta composición

¿Qué impide que una distancia vectorial continua aproxime lógica formal? ¿Cuáles son los mecanismos computacionales concretos que el kernel Booleano provee y que el paradigma continuo no puede replicar?

## Cadena argumentativa (átomos en orden de lectura)

1. **[[Acoplamiento_Neuro_Estocastico_Simbolico]]** — Arquitectura híbrida que desacopla la capa neuro-estocástica del kernel Booleano (MEEL). El LLM propone; MEEL verifica. La compuerta $S_i$ es binaria: no hay interpolación posible entre *Sinnvoll* y *Unsinnig*.

2. **[[Capa_Sentido_Si]]** — Máscara Booleana que colapsa a $0$ o $1$ sin gradientes intermedios. Una distancia vectorial nunca puede producir este colapso determinista — siempre deja un residuo probabilístico.

3. **[[Capa_Verdad_Vi]]** — Matriz de verdad factual $\in \{0, 1\}$, consultable como coordenada binaria directa. Reemplaza la decodificación Softmax (que maximiza verosimilitud, no verdad) por una lectura bitwise $\mathcal{O}(1)$.

4. **[[Operaciones_MEEL]]** + **[[Inferencia_Deductiva_Matricial]]** — Operaciones de deducción en semianillo Booleano ($\land, \lor, \neg$). La clausura transitiva matricial produce resultados deterministas; el espacio continuo solo puede *estimar* la transitividad vía similitud de coseno, sin garantía de completitud.

## Síntesis

Desde la capa computacional, lo que impide la aproximación continua de la lógica es la naturaleza de las operaciones mismas:
- **Compuertas categóricas ($S_i$)**: No existe una "distancia parcial" al absurdo. Una proposición es categóricamente válida o no lo es — el espacio continuo siempre deja un gradiente residual.
- **Lectura binaria directa ($V_i$)**: La consulta por coordenada discreta reemplaza la inferencia probabilística; no hay muestreo, no hay softmax, no hay riesgo de decodificación infiel.
- **Deducción determinista**: La multiplicación Booleana en semianillo produce clausura transitiva exacta; el espacio continuo produce "trayectos probables" sin garantía deductiva.

## Gaps detectados
