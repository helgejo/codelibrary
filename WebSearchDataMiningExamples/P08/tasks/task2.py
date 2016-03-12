# Indexing the CACM collection with Whoosh
# ========================================

# Task
# ------
#   - The CACM collection in `data/cacm.xml` contains 3024 documents.
#   - Build an index of this collection using Whoosh by selecting the appropriate
#     [Analyzer](http://whoosh.readthedocs.org/en/latest/api/analysis.html).
#   - Check index statistics (see Task 1 for ideas).

# Solution
# --------

import os.path
import whoosh.index as index
from whoosh.fields import Schema, ID, TEXT

index_dir = "../data/index_cacm"


def create_index():
    # TODO We create the index schema.
    schema = Schema()

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    # The writer() method of the Index object returns an IndexWriter object that lets us add documents to the index.
    writer = ix.writer()

    # Add documents to the index.
    for doc in docs:
        # TODO add document
        # Notes:
        # - Indexed text fields must be passed a unicode value. (use "str".decode())
        # - Fields can be left empty, i.e., we don't have to fill in a value for every field.
        writer.add_document()

    # Calling commit() on the IndexWriter saves the added documents to the index.
    writer.commit()

    ix.close()


def read_index():
    # Check if index exists in `index_dir`
    if not index.exists_in(index_dir):
        print "Index does not exist"
        return None

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    # TODO

    ix.close()


if __name__ == '__main__':
    create_index()
    #read_index()
