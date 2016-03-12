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
    xmldoc = minidom.parse(query_file)
    for query in xmldoc.getElementsByTagName("query"):
        query_id = query.getElementsByTagName("number")[0].firstChild.nodeValue
        text = query.getElementsByTagName("text")[0].firstChild.nodeValue
        queries.append({'id': query_id, 'text': text})

    return queries


if __name__ == "__main__":

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    queries = load_queries()

    outfile = open(output_file, "w")

    for query in queries:
        print "Processing query number", query['id']

        # Retrieve documents using the vector space model
        res = retrieve_vsm(reader, query['text'])

        # Output max 10 results
        for docnum in sorted(res, key=res.get, reverse=True)[:10]:
            # Look up our docID
            stored = reader.stored_fields(docnum)
            # Write `docID Q0 queryID score` into `data/cacm.out`
            outfile.write(query['id']+ " Q0 " + stored['id'] + " " + str(res[docnum]) + "\n")

    outfile.close()
    ix.close()
