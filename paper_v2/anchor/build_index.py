#!/usr/bin/env python3
"""
anchor/build_index.py — Fase 0+1: anclaje determinista KB -> paper.

Bridges:
  a. atoms_index.json    : indice de los atomos .md de la KB (frontmatter + links + predicados)
  b. paragraphs          : parseo de paragraphs/*.md (anchor, seccion, texto, bibkeys)
  c. bib bridge          : bibkeys <-> atomos Source_PDF_* via comp_fuentes.md (Apellido+anyo)
                           + transitivo via predicado grounded_by
  d. lexical bridge      : solape de terminos distintivos texto-parrafo vs titulo/filename atomo
  e. composition bridge  : cadenas de composiciones_review/comp_*.md + draft section_compositions

Salidas en anchor/build/: atoms_index.json, candidates.json, mapping_draft.yaml, summary.md

Uso:  python3 anchor/build_index.py        (desde paper_v2/)
Solo stdlib + pyyaml. No modifica ningun archivo existente.
"""

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import yaml

# ---------------------------------------------------------------- paths
SCRIPT_DIR = Path(__file__).resolve().parent            # paper_v2/anchor
PAPER_V2 = SCRIPT_DIR.parent                            # paper_v2/
MATRIX_ROOT = PAPER_V2.parent                           # Matrix/
ATOMS_DIR = MATRIX_ROOT / "TractatusKnowledgeMachine" / "atoms"
PARAGRAPHS_DIR = PAPER_V2 / "paragraphs"
SECTIONS_DIR = PAPER_V2 / "sections"
BIB_FILE = MATRIX_ROOT / "Neurips_peiper" / "references.bib"
BUILD_DIR = SCRIPT_DIR / "build"

EXPECTED_SECTIONS = [
    "01_introduction",
    "01_1_sota",
    "02_philosophical_foundation",
    "03_proposed_representation",
    "04_discussion",
    "09_conclusion",
]

# Draft curado (determinista): seccion -> [(composicion, justificacion)]
# Justificaciones contrastadas con el frontmatter 'question' de cada comp_*.md.
CURATED_SECTION_COMPS = {
    "01_introduction": [
        ("comp_antecedentes",
         "El intro plantea la necesidad de primitivos discretos: la pregunta central de esta composicion."),
        ("comp_isomorfismo",
         "La tesis del intro (la discrecion es exigencia, no opcion) es exactamente la pregunta del isomorfismo Tractatus-Algebra."),
    ],
    "01_1_sota": [
        ("comp_eje_d",
         "El SotA diferencia el marco de RAG, KGs/OWL y neuro-simbolicos previos: contenido literal del Eje D."),
        ("comp_fuentes",
         "Las citas del SotA (hallucination detection, model collapse, HK+/-) son los Source_PDF de esta composicion."),
        ("comp_antecedentes",
         "El estado del arte sobre alucinaciones y limites del continuo corresponde a la carpeta Antecedentes."),
    ],
    "02_philosophical_foundation": [
        ("comp_filosofia",
         "Fundamentacion filosofica: discontinuidades ontologicas que ningun espacio continuo aproxima."),
        ("comp_isomorfismo",
         "El isomorfismo Tractatus-Algebra es la base formal de la seccion filosofica."),
    ],
    "03_proposed_representation": [
        ("comp_computacion",
         "La representacion propuesta (kernel Booleano, Si binaria) es la cadena de la carpeta Computacion."),
        ("comp_matematica",
         "Las pruebas de imposibilidad continua justifican matematicamente la representacion discreta propuesta."),
        ("comp_eje_b",
         "Eje B responde como se crean S_i y V_i a escala: nucleo operativo de la representacion propuesta."),
    ],
    "04_discussion": [
        ("comp_eje_a",
         "La discusion recorre necesidad, limite del continuo y demostracion: las tres sub-preguntas del Eje A."),
        ("comp_gaps",
         "Limitaciones y trabajo futuro de la discusion se apoyan en el registro de gaps argumentativos."),
        ("comp_aplicaciones",
         "Las validaciones empiricas discutidas corresponden a la composicion de Aplicaciones."),
    ],
    "09_conclusion": [
        ("comp_eje_e",
         "La conclusion apunta a la implementacion ejecutable (metricas, arquitectura activa): pregunta del Eje E."),
        ("comp_aplicaciones",
         "Las demostraciones empiricas que cierran el argumento pertenecen a Aplicaciones."),
    ],
}

