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
        pass

    def to_string(self):
        return ""


# Query containing a single search term
class TermQuery(Query):

    def __init__(self, term):
        self.term = term

    def to_string(self):
        return self.term

    def get_matches(self, index):
        res = index.get_docs_set(self.term)
        return res


# NOT query for negating any query
class NotQuery(Query):

    def __init__(self, query):
        self.query = query

    def to_string(self):
        return "NOT (" + self.query.to_string() + ")"

    def get_matches(self, index):
        res = index.get_docs_set() - self.query.get_matches(index)
        return res


# AND or OR query
class BooleanQuery(Query):

    def __init__(self, operator, subqueries):
        self.operator = operator
        self.subqueries = subqueries

    def to_string(self):
        substr = []
        for sq in self.subqueries:
            substr.append(sq.to_string())
        return "(" + (" " + self.operator + " ").join(substr) + ")"

    def get_matches(self, index):
        # Collect results for sub-queries
        subres = []
        for sq in self.subqueries:
            subres.append(sq.get_matches(index))
        if self.operator == "AND":
            res = set.intersection(*subres)
        if self.operator == "OR":
            res = set.union(*subres)
        return res

# Retrieve documents matching a query and displaying the number of results.
# If there are less than 20 matching documents, list the titles of the matches.
def run_query(query, index):
    print "Query:   ", query.to_string()
    docs = query.get_matches(index)
    print "Results: ", len(docs)
    if len(docs) < 20:
        print "---- RESULTS ----"
        for doc_id in docs:
            docmeta = index.get_doc_meta(doc_id)
            print docmeta['date'], docmeta['title']

# Load index
index = Index()
index.load_from_file("../data/index.txt", "../data/meta.txt")

# Term query: `states`
q1 = TermQuery("states")
run_query(q1, index)

# NOT query: `NOT (washington)`
q2 = NotQuery(TermQuery("washington"))
run_query(q2, index)

# AND query: `(united AND states)`
q3 = BooleanQuery("AND", [TermQuery("united"), TermQuery("states")])
run_query(q3, index)

# OR query: `(us OR (united AND states))`
q4 = BooleanQuery("OR", [TermQuery("us"), q3])
run_query(q4, index)

# Complex query: `((us OR (united AND states)) AND NOT (washington))`
q5 = BooleanQuery("AND", [q4, q2])
run_query(q5, index)
