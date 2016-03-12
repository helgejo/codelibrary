# Computing similarity between documents
# ======================================

# Task
# ----
#  - Compute the similarity between two documents.
#  - Represent each document as a vector of binary attributes: if a given word is present
#    in the document or not.
#  - You can then use the Jaccard coefficient.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# The input documents are given here as strings.
# We use triple-quoted strings (note that we will need to deal with newlines when processing them).
doc1 = """Yellow Submarine
By: The Beatles

In the town where I was born
Lived a man who sailed to sea
And he told us of his life
In the land of submarines

So we sailed up to the sun
Till we found the sea of green
And we lived beneath the waves
In our yellow submarine"""

doc2 = """Son of a son of a sailor
By: Jimmy Buffett

As the son of a son of a sailor
I went out on the sea for adventure
Expanding the view of the captain and crew
Like a man just released from indenture

As a dreamer of dreams and a travelin man
I have chalked up many a mile
Read dozens of books about heroes and crooks
And I learned much from both of their styles
"""

# This function returns a list of unique terms in a document
def get_terms(doc):
    terms = []
    for term in doc.lower().split():
        if term not in terms:
            terms.append(term)
    return terms

# This function computes the similarity between two documents based on the Jaccard coefficient.
# Put simply, it is the number of words that appear in both documents, divided by the number
# of words that appear in any of the two documents.
def sim(doc1, doc2):
    terms1 = get_terms(doc1)
    terms2 = get_terms(doc2)
    common_terms = set(terms1) & set(terms2)
    all_terms = set(terms1) | set(terms2)
    return len(common_terms) / len(all_terms)

# Print similarity
print(sim(doc1, doc2))
