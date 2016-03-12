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

    def __init__(self, index_dir, k1=1.2, b=0.75):
        MyBaseScorer.__init__(self, index_dir)
        self.k1 = k1
        self.b = b

    def score_term(self, field, t, ftq, qlen, ftd, doclen):
        # B = 1 - b + b (|d| / avgdl)
        avgdl = self.reader.field_length(field) / self.reader.doc_count()
        B = 1 - self.b + self.b * doclen / avgdl
        # idf
        idf = math.log(self.reader.doc_count() / self.reader.doc_frequency(field, t))
        return (ftd * (1 + self.k1)) / (ftd + self.k1 * B) * idf


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
