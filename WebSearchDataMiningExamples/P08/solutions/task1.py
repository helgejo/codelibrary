# Indexing documents with Whoosh
# ==============================

# Task
# ------
#   - Build an index of a toy document collection using Whoosh.
#     * Add `title` and `content` as indexed
#     * See [this page](http://whoosh.readthedocs.org/en/latest/schema.html) for details on how to design the index schema
#   - Load the index and check whether everything was done correctly by requesting the following information from it:
#     * Number of documents the index contains
#     * Number of times the term `document` appears in the title and content fields (i.e., term frequency)
#     * Number of documents the term `document` appears in the title and content fields (i.e., document frequency)
#     * Total length (number of terms) in the title and content fields
#     * The posting list for the term `document` for the content field
#   - See the [IndexReader](http://whoosh.readthedocs.org/en/latest/api/reading.html)
#     and the [Whoosh recipes](http://whoosh.readthedocs.org/en/latest/recipes.html) pages for help.

# Solution
# --------

import os.path
import whoosh.index as index
from whoosh.fields import Schema, ID, TEXT

# Document collection
docs = [
    {'id': "001", 'title': "My document", 'content': "This is my document!"},
    {'id': "002", 'title': "Second try", 'content': "This is my second example."},
    {'id': "003", 'title': "Third time's the charm", 'content': "Examples are many."},
    {'id': "004", 'title': "Final example document", 'content': "Document, second document, third document, my document."},
]

index_dir = "../data/index"


def create_index():
    # We create the index schema.
    schema = Schema(id=ID(stored=True), title=TEXT, content=TEXT)

    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = index.create_in(index_dir, schema)

    # The writer() method of the Index object returns an IndexWriter object that lets us add documents to the index.
    writer = ix.writer()

    # Add documents to the index.
    for doc in docs:
        # Add document
        # Notes:
        # - Indexed text fields must be passed a unicode value. (use "str".decode())
        # - Fields can be left empty, i.e., we don't have to fill in a value for every field.
        writer.add_document(id=doc['id'].decode(), title=doc['title'].decode(), content=doc['content'].decode())

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
    print reader.doc_count()  # 4

    # Number of times the term `document` appears in the title and content fields (i.e., term frequency)
    print reader.frequency("title", "document")  # 2
    print reader.frequency("content", "document")  # 5

    # Number of documents the term `document` appears in the title and content fields (i.e., document frequency)
    print reader.doc_frequency("title", "document")  # 2
    print reader.doc_frequency("content", "document")  # 2

    # Total length (number of terms) in the title and content fields
    print reader.field_length("title")  # 10
    print reader.field_length("content") # 14

    # The posting list for the term `document` for the content field
    if reader.frequency("content", "document") > 0:  # Check if the term is in the index at all
        pr = reader.postings("content", "document")
        while pr.is_active():
            print "docno=", pr.id(), " freq=", pr.value_as("frequency")  # docno, term frequency
            pr.next()
    # Output:
    # docno= 0  freq= 1
    # docno= 3  freq= 4

    ix.close()


if __name__ == '__main__':
    create_index()  # note that this has to be done only once
    read_index()
