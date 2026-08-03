# Formulacion algoritmica

Este documento presenta una formulacion algoritmica del sistema sin comprometerse con un lenguaje de implementacion. Se priorizan:

- estructuras de datos tipadas,
- operatoria explicita,
- diagramas UML en texto,
- y pseudocodigo independiente de plataforma.

El objetivo es dejar claro que debe almacenar la maquina, que transformaciones debe soportar y en que orden deben ejecutarse.

## 1. Objetivo operacional

La maquina debe poder:

- representar contextos logicos tipados,
- almacenar verdad y sentido por separado,
- proyectar una capa operativa booleana,
- expandir contextos de manera controlada,
- construir y proyectar subcontextos,
- detectar tautologias y ambiguedades,
- indexar hechos y responder queries.

## 2. Arquitectura minima

```text
+---------------------+
| Context Repository  |
|---------------------|
| almacena contextos, |
| subcontextos e      |
| indices             |
+----------+----------+
           |
           v
+---------------------+        +----------------------+
| Type System         |<------>| Logic Space Builder  |
|---------------------|        |----------------------|
| valida firmas,      |        | construye L_i        |
| aridades y tipos    |        | y sus extensiones    |
+----------+----------+        +----------+-----------+
           |                              |
           v                              v
+---------------------+        +----------------------+
| Truth Store         |        | Sense Store          |
|---------------------|        |----------------------|
| mantiene V_i        |        | mantiene S_i         |
+----------+----------+        +----------+-----------+
           \                              /
            \                            /
             v                          v
              +------------------------+
              | Operational Projector  |
              |------------------------|
              | calcula W_i^*          |
              +-----------+------------+
                          |
                          v
              +------------------------+
              | Query and Index Engine |
              |------------------------|
              | indexa, filtra,        |
              | intersecta y proyecta  |
              +-----------+------------+
                          |
                          v
              +------------------------+
              | Refinement Engine      |
              |------------------------|
              | detecta colisiones,    |
              | crea subcontextos      |
              +------------------------+
```

## 3. Modelo de datos

## 3.1. Tipos base

```text
type ContextId
type EntityId
type RelationId
type PropertyId
type TypeId
type CoordinateId

enum TruthValue = { True, False }
enum SenseValue = { Applicable, Inapplicable }

enum EvaluationStatus = {
  TrueWithSense,
  FalseWithSense,
  Inapplicable,
  OutOfLogicSpace,
  IllFormed,
  Trivial
}
```

## 3.2. Firmas y coordenadas

```text
type RelationSignature = {
  relation: RelationId,
  arity: Integer,
  argumentTypes: TypeId[]
}

type UnaryCoordinate = {
  relation: PropertyId,
  subject: EntityId
}

type NaryCoordinate = {
  relation: RelationId,
  arguments: EntityId[]
}

type Coordinate = UnaryCoordinate | NaryCoordinate
```

## 3.3. Capas de almacenamiento

```text
type TruthStore = Map<Coordinate, TruthValue>
type SenseStore = Map<Coordinate, SenseValue>
type OperationalStore = BitSet<Coordinate>
```

## 3.4. Indices

```text
type EntityIndex = Map<EntityId, Set<Coordinate>>
type RelationIndex = Map<RelationId | PropertyId, Set<Coordinate>>
type SignatureIndex = Map<RelationSignature, Set<Coordinate>>
type ContextIndex = Map<ContextId, Set<Coordinate>>
```

## 3.5. Estructura principal del contexto

```text
type Context = {
  id: ContextId,
  entities: Set<EntityId>,
  properties: Set<PropertyId>,
  relations: Set<RelationSignature>,
  logicSpace: Set<Coordinate>,
  truthStore: TruthStore,
  senseStore: SenseStore,
  operationalStore: OperationalStore,
  entityIndex: EntityIndex,
  relationIndex: RelationIndex,
  signatureIndex: SignatureIndex,
  parentContext: ContextId | Null,
  childContexts: Set<ContextId>
}
```

## 4. Diagrama UML principal