# ---------------------------------------------------------------- regex
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
PRED_RE = re.compile(r"\[([a-z_][a-z0-9_]*)::\s*\[\[([^\]]+)\]\]")
MATH_EXPR_RE = re.compile(r"\$([^$]+)\$")
MATH_SYM_RE = re.compile(r"(?i)(?<![a-z0-9])([vs wl]_?i)(?![a-z0-9])".replace(" ", ""))
HK_RE = re.compile(r"(?i)\bhk\s*(?:\^|_)?\s*([+-])\b|hk[_-](plus|minus)\b")
TOKEN_RE = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9-]*")

STOPWORDS = {
    # EN basicas
    "the", "and", "for", "with", "that", "this", "from", "are", "was", "were",
    "have", "has", "had", "been", "not", "but", "all", "can", "will", "would",
    "could", "should", "may", "might", "than", "then", "they", "them", "their",
    "there", "where", "when", "what", "which", "while", "these", "those", "such",
    "into", "over", "under", "between", "through", "during", "before", "after",
    "more", "most", "other", "others", "some", "only", "also", "very", "just",
    "about", "above", "across", "each", "both", "does", "doing", "done", "being",
    "however", "thus", "therefore", "hence", "since", "although", "though",
    "because", "within", "without", "among", "along", "per", "via", "its", "our",
    "out", "use", "used", "using", "based", "form", "forms", "make", "makes",
    "made", "show", "shows", "shown", "given", "rather", "either", "neither",
    "whether", "often", "even", "still", "yet", "already", "always", "never",
    "sometimes", "respectively", "furthermore", "moreover", "nevertheless",
    "nonetheless", "consequently", "instead", "indeed", "otherwise", "regarding",
    "despite", "towards", "toward", "upon", "onto", "here", "thereby", "wherein",
    "whereby", "whose", "whom", "must", "shall", "let", "say", "says", "way",
    "ways", "like", "unlike", "much", "many", "few", "less", "least", "several",
    "own", "same", "different", "following", "follows", "according", "provide",
    "provides", "remain", "remains", "become", "becomes", "due", "lack", "lacks",
    # ES basicas
    "los", "las", "una", "unas", "unos", "del", "que", "con", "por", "para",
    "como", "mas", "sus", "son", "esta", "este", "esto", "estos", "estas",
    "entre", "sobre", "desde", "hacia", "donde", "cuando", "cual", "cuales",
    "cuyo", "cuya", "tambien", "pero", "sino", "aunque", "porque", "pues",
    "cada", "todo", "toda", "todos", "todas", "otro", "otra", "otros", "otras",
    "mismo", "misma", "tanto", "tanta", "muy", "sin", "tras", "ante", "bajo",
    "segun", "mediante", "ademas", "entonces", "asimismo", "embargo", "forma",
    "parte", "caso", "casos", "tipo", "tipos", "ejemplo", "decir", "es decir".split()[-1],
    "puede", "pueden", "debe", "deben", "ser", "sea", "sean", "sido", "estan",
    "hay", "tiene", "tienen", "hace", "hacen", "vez", "veces", "algo", "nada",
    "solo", "tan", "asi", "ahi", "aqui", "ahora", "antes", "despues", "siempre",
    "nunca", "quien", "quienes", "cualquier", "cualquiera", "ningun", "ninguna",
    "gran", "grande", "grandes", "nuevo", "nueva", "nuevos", "nuevas",
    # estructurales del corpus KB
    "source", "pdf", "atom", "atomo", "atomos", "carpeta", "composicion",
}

