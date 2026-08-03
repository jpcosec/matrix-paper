# CanonicalHypertensor

El `CanonicalHypertensor` representa el estado global del "Mundo" como un objeto matemático estructurado y procesado a través de JAX. Encapsula la matriz de estados lógicos y las probabilidades asociadas a los hechos, garantizando que el estado sea un modelo válido y consistente.

## Estructura de Software

```python
import jax.numpy as jnp
import jax

class CanonicalHypertensor:
    def __init__(self, dimensions: int):
        self.shape = tuple([2] * dimensions)  # 2 estados (V/F) por dimensión
        self._tensor = jnp.zeros(shape=self.shape)
        self._mask = jnp.ones_like(self._tensor, dtype=bool)

    def update_state(self, tensor_update: jax.Array) -> None:
        """Actualiza el estado tensorial interno utilizando operaciones JAX optimizadas."""
        pass
        
    def get_state(self) -> jax.Array:
        """Retorna el estado tensorial actual para consultas, visualizaciones o serialización."""
        return self._tensor
        
    def collapse(self, observation_mask: jax.Array) -> None:
        """Reduce el espacio de estados eliminando (poniendo a 0) los mundos posibles inconsistentes con la observación."""
        pass
```

## Relaciones (5W1H+)
- **WHAT**: Estructura de datos core que almacena el tensor JAX subyacente del espacio lógico.
- **WHY**: Para mantener un estado inmutable/versionado compatible con aceleración en hardware (GPU/TPU) vía JAX.
- **HOW**: Utiliza `jax.numpy.ndarray` para representar el espacio de estados discretos propuesto por Wittgenstein.
- **WHERE_USES**: Interactúa con los átomos matemáticos de álgebra tensorial en JAX.
- **WHO_USES**: `MEELEngine` lo instancia, muta y consulta a lo largo del ciclo de vida de la aplicación.
