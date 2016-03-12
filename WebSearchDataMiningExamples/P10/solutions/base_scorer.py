import whoosh.index as index
from collections import Counter


# Class used for scoring all documents given a query
class MyBaseScorer(object):

    def __init__(self, index_dir):
        self.index =  index.open_dir(index_dir)
        self.reader = self.index.reader()

    # Score a given term in a given document
    def score_term(self, field, t, ftq, ftd, doclen):
        raise NotImplementedError(self.__class__.__name__)

    # Score all documents
    def score_all(self, query, field):
        qt = Counter(query)  # raw query term frequencies
        qlen = len(query)  # query length
        scores = {}  # retrieval score for each doc ($score(q,d)$)

        # for each query term t
        for t, ftq in qt.iteritems():
            # ignore terms not in the index
            if self.reader.frequency(field, t) == 0:
                print "Query term", t, "ignored"
                continue

            # for each doc that contains t (i.e., docs in the posting list of t)
            pr = self.reader.postings(field, t)
            while pr.is_active():
                docnum = pr.id()  # docnum is the internal (Whoosh) docID
                if docnum not in scores:
                    scores[docnum] = 0
                ftd = pr.value_as("frequency")  # term freq of t in doc ($f_{t,q}$)
                doclen = self.reader.doc_field_length(docnum, field)
                scores[docnum] += self.score_term(field, t, ftq, qlen, ftd, doclen)
                pr.next()

        # Print the ranked list of documents
        for docnum in sorted(scores, key=scores.get, reverse=True):
            # Look up our docID (stored field in the index)
            stored = self.reader.stored_fields(docnum)
            print stored['id'], str(scores[docnum])[0:6]  # doc id and score

    # Close index
    def close(self):
        self.reader.close()
        self.index.close()
