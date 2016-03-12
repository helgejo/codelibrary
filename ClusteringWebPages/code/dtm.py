
from __future__ import division
import textmining
import math
from sklearn.feature_extraction.text import CountVectorizer
__author__ = 'HELGJO'

# Set of input documents
doc = "The King's Speech"
doc1 = 'John and Bob are brothers.'
doc2 = "The Lord of the Rings: The Return of the King"
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
tdm = textmining.TermDocumentMatrix()
tdm.add_doc(doc)
tdm.add_doc(doc1)
tdm.add_doc(doc2)



for row in tdm.rows(cutoff=1):
    print row

print [row[1] for row in tdm.rows(cutoff=1)]
#print textmining.read_names("E:\Github\ass2data\test\Alvin_Cooper\docs\002.html")
#can this be used to extract the names?
#print cosine(tdm[0], tdm[1])

cv = CountVectorizer(stop_words="english")

# Learns the vocabulary and returns the Document-term matrix
counts = cv.fit_transform(docs)

# Vocabulary
print cv.vocabulary_
# Document-term matrix
print counts.toarray()
print counts
