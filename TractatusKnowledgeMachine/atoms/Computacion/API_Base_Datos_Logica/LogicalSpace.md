# LogicalSpace

El `LogicalSpace` define la topología, las dimensiones y las variables proposicionales sobre las cuales el `CanonicalHypertensor` operará. Actúa como el esquema, registro o diccionario de datos que mapea los conceptos humanos y semánticos (ej. "Llueve", "Hace frío") a los ejes y coordenadas específicas del hipertensor.

## Estructura de Software

```python
class LogicalSpace:
    def __init__(self, vocab: dict[str, int] = None):
        self.vocabulary = vocab or {}  # Mapeo de proposiciones (str) a ejes (int)
        
    @property
    def dimensions(self) -> int:
        return len(self.vocabulary)
        
    def register_proposition(self, name: str) -> int:
        """Registra una nueva proposición atómica y expande las dimensiones lógicas del espacio."""
        if name not in self.vocabulary:
            self.vocabulary[name] = self.dimensions
        return self.vocabulary[name]
        
    def proposition_to_index(self, name: str) -> int:
        """Traduce un símbolo de proposición atómica a su correspondiente índice de eje tensorial."""
        return self.vocabulary.get(name, -1)
        
    def validate_bounds(self, index: int) -> bool:
        """Asegura que las operaciones tensoriales no excedan los límites dimensionales registrados en el espacio."""
        return 0 <= index < self.dimensions
```

## Relaciones (5W1H+)
- **WHAT**: Mapeo simbólico-numérico y definición de las dimensiones del hiperespacio lógico.
- **WHY**: Permite a la capa superior (motor) trabajar con símbolos semánticos interpretables ("p", "q") mientras el backend JAX opera nativamente sobre índices y ejes numéricos.
- **HOW**: Manteniendo tablas hash o diccionarios bidireccionales eficientes en memoria.
- **WHERE_USES**: Complementa a `CanonicalHypertensor` para darle semántica a sus dimensiones.
- **WHO_USES**: `MEELEngine` lo utiliza para traducir y enrutar las aserciones y consultas hacia operaciones matemáticas concretas.
