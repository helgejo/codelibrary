# Performing entity retrieval using DBpedia
# =========================================

# Task
# ------

# - Build an entity index with the following fields:
#   * _names_: entity names from `labels_en.nt`
#   * _abstract_: short description (abstract) from `short_abstracts_en.nt`
#   * _categories_: associated Wikipedia categories from `article_categories_en.nt`
# - Perform entity retrieval using a fielded model (BM25F). Compare different configurations:
#   * Using only the names
#   * Using names and abstract
#   * Using names, abstract, and categories

# Solution
# --------

from ntriples import *
import os.path
import whoosh.index as index
from whoosh.fields import Schema, ID, TEXT
from whoosh import qparser
from whoosh.qparser import MultifieldParser


entities = {}  # dictionary holding all entity data
DATA_DIR = "../data"
INDEX_DIR = DATA_DIR + "/index"


# Loads a given NTriples file into a given field
def load_file(filename, field):
    with open(filename) as f:
        for line in f:
            if line[0] != "#":  # skip comment lines
                (s, p, o) = nt_parse_line(line)
                if s not in entities:
                    entities[s] = {}
                # clean up the object value
                if o[0] != "<":  # if it's a literal
                    value = o[1:-4]  # remove leading " and trailing "@en
                elif o[0:38] == "<http://dbpedia.org/resource/Category:":  # Wikipedia category
                    value = o[38:-1].replace("_", " ")
                else:    
                    value = o
                entities[s][field] = value


# Load entities from multiple NTriples files (and stores all data in the `entities` dict)
def load_entities():
    load_file(DATA_DIR + "/labels_en.nt", "name")
    load_file(DATA_DIR + "/short_abstracts_en.nt", "abstract")
    load_file(DATA_DIR + "/article_categories_en.nt", "categories")


# Indexing is based on P10/task0.py. For each entity, a fielded document is created.
def index_entities(index_dir=INDEX_DIR):
    # We create the index schema.
    schema = Schema(uri=ID(stored=True), name=TEXT, abstract=TEXT, categories=TEXT)

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    writer = ix.writer()

    # Add documents to the index.
    for uri,entity in entities.iteritems():
        if "name" not in entity:  # ignore entities without name
            continue
        abs = entity['abstract'] if "abstract" in entity else ""  # the abstract may be missing
        cat = entity['categories'] if "categories" in entity else ""  # categories may be missing
        writer.add_document(uri=uri.decode(), name=entity['name'].decode(), abstract=abs.decode(), categories=cat.decode())

    writer.commit()

    ix.close()    


# Search for entities that match the given query using BM25F scoring.
# If field is not provided than it searches in all fields; otherwise only in the given field.
# The query parser is configured to connect terms by OR (the default setting is AND,
# i.e., the document must contain all query terms).
def search_entities(query, field=None, index_dir=INDEX_DIR):
    ix = index.open_dir(index_dir)
    with ix.searcher() as searcher:
        # Parse the user query
        if field is None:  # search in all fields
            qp = MultifieldParser(["name", "abstract", "categories"], schema=ix.schema, group=qparser.OrGroup)
        else:  # search in a given field
            qp = qparser.QueryParser(field, schema=ix.schema, group=qparser.OrGroup)
        q = qp.parse(query)
        # Print out the parsed query
        print q

        # Search for matching documents (representing entities)
        results = searcher.search(q)
        for r in results:
            print r['uri'], str(r.score)[0:6]

    ix.close()

    
if __name__ == "__main__":
    # Indexing
    # For indexing the collection, uncomment the following lines (this needs to be done only once)
    #load_entities()
    # Check what information is loaded for a given entity
    #print entities["<http://dbpedia.org/resource/Academy_Award_for_Best_Production_Design>"]
    #index_entities()

    # Searching
    query = "greek hero"
    search_entities(query, "name")  # search in name
    search_entities(query)  # search in all fields