# Understanding BM25 scoring
# ==========================

# Task
# ------

#  - Rank the toy document set for the given query by implementing BM25 scoring.
#  - Compare with the document ranking you get using the BM25 scorer implemented in Whoosh.
#  - Check the document rankings with different parameter settings

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


class MyBM25Scorer(MyBaseScorer):

    def __init__(self, index_dir):
        MyBaseScorer.__init__(self, index_dir)

    def score_term(self, field, t, ftq, qlen, ftd, doclen):
        # TODO
        return 0


if __name__ == "__main__":

    # Self scorer
    print "Our ranking:"
    scorer = MyBM25Scorer(index_dir)
    scorer.score_all(query, field)
    scorer.close()

    # Whoosh scorer
    print "Whoosh ranking:"
    ix = index.open_dir(index_dir)
    with ix.searcher(weighting=scoring.BM25F()) as searcher:
        qp = qparser.QueryParser(field, schema=ix.schema)
        q = qp.parse(" ".join(query))  # we contatenate query terms
        results = searcher.search(q)
        for r in results:
            print r['id'], str(r.score)[0:6]
    ix.close()
