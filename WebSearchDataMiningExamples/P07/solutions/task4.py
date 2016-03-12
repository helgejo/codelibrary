# Retrieval using the Vector Space Model
# ======================================

# Task
# ------
#   - Load the index from the disk that was created in Tasks 1 and 2.
#   - Rank documents using keyword queries (e.g., "united states") using the Vector Space Model
#     * Use TF-IDF term weighting and cosine similarity
#   - Display a ranked list of the top 10 matching documents, along with the corresponding relevance scores
#   - Extend `indexer.py` with the necessary methods
#     * Hint: you will need a method that returns the set of documents that contain a given term
#   - Homework: try some of the [different variants for TF and IDF weights](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

# Solution
# --------

from __future__ import division

from indexer import Index, parse
import math
from collections import Counter


# Compute the TFIDF weight of a term
def tfidf(index, term, count, length):
    # Normalized count of the term occurrences in the document
    tf = count / length
    # log (N/n_k), where N is the total number of documents and
    # n_k is the number of documents that contain `term`
    idf = math.log(index.num_docs() / len(index.get_postings(term)))
    return tf*idf


# Scoring all documents in the collection against the query
# using the Vector Space Model
def retrieve_vsm(index, query):
    # Preprocess the query (the same way as we preprocesssed documents)
    qterms = parse(query)
    qt = Counter(qterms)

    N = index.num_docs()  # number of documents
    scores = {}  # retrieval score for each doc
    doc_norm = {}  # score normalizer for each doc
    q_norm = 0  # normalizer for query (could be ignored)

    # for each query term t
    for t, cnt in qt.iteritems():
        postings = index.get_postings(t)
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
            freq = int(p.payload)
            doclen = index.get_doc_meta(doc_id)['length']
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
    index = Index()
    index.load_from_file("../data/index.txt", "../data/meta.txt")

    # Input query
    query = "financial japan world news"

    # Retrieve documents using the vector space model
    res = retrieve_vsm(index, query)

    # Print relevance scores and document titles for the top 10 results
    for doc_id in sorted(res, key=res.get, reverse=True)[:10]:
        docmeta = index.get_doc_meta(doc_id)
        print res[doc_id], docmeta['title']
