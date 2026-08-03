---
system: matrix
layer: review
domain: limitations
topic: limitaciones-y-trabajo-futuro-implementacion
use_when: "Aplicable al contexto semantico y factual de Limitaciones y Trabajo Futuro Implementacion."
do_not_use_when: "No utilizar fuera del dominio formal de limitations."
---

# Limitaciones y Trabajo Futuro sobre la Implementación

**Categoría Padre:** [[composiciones_review]]
**Relaciones 5W1H+:**
* [explains_failure_of:: [[comp_eje_e]]]
* [explains_failure_of:: [[comp_eje_reviewer]]]
* [explains_failure_of:: [[Integracion_Teorica_con_LLMs_y_Trabajo_Futuro]]]

---

## Qué es
Es la delimitación final del alcance actual del proyecto. Matrix presenta un **sustrato de representación lógica auditable** y un **motor de evaluación discreta**. No presenta todavía una validación experimental end-to-end contra baselines abiertos ni una integración profunda con arquitecturas neuronales.

## Lo que sí existe hoy

- arquitectura ejecutable del motor lógico;
- 105 tests verdes del núcleo lógico;
- rechazo determinista de proposiciones `unsinnig`;
- pipeline de lowering y evaluación post-generación;
- representación booleana auditable en contextos cerrados.

## Lo que no existe hoy

### E1 — Evaluación experimental end-to-end
No existe todavía:
- benchmark con/sin $S_i$ sobre alucinaciones;
- comparación contra RAG o KGs en FEVER / HaluEval;
- benchmark de latencia contra graph traversal externo;
- curva de escalabilidad publicada con $N$ creciente.

### E2 — Tests de integración LLM→MEEL
Sí existe código del pipeline, pero una parte de los tests de integración (`test_shrdlu_*`, `test_ragout_demonstration`) falla por problemas de imports/entorno.

### R1 — Demostración formal de mapping NL→lógica
No existe evaluación robusta del traductor NL→representación lógica:
- precisión de lowering;
- cobertura de dominios;
- robustez ante ambigüedad;
- comparación con parsers existentes.

### R2 — Conexión con arquitectura real de redes
No existe un mapping directo entre coordenadas de $L_i$ y posiciones/tokenización interna del Transformer. La implementación actual está desacoplada:
- el LLM genera superficie textual;
- Matrix parsea y valida después.

## Posición correcta para el paper

### No debe afirmarse
- que ya existe validación end-to-end contra baselines estándar;
- que el lowering NL→lógica está demostrado de forma general;
- que Matrix ya modifica Transformers por dentro;
- que los tests de integración están completamente estabilizados.

### Sí puede afirmarse
- que existe un motor lógico ejecutable;
- que existe una representación auditable en contextos cerrados;
- que la contribución principal está en Fases 1 y 2;
- que Fase 3 (integración neuronal profunda) queda como trabajo futuro.

## Respuesta corta al revisor

La implementación actual demuestra el sustrato lógico, no el ciclo experimental completo contra modelos abiertos. El proyecto ya prueba el núcleo determinista y la auditoría post-generación, pero deja como trabajo futuro la validación empírica masiva, la estabilización completa del pipeline de integración y el cruce profundo con redes neuronales.
