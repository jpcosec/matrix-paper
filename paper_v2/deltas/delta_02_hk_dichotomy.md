# Delta 2 — Dicotomía HK⁺/HK⁻ en SOTA

**Responde a:** Eje A / `ppL8` (literatura de causas: ICLR). Refuerza el argumento central: el modelo *sabe* pero corrompe al decodificar.

## DESDE (átomos KB origen)

| Átomo | Aporta |
|---|---|
| `Antecedentes/Alucinaciones/Dicotomia_HK_Minus_vs_HK_Plus.md` | Dicotomía HK⁻ (ignorancia) vs HK⁺ (conocimiento latente corrompido en decodificación) |
| `Antecedentes/Limites_Espacio_Continuo/Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente.md` | Marco: incongruencia decodificación estocástica vs conocimiento latente |
| `Antecedentes/Limites_Espacio_Continuo/Probing_Latente_y_Decodificacion.md` | Evidencia de probing: tokens internos codifican veracidad |

## DESDE+ ampliación KB (referencias adicionales)

| Átomo | Aporte |
|---|---|
| `Computacion/Estructuras_Matriciales/Distincion_Ausencia_vs_Unsinnig.md` | Tres estados por celda: ausencia ≠ unsinnig ≠ verdad — base operativa de HK$^-$/HK$^+$ |
| `Filosofia/Epistemologia_y_Contextos/Estados_Verdad_Epistemicos_Semanticos.md` | Separación explícita estado semántico ($S_i$) / epistémico / veritativo |
| `Computacion/Estructuras_Matriciales/Capa_Verdad_Vi.md` | $V_i$: capa veritativa con ausencia explícita de hecho |
| `Computacion/Estructuras_Matriciales/Procedencia_y_Evidencia.md` | Procedencia y evidencia por hecho (trazabilidad HK) |
| `Computacion/Operaciones_DB_Logica/Operacion_Identificar_Faltantes.md` | HK$^-$ operacionalizado: detectar lo desconocido |
| `Computacion/Operaciones_DB_Logica/Operacion_Justificar.md` | Justificación determinista (vs. "know more than they show") |
| `Antecedentes/Alucinaciones/Diferenciacion_Factualidad_Conocimiento_Alucinacion.md` | Taxonomía factualidad/conocimiento/alucinación |
| `Antecedentes/Alucinaciones/Ley_del_Ocultamiento_del_Conocimiento_Knowledge_Overshadowing.md` | Knowledge overshadowing (mecanismo HK$^+$) |
| `Antecedentes/Alucinaciones/Ilusion_de_la_Autocorreccion.md` | HK$^+$: autocorrección ilusoria sin señal externa |

**Extensión mapping (`01_1_sota-p03`, bridge `delta2_review`):**
```yaml
   - {atom_id: atom-distincion-ausencia-vs-unsinnig, atom_path: Computacion/Estructuras_Matriciales/Distincion_Ausencia_vs_Unsinnig.md, bridge: delta2_review, score: 0.9, detail: "three cell states: absence/unsinnig/truth"}
   - {atom_id: atom-estados-verdad-epistemicos-semanticos, atom_path: Filosofia/Epistemologia_y_Contextos/Estados_Verdad_Epistemicos_Semanticos.md, bridge: delta2_review, score: 0.9, detail: "semantic vs epistemic vs truth state"}
   - {atom_id: atom-capa-verdad-vi, atom_path: Computacion/Estructuras_Matriciales/Capa_Verdad_Vi.md, bridge: delta2_review, score: 0.85, detail: "V_i veritative layer, explicit absence"}
   - {atom_id: atom-procedencia-y-evidencia, atom_path: Computacion/Estructuras_Matriciales/Procedencia_y_Evidencia.md, bridge: delta2_review, score: 0.85, detail: "per-fact provenance"}
   - {atom_id: atom-operacion-identificar-faltantes, atom_path: Computacion/Operaciones_DB_Logica/Operacion_Identificar_Faltantes.md, bridge: delta2_review, score: 0.85, detail: "HK- operationalized"}
   - {atom_id: atom-operacion-justificar, atom_path: Computacion/Operaciones_DB_Logica/Operacion_Justificar.md, bridge: delta2_review, score: 0.8, detail: "deterministic justification"}
   - {atom_id: atom-diferenciacion-factualidad-conocimiento-alucinacion, atom_path: Antecedentes/Alucinaciones/Diferenciacion_Factualidad_Conocimiento_Alucinacion.md, bridge: delta2_review, score: 0.8, detail: "factuality/knowledge/hallucination taxonomy"}
   - {atom_id: atom-ley-del-ocultamiento-del-conocimiento-knowledge-overshadowing, atom_path: Antecedentes/Alucinaciones/Ley_del_Ocultamiento_del_Conocimiento_Knowledge_Overshadowing.md, bridge: delta2_review, score: 0.75, detail: "knowledge overshadowing (HK+ mechanism)"}
   - {atom_id: atom-ilusion-de-la-autocorreccion, atom_path: Antecedentes/Alucinaciones/Ilusion_de_la_Autocorreccion.md, bridge: delta2_review, score: 0.75, detail: "illusory self-correction (HK+)"}
```