```text
+-------------------+
| Context           |
+-------------------+
| id                |
| entities          |
| properties        |
| relations         |
| logicSpace        |
| truthStore        |
| senseStore        |
| operationalStore  |
| entityIndex       |
| relationIndex     |
| signatureIndex    |
+-------------------+
| extendEntity      |
| extendProperty    |
| extendRelation    |
| createSubcontext  |
| projectSubcontext |
| evaluate          |
| query             |
+---------+---------+
          |
          | uses
          v
+-------------------+      +-------------------+
| TypeSystem        |      | QueryEngine       |
+-------------------+      +-------------------+
| validateSignature |      | select            |
| validateCoordinate|      | conjunct          |
| validateExtension |      | disjunct          |
+-------------------+      | patternMatch      |
                           +---------+---------+
                                     |
                                     v
                           +-------------------+
                           | RefinementEngine  |
                           +-------------------+
                           | detectTautology   |
                           | detectCollision   |
                           | suggestExtension  |
                           +-------------------+
```

## 5. Invariantes de la estructura

Todo contexto debe satisfacer:

- toda coordenada en `truthStore` pertenece a `logicSpace`,
- toda coordenada en `senseStore` pertenece a `logicSpace` o a una extension declarada de este,
- `operationalStore(c) = 1` si y solo si `truthStore(c)=True` y `senseStore(c)=Applicable`,
- todo indice debe poder reconstruirse a partir de `logicSpace`, `truthStore` y `senseStore`,
- todo subcontexto debe declarar su relacion con un contexto padre o su autonomia.

## 6. Operatoria minima

## 6.1. Construccion del contexto

```text
procedure BuildContext(specification):
  context <- NewContext(specification.id)

  context.entities <- specification.entities
  context.properties <- specification.properties
  context.relations <- specification.relations

  context.logicSpace <- GenerateLogicSpace(
    context.entities,
    context.properties,
    context.relations
  )

  context.senseStore <- InitializeSenseStore(
    context.logicSpace,
    specification.applicabilityRules
  )

  context.truthStore <- InitializeTruthStore(
    context.logicSpace,
    specification.factAssignments
  )

  context.operationalStore <- ProjectOperationalStore(
    context.truthStore,
    context.senseStore
  )

  RebuildIndexes(context)

  return context
end procedure
```

## 6.2. Evaluacion de coordenadas

```text
procedure EvaluateCoordinate(context, coordinate):
  if not IsWellFormed(coordinate, context.relations) then
    return IllFormed
  end if

  if coordinate not in context.logicSpace then
    return OutOfLogicSpace
  end if

  if context.senseStore[coordinate] = Inapplicable then
    return Inapplicable
  end if

  if IsTrivial(context, coordinate) then
    return Trivial
  end if

  if context.truthStore[coordinate] = True then
    return TrueWithSense
  end if

  return FalseWithSense
end procedure
```

## 6.3. Proyeccion operativa

```text
procedure ProjectOperationalStore(truthStore, senseStore):
  projected <- EmptyBitSet()

  for each coordinate in truthStore.keys do
    if truthStore[coordinate] = True and senseStore[coordinate] = Applicable then
      projected.add(coordinate)
    end if
  end for

  return projected
end procedure
```

## 6.4. Consulta

### Seleccion por propiedad

```text
procedure SelectByProperty(context, property):
  result <- {}

  for each entity in context.entities do
    coordinate <- MakeUnaryCoordinate(property, entity)
    status <- EvaluateCoordinate(context, coordinate)

    if status = TrueWithSense then
      result <- result union {entity}
    end if
  end for

  return result
end procedure
```

### Consulta conjuntiva

```text
procedure ConjunctiveQuery(context, properties):
  candidates <- context.entities

  for each property in properties do
    candidates <- candidates intersect SelectByProperty(context, property)
  end for

  return candidates
end procedure
```

### Consulta por patron relacional

```text
procedure PatternQuery(context, partialCoordinate):
  candidates <- RetrieveByRelationIndex(context, partialCoordinate.relation)
  return FilterByBoundArguments(candidates, partialCoordinate)
end procedure
```

## 6.5. Deteccion de tautologias

