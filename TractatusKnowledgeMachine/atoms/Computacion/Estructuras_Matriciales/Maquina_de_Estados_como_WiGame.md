---
topic: maquina-de-estados-como-wigame
use_when: Para mapear una maquina de estados (circuito digital, FSM, procedimiento)
  al modelo de WiGame y saber que operaciones del motor la analizan.
do_not_use_when: No utilizar para contenido descriptivo sin secuencia (usar
  [[WiGame_Contexto_y_Desambiguacion]]) ni para la operatoria de un dominio
  particular (usar [[Operatoria_Lectura_de_Recetas]]).
id: atom-maquina-de-estados-como-wigame
title: Maquina de Estados como WiGame
five_wh_one_plus: what
tags:
- system:matrix
---
# Máquina de Estados como WiGame

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [defines:: [[WiGame]]]
* [implements:: [[Capa_Verdad_Vi]]]
* [implements:: [[Capa_Sentido_Si]]]
* [is_solved_by:: [[Colapso_Dimensional]]]
* [is_solved_by:: [[Juego_de_Desambiguacion]]]
* [mathematically_proves:: [[Enrutamiento_Jerarquico]]]

---

## Qué es
Es la identificación estructural entre una máquina de estados y un `WiGame` secuencial: la misma matriz que el motor usa para hechos se usa como matriz de transición.

- `Vi[estado][estado]` = transición (arista dirigida).
- `Si[estado][transición]` = **guarda**: la transición es admisible en este contexto.
- Contexto = programa / receta / circuito; un WiGame por `(contexto, relación)`.
- `precede` es asimétrico y transitivo, a diferencia de lo descriptivo.

## Por qué es necesario
Porque el motor ya tenía la capa de circuitos y la estaba usando como almacén:

| primitiva | lectura secuencial |
|---|---|
| `BooleanMatrix.transitive_closure()` | alcanzabilidad (`A*`) |
| `A · A*` (`bool_mult`) | alcanzabilidad estricta (`A+`, caminos de largo ≥1) |
| `to_row_bitmasks()` | firma de salidas de un estado (base de minimización) |
| `collapse_similarity()` | equivalencia/compatibilidad de estados |
| `RuleMatrixCompiler` + `modus_ponens` | un disparo de la máquina (`v ⊗ I*`) |
| `kernel/bitwise_execution.py` | evaluación de todos los estados en paralelo |

## Cómo funciona
1. Se declara la operatoria del dominio (qué relación es transición, qué cierra, qué errores son válidos).
2. Se extraen o autoran aristas (`precede`) y guardas (`requiere`).
3. `compile` aplica el álgebra: cierre transitivo ⇒ hechos derivados.
4. Se analiza con oráculo independiente: cierre (motor) vs BFS (oráculo); acuerdo total o hay bug.
5. Sobre aristas **crudas** (no derivadas) se calculan ciclos, inalcanzables y clases de equivalencia.

## Cuándo interviene
Al analizar procedimientos, runbooks, recetas o circuitos: alcanzabilidad, detección de deadlock/ciclo, estados inalcanzables, minimización.

## Dónde reside
Generador y specs en `tools/kb/machine.py`, `tools/kb/machines/*.yaml`; análisis en `tools/kb/reach.py`; álgebra aplicada en `tools/kb/compile.py`.

## Para qué / Para quién
Para que instrucciones y secuencias se validen con la misma maquinaria que los hechos, y para explotar la equivalencia con circuitos digitales sin código nuevo.

## Medición de referencia
`trafico`: ciclo esperado (`rojo→verde→amarillo→rojo`), `verde_peatonal` inalcanzable desde `rojo` y equivalente a `verde` (misma firma cruda de salidas). `ragout`/`guiso`/`bechamel`: acíclicas, con cierre derivado. Oráculo BFS: acuerdo total en todos los contextos.
