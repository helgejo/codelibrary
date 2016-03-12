# Retrieval using the Boolean model
# =================================

# Task
# ------
#   - Load the index from the disk that was created in Tasks 1 and 2.
#   - Compose a boolean query by combining terms with operators AND, OR, NOT.
#     * Hint: a single term query is the atomic unit (TermQuery class); operators should combine one or more term
#       queries (i.e., classes that take one or more term queries as parameters)
#   - Try to create the following (or similar) queries:
#     * "states"
#     * "NOT washington"
#     * "united AND states"
#     * "(us OR (united AND states)) AND NOT washington"
#   - Retrieve matching documents
#     * Display the number of matching documents
#     * If there are less than 20 matching documents, list the titles of the matches
#   - Extend `indexer.py` with the necessary methods
#     * Hint: you will need a method that returns the set of documents that contain a given term
#   - Homework: Write a query parser that supports AND, OR, and NOT operators and grouping using ().
#     E.g., be able to handle the query "(us OR (united AND states)) AND NOT washington"

# Solution
# --------

from indexer import Index

# Base query class (parent of all query classes)
class Query(object):

    def __init__(self):
        pass

    def get_matches(self, index):
        # TODO, return all documents IDs (as a set) from the index
        pass

# Query containing a single search term
class TermQuery(Query):

    def __init__(self, term):
        self.term = term

    def get_matches(self, index):
        # TODO, return all documents IDs (as a set) that contain the search term
        pass


# Load index
index = Index()
index.load_from_file("data/index.txt")

# TODO, construct the following (or similar) queries and get results
# - "states"
# - "NOT washington"
# - "united AND states"
# - "(us OR (united AND states)) AND NOT washington"
