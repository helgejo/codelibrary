# Understanding LM scoring
# ========================

# Task
# ------

#  - Rank the toy document set for the given query by implementing LM scoring.

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


class MyLMScorer(MyBaseScorer):

    def __init__(self, index_dir, lambd=0.1):
        MyBaseScorer.__init__(self, index_dir)
        self.lambd = lambd

    def score_term(self, field, t, ftq, qlen, ftd, doclen):
        # P(t|d): relative freq. of the term in the document
        ptd = ftd / doclen
        # P(t|c): relative freq. of the term in the collection
        ptc = self.reader.frequency(field, t) / self.reader.field_length(field)
        # \log P(t|\theta_d) * f_{t,q}
        return math.log((1 - self.lambd) * ptd + self.lambd * ptc) * ftq


if __name__ == "__main__":

    # Self scorer
    print "Our ranking:"
    scorer = MyLMScorer(index_dir)
    scorer.score_all(query, field)
    scorer.close()