```text
procedure DetectTautologicalProperties(context):
  tautologies <- {}

  for each property in context.properties do
    allTrue <- True

    for each entity in context.entities do
      coordinate <- MakeUnaryCoordinate(property, entity)

      if context.senseStore[coordinate] = Applicable and
         context.truthStore[coordinate] = False then
        allTrue <- False
        break
      end if
    end for

    if allTrue then
      tautologies <- tautologies union {property}
    end if
  end for

  return tautologies
end procedure
```

## 6.6. Deteccion de ambiguedad

```text
procedure DetectIndistinguishableEntities(context, featureBasis):
  signatures <- EmptyMap()

  for each entity in context.entities do
    vector <- []

    for each property in featureBasis do
      coordinate <- MakeUnaryCoordinate(property, entity)
      vector.append((context.truthStore[coordinate], context.senseStore[coordinate]))
    end for

    signatures[entity] <- vector
  end for

  return GroupEqualVectors(signatures)
end procedure
```

## 6.7. Creacion de subcontextos

```text
procedure CreateSubcontext(parentContext, entityFilter, propertyFilter, relationFilter):
  child <- NewContext(NewContextId())

  child.entities <- Filter(parentContext.entities, entityFilter)
  child.properties <- Filter(parentContext.properties, propertyFilter)
  child.relations <- Filter(parentContext.relations, relationFilter)
  child.logicSpace <- RestrictLogicSpace(parentContext.logicSpace, child)
  child.truthStore <- RestrictTruthStore(parentContext.truthStore, child.logicSpace)
  child.senseStore <- RestrictSenseStore(parentContext.senseStore, child.logicSpace)
  child.operationalStore <- ProjectOperationalStore(child.truthStore, child.senseStore)
  child.parentContext <- parentContext.id

  RebuildIndexes(child)
  RegisterChild(parentContext, child)

  return child
end procedure
```

## 6.8. Proyeccion de subcontextos sobre el contexto base

```text
procedure ProjectSubcontext(parentContext, childContext, newProperties):
  for each property in newProperties do
    parentContext.properties.add(property)

    for each entity in parentContext.entities do
      coordinate <- MakeUnaryCoordinate(property, entity)
      parentContext.logicSpace.add(coordinate)

      if entity in childContext.entities then
        parentContext.senseStore[coordinate] <- Applicable
        parentContext.truthStore[coordinate] <- childContext.truthStore[coordinate]
      else
        parentContext.senseStore[coordinate] <- Inapplicable
      end if
    end for
  end for

  parentContext.operationalStore <- ProjectOperationalStore(
    parentContext.truthStore,
    parentContext.senseStore
  )

  RebuildIndexes(parentContext)

  return parentContext
end procedure
```

## 6.9. Extension del contexto

### Nueva entidad

```text
procedure ExtendWithEntity(context, entity, senseEvaluator, truthEvaluator):
  context.entities.add(entity)

  for each property in context.properties do
    coordinate <- MakeUnaryCoordinate(property, entity)
    context.logicSpace.add(coordinate)
    context.senseStore[coordinate] <- senseEvaluator(entity, property)

    if context.senseStore[coordinate] = Applicable then
      context.truthStore[coordinate] <- truthEvaluator(entity, property)
    end if
  end for

  context.operationalStore <- ProjectOperationalStore(context.truthStore, context.senseStore)
  RebuildIndexes(context)

  return context
end procedure
```

### Nueva propiedad

```text
procedure ExtendWithProperty(context, property, senseEvaluator, truthEvaluator):
  context.properties.add(property)

  for each entity in context.entities do
    coordinate <- MakeUnaryCoordinate(property, entity)
    context.logicSpace.add(coordinate)
    context.senseStore[coordinate] <- senseEvaluator(entity, property)

    if context.senseStore[coordinate] = Applicable then
      context.truthStore[coordinate] <- truthEvaluator(entity, property)
    end if
  end for

  context.operationalStore <- ProjectOperationalStore(context.truthStore, context.senseStore)
  RebuildIndexes(context)

  return context
end procedure
```

### Nueva relacion

