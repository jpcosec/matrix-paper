---
title: Demostraciones empíricas del acoplamiento discreto — Aplicaciones
folder: Aplicaciones
question: ¿Qué demostraciones empíricas validan que el acoplamiento neuro-simbólico
  discreto resuelve las patologías del espacio continuo?
atom_count: 4
tags: []
---

# Demostraciones empíricas del acoplamiento discreto — Aplicaciones

## Carpeta Revisada

`atoms/Aplicaciones/`

## Pregunta que responde esta composición

¿Qué prototipos y demostraciones empíricas prueban que el acoplamiento neuro-simbólico (LLM + kernel Booleano) resuelve las patologías del paradigma puramente continuo?

## Cadena argumentativa (átomos en orden de lectura)

1. **[[Demostracion_Compilacion_Reglas_y_Modus_Ponens]]** — Valida que la compilación de reglas en el kernel Booleano produce deducción determinista (Modus Ponens matricial), sin decodificación estocástica.

2. **[[Demostracion_Juego_Desambiguacion_WiGame]]** — El juego WiGame prueba que la máscara de sentido $S_i$ discrimina categóricamente entre proposiciones *Sinnvoll* y *Unsinnig* sin gradiente residual.

3. **[[Demostracion_Mundo_Bloques_SHRDLU]]** — Prototipo SHRDLU demuestra que el LLM propone pero MEEL dispone: la ejecución en el mundo de bloques es verificada por el kernel Booleano antes de comprometerse.

4. **[[Demostracion_Dominio_Culinario_Ragout]]** — Caso end-to-end en dominio culinario: la consulta sobre ingredientes es propuesta por el LLM, filtrada por $S_i$, verificada en $V_i$, y la respuesta es verbalizada por el LLM solo si el kernel Booleano aprueba.

## Síntesis

Las aplicaciones validan empíricamente lo que la filosofía y la matemática prueban formalmente:
- **Modus Ponens matricial**: La deducción Booleana produce resultados exactos; el LLM no "decide" la verdad.
- **WiGame**: La máscara $S_i$ opera como compuerta categórica — no hay "casi Unsinnig".
- **SHRDLU + Ragout**: El patrón LLM-propone / MEEL-dispone funciona end-to-end en dominios reales.

## Gaps detectados

No se detecta un prototipo que demuestre explícitamente la **barrera AUROC 0.48** (Error Tipo III) en un benchmark de alucinaciones. Sería valioso un demo que muestre: (a) el LLM falla al distinguir verdad de mentira en embeddings, (b) MEEL sí lo hace vía $V_i$. Los átomos de Fuentes contienen los PDFs pero no hay un átomo de demostración de esta barrera.
