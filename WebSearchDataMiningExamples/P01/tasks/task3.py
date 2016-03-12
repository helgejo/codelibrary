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

# This function computes the similarity between two documents based on the Jaccard coefficient.
# TODO
def sim(doc1, doc2):
    return 0

# Print similarity
print(sim(doc1, doc2))
