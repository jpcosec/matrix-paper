---
system: matrix
layer: operational-architecture
domain: system-architecture
topic: arquitectura-end-to-end-ejecutable
use_when: "Aplicable al contexto semantico y factual de Arquitectura End to End Ejecutable."
do_not_use_when: "No utilizar fuera del dominio formal de system-architecture."
---

# Arquitectura End-to-End Ejecutable

**Categoría Padre:** [[Computacion]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_system_logical_system_py]]]
* [implements:: [[Source_Code_src_operational_model_engine_meel_engine_py]]]
* [implements:: [[Source_Code_src_operational_model_language_s_expressions_py]]]
* [implements:: [[Source_Code_src_operational_model_matrices_si_matrix_py]]]
* [implements:: [[Source_Code_src_operational_model_matrices_vi_matrix_py]]]
* [implements:: [[Source_Code_src_operational_model_matrices_block_matrix_py]]]
* [implements:: [[Source_Code_src_operational_model_kernel_rule_matrix_py]]]

---

## Qué es
Es el diagrama de arquitectura del sistema Matrix/MEEL ejecutable, mostrando cómo los módulos de código se conectan end-to-end desde la entrada de lenguaje natural hasta la consulta booleana.

## Arquitectura por Capas

```
┌─────────────────────────────────────────────────────────┐
│                 CAPA DE SUPERFICIE (S)                   │
│  LLM (Neuro-Estocástico)  ←→  Usuario                  │
│  Input: NL  /  Output: NL redactado                     │
└──────────────────────┬──────────────────────────────────┘
                       │ Lowering + S-Expr Parser
                       ▼
┌─────────────────────────────────────────────────────────┐
│              CAPA DE SIGNIFICADO (M)                     │
│  SExpressionRuntime  →  MEEL Engine                      │
│  ├─ check (R a b)   →  Si.get + Vi.get                  │
│  ├─ assert (R a b)  →  add_fact + algebra               │
│  ├─ ingest           →  accepts? → reject/accept         │
│  └─ create           →  register_thing/relation/li/wg    │
└──────────────────────┬──────────────────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
┌──────────────┐ ┌──────────┐ ┌──────────────┐
│  SiMatrix    │ │ ViMatrix │ │ BlockMatrix  │
│  (Sentido)   │ │ (Verdad) │ │ (Contexto)   │
│  Sinnvoll    │ │ 1 / 0 / ∅│ │ WCi ruteo   │
│  Sinnlos     │ │          │ │              │
│  Unsinnig    │ │          │ │              │
└──────┬───────┘ └────┬─────┘ └──────┬───────┘
       │              │              │
       └──────────────┼──────────────┘
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   CAPA DE GRAFO (G)                      │
│  LiSpace  →  WiGame  →  RoutingProjection               │
│  Symbol Spaces  →  LogicalSystem                         │
│  Contexts  →  Projections  →  Multi-hop search           │
└─────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 KERNEL BOOLEANO                          │
│  BooleanAlgebra  →  RuleMatrixCompiler                   │
│  BitwiseExecution (uint64)  →  TransitiveClosure         │
│  PropositionalInference  →  FormulaEvaluation            │
└─────────────────────────────────────────────────────────┘
```

## Módulos de Código (50+ archivos)

| Capa | Módulo | Archivo fuente |
|:---|:---|:---|
| **Núcleo** | Thing, Symbol, Proposition, Fact | `core/thing.py`, `core/symbol.py`, `core/proposition.py`, `core/fact.py` |
| **Valores** | TruthValue, SenseValue | `core/truth_value.py`, `core/sense_value.py` |
| **Matrices** | Vi, Si, Block | `matrices/vi_matrix.py`, `matrices/si_matrix.py`, `matrices/block_matrix.py` |
| **Kernel** | BooleanAlgebra, RuleMatrix, BitwiseExec | `kernel/boolean_algebra.py`, `kernel/rule_matrix.py`, `kernel/bitwise_execution.py` |
| **Lenguaje** | S-Expr, OWL2Matrix, SHRDLU lowering | `language/s_expressions.py`, `language/owl2matrix.py` |
| **Runtime** | SExpressionRuntime, LogicalSystem | `system/s_expression_runtime.py`, `system/logical_system.py` |
| **Ruteo** | Context, RoutingProjection | `routing/context.py`, `routing/routing_projection.py` |
| **Juego** | WiGame, WiGameQueries, WiGameRegistry | `system/wigame.py`, `system/wi_game_queries.py` |

## Tests (105 pasan)

| Test | Archivo |
|:---|:---|
| Inferencia proposicional | `test_propositional_inference.py` |
| Compilador de reglas | `test_rule_matrix_compiler.py` |
| Multiplicación booleana | `test_bool_mult.py` |
| Ejecución bitwise | `test_bitwise_execution.py` |
| Runtime S-Expr | `test_s_expression_runtime.py` |
| Ágebra relacional | `test_relation_algebra.py` |
| Serialización | `test_serialization_roundtrip.py` |
| Aserciones tipadas | `test_typed_assertions.py` |

## Cuándo interviene
Cuando un revisor pregunta "¿Dónde está la implementación funcional?" — esta arquitectura documenta la respuesta completa.
