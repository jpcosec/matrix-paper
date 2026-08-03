# Vista Materializada: Clausura Transitiva Persistente

Una "Vista Materializada" clásica es el pre-cálculo y almacenamiento del resultado de un Query muy costoso computacionalmente, para acelerar su consumo posterior. En MEEL, este concepto se extrapola a la **persistencia de la inferencia deductiva**.

- **El Costo del `Deduce`:** El motor deductivo toma el tensor de hechos explícitos y aplica iterativamente las reglas lógicas del sistema, propagando la verdad matemática hasta que no se deducen hechos nuevos.
- **La Vista Materializada como Clausura:** El hiper-tensor resultante, tras un ciclo exhaustivo de `Deduce`, encierra en sí la *clausura transitiva* del conocimiento: todo hecho implícito ha sido explícitamente derivado y posicionado en sus coordenadas ortogonales.
- **O(1) para Teoremas:** Al persistir este hiper-tensor denso (Vista Materializada), futuras operaciones o queries que dependan de razonamientos complejos no tendrán que re-evaluar la matriz lógica. Teoremas e inferencias de múltiples saltos se habrán "cristalizado" en coordenadas factuales de acceso directo, ofreciendo rendimiento de lectura instantáneo.
