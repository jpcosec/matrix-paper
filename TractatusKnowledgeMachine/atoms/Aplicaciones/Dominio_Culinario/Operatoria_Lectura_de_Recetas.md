---
topic: operatoria-lectura-de-recetas
use_when: Para leer una receta (o cualquier procedimiento) como maquina de estados:
  que relaciones usar, que algebra declarar, que operaciones son admisibles y que
  errores tipificar.
do_not_use_when: No utilizar para recetas particulares (usar el contexto de esa receta)
  ni para el motor generico de contextos (usar [[WiGame_Contexto_y_Desambiguacion]]).
id: atom-operatoria-lectura-de-recetas
title: Operatoria Lectura de Recetas
five_wh_one_plus: how
tags:
- system:matrix
---
# Operatoria: Lectura de Recetas

**Categoría Padre:** [[Dominio_Culinario]]
**Relaciones 5W1H+:**
* [defines:: [[WiGame]]]
* [is_solved_by:: [[Maquina_de_Estados_como_WiGame]]]
* [implements:: [[Capa_Sentido_Si]]]
* [restricts:: [[Demostracion_Dominio_Culinario_Ragout]]]
* [mathematically_proves:: [[Colapso_Dimensional]]]

---

## Qué es
Es la **spec autorada** que define cómo se lee una receta como máquina de estados. No sale del pipeline de extracción: se escribe, se versiona y se revisa como cualquier propuesta, porque es la capa de mayor leverage (un error acá se propaga a todas las recetas).

Se materializa como un contexto más (`ctx:operatoria`, `wigame:operatoria:declara`) y `compile` la consulta para decidir qué clausuras aplica y qué validaciones corre.

## Por qué es necesario
La receta sola aporta pasos y orden parcial: no alcanza para inferir la máquina. La composición (qué cierra transitivamente, qué es una guarda, qué es un ciclo prohibido, qué operación es admisible) no está escrita en ninguna receta: es el contrato de operación del dominio.

Sin operatoria, lo descriptivo funciona porque su semántica viene de fábrica (`es`, `causa`); lo secuencial necesita declararla.

## Cómo funciona
**Reglas de lectura (texto → proposiciones):**

| marca | proposición |
|---|---|
| orden explícito ("luego", "una vez que") | `(precede A B)` |
| precondición ("cuando…", "hasta que") | `(requiere A condición)` |
| ingrediente o herramienta | `(usa A item)` |
| resultado ("hasta obtener…") | `(produce A resultado)` |
| simultaneidad ("mientras", "en paralelo") | `(paralelo_con A B)` |
| equivalencia ("si no hay X, usar Y") | `(sustituye_a X Y)` |

**Álgebra declarada:** `precede` y `sustituye_a` transitivas (⇒ cierre, alcanzabilidad, cadenas de sustitución); `paralelo_con` conmutativa (⇒ orden indistinto); `requiere`/`usa`/`produce` simples.

**Operaciones admisibles:** `cierre_precede`, `orden_aciclico` (recetas: sin ciclos), `alcanzable` (cierre vs oráculo BFS), `guarda_precondicion`, `sustitucion_transitiva`; en FSM además `scc` y `minimizar_estados`.

**Errores tipificados:** `ciclo`, `precondicion_insatisfecha`, `sustituible_incompatible`; en FSM `estado_inalcanzable`, `guarda_inalcanzable`.

## Cuándo interviene
Antes de extraer pasos de cualquier receta o procedimiento, y cada vez que `compile` necesita saber si una relación cierra transitivamente o si el orden debe ser acíclico. `Si` distingue operación aplicable de operación fuera de dominio (`unsinnig`).

## Dónde reside
Specs en `tools/kb/operatoria/{recetas,fsm}.yaml`; materialización en el contexto `operatoria` de la KB; documentación en `Matrix/docs/operatoria_recetas.md`; verificación en `tools/kb/reach.py` (cierre vs BFS) y `tests/test_kb_machine.py`.

## Para qué / Para quién
Para que el texto de una receta se convierta en máquina verificable, y para reusar el mismo par (contenido + operatoria) en cualquier dominio secuencial: runbooks, contratos, circuitos.