DF_MAX_FRAC = 0.10          # termino presente en >10% de atomos => no distintivo
LEX_TOP_K = 5
COMP_TOP_K = 10
SCORE_BIB = 1.0
SCORE_BIB_TRANSITIVE = 0.8
SCORE_COMPOSITION = 0.4


# ---------------------------------------------------------------- helpers
def norm_text(s: str) -> str:
    """minusculas + sin tildes/diacriticos."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()


def wikilink_stem(raw: str) -> str:
    """[[a/b/C]] -> C ; recorta espacios."""
    return raw.strip().split("/")[-1].strip()


def split_frontmatter(text: str):
    """-> (frontmatter dict, body)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), text[m.end():]


def tokens_from(text: str, stop: set) -> set:
    """tokens alfanumericos >=4 chars, normalizados, sin stopwords."""
    out = set()
    for tok in TOKEN_RE.findall(text):
        t = norm_text(tok).strip("-")
        if len(t) >= 4 and not t.isdigit() and t not in stop:
            out.add(t)
    return out


def math_symbols(text: str) -> set:
    """simbolos matematicos tipo $V_i$,$S_i$,$W_i$,$L_i$ y HK+/HK-/HK_Plus/HK_Minus."""
    out = set()
    for expr in MATH_EXPR_RE.findall(text):
        for m in re.finditer(r"(?i)\b([vswl])\^?\{?_?i\}?\b", expr):
            out.add(m.group(1).lower() + "i")
        for m in re.finditer(r"(?i)hk\s*\^\s*([+-])", expr):
            out.add("hk_plus" if m.group(1) == "+" else "hk_minus")
    for m in MATH_SYM_RE.finditer(text):
        out.add(m.group(1).lower().replace("_", "").replace(" ", "") )
    for m in HK_RE.finditer(text):
        g = m.group(1) or m.group(2) or ""
        out.add("hk_plus" if g in ("+", "plus") else "hk_minus")
    return {s.replace("_", "") for s in out}


# ---------------------------------------------------------------- (a) atoms
def index_atoms():
    atoms = []
    for path in sorted(ATOMS_DIR.rglob("*.md")):
        rel = path.relative_to(ATOMS_DIR).as_posix()
        text = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        stem = path.stem
        title = fm.get("title")
        if not title:
            h1 = re.search(r"^#\s+(.+)$", body, re.M)
            title = h1.group(1).strip() if h1 else stem
        tags = fm.get("tags") or []
        if not isinstance(tags, list):
            tags = [str(tags)]
        wikilinks = [wikilink_stem(w) for w in WIKILINK_RE.findall(body)]
        preds = defaultdict(list)
        for pred, target in PRED_RE.findall(body):
            preds[pred].append(wikilink_stem(target))
        parent = str(Path(rel).parent)
        atoms.append({
            "id": str(fm.get("id") or stem),
            "path": rel,
            "title": str(title).strip(),
            "tags": [str(t) for t in tags],
            "folder": "" if parent == "." else parent.replace("\\", "/"),
            "wikilinks_out": wikilinks,
            "predicados": {k: v for k, v in sorted(preds.items())},
        })
    return atoms


# ---------------------------------------------------------------- (b) paragraphs
def parse_paragraphs(bib_keys: set):
    paras = []
    for path in sorted(PARAGRAPHS_DIR.glob("*.md")):
        anchor = path.stem
        m = re.match(r"^(.*)-p(\d+)$", anchor)
        section_id, pidx = (m.group(1), int(m.group(2))) if m else ("?", 0)
        text = path.read_text(encoding="utf-8")
        mt = re.search(r"^## Paragraph Text\s*\n(.*?)(?=^## )", text, re.S | re.M)
        ptext = mt.group(1).strip() if mt else ""
        cited = []
        for grp in re.findall(r"\[([^\]]*@[^\]]*)\]", ptext):
            for key in re.findall(r"@([A-Za-z0-9_:-]+)", grp):
                if key in bib_keys and key not in cited:
                    cited.append(key)
        paras.append({
            "anchor": anchor,
            "section_id": section_id,
            "paragraph_index": pidx,
            "text": ptext,
            "bibkeys": cited,
        })
    return paras


