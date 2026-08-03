#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from rdflib import Graph

from rdflib.namespace import RDF
from converters.mermaid import load_mermaid, dump_mermaid
from converters.puml import load_puml, dump_puml
from converters.owl_viz import dump_owl_mermaid
from converters.dims import ONTO

LOADERS = {
    ".ttl":  lambda p: _rdf_load(p, "turtle"),
    ".owl":  lambda p: _rdf_load(p, "xml"),
    ".rdf":  lambda p: _rdf_load(p, "xml"),
    ".mmd":  lambda p: load_mermaid(Path(p).read_text()),
    ".puml": lambda p: load_puml(Path(p).read_text()),
}

def _dump_mermaid_auto(g: Graph, p: str):
    has_instances = any(True for _ in g.triples((None, RDF.type, ONTO.OntologyEdge)))
    content = dump_mermaid(g) if has_instances else dump_owl_mermaid(g)
    Path(p).write_text(content)

DUMPERS = {
    ".ttl":  lambda g, p: _rdf_dump(g, p, "turtle"),
    ".owl":  lambda g, p: _rdf_dump(g, p, "xml"),
    ".rdf":  lambda g, p: _rdf_dump(g, p, "xml"),
    ".n3":   lambda g, p: _rdf_dump(g, p, "n3"),
    ".mmd":  _dump_mermaid_auto,
    ".puml": lambda g, p: Path(p).write_text(dump_puml(g)),
}

def _rdf_load(path: str, fmt: str) -> Graph:
    g = Graph()
    g.parse(path, format=fmt)
    return g

def _rdf_dump(g: Graph, path: str, fmt: str):
    Path(path).write_text(g.serialize(format=fmt))


def cmd_parse(args):
    src = Path(args.input)
    dst = Path(args.output)

    loader = LOADERS.get(src.suffix.lower())
    dumper = DUMPERS.get(dst.suffix.lower())

    if not loader:
        print(f"Formato de entrada no soportado: {src.suffix}", file=sys.stderr)
        sys.exit(1)
    if not dumper:
        print(f"Formato de salida no soportado: {dst.suffix}", file=sys.stderr)
        sys.exit(1)

    print(f"Cargando {src}...")
    g = loader(str(src))
    print(f"  {len(g)} tripletas")

    dst.parent.mkdir(parents=True, exist_ok=True)
    print(f"Guardando {dst}...")
    dumper(g, str(dst))
    print("  listo.")


def main():
    parser = argparse.ArgumentParser(prog="ontomap", description="OntoMap CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_parse = sub.add_parser("parse", help="Convierte entre formatos (ttl, owl, mmd, puml)")
    p_parse.add_argument("input",  help="Archivo de entrada")
    p_parse.add_argument("output", help="Archivo de salida")
    p_parse.set_defaults(func=cmd_parse)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
