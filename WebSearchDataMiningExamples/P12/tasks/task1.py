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
                # TODO store this information for the respective entity (the entity is `s`, the value is `o`)


# Load entities from multiple NTriples files (and stores all data in the `entities` dict)
def load_entities():
    load_file(DATA_DIR + "/labels_en.nt", "name")
    load_file(DATA_DIR + "/short_abstracts_en.nt", "abstract")
    load_file(DATA_DIR + "/article_categories_en.nt", "categories")


# Indexing is based on P10/task0.py. For each entity, a fielded document is created.
def index_entities(index_dir=INDEX_DIR):
    # TODO create the index schema.
    schema = Schema()

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    writer = ix.writer()

    # Add documents to the index.
    for uri,entity in entities.iteritems():
        # TODO
        writer.add_document()

    writer.commit()

    ix.close()    


# Search for entities that match the given query using BM25F scoring.
# If field is not provided than it searches in all fields; otherwise only in the given field.
# The query parser is configured to connect terms by OR (the default setting is AND,
# i.e., the document must contain all query terms).
def search_entities(query, field=None, index_dir=INDEX_DIR):
    ix = index.open_dir(index_dir)
    with ix.searcher() as searcher:
        # TODO Parse the user query
        q = None
        # Print out the parsed query
        print q

        # Search for matching documents (representing entities)
        results = searcher.search(q)
        for r in results:
            # TODO print out the entity URI and the score
            print r

    ix.close()

    
if __name__ == "__main__":
    # Indexing
    # For indexing the collection, uncomment the following lines (this needs to be done only once)
    load_entities()
    # Check what information is loaded for a given entity
    print entities["<http://dbpedia.org/resource/Academy_Award_for_Best_Production_Design>"]
    index_entities()

    # Searching
    query = "greek hero"
    search_entities(query, "name")  # search in name
    search_entities(query)  # search in all fields