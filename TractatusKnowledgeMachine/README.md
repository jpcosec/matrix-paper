# Tractatus Knowledge Machine — SSOT de átomos

Base de conocimiento atómica de **Matrix**. Acá vive la verdad durable sobre
arquitectura, conceptos, demostraciones y fuentes; los `docs/` de los repos
consumidores son **materializaciones** de estos átomos, no la fuente.

- Índice/taxonomía: [`atoms/Propuesta_Indice.md`](atoms/Propuesta_Indice.md)
- Catálogo de predicados: [`atoms/predicates-5w1h.yaml`](atoms/predicates-5w1h.yaml)
- Repo que materializa estos átomos: [`../Matrix`](../Matrix) (gitlink pineado al commit correspondiente)

## Estructura

```
atoms/
  Antecedentes/            límites del paradigma estocástico, alucinaciones
  Aplicaciones/            demostraciones ejecutables y dominios (culinario, KB fan-out)
  Computacion/             kernel, matrices, modelos de datos, operaciones, runtimes
  Filosofia/               epistemología, contextos, Tractatus
  Fuentes/                 átomos de código y PDFs oráculo
  Isomorfismo_Tractatus_Algebra/
  Matematica/              álgebra booleana, retículos, tensores, desambiguación
  Teoria_de_Bases_de_Datos/
  composiciones_review/    composiciones (trackeadas por SLDB)
  composiciones_spec/      specs (trackeadas por SLDB)
```

## Formato de un átomo

Frontmatter YAML:

```yaml
topic: <slug-del-tema>
use_when: Cuándo corresponde usar/consultar este átomo.
do_not_use_when: Cuándo NO (evita solapamientos).
id: atom-<slug>
title: <Título>
five_wh_one_plus: what | how | why | when | where | who | provenance
tags:
- system:matrix
```

Cuerpo:

```markdown
# <Título>

**Categoría Padre:** [[<Área o submódulo>]]
**Relaciones 5W1H+:**
* [<predicado>:: [[<Átomo destino>]]]

## Qué es
## Por qué es necesario
## Cómo funciona
## Cuándo interviene
## Dónde reside
## Para qué / Para quién
```

Predicados disponibles (ver `atoms/predicates-5w1h.yaml`):

| predicado | eje | uso |
|---|---|---|
| `defines` | WHAT | define el concepto destino |
| `is_solved_by` | HOW | cómo se resuelve |
| `implements` | HOW | mapea teoría → código ejecutable |
| `mathematically_proves` | WHY | demostración formal |
| `explains_failure_of` | WHY | por qué falla un enfoque alternativo |
| `grounded_by` | PROVENANCE | anclaje a fuente oráculo |
| `restricts` | WHEN/WHERE | ámbito de aplicabilidad (frontera de `Si`) |

## Cómo agregar un átomo

1. Elegí el área y subcarpeta en `atoms/` (si es nueva, agregala al índice).
2. Copiá el formato de arriba; `use_when` y `do_not_use_when` no son opcionales.
3. Enlazá con 2–4 predicados a átomos existentes (evitá huérfanos).
4. Actualizá `atoms/Propuesta_Indice.md` (conteo del subdirectorio + bullet).
5. Si el átomo cambia una regla de un repo consumidor, materializala ahí (docs) y dejá el átomo como fuente.

## Átomos recientes relevantes

| átomo | qué fija |
|---|---|
| `Computacion/Modelos_Datos_MEEL/WiGame_Contexto_y_Desambiguacion` | un WiGame es (ejes + relación) **bajo un contexto**; `Si` local, árbol de contextos, desambiguación acumulativa, identidad por curación |
| `Computacion/Estructuras_Matriciales/Maquina_de_Estados_como_WiGame` | `Vi` = matriz de transición, `Si` = guarda; cierre = alcanzabilidad, firmas = minimización |
| `Aplicaciones/Dominio_Culinario/Operatoria_Lectura_de_Recetas` | operatoria autorada para leer recetas como máquinas de estados |
| `Aplicaciones/KB_Fanout_y_Stress_de_Contextos` | pipeline propuestas→revisión→compile context-scoped y mediciones de escala |
| `Aplicaciones/Dominio_Culinario/Demostracion_Dominio_Culinario_Ragout` | demo de 5 etapas (`W* = (Vi ∨ Di) ∧ Si`), hoy ejecutable en `Matrix/examples/ragout_demonstration.py` |

## Estado

- Átomos: 273+ `.md` en `atoms/`.
- `composiciones_review/` y `composiciones_spec/` están trackeadas por SLDB (`.sldb/`); el resto de `atoms/` se versiona como Markdown.
