# Generate retrieval results in "batch mode"
# ==========================================

# Task
# ------

# - Using the retrieval algorithm from Task 3, process the queries in `data/cacm.query.xml`
#   and output the top 10 results to a single file, `data/cacm.out`,
#   in the following format (one result per line) `queryID Q0 docID score`

# Solution
# --------

from __future__ import division

import whoosh.index as index
from xml.dom import minidom
from task3 import retrieve_vsm

index_dir = "../data/index_cacm"
query_file = "../data/cacm.query.xml"
output_file = "../data/cacm.out"
default_field = "content"


# Load queries from the query xml file
def load_queries():
    queries = []
    # TODO store id and text for each query
    # e.g., in a dict: `queries.append({'id': query_id, 'text': text})`
    return queries


if __name__ == "__main__":

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    # TODO load queries
    queries = load_queries()

    # TODO write results to file

    for query in queries:
        print "Processing query number", query['id']

        # Retrieve documents using the vector space model
        res = retrieve_vsm(reader, query['text'])

        # Output max 10 results
        for docnum in sorted(res, key=res.get, reverse=True)[:10]:
            # Look up our docID
            stored = reader.stored_fields(docnum)
            # TODO Write `queryID Q0 docID score` into `data/cacm.out`
            print stored['id'], res[docnum]  # doc id and score

    ix.close()
