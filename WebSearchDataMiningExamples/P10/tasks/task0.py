# Index the toy document colletion
# ================================

# Task
# ------
#  - Build an index of a toy document collection using Whoosh.
#  - The code is written, you just need to run it.


import os.path
import whoosh.index as index
from whoosh.fields import Schema, ID, TEXT

# Toy document collection
docs = [
    {'id': "001", 'title': "t1", 'content': "t1 t3 t4 t5"},
    {'id': "002", 'title': "t2", 'content': "t6 t7"},
    {'id': "003", 'title': "t3", 'content': "t1 t8 t9"},
    {'id': "004", 'title': "t1 t3", 'content': "t1 t1 t3 t3 t4 t5"},
    {'id': "005", 'title': "t2 t2", 'content': "t10"},
]

index_dir = "index"


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
        writer.add_document(id=doc['id'].decode(), title=doc['title'].decode(), content=doc['content'].decode())

    # Calling commit() on the IndexWriter saves the added documents to the index.
    writer.commit()

    ix.close()


if __name__ == '__main__':
    create_index()  # note that this has to be done only once
