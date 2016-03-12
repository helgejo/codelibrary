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
    # Tokenization
    # Lowercasing
    # Stopword removal
    # Suffix-s stemming
    return terms


# Create (and print out) the document-term matrix from an input set of documents
def doc_term_matrix(docs, display=True):
    dtm = []
    for d in docs:
        terms = preprocess(d)
        # TODO create term vector out of preprocessed terms and add to matrix

    if display:
        # TODO print out doc-term matrix
        pass

    return dtm


# Compute the Jaccard similarity of two term vectors
def jaccard(tv1, tv2):
    # tv1 and tv2 must have the same length
    if len(tv1) != len(tv2):
        print "Error: term vectors must have the same length!"
        return -1

    # TODO

    return 0


# Compute the cosine similarity of two term vectors
def cosine(tv1, tv2):
    # tv1 and tv2 must have the same length
    if len(tv1) != len(tv2):
        print "Error: term vectors must have the same length!"
        return -1

    # TODO

    return 0


if __name__ == '__main__':

    # Create document-term matrix
    dtm = doc_term_matrix(docs)

    # Compute the Jaccard similarity of documents
    print jaccard(dtm[0], dtm[1])  # doc 0 vs doc 1

    # Compute the cosine similarity of documents
    print cosine(dtm[0], dtm[1])  # doc 0 vs doc 1
