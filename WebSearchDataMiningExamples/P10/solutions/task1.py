# Understanding TFIDF scoring
# ===========================

# Task
# ------

#  - - Rank the toy document set for the given query by implementing TFIDF scoring.
#  - Compare with the document ranking you get using the TFIDF scorer implemented in Whoosh.

# Solution
# --------

from __future__ import division
from base_scorer import MyBaseScorer
import whoosh.index as index
import math
from whoosh import qparser
from whoosh import scoring


index_dir = "index"
field = "content"
query = ["t1"]  # query is given as a list of terms


class MyTFIDFScorer(MyBaseScorer):

    def __init__(self, index_dir):
        MyBaseScorer.__init__(self, index_dir)

    def score_term(self, field, t, ftq, qlen, ftd, doclen):
        # idf
        idf = math.log(self.reader.doc_count() / self.reader.doc_frequency(field, t))
        # doc tf
        tf_d = ftd / doclen
        # query tf
        tf_q = ftq / qlen
        # tfidf_t,d * tfidf_t,q
        return tf_d * idf * tf_q * idf
        # Note for Assignment 3: this variant performs better: math.log(ftd) * idf * ftq


if __name__ == "__main__":

    # Self scorer
    print "Our ranking:"
    scorer = MyTFIDFScorer(index_dir)
    scorer.score_all(query, field)
    scorer.close()

    # Whoosh scorer
    print "Whoosh ranking:"
    ix = index.open_dir(index_dir)
    with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
        qp = qparser.QueryParser(field, schema=ix.schema)
        q = qp.parse(" ".join(query))  # we contatenate query terms
        results = searcher.search(q)
        for r in results:
            print r['id'], str(r.score)[0:6]
    ix.close()
