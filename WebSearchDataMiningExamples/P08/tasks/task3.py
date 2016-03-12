# Retrieval using the Vector Space Model
# ======================================

# Task
# ------

# - Take Task 4 from the last practicum (P07) and update the code such that
#   the term statistics are taken from the Whoosh index we built in Task 2

# Solution
# --------

from __future__ import division

import whoosh.index as index
import math
from collections import Counter

index_dir = "../data/index_cacm"


# Compute the TFIDF weight of a term
def tfidf(index, term, count, length):
    # Normalized count of the term occurrences in the document
    tf = count / length
    # log (N/n_k), where N is the total number of documents and
    # n_k is the number of documents that contain `term`
    idf = math.log(index.num_docs() / len(index.get_postings(term)))  # TODO update
    return tf*idf


# Scoring all documents in the collection against the query
# using the Vector Space Model
def retrieve_vsm(index, query):
    # Preprocess the query (the same way as we preprocesssed documents)
    qterms = parse(query)  # TODO update
    qt = Counter(qterms)

    N = index.num_docs()  # number of documents  # TODO update
    scores = {}  # retrieval score for each doc
    doc_norm = {}  # score normalizer for each doc
    q_norm = 0  # normalizer for query (could be ignored)

    # for each query term t
    for t, cnt in qt.iteritems():
        postings = index.get_postings(t)  # TODO update
        # ignore terms not in the index
        if postings is None:
            continue

        # calculate w_t,q
        wtq = tfidf(index, t, cnt, len(qterms))
        q_norm += wtq * wtq

        # for each doc in the posting list of t
        for p in postings:
            doc_id = p.doc_id
            if doc_id not in scores:
                scores[doc_id] = 0
                doc_norm[doc_id] = 0
            # term freq of t in doc
            freq = int(p.payload)  # TODO update
            doclen = index.get_doc_meta(doc_id)['length']  # TODO update
            wtd = tfidf(index, t, freq, doclen)
            scores[doc_id] += wtq * wtd
            doc_norm[doc_id] += wtd * wtd

    # `scores` at this points holds the counter of the cosine formula
    # we need to perform normslization dividing by sqrt(q_norm * doc_norm)
    for doc_id, score in scores.iteritems():
        scores[doc_id] = scores[doc_id] / math.sqrt(q_norm * doc_norm[doc_id])

    return scores


if __name__ == "__main__":

    # Load index
    index = Index()  # TODO update
    index.load_from_file("../data/index.txt", "../data/meta.txt")

    # Input query
    query = "financial japan world news"

    # Retrieve documents using the vector space model
    res = retrieve_vsm(index, query)

    # Print relevance scores and document titles for the top 10 results
    for doc_id in sorted(res, key=res.get, reverse=True)[:10]:
        docmeta = index.get_doc_meta(doc_id)
        print res[doc_id], docmeta['title']