# ---------------------------------------------------------------- bib + comp_fuentes
def parse_bib():
    entries = {}
    raw = BIB_FILE.read_text(encoding="utf-8")
    for m in re.finditer(r"@\w+\{([^,]+),(.*?)(?=\n@|\Z)", raw, re.S):
        key, body = m.group(1).strip(), m.group(2)
        am = re.search(r"author\s*=\s*\{(.*?)\}\s*,", body, re.S)
        ym = re.search(r"year\s*=\s*\{?(\d{4})", body)
        surname = ""
        if am:
            first = re.split(r"\s+and\s+", am.group(1))[0]
            surname = first.split(",")[0].strip() if "," in first else first.strip()
        entries[key] = {
            "surname": norm_text(surname),
            "surname_raw": surname,
            "year": ym.group(1) if ym else "",
        }
    return entries


def parse_comp_fuentes():
    """lineas '**[[Source_PDF_x]]** — Apellido et al. (anyo):' -> tabla de matching."""
    path = ATOMS_DIR / "composiciones_review" / "comp_fuentes.md"
    table = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        links = WIKILINK_RE.findall(line)
        links = [wikilink_stem(l) for l in links if "Source_PDF" in l]
        if not links:
            continue
        m = re.search(r"—\s*([A-Za-zÀ-ÿ'’\-]+)\s+(?:et al\.\s+)?\(([^)]*)\)", line)
        surname = norm_text(m.group(1)) if m else None
        ym = re.search(r"(\d{4})", m.group(2)) if m else None
        for stem in links:
            table[stem] = {
                "surname": surname,
                "year": ym.group(1) if ym else None,
                "line": line.strip()[:160],
            }
    return table


def match_bibkeys(bib, source_table, atom_stems):
    """bibkey -> [Source_PDF stems]. exact (apellido+anyo) > apellido unico > filename."""
    key2atoms, unmatched, details = {}, [], {}
    by_surname = defaultdict(list)
    for stem, row in source_table.items():
        if row["surname"]:
            by_surname[row["surname"]].append(stem)
    for key in sorted(bib):
        row = bib[key]
        s, y = row["surname"], row["year"]
        hits, how = [], ""
        if s:
            exact = [st for st in by_surname.get(s, []) if source_table[st]["year"] == y]
            if exact:
                hits, how = exact, f"apellido+anyo ({row['surname_raw']} {y})"
            elif len(by_surname.get(s, [])) == 1:
                st = by_surname[s][0]
                hits, how = [st], (f"solo-apellido ({row['surname_raw']}; "
                                   f"bib {y} vs atom {source_table[st]['year']})")
        if not hits:
            nk = norm_text(key)
            cand = [st for st in source_table
                    if nk in norm_text(st) or (s and s in norm_text(st) and y and y in st)]
            cand = [st for st in cand if st in atom_stems]
            if cand:
                hits, how = cand, f"filename (~{key})"
        if hits:
            key2atoms[key] = hits
            details[key] = how
        else:
            unmatched.append(key)
    return key2atoms, unmatched, details


# ---------------------------------------------------------------- (e) composiciones
def parse_compositions(atom_stems):
    comps = {}
    for path in sorted((ATOMS_DIR / "composiciones_review").glob("comp_*.md")):
        fm, body = split_frontmatter(path.read_text(encoding="utf-8"))
        chain, seen = [], set()
        for w in WIKILINK_RE.findall(body):
            st = wikilink_stem(w)
            if st not in seen:
                seen.add(st)
                chain.append(st)
        comps[path.stem] = {
            "title": str(fm.get("title") or path.stem),
            "folder": str(fm.get("folder") or ""),
            "question": str(fm.get("question") or "").strip(),
            "chain": chain,
            "chain_resolved": [s for s in chain if s in atom_stems],
        }
    return comps


