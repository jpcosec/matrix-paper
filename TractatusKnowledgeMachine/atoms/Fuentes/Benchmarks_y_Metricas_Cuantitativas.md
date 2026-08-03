---
system: matrix
layer: benchmarks
domain: quantitative-evaluation
topic: benchmarks-y-metricas-cuantitativas
use_when: "Aplicable al contexto semantico y factual de Benchmarks y Metricas Cuantitativas."
do_not_use_when: "No utilizar fuera del dominio formal de quantitative-evaluation."
---

# Benchmarks y Métricas Cuantitativas Existentes

**Categoría Padre:** [[Computacion/Optimizacion_y_Seguridad]]
**Relaciones 5W1H+:**
* [implements:: [[Source_Code_src_operational_model_system_logical_system_py]]]
* [implements:: [[Source_Code_src_operational_model_optimization_information_energy_py]]]

---

## Qué es
Es el inventario de métricas cuantitativas y tests automatizados que demuestran la funcionalidad del sistema Matrix/MEEL ejecutable.

## Tests Automatizados (105 pasan)

```
cd Matrix/Matrix && python -m pytest tests/ -q
........................................ [38%]
........................................ [76%]
.............................            [100%]
105 passed in 0.13s
```

| Categoría | Tests | Archivo |
|:---|:---|:---|
| Álgebra booleana | Operaciones bool, normalización | `test_bool_mult.py`, `test_propositional_normal_forms.py` |
| Inferencia proposicional | Modus ponens, deducción | `test_propositional_inference.py` |
| Compilador de reglas | Reglas → matrices Booleanas | `test_rule_matrix_compiler.py` |
| Ejecución bitwise | uint64, compuertas nativas | `test_bitwise_execution.py` |
| Runtime S-Expr | check/assert/ingest/create | `test_s_expression_runtime.py` |
| Álgebra relacional | Operaciones entre relaciones | `test_relation_algebra.py` |
| Serialización | Roundtrip YAML ↔ WiGame | `test_serialization_roundtrip.py` |
| Aserciones tipadas | Validación por tipo | `test_typed_assertions.py` |
| Kernel de símbolos | Registro, espacios, equivalencia | `test_symbol_kernel.py` |
| Subsunción booleana | Inclusión entre vectores | `test_boolean_subsumption.py` |
| Gramática proposicional | Parsing de fórmulas | `test_propositional_grammar.py` |

## Métricas Internas del Sistema

| Métrica | Fórmula | Implementación | Significado |
|:---|:---|:---|:---|
| **Energía de Información** | $E(R) = \frac{1}{4}(c + i + o + d)$ | `wi_game_queries.information_energy()` | Calidad de la partición lógica |
| **Densidad de sentido** | $c = \text{sinnvoll} / \text{total}$ | `_count_sinnvoll()` | Proporción de celdas válidas |
| **Densidad factual** | $i = \text{true} / \text{total}$ | `_count_true_facts()` | Proporción de hechos afirmados |
| **Observabilidad** | $o = \text{facts} / \text{total}$ | `len(facts) / total` | Proporción observada |
| **Poder discriminativo** | $d = 1 - \text{tautológicas} / m$ | `tautological_columns()` | Capacidad de distinguir |

## Métricas Faltantes (⚠️ Gaps)

| Métrica | Status | Prioridad |
|:---|:---|:---|
| Precisión de inferencia vs. baselines | ❌ No existe | Alta |
| Latencia bitwise vs. graph traversal | ❌ No existe | Alta |
| Reducción de alucinaciones con/sin $S_i$ | ❌ No existe | Crítica |
| Cobertura de test del pipeline end-to-end | ❌ No existe | Alta |
| Benchmarks contra datasets estándar (FEVER, HaluEval) | ❌ No existe | Media |
| Escalabilidad empírica con $N$ creciente | ❌ No existe | Media |

## Nota sobre Tests Rotos

5 tests de SHRDLU y ragout tienen errores de import (módulos dependientes no instalados). Estos tests prueban la integración LLM→MEEL:
- `test_shrdlu_english_parser.py`
- `test_shrdlu_lexicon.py`
- `test_shrdlu_lowering.py`
- `test_shrdlu_dialog.py`
- `test_ragout_demonstration.py`

Restaurar estos tests cerraría el gap de demostración end-to-end.
