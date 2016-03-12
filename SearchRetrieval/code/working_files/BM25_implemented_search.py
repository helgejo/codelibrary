from __future__ import division
import whoosh.index as index
import math
from collections import Counter
# For parsing the XML file
from xml.dom import minidom

__author__ = 'HELGE BJORLAND'

index_dir = "../data/index3"
query_file = "../data/queries.xml"
output_file = "../output/baseline_bm25_custom.out"
default_field = "title"
k1 = 1.2
b = 0.75

def bm25(reader, term, count, length):
    avgdl = reader.field_length(default_field) / reader.doc_count()
    B = 1 - b + b * length / avgdl
    idf = math.log(reader.doc_count() / reader.doc_frequency(default_field, term))
    return (count * (1 + k1)) / (count + k1 * B) * idf

def retrieve_bm25(reader, query):
    # Preprocess the query in a naive way
    qterms = query.split()
    qt = Counter(qterms)

    scores = {}  # retrieval score for each doc

    # for each query term t
    for t, cnt in qt.items():
    # for t, cnt in qt.iteritems():

        # ignore terms not in the index
        if reader.frequency(default_field, t) == 0:
            #print "Query term", t, "ignored"
            continue

        # calculate w_t,q
        # wtq = tfidf(reader, t, cnt, len(qterms))

        # for each doc in the posting list of t
        pr = reader.postings(default_field, t)
        while pr.is_active():
            docnum = pr.id()  # docnum is the internal (Whoosh) docID
            if docnum not in scores:
                scores[docnum] = 0
            # term freq of t in doc
            freq = pr.value_as("frequency")
            doclen = reader.doc_field_length(docnum, default_field)
            scores[docnum] += bm25(reader, t, freq, doclen)
            pr.next()

    # `scores` at this points holds the counter of the cosine formula
    # we need to perform normslization dividing by sqrt(q_norm * doc_norm)
    # for docnum, score in scores.iteritems():
    # for docnum, score in scores.items():
    #     scores[docnum] = scores[docnum] / math.sqrt(q_norm * doc_norm[docnum])

    return scores

# Load queries from the query xml file
def load_queries():
    queries = []
    xmldoc = minidom.parse(query_file)
    queriez = xmldoc.getElementsByTagName("query")
    for query in queriez:
            query_id = query.getAttribute("id")
            text = query.firstChild.nodeValue
            queries.append({'id': query_id, 'text': text})
    return queries

def score_to_file():

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    queries = load_queries()

    outfile = open(output_file, "w")

    for query in queries:
        print("Processing query number", query['id'])

        # Retrieve documents using the vector space model
        res = retrieve_bm25(reader, query['text'])

        # Output max 50 results
        for docnum in sorted(res, key=res.get, reverse=True)[:50]:
            # Look up our docID
            stored = reader.stored_fields(docnum)
            # Write `docID Q0 queryID score` into output file
            outfile.write(query['id'] + " Q0 " + stored['id'] + " " + str(res[docnum]) + "\n")

    outfile.close()
    ix.close()

if __name__ == '__main__':
    score_to_file()