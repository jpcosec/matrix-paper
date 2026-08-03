# MEELEngine

El `MEELEngine` es el orquestador principal del motor de inferencia Matrix MEEL. Actúa como la interfaz pública (API) que abstrae la complejidad matemática subyacente de las operaciones tensoriales en JAX, permitiendo interactuar con el espacio lógico mediante aserciones, deducciones y consultas.

## Firmas de Métodos Principales

```python
class MEELEngine:
    def __init__(self, logical_space: 'LogicalSpace'):
        self.space = logical_space
        self.hypertensor = CanonicalHypertensor(logical_space.dimensions)

    def assert_fact(self, proposition: 'Proposition') -> 'CanonicalHypertensor':
        """Asienta un hecho atómico o molecular en el espacio lógico, actualizando el hipertensor canónico."""
        pass

    def deduce(self) -> 'CanonicalHypertensor':
        """Aplica las reglas de inferencia para propagar el valor de verdad a través de las relaciones lógicas (multiplicación tensorial)."""
        pass

    def query(self, query_proposition: 'Proposition') -> 'TruthValue':
        """Consulta el estado de verdad de una proposición específica en la configuración actual del mundo."""
        pass
        
    def evaluate_sense(self, proposition: 'Proposition') -> bool:
        """Evalúa si una proposición tiene sentido (bipolaridad) dentro de los límites del espacio lógico definido."""
        pass
```

## Relaciones (5W1H+)
- **WHAT**: API principal del motor de inferencia probabilístico-lógico.
- **WHY**: Abstrae las operaciones de álgebra lineal y tensores (JAX) en operaciones lógicas semánticamente ricas.
- **HOW**: Envolviendo las mutaciones de estado sobre `CanonicalHypertensor` mediante llamadas a backend JAX.
- **WHO_USES**: Capa de aplicación, agentes lógicos, sistemas de consulta simbólica.
- **WHERE_USES**: Apunta a `CanonicalHypertensor.md` y `LogicalSpace.md`.
- **WHEN**: Durante la inicialización del sistema y el ciclo de interacción aserción-deducción-consulta.
