# Fase 1: Sin dimension lenguaje

## Objetivo

Validar el nucleo del sistema sin introducir todavia ambiguedad lexical, sintaxis textual ni interpretacion probabilistica del signo.

## Fuente de datos sugerida

- ontologias `OWL`
- grafos `RDF`
- bases de conocimiento formalmente tipadas

## Por que esta fase va primero

- permite probar `L_i`, `V_i`, `S_i` y `W_i^*` en un entorno controlado
- permite estudiar desambiguacion sin contaminarla con polisemia linguistica
- permite evaluar composicion y subcontextos sobre estructuras ya formalizadas
- permite demostrar queries algebraicas sobre conocimiento util y existente

## Que deberia demostrarse

- construccion de contextos `C_i` a partir de ontologias
- derivacion del espacio logico `L_i` desde clases, propiedades y firmas
- construccion de `V_i` desde hechos afirmados o inferidos
- construccion de `S_i` desde dominio, rango, restricciones y aplicabilidad contextual
- proyeccion a `W_i^*`
- deteccion de tautologias contextuales
- deteccion de ambiguedad por indistinguibilidad estructural
- refinamiento por nuevas propiedades o subcontextos
- queries booleanas y algebraicas

## Preguntas de investigacion

- como se mapea una ontologia `OWL` a una familia de contextos `C_i`?
- que parte de `S_i` puede derivarse automaticamente desde restricciones ontologicas?
- como se representa la inferencia ontologica dentro de `V_i`?
- cuando conviene expandir un contexto y cuando conviene factorizar un subcontexto?

## Entregables sugeridos

- un pipeline formal `OWL -> C_i, L_i, V_i, S_i, W_i^*`
- uno o mas dominios de prueba
- ejemplos de crecimiento del sistema con nuevas filas, columnas o relaciones
- ejemplos de composicion de subcontextos
- benchmarks de consulta e indexacion

## Resultado esperado

Al final de esta fase, el sistema deberia poder demostrarse como una maquina algebraica de representacion y consulta sobre conocimiento estructurado, aun sin incorporar lenguaje natural.
