# Fase 2: Dimension semi-linguistica

## Objetivo

Introducir una capa intermedia entre signo y simbolo sin saltar todavia a lenguaje natural abierto.

## Fuente de datos sugerida

- `UNL` (Universal Networking Language)
- representaciones semanticas controladas
- corpus anotados con estructuras logicas o semanticas explicitas

## Rol de esta fase

Esta fase permite estudiar el punto donde el sistema deja de operar solo sobre conocimiento estructurado ya resuelto y empieza a enfrentar la mediacion del signo.

## Que deberia demostrarse

- como un signo se proyecta a simbolos dentro de un contexto
- como una representacion semi-linguistica puede inducir `L_i`
- como se distinguen ambiguedad lexical y ambiguedad estructural
- como se construyen `V_i` y `S_i` cuando la fuente no es una ontologia pura sino una representacion semantica intermedia
- como la mascara de sentido ayuda a resolver colisiones entre formulaciones linguisticas distintas

## Preguntas de investigacion

- que parte del paso signo -> simbolo puede resolverse deterministicamente?
- que parte sigue siendo contextual o estocastica?
- como se preserva la distincion entre forma logica y superficie de representacion?
- puede construirse una familia de documentos semanticamente equivalentes sobre el mismo espacio logico?

## Entregables sugeridos

- un modelo de interfaz entre recursos semi-linguisticos y contextos `C_i`
- ejemplos de mapping desde `UNL` o estructuras similares hacia `L_i`, `V_i` y `S_i`
- casos donde una misma estructura logica admita varias superficies de expresion
- casos donde la misma expresion superficial requiera desambiguacion contextual

## Resultado esperado

Al final de esta fase, el sistema deberia poder operar sobre una representacion donde el lenguaje ya aparece, pero todavia de forma acotada, controlada y estructuralmente explicita.
