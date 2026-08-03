# Fase 3: Texto natural

## Objetivo

Incorporar lenguaje natural abierto como fuente para construir o poblar contextos, manteniendo la separacion entre signo, simbolo, verdad y sentido.

## Fuente de datos sugerida

- textos tecnicos
- documentacion estructurada
- diccionarios especializados
- reportes o corpus de dominio acotado

## Rol de esta fase

Esta fase aborda el problema mas dificil: como pasar desde lenguaje natural a una representacion logico-algebraica sin perder auditabilidad contextual.

## Que deberia demostrarse

- extraccion de candidatos a entidades, relaciones y propiedades
- construccion o extension de `C_i` y `L_i` desde texto
- separacion entre incertidumbre linguistica y estructura simbolica
- asignacion provisional o probabilistica del paso signo -> simbolo
- validacion posterior mediante `S_i` y `V_i`
- integracion de nuevo conocimiento en contextos ya existentes

## Preguntas de investigacion

- cuanto del paso texto -> simbolo puede automatizarse sin romper la coherencia contextual?
- como se representa incertidumbre en la entrada sin destruir el nucleo booleano interno?
- conviene usar una capa previa probabilistica y luego proyectar a `C_i`, `L_i`, `V_i`, `S_i`?
- que tipos de documentos son mas adecuados para una primera prueba?

## Entregables sugeridos

- una arquitectura de ingestion desde texto natural
- ejemplos de extraccion y normalizacion de hechos
- un regimen de validacion para decidir que hechos entran realmente al sistema
- comparacion entre representacion textual y representacion logico-algebraica final

## Resultado esperado

Al final de esta fase, el sistema deberia poder recibir conocimiento desde lenguaje natural y transformarlo en estructuras auditables por contexto, verdad, sentido, desambiguacion e indexacion.
