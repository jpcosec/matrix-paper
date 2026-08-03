from rdflib import Graph, Namespace, RDF
from rdflib.plugins.sparql import prepareQuery

ONTO = Namespace("http://ontomap.io/ontology#")
WS   = Namespace("http://ontomap.io/workspace#")

g = Graph()
g.parse("ontology/core.ttl",      format="turtle")
g.parse("ontology/workspace.ttl", format="turtle")

print(f"Grafo cargado: {len(g)} tripletas\n")

PROJECTIONS = {
    "Árbol de composición (where=contains)": """
        PREFIX onto: <http://ontomap.io/ontology#>
        SELECT ?parent ?child WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?parent ;
               onto:target ?child ;
               onto:contains ?child .
        } ORDER BY ?parent
    """,

    "Flujo de estados (what=transitionsTo)": """
        PREFIX onto: <http://ontomap.io/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?from ?to ?phase ?mechanism WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?from ;
               onto:target ?to ;
               onto:transitionsTo ?to .
            OPTIONAL { ?e onto:when ?phase }
            OPTIONAL { ?e onto:how  ?mechanism }
        } ORDER BY ?phase
    """,

    "Interacciones de actores (source=Actor)": """
        PREFIX onto: <http://ontomap.io/ontology#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?actor ?target ?how ?why WHERE {
            ?e a onto:OntologyEdge ;
               onto:source ?actor ;
               onto:target ?target .
            ?actor a ?actorType .
            FILTER(?actorType IN (onto:LLMAgent, onto:CLI))
            OPTIONAL { ?e onto:how ?how }
            OPTIONAL { ?e onto:why ?why }
        } ORDER BY ?actor
    """,

    "Verificación de ciclos en containment (debe ser vacío)": """
        PREFIX onto: <http://ontomap.io/ontology#>
        SELECT ?a ?b WHERE {
            ?e1 a onto:OntologyEdge ; onto:source ?a ; onto:target ?b ; onto:contains ?b .
            ?e2 a onto:OntologyEdge ; onto:source ?b ; onto:target ?a ; onto:contains ?a .
        }
    """,
}

for title, query in PROJECTIONS.items():
    print(f"── {title} ──")
    rows = list(g.query(query))
    if rows:
        for row in rows:
            print("  ", " | ".join(str(v).split("/")[-1] if v else "–" for v in row))
    else:
        print("  (vacío)")
    print()
