# Text preprocessing using scikit-learn
# =====================================

# Task
# ----
#   - Create the document-term matrix from Task 2 using scikit-learn
#   - See [this document](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)

# Solution
# --------

from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "The King's Speech",
    "The Lord of the Rings: The Return of the King",
    "Street Kings",
    "The Scorpion King",
    "The Lion King"
]

cv = CountVectorizer(stop_words="english")

# Learns the vocabulary and returns the Document-term matrix
counts = cv.fit_transform(docs)

# Vocabulary
print cv.vocabulary_

# Document-term matrix
print counts.toarray()
