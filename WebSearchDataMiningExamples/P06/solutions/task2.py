# Text preprocessing and document similarity
# ==========================================

# Task
# ----
#   - Write a function that creates (and prints out) the document-term matrix from an input set of documents
#   - Apply the following preprocessing steps:
#     * Tokenization
#     * Lowercasing
#     * Stopword removal
#     * Suffix-s stemming
#   - Implement a function that computes the Jaccard similarity of two term vectors
#   - Implement a function that computes the cosine similarity of two term vectors

# Solution
# --------

from __future__ import division

import math


# Set of input documents
docs = [
    "The King's Speech",
    "The Lord of the Rings: The Return of the King",
    "Street Kings",
    "The Scorpion King",
    "The Lion King"
]

# Stopwords list
stopwords = [
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in",
    "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the",
    "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"
]


# Preprocess a given document and return a sequence of terms
def preprocess(doc):
    terms = []
    # Replace specific characters with space
    chars = ["'", ".", ":", ",", "!", "?", "(", ")"]
    for ch in chars:
        if ch in doc:
            doc = doc.replace(ch, " ")

    # Tokenization
    for term in doc.split():  # default behavior of the split is to split on one or more whitespaces
        # Lowercasing
        term = term.lower()
        # Stopword removal
        if term in stopwords:
            continue
        # Suffix-s stemming
        if len(term) > 1 and term.endswith("s"):
            term = term[:-1]
        terms.append(term)

    return terms


# Create (and print out) the document-term matrix from an input set of documents
def doc_term_matrix(docs, display=True):
    voc = []  # vocabulary
    # First collect terms in a dictionary for each document
    dtd = []
    for d in docs:
        td = {}  # term dictionary for document d
        terms = preprocess(d)
        for t in terms:
            # add the term to vocabulary if it's not there
            if t not in voc:
                voc.append(t)
            if t not in td:
                td[t] = 0
            td[t] += 1
        dtd.append(td)

    # Convert the document-term dictionaries to a document-term matrix
    dtm = []
    for td in dtd:
        # initialize term vector for document d, with 0 for each term in the vocabulary
        tv = [0] * len(voc)
        # add term counts from the document dictionary
        for t, cnt in td.iteritems():
            tv[voc.index(t)] = cnt
        dtm.append(tv)

    # Print out doc-term matrix
    if display:
        header = [""] + voc
        print ("{:>10}" * len(header)).format(*header)
        print "-" * 10 * len(header)

        for idx, tv in enumerate(dtm):
            print "{:<9}".format("Doc #" + str(idx)), ("{:>10}" * len(tv)).format(*tv)

    return dtm


# Compute the Jaccard similarity of two term vectors
def jaccard(tv1, tv2):
    # tv1 and tv2 must have the same length
    if len(tv1) != len(tv2):
        print "Error: term vectors must have the same length!"
        return -1

    cnt = sum = 0
    for i in range(len(tv1)):
        if tv1[i] == 1 or tv2[i] == 1:  # ignore 0-0 matches
            sum += 1
            if tv1[i] * tv2[i] > 0:  # both of them are non-zero
                cnt += 1

    return cnt / sum


# Compute the cosine similarity of two term vectors
def cosine(tv1, tv2):
    # tv1 and tv2 must have the same length
    if len(tv1) != len(tv2):
        print "Error: term vectors must have the same length!"
        return -1

    cnt = sum1 = sum2 = 0
    for i in range(len(tv1)):
        cnt += tv1[i] * tv2[i]
        sum1 += tv1[i] * tv1[i]
        sum2 += tv2[i] * tv2[i]

    return 0 if sum1 * sum2 == 0 else cnt / math.sqrt(sum1 * sum2)


if __name__ == '__main__':

    # Create document-term matrix
    dtm = doc_term_matrix(docs)

    # Compute the Jaccard similarity of documents
    print jaccard(dtm[0], dtm[1])  # doc 0 vs doc 1

    # Compute the cosine similarity of documents
    print cosine(dtm[0], dtm[1])  # doc 0 vs doc 1
