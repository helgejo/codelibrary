# Creating an inverted index
# ==========================

# Task 1
# ------
#   - Create an inverted index from a subset of the Reuters-21578 document collection given in `data/reuters21578-000.xml`
#     * A skeleton that parses the XML file is already given
#     * Extract index terms by preprocessing the text (tokenize, lowercase, remove stopwords -- see Practicum 6)
#     * [The Reuters-21578 data collection](http://www.daviddlewis.com/resources/testcollections/reuters21578/)
#   - Create an inverted index with the term frequencies stored
#   - Save the inverted index in a text file. E.g., `termID docID1:freq1 docID2:freq2 ...`

# Task 2
# ------
#   - For the retrieval part, we will also need document metadata: the length, date, and title of each document.
#     Extend the indexing process (i.e., `indexer.py`) such that it also generates a document (meta)data store.
#   - Save the document metadata in a separate text file. E.g., `docID length date title` tab-separated.

# Task 3
# ------
#   - Extend `indexer.py` with the necessary methods to support retrieval with the Boolean model

# Task 4
# ------
#   - Extend `indexer.py` with the necessary methods to support retrieval with the Vector Space model

# Solution
# --------

from xml.dom import minidom


# Parse an input text and return a list of indexable terms
def parse(text):
    # TODO, Task 1: tokenization, lowercasing, stopword removal, plus anything collection-specific
    return text.split()


# A "posting" is an entry in the index.
# We use the payload to store a single number, the frequency of the term in the document.
class Posting(object):

    def __init__(self, doc_id, payload):
        self.doc_id = doc_id
        self.payload = payload


# The Indexer class takes care of the entire indexing process.
class Index(object):

    def __init__(self):
        self.index = {}  # the inverted index is represented as a dictionary (terms) of lists (postings, i.e., docs with frequencies)

    def add_posting(self, term, doc_id, payload):
        if term not in self.index:  # if term not in index, initialize empty posting list
            self.index[term] = []
        # TODO, Task 1: append new posting to the posting list

    # Index a given document
    def index_doc(self, doc_id, date, title, body):
        #print date, title
        terms = parse(title + " " + body)  # include both title and body content in the index
        #print terms
        # TODO, Task 1: create a posting from each term with the freqency as payload
        # (Hint: create a dictionary from terms with frequencies first, then make a posting from each dictionary entry)

    # Create an index from an input XML file
    def index_file(self, input_file):
        xmldoc = minidom.parse(input_file)
        # iterate documents in the XML file
        itemlist = xmldoc.getElementsByTagName("REUTERS")
        doc_id = 0
        for doc in itemlist:
            doc_id += 1
            date = doc.getElementsByTagName("DATE")[0].firstChild.nodeValue
            # skip documents without a title or body
            if not (doc.getElementsByTagName("TITLE") and doc.getElementsByTagName("BODY")):
                continue
            title = doc.getElementsByTagName("TITLE")[0].firstChild.nodeValue
            body = doc.getElementsByTagName("BODY")[0].firstChild.nodeValue
            self.index_doc(doc_id, date, title, body)
            # TODO, Task 2: Add document to the document metadata store

    # Save the index to a file
    def write_to_file(self, filename):
        # TODO, Task 1
        pass

    # Load the index from a file
    def load_from_file(self, filename):
        # TODO, Task 3
        pass

# If it runs as a stand-alone program
if __name__ == "__main__":
    index = Index()
    # You need to change the paths to "../data" if you are working on your local machine
    index.index_file("data/reuters21578-000.xml")
    index.write_to_file("data/index.txt")