def build_section_compositions(comps):
    out = {}
    for sec in EXPECTED_SECTIONS:
        entries = []
        for comp_stem, why in CURATED_SECTION_COMPS.get(sec, []):
            c = comps.get(comp_stem)
            if not c:
                continue
            entries.append({
                "composition": comp_stem,
                "path": f"composiciones_review/{comp_stem}.md",
                "atom_count": len(c["chain"]),
                "question": c["question"],
                "justificacion": why,
            })
        out[sec] = entries
    return out


# ---------------------------------------------------------------- lexical
def atom_terms(atom):
    raw = atom["title"] + " " + atom["path"].rsplit("/", 1)[-1].replace("_", " ")
    return tokens_from(raw, STOPWORDS) | math_symbols(atom["title"] + " " + atom["path"])


def lexical_candidates(para, atom_term_map, df, n_atoms):
    p_terms = (tokens_from(para["text"], STOPWORDS) | math_symbols(para["text"]))
    df_cap = max(2, int(DF_MAX_FRAC * n_atoms))
    p_terms = {t for t in p_terms if df.get(t, 0) <= df_cap or t in MATH_TOKENS_ALL}
    scored = []
    for atom_id, a_terms in atom_term_map.items():
        if not a_terms:
            continue
        inter = p_terms & a_terms
        if not inter:
            continue
        score = len(inter) / len(a_terms)     # coeficiente de solape (contencion del atomo)
        scored.append((round(score, 4), atom_id, sorted(inter)))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[:LEX_TOP_K]


MATH_TOKENS_ALL = {"vi", "si", "wi", "li", "hk_plus", "hk_minus"}