```text
procedure ExtendWithRelation(context, relationSignature, coordinateGenerator, senseEvaluator, truthEvaluator):
  context.relations.add(relationSignature)

  newCoordinates <- coordinateGenerator(context, relationSignature)

  for each coordinate in newCoordinates do
    context.logicSpace.add(coordinate)
    context.senseStore[coordinate] <- senseEvaluator(coordinate)

    if context.senseStore[coordinate] = Applicable then
      context.truthStore[coordinate] <- truthEvaluator(coordinate)
    end if
  end for

  context.operationalStore <- ProjectOperationalStore(context.truthStore, context.senseStore)
  RebuildIndexes(context)

  return context
end procedure
```

## 7. Maquina de estados de evaluacion

```text
                 +------------------+
                 | Input Coordinate |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Well formed?     |
                 +----+--------+----+
                      |        |
                    no|        |yes
                      |        v
                      |  +------------------+
                      |  | In logic space?  |
                      |  +----+--------+----+
                      |       |        |
                      |     no|        |yes
                      |       |        v
                      |       |  +------------------+
                      |       |  | Has sense?       |
                      |       |  +----+--------+----+
                      |       |       |        |
                      |       |     no|        |yes
                      |       |       |        v
                      |       |       |  +------------------+
                      |       |       |  | Is trivial?      |
                      |       |       |  +----+--------+----+
                      |       |       |       |        |
                      |       |       |     yes        | no
                      |       |       |       |        v
                      |       |       |       |  +------------------+
                      |       |       |       |  | Truth value?     |
                      |       |       |       |  +----+--------+----+
                      |       |       |       |       |        |
                      |       |       |       |     0 |        | 1
                      v       v       v       v       v        v
                 IllFormed OutOfLogicSpace Inapplicable Trivial FalseWithSense TrueWithSense
```

## 8. Ejemplo: verduras

## 8.1. Contexto base

```text
Context Vegetables
  Entities   = {lettuce, spinach, carrot, celery}
  Properties = {vegetable, food, leaf, root, stem}
```

## 8.2. Resultado analitico esperado

```text
DetectTautologicalProperties(Vegetables)
  returns {vegetable, food}

DetectIndistinguishableEntities(Vegetables, {leaf, root, stem})
  returns {{lettuce, spinach}}
```

## 8.3. Refinamiento y reproyeccion

```text
child <- CreateSubcontext(
  Vegetables,
  entityFilter   = entities with leaf = 1,
  propertyFilter = {rough, smooth},
  relationFilter = unary only
)

ProjectSubcontext(Vegetables, child, {rough, smooth})
```

Efecto esperado:

- `rough` y `smooth` quedan disponibles en el espacio base,
- para `lettuce` y `spinach` tienen `S_i = Applicable`,
- para `carrot` y `celery` tienen `S_i = Inapplicable`.

## 9. Indices minimos recomendados

Para que la maquina sea realmente consultable, conviene mantener al menos estos indices materializados:

- indice por entidad,
- indice por propiedad o relacion,
- indice por firma relacional,
- indice por contexto y subcontexto,
- indice de colisiones descriptivas para bases de rasgos frecuentes.

## 10. Decisiones de diseño

- `truthStore` y `senseStore` deben ser fuentes primarias,
- `operationalStore` debe ser siempre derivado,
- toda extension debe disparar recalculo local de indices,
- la desambiguacion debe poder producir nuevas propiedades o nuevos subcontextos,
- la proyeccion de subcontextos debe conservar explicitamente los casos `Inapplicable`,
- la implementacion debe distinguir siempre entre `FalseWithSense` e `Inapplicable`.

## 11. Cierre

La forma mas estable de implementar el sistema es tratarlo como una maquina de capas bien diferenciadas:

- una capa de firmas y tipos,
- una capa de coordenadas logicas,
- una capa de verdad,
- una capa de sentido,
- una proyeccion operativa derivada,
- una capa de indices,
- y una capa de refinamiento contextual.

Con esa separacion, el paso desde la teoria a una implementacion concreta puede hacerse despues en cualquier lenguaje sin perder claridad sobre las estructuras de datos ni sobre la operatoria necesaria.
