# paper_v2 astro app

UI mínima para ver y editar la estructura de `paper_v2`.

## Qué hace

- lista docs de:
  - `sources/`
  - `notes/`
  - `paragraphs/`
  - `sections/`
  - `manuscript/`
  - `build/`
- abre un doc en textarea
- guarda cambios al archivo real
- ejecuta `python3 build_pipeline.py`
- permite cargar rápido `build/paper.composed.md`

## Ejecutar

```bash
cd paper_v2/astro_app
npm install
npm run dev
```

Luego abre:

```text
http://localhost:4321
```

## Endpoints

- `GET /api/tree.json`
- `GET /api/doc.json?path=...`
- `POST /api/doc.json`
- `POST /api/rebuild.json`
