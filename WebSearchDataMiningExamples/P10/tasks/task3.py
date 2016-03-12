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

    def __init__(self, index_dir):
        MyBaseScorer.__init__(self, index_dir)

    def score_term(self, field, t, ftq, qlen, ftd, doclen):
        # TODO
        return 0


if __name__ == "__main__":

    # Self scorer
    print "Our ranking:"
    scorer = MyLMScorer(index_dir)
    scorer.score_all(query, field)
    scorer.close()