# ---------------------------------------------------------------- main
def main():
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    # (a) indice de atomos
    atoms = index_atoms()
    atoms_by_id = {a["id"]: a for a in atoms}
    atoms_by_stem = {Path(a["path"]).stem: a for a in atoms}
    (BUILD_DIR / "atoms_index.json").write_text(
        json.dumps({"count": len(atoms), "atoms": atoms}, ensure_ascii=False, indent=2),
        encoding="utf-8")

    # anomalias: duplicados
    stem_counts = Counter(Path(a["path"]).stem for a in atoms)
    id_counts = Counter(a["id"] for a in atoms)
    dup_stems = {k: v for k, v in stem_counts.items() if v > 1}
    dup_ids = {k: v for k, v in id_counts.items() if v > 1}

    # (b) bib + parrafos
    bib = parse_bib()
    paras = parse_paragraphs(set(bib))

    # (c) puente bib
    source_table = parse_comp_fuentes()
    atom_stems = set(atoms_by_stem)
    key2atoms, unmatched_all, match_how = match_bibkeys(bib, source_table, atom_stems)
    cited_keys = sorted({k for p in paras for k in p["bibkeys"]})
    unmatched_cited = [k for k in cited_keys if k in unmatched_all]

    # mapa transitivo: Source_PDF stem -> atomos con grounded_by hacia el
    grounded_reverse = defaultdict(list)
    for a in atoms:
        for tgt in a["predicados"].get("grounded_by", []):
            if tgt.startswith("Source_PDF"):
                grounded_reverse[tgt].append(a["id"])

    # (d) puente lexico
    atom_term_map = {a["id"]: atom_terms(a) for a in atoms}
    df = Counter()
    for terms in atom_term_map.values():
        df.update(terms)

    # (e) composiciones
    comps = parse_compositions(atom_stems)
    section_comps = build_section_compositions(comps)
    comp_chains_by_section = {}
    for sec, entries in section_comps.items():
        chain = []
        for e in entries:
            for st in comps[e["composition"]]["chain_resolved"]:
                if st not in [c[0] for c in chain]:
                    chain.append((st, e["composition"]))
        comp_chains_by_section[sec] = chain[:COMP_TOP_K]

    # (f) candidatos por parrafo
    out_paras, bridge_counts, bridge_para_hits = [], Counter(), Counter()
    n_bib_or_lexhigh = 0
    for p in paras:
        cands = []
        seen = set()
        # bib
        src_stems = []
        for key in p["bibkeys"]:
            for st in key2atoms.get(key, []):
                src_stems.append((st, key))
        for st, key in src_stems:
            a = atoms_by_stem.get(st)
            if a and a["id"] not in seen:
                seen.add(a["id"])
                cands.append({"atom_id": a["id"], "atom_path": a["path"],
                              "bridge": "bib", "score": SCORE_BIB,
                              "detail": f"bibkey @{key} -> {match_how[key]}"})
        # bib transitivo
        for st, key in src_stems:
            for aid in grounded_reverse.get(st, []):
                a = atoms_by_id[aid]
                if aid not in seen:
                    seen.add(aid)
                    cands.append({"atom_id": aid, "atom_path": a["path"],
                                  "bridge": "bib_transitive", "score": SCORE_BIB_TRANSITIVE,
                                  "detail": f"grounded_by -> [[{st}]] (via @{key})"})
        # lexico
        for score, aid, shared in lexical_candidates(p, atom_term_map, df, len(atoms)):
            a = atoms_by_id[aid]
            if aid not in seen:
                seen.add(aid)
            cands.append({"atom_id": aid, "atom_path": a["path"], "bridge": "lexical",
                          "score": score, "detail": "terminos: " + ", ".join(shared)})
        # composicion
        for st, comp_stem in comp_chains_by_section.get(p["section_id"], []):
            a = atoms_by_stem.get(st)
            if a and a["id"] not in seen:
                seen.add(a["id"])
                cands.append({"atom_id": a["id"], "atom_path": a["path"],
                              "bridge": "composition", "score": SCORE_COMPOSITION,
                              "detail": f"cadena {comp_stem} (seccion {p['section_id']})"})
        # confianza (bib | bib_transitive => high; lexico por bandas)
        lex_scores = [c["score"] for c in cands if c["bridge"] == "lexical"]
        has_bib = any(c["bridge"] in ("bib", "bib_transitive") for c in cands)
        lex_max = max(lex_scores) if lex_scores else 0.0
        if has_bib or lex_max >= 0.5:
            conf = "high"
        elif lex_max >= 0.25:
            conf = "medium"
        else:
            conf = "low"
        if has_bib or lex_max >= 0.5:
            n_bib_or_lexhigh += 1
        for c in cands:
            bridge_counts[c["bridge"]] += 1
        for b in {c["bridge"] for c in cands}:
            bridge_para_hits[b] += 1
        out_paras.append({**{k: p[k] for k in ("anchor", "section_id", "paragraph_index", "bibkeys")},
                          "confidence": conf, "candidates": cands})

    # wikilinks rotos (top-20 por frecuencia)
    dir_names = {d.name for d in ATOMS_DIR.rglob("*") if d.is_dir()}
    broken = Counter()
    broken_where = defaultdict(set)
    for a in atoms:
        for w in a["wikilinks_out"]:
            if w not in atom_stems and w not in dir_names:
                broken[w] += 1
                broken_where[w].add(a["id"])
    broken_top = broken.most_common(20)

    # ---------------- escritura de salidas
    (BUILD_DIR / "candidates.json").write_text(json.dumps({
        "meta": {
            "atoms_indexed": len(atoms),
            "paragraphs": len(out_paras),
            "bibkeys_in_bib": len(bib),
            "bibkeys_cited": len(cited_keys),
            "bibkeys_matched": len([k for k in cited_keys if k in key2atoms]),
            "paragraphs_bib_or_lexical_high": n_bib_or_lexhigh,
            "bridge_candidate_counts": dict(bridge_counts),
            "bridge_paragraph_coverage": dict(bridge_para_hits),
        },
        "paragraphs": out_paras,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    mapping = {
        "fase": "0+1 draft (determinista, generado por anchor/build_index.py)",
        "section_compositions": section_comps,
        "bibkeys_sin_match": unmatched_cited,
        "paragraphs": out_paras,
    }
    (BUILD_DIR / "mapping_draft.yaml").write_text(
        yaml.safe_dump(mapping, allow_unicode=True, sort_keys=False, width=140),
        encoding="utf-8")

    # ---------------- summary.md
    residual = [p for p in out_paras if p["confidence"] in ("low", "medium")]
    lines = []
    lines.append("# Summary — Fase 0+1 anclaje KB->paper\n")
    lines.append(f"- Atomos indexados: **{len(atoms)}** ({ATOMS_DIR})")
    lines.append(f"- Parrafos parseados: **{len(out_paras)}**")
    lines.append(f"- Entradas bib: **{len(bib)}**; bibkeys citadas: **{len(cited_keys)}**; "
                 f"con match Source_PDF: **{len([k for k in cited_keys if k in key2atoms])}**")
    lines.append(f"- Parrafos con >=1 candidato bib o lexical>=0.5: **{n_bib_or_lexhigh}**\n")
    lines.append("## Conteos por bridge\n")
    lines.append("| bridge | candidatos | parrafos con >=1 |")
    lines.append("|---|---|---|")
    for b in ("bib", "bib_transitive", "lexical", "composition"):
        lines.append(f"| {b} | {bridge_counts.get(b, 0)} | {bridge_para_hits.get(b, 0)} |")
    conf_counts = Counter(p["confidence"] for p in out_paras)
    lines.append(f"\nConfianza: high={conf_counts.get('high',0)}, "
                 f"medium={conf_counts.get('medium',0)}, low={conf_counts.get('low',0)}\n")
    lines.append("## Residual Fase 2 (parrafos low/medium)\n")
    for p in residual:
        lex = [c["score"] for c in p["candidates"] if c["bridge"] == "lexical"]
        lines.append(f"- `{p['anchor']}` ({p['section_id']}) conf={p['confidence']} "
                     f"lex_max={max(lex) if lex else 0:.2f} bibkeys={p['bibkeys'] or '—'}")
    lines.append("\n## Bibkeys citadas sin match Source_PDF\n")
    for k in unmatched_cited:
        r = bib[k]
        lines.append(f"- `@{k}` ({r['surname_raw']} {r['year']})")
    lines.append("\n## Anomalias\n")
    lines.append(f"- Stems duplicados: {dup_stems or 'ninguno'}")
    lines.append(f"- IDs duplicados: {dup_ids or 'ninguno'}")
    lines.append(f"\n### Wikilinks rotos top-{len(broken_top)} (total distintos: {len(broken)})\n")
    for w, n in broken_top:
        srcs = sorted(broken_where[w])[:3]
        lines.append(f"- `[[{w}]]` x{n} (p.ej. en {', '.join(srcs)})")
    (BUILD_DIR / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ---------------- consola
    print(f"[OK] atomos indexados: {len(atoms)}")
    print(f"[OK] parrafos: {len(out_paras)} | bibkeys citadas: {len(cited_keys)} "
          f"| matched: {len([k for k in cited_keys if k in key2atoms])} "
          f"| sin match: {len(unmatched_cited)}")
    print(f"[OK] candidatos por bridge: {dict(bridge_counts)}")
    print(f"[OK] parrafos bib-o-lexical-high: {n_bib_or_lexhigh} "
          f"(meta >=30: {'CUMPLIDA' if n_bib_or_lexhigh >= 30 else 'NO CUMPLIDA'})")
    print(f"[OK] confianza: {dict(conf_counts)}")
    print(f"[OK] residual low/medium: {len(residual)} parrafos; primeros 5:")
    for p in residual[:5]:
        print(f"     - {p['anchor']} ({p['confidence']})")
    print(f"[OK] wikilinks rotos distintos: {len(broken)} (top-20 en summary.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
