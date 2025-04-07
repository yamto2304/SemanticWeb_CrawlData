from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

# Khởi tạo SPARQLWrapper
def init_sparql(endpoint="https://dbpedia.org/sparql"):
    """Khởi tạo SPARQLWrapper với endpoint cho trước."""
    sparql = SPARQLWrapper(endpoint)
    sparql.setReturnFormat(JSON)
    return sparql

# Tạo truy vấn SPARQL cho danh sách triều đại
def create_dynasties_query(category_uri):
    """Tạo truy vấn SPARQL để lấy danh sách thực thể từ một category."""
    query = f"""
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?dynasty ?label
    WHERE {{
        ?dynasty dct:subject <{category_uri}> .
        ?dynasty rdfs:label ?label .
        FILTER (lang(?label) = "en")
    }}
    LIMIT 200
    """
    return query

# Tạo truy vấn SPARQL cho chi tiết triều đại
def create_dynasty_details_query(dynasty_uri):
    """Tạo truy vấn SPARQL để lấy chi tiết của một triều đại."""
    query = f"""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    SELECT ?property ?value
    WHERE {{
        <{dynasty_uri}> ?property ?value .
    }}
    LIMIT 200
    """
    return query