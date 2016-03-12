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

# For parsing the XML file
from xml.dom import minidom

index_dir = "../data/index_cacm"
input_file = "../data/cacm.xml"


def create_index():
    # We create the index schema.
    schema = Schema(id=ID(stored=True), content=TEXT)

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    # The writer() method of the Index object returns an IndexWriter object that lets us add documents to the index.
    writer = ix.writer()

    xmldoc = minidom.parse(input_file)

    # Add documents to the index.
    for doc in xmldoc.getElementsByTagName("doc"):
        doc_id = doc.attributes['id'].value
        content = doc.firstChild.data
        print doc_id
        # Add document
        # Notes:
        # - Indexed text fields must be passed a unicode value. (use "str".decode())
        # - Fields can be left empty, i.e., we don't have to fill in a value for every field.
        writer.add_document(id=doc_id, content=content)

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

    # Number of documents the index contains
    print reader.doc_count()  # 3204

    # Number of times the term "reference" appears in the content field
    print reader.frequency("content", "reference")  # 81

    ix.close()


if __name__ == '__main__':
    create_index()  # note that this has to be done only once
    read_index()
