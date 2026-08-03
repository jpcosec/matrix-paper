# Contextual Insertion Algorithm

## Summary
Algorithm for inserting a new concept into an existing local universe within an active context, using only discriminative features needed for differentiation.

## Concepts
- Contextual concept insertion
- Universe membership verification
- Context projection for new concepts
- Discriminative dimension expansion
- Local vs global representation maintenance

## Content

### Algorithm: insertar(concepto_nuevo, universo_local, contexto)

1. **Detect active domain** — fix interpretation frame (e.g., cocina)
2. **Verify minimal membership** — does the new concept belong to the same practical field?
   - `apio: alimento=1, planta=1, vegetal=1` → yes, enters universe
   - `martillo: alimento=0, planta=0` → reject or expand context
3. **Project concept to active axis** — only represent what matters for the current discriminative dimension
   - Active axis: `parte_comestible` → `apio: tallo=1`
4. **Compare against existing concepts**
   - lechuga: `[hoja=1, raiz=0, tallo=0]`
   - zanahoria: `[hoja=0, raiz=1, tallo=0]`
   - apio: `[hoja=0, raiz=0, tallo=1]`
5. **Update discriminative bits**
   - Extend: `[hoja_comestible, raiz_comestible, tallo_comestible]`
6. **Check if dimension still suffices**
   - If new concept collides (e.g., espinaca = `[1,0,0]` = lechuga), find new discriminative dimension
   - Add: `forma_hoja`, `uso_culinario`, `textura`
7. **Maintain separate global representation**
   - Local: `apio_en_contexto_cocina: discriminante: tallo`
   - Global: `apio: es_un: [planta, vegetal, alimento], partes: [tallo, hoja, raiz]`

### Compact Example
```
contexto:
  dominio: cocina
  objetivo: distinguir
  universo_local: [lechuga, zanahoria, apio]
  dimensiones_discriminantes: [parte_comestible_principal]

valores:
  hoja:  [1,0,0]
  raiz:  [0,1,0]
  tallo: [0,0,1]

conceptos:
  lechuga:   vector: [1,0,0]
  zanahoria: vector: [0,1,0]
  apio:      vector: [0,0,1]
```

### Key Principle
Don't ask "what is X in absolute terms?" Ask "what feature of X do I need to distinguish it from current candidates in this context?"

## Semantic Hashing

The system functions as a **semantic hash**: context-dependent signatures that identify concepts without storing the full representation.

```
hash_contextual(concepto, contexto) ≠ hash_global(concepto)
```

Example: zanahoria in different contexts:
- cocina: `[vegetal=1, alimento=1, raiz_comestible=1]`
- biología: `[organismo=1, planta=1, raiz=1]`
- comercio: `[producto=1, perecible=1, vendido_por_peso=1]`

Each context produces a distinct signature, all pointing to the same base node `zanahoria`.

## Search Tree / Decision Tree

The bit vector acts as a dynamic decision tree — only ask questions that reduce ambiguity:

```
¿es vegetal? 
  sí → ¿qué parte comestible principal?
         hoja → lechuga / espinaca / acelga
         raiz → zanahoria / betarraga / rábano
         tallo → apio / espárrago
```

When collisions occur (e.g., lechuga vs espinaca both `[hoja=1]`), add another question:
```
hoja → ¿forma una cabeza compacta?
         sí → lechuga
         no → ¿hoja pequeña y suelta? → espinaca
```

## Horizontal Relations & Similarity

Concepts sharing bits become **horizontally related**:
- `lechuga ~ espinaca` (both `hoja_comestible`)
- `zanahoria ~ betarraga` (both `raiz_comestible`)
- `lechuga ~ zanahoria` (both `vegetal + alimento`)

Operations enabled:
- **Exact search**: `[1,1,0,1,0]` → zanahoria
- **Partial search**: `[1,1,*,*,*]` → lechuga, espinaca, zanahoria, apio
- **Similarity search**: most similar to lechuga → espinaca

### Explicit Horizontal Relations
```
relaciones:
  lechuga:
    similar_a:
      - concepto: espinaca
        porque: [hoja_comestible, vegetal, alimento]
    contrasta_con:
      - concepto: zanahoria
        porque: [hoja_vs_raiz]
```

## Core Representation

```
Concepto C + Contexto K → Proyección P(C, K)
P(C, K) = {
  bits discriminantes,
  camino jerárquico,
  relaciones horizontales,
  colisiones pendientes
}
```

Collisions signal missing dimensions — expand only when needed ("necesidad discriminativa").

## References
- turn-12.md (complete insertion algorithm with 8-step process)
- turn-14.md (semantic hashing, search trees, horizontal relations, projections)

## Version Notes
- Turn 12: defined the contextual insertion algorithm as an 8-step process
