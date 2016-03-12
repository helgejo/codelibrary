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

from indexer import Index

# Compute the TFIDF weight of a term
def tfidf(index, term, count):
    # TODO
    return 0

def retrieve_vsm(index, query):
    # TODO implement retrieval

    # Basic algorithm
    # - N is the number of documents
    # - w_t,q and w_t,d are TFIDF term weights in the query/document
    # ----
    # scores[N] = 0  // score for each doc
    # doc_norm[N] = 0  // normalizer for each doc
    # q_norm = 0  // normalizer for query
    # for each query term t
    #   calculate w_t,q
    #   q_norm += (w_t,q)^2
    #   for each doc in the posting list of t
    #     scores[doc] += w_t,q * w_t,d
    #     doc_norm[doc] += (w_t,d)^2
    #   // scores at this points holds the counter of the cosine formula
    #   // we need to divide by sqrt(q_norm * doc_norm)
    #   for each doc
    #     scores[doc] = scores[doc] / sqrt(q_norm * doc_norm[doc])
    #   sort(scores)  // sort docs by scores desc
    pass


if __name__ == "__main__":

    # Load index
    index = Index()
    index.load_from_file("data/index.txt")

    query = "united states"
    # Retrieve documents using the vector space model
    retrieve_vsm(index, query)
