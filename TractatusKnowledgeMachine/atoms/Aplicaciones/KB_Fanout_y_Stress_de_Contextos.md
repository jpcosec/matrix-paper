---
topic: kb-fanout-y-stress-de-contextos
use_when: Para recordar como se puebla la KB de Matrix desde texto real (propuestas + revision),
  como se indexan contextos, y que se midio al escalar contextos/WiGames.
do_not_use_when: No utilizar como contrato de API del harness (ver tools/kb) ni como sustituto
  de [[WiGame_Contexto_y_Desambiguacion]].
id: atom-kb-fanout-y-stress-de-contextos
title: KB Fan-out y Stress de Contextos
five_wh_one_plus: what
tags:
- system:matrix
---
# KB Fan-out y Stress de Contextos

**Categoría Padre:** [[Aplicaciones]]
**Relaciones 5W1H+:**
* [implements:: [[WiGame_Contexto_y_Desambiguacion]]]
* [implements:: [[Maquina_de_Estados_como_WiGame]]]
* [is_solved_by:: [[Operatoria_Lectura_de_Recetas]]]
* [implements:: [[Hipertensor_Canonico]]]
* [is_solved_by:: [[Juego_de_Desambiguacion]]]
* [mathematically_proves:: [[Colapso_Dimensional]]]
* [grounded_by:: [[Capa_Sentido_Si]]]

---

## Qué es
Es el registro del harness que puebla la KB de Matrix desde texto real (artículos), y de las mediciones hechas al escalar contextos y WiGames.

Pipeline implementado en `tools/kb/` del repo Matrix:

1. `fetch`/`prepare`: baja el texto y lo parte en chunks; genera un prompt por chunk. Alternativa determinística: `software` extrae por AST módulos como contextos (relaciones `define_en`, `usa`, `importa`, `hereda_de`) sin LLM.
2. **Subagentes libres** (`pi` + `deepseek-flash`, un worker por chunk) escriben JSONL de candidatos. No tocan la KB.
3. `ingest`: valida determinísticamente (oración verbatim del chunk, sujeto/objeto presentes, relación del vocabulario, sin auto-referencia) y produce **propuestas `pending`**, context-scoped.
4. **Review gate**: `review approve|reject` sobre `kb/review.yaml`. Nada entra a la KB sin decisión (reviewer + nota + fecha).
5. `compile`: materializa sólo aprobadas en WiGames `wigame:<contexto>:<relación>` con `context_id`, escribe el árbol `contexts.yaml` (`ctx:kb` → `ctx:<fuente>` → hojas) y aplica `aliases.yaml` (curación) para canonicalizar ocurrencias por contexto.
6. **Identidad cross-contexto**: `RoutingProjection` entre contextos que comparten un referente canónico.
7. `verify`: re-chequea cada hecho por `SExpressionRuntime` y valida `context_id`, contextos y proyecciones.

## Por qué es necesario
Sin contexto en la identidad del WiGame, la KB acumula homónimos en vez de desambiguar. Este harness es la prueba operativa de que `(R a b)` en dos artículos son dos hechos en dos contextos, y que la identidad entre contextos es una decisión revisada, no una coincidencia de strings.

Además fija los límites de costo reales antes de escalar el Hipertensor.

## Cómo funciona — mediciones
Sintético (250 contextos, 4640 facts, 995 WiGames): `load_system` (cold) 7.0s; ruteo **hot** p50 0.012ms; ruteo cold ~7.1s; proyecciones topadas en 2000; RSS 96MB; disco 13MB.

Real (DBpedia, categoría "20th-century women scientists": 172 personas, 200 categorías-contexto, 1498 facts): ingest 0.27s / compile 4.1s / verify 5.6s; `load_system` 5.8s; ruteo hot p50 0.010ms; proyecciones 2000 (cap); RSS 66MB.

Curva de desambiguación (homónimos por apellido real, perfil = categorías): k=1 → 83%, k=2 → **100%** (sobrevivientes 1.17 → 1.0). En sintético, con más homónimos: k=1 → 52%, k=4 → 100%.

Lectura: la acumulación de contextos identifica el referente sin curación previa; el cuello de botella es la hidratación total y la generación O(contextos²) de pares de proyección, no el ruteo.

Corpus de software (este repo, `src/operational_model` + `tests`, 86 módulos): 1494 facts, 211 WiGames, 1736 proyecciones, 0 rechazos, `capabilities` 26/26. El ruteo cross-contexto vincula módulos por dependencias compartidas (`vi_matrix` ↔ `si_matrix` vía `booleanmatrix`, `new_id`). Hallazgo: los homónimos también existen en código (`post_init` definido en 4 clases distintas; `self`/`cls`/`payload` en `usa`), así que la curación por símbolo calificado es necesaria igual que con apellidos.

Corpus secuencial (operatoria + FSM/recetas: `trafico`, `ascensor`, `ragout`, `bechamel`, `guiso`): 103 facts, 34 derivados por cierre transitivo, 20 WiGames, 8 proyecciones. Las recetas resultan acíclicas y las FSM con ciclo esperado; `verde_peatonal` queda inalcanzable y equivalente a `verde`. El cierre del motor coincide con el oráculo BFS en todos los contextos. Ver [[Maquina_de_Estados_como_WiGame]] y [[Operatoria_Lectura_de_Recetas]].

## Cuándo interviene
Al poblar o auditar la KB, al agregar una fuente nueva, y al decidir si conviene escalar contextos (ahí aplican los caps y los costos medidos).

## Dónde reside
`tools/kb/` (harness), `.pi/skills/matrix-kb-fanout/` (skill de uso), `docs/kb_fanout_harness.md` (materialización), `tests/test_kb_fanout.py` (contrato ejecutable). El stress real usa DBpedia (una query SPARQL, cacheada) o Wikipedia (con pacing).

## Para qué / Para quién
Para que la KB pueda crecer con fuentes reales sin contaminarse, y para tener números reproducibles antes de optimizar carga y proyecciones.