## HACIA (párrafo destino)

- **`Neurips_peiper/sections/01_1_sota.md`**, párrafo `Internal Representations and Latent Probing` (hoy `01_1_sota-p03`).
- **Modo:** añadir 2 frases **al final de ese párrafo**, antes de su punto final actual. No crea párrafo nuevo → no renumeración.
- **No requiere anexo.**

## Propuesta de texto (añadir tras `…rather than a mere absence of information.`)

```markdown
This dichotomy is now empirically grounded: hallucinations split into $HK^{-}$ cases, where the model genuinely lacks the knowledge, and $HK^{+}$ cases, where the correct answer is encoded in latent activations yet corrupted during stochastic decoding [@orgad2025iclr; @simhi2024distinguishing]. The $HK^{+}$ regime is precisely the failure mode a discrete sense mask addresses: the knowledge exists, but no rigid boundary prevents its corruption.
```

## bib / átomos / mapping

- **bib:** nada — `orgad2025iclr` y `simhi2024distinguishing` ya están en `references.bib`.
- ⚠️ **Resolver duplicado:** `orgad2025apple` ("Language Models Know More Than They Show…") y `orgad2025iclr` ("LLMs Know More Than They Show…", ICLR) parecen el mismo paper retitulado. Propuesta: conservar `orgad2025iclr` (versión publicada), citar solo esa, y borrar `orgad2025apple` de bib + reemplazar su cita en p03. El átomo `Fuentes/Source_PDF_iclr2025_a712d4_pdf.md` ya representa ese paper.
- **Átomos nuevos:** 1 vía `atomize_sources.py` → `Source_PDF_simhi2024distinguishing_pdf.md` (el de Orgad ya existe como `iclr2025_a712d4`).
- **mapping.yaml** (`01_1_sota-p03`, añadir):
```yaml
   - {atom_id: atom-source-pdf-simhi2024distinguishing, atom_path: Fuentes/Source_PDF_simhi2024distinguishing_pdf.md, bridge: bib, score: 1.0, detail: "[@simhi2024distinguishing]"}
   - {atom_id: atom-incongruencia-decodificacion-estocastica-vs-conocimiento-latente, atom_path: Antecedentes/Limites_Espacio_Continuo/Incongruencia_Decodificacion_Estocastica_vs_Conocimiento_Latente.md, bridge: delta2_review, score: 0.9, detail: "marco incongruencia decodificación/latente"}
   - {atom_id: atom-probing-latente-y-decodificacion, atom_path: Antecedentes/Limites_Espacio_Continuo/Probing_Latente_y_Decodificacion.md, bridge: delta2_review, score: 0.85, detail: "probing: tokens internos codifican veracidad"}
```
(`Dicotomia_HK_Minus_vs_HK_Plus` ya está anclada a p03 vía `bib_transitive`.)

## Riesgos
- Confirmar que apple/iclr son el mismo paper leyendo ambos PDFs (`review/related_papers/` no los incluye; están fuera del repo).
