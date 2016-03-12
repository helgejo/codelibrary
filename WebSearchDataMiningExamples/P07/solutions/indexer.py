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
from collections import Counter
import re

# Stopwords list
stopwords = [
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in",
    "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the",
    "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"
]


# Strip tags using regex
def striptags(text):
    p = re.compile(r'<.*?>')
    return p.sub('', text)


# Parse an input text and return a list of indexable terms
def parse(text):
    terms = []
    # Replace specific characters with space
    chars = ["'", ".", ":", ",", "!", "?", "(", ")"]
    for ch in chars:
        if ch in text:
            text = text.replace(ch, " ")

    # Remove tags
    text = striptags(text)

    # Tokenization
    for term in text.split():  # default behavior of the split is to split on one or more whitespaces
        # Lowercasing
        term = term.lower()
        # Stopword removal
        if term in stopwords:
            continue
        terms.append(term)

    return terms


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
        self.docs = {}  # the document metadata store is represented as a dictionary (docID) of dictionaries (length, date, title)

    def add_posting(self, term, doc_id, payload):
        if term not in self.index:  # if term not in index, initialize empty posting list
            self.index[term] = []
        # append new posting to the posting list
        self.index[term].append(Posting(doc_id, payload))

    # Index a given document and returns the length of the document
    def index_doc(self, doc_id, date, title, body):
        terms = parse(title + " " + body)  # include both title and body content in the index
        for term, cnt in Counter(terms).iteritems():
            self.add_posting(term, doc_id, cnt)
        return len(terms)

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
            doclen = self.index_doc(doc_id, date, title, body)
            # Add document to the document metadata store
            self.docs[doc_id] = {
                "length": doclen,
                "date": date,
                "title": title
                }

    # Save the index and document metadata files
    def write_to_file(self, filename_index, filename_meta):
        # Write index to file
        f = open(filename_index, "w")
        for term, postings in self.index.iteritems():
            f.write(term)
            for posting in postings:
                f.write(" " + str(posting.doc_id) + ":" + str(posting.payload))
            f.write("\n")
        f.close()

        # Write document metadata to file
        f = open(filename_meta, "w")
        for doc_id, meta in self.docs.iteritems():
            f.write("\t".join([str(doc_id), str(meta['length']), meta['date'], meta['title']]) + "\n")
        f.close()

    # Load index and document metadata from a file
    def load_from_file(self, filename_index, filename_meta):
        # Load index
        self.index = {}
        for line in open(filename_index, "r"):
            tmp = line.split()
            term = tmp[0]
            self.index[term] = []
            for i in range(1,len(tmp)):
                [doc_id, cnt] = tmp[i].split(":")
                self.index[term].append(Posting(doc_id, cnt))

        # Load document metadata
        self.docs = {}
        for line in open(filename_meta, "r"):
            tmp = line.split("\t")
            doc_id = tmp[0]
            self.docs[doc_id] = {
                "length": int(tmp[1]),
                "date": tmp[2],
                "title": tmp[3]
                }

    # Return a set of document IDs that contain the given term,
    # or the set of all documents if there is no term given
    # (Added for Task 3)
    def get_docs_set(self, term=None):
        if term is None:
            return set(self.docs.keys())
        if term in self.index:
            return set([p.doc_id for p in self.index[term]])
        return set()

    # Get metadata for a given document
    # (Added for Task 3)
    def get_doc_meta(self, doc_id):
        if doc_id in self.docs:
            return self.docs[doc_id]
        return None

    # Get the number of documents in the index
    # (Added for Task 4)
    def num_docs(self):
        return len(self.docs)

    # Get the posting list for a given term
    # (Added for Task 4)
    def get_postings(self, term):
        if term in self.index:
            return self.index[term]
        return None


# If it runs as a stand-alone program
if __name__ == "__main__":
    index = Index()
    # You need to change the paths to "../data" if you are working on your local machine
    index.index_file("../data/reuters21578-000.xml")
    index.write_to_file("../data/index.txt", "../data/meta.txt")
