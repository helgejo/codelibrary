from __future__ import division
from whoosh import scoring
from whoosh import qparser
import whoosh.index as index
from xml.dom import minidom
from whoosh.searching import Searcher

__author__ = 'HELGE BJORLAND'

index_dir = "../data/index3"
query_file = "../data/queries.xml"
output_file = "../output/baseline_bm25_test1.out"
field = "content"
fields = ["title", "content"]


# Load queries from the query xml file
def load_queries():
    queries = []
    xmldoc = minidom.parse(query_file)
    queriez = xmldoc.getElementsByTagName("query")
    for query in queriez:
            query_id = query.getAttribute("id")
            text = query.firstChild.nodeValue
            queries.append({'id': query_id, 'text': text})
    return queries


def score_to_file():

    # Open index
    ix = index.open_dir(index_dir)

    # Use the reader to get statistics
    reader = ix.reader()

    queries = load_queries()

    outfile = open(output_file, "w")
    with ix.searcher(weighting=scoring.BM25F()) as searcher:
    # with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
        qp = qparser.QueryParser(field, schema=ix.schema)
        # qp = qparser.MultifieldParser(fields, schema=ix.schema)
        for query in queries:
            print("Processing query number", query['id'])

            # Retrieve documents using the vector space model
            q = qp.parse(query['text'])  # we contatenate query terms
            res = searcher.search(q)
            # res = get_score(searcher, qp, query['text'])
            for r in res:
                outfile.write(query['id'] + " Q0 " + r['id'] + " " + str(r.score) + "\n")
            # Output max 50 results
            # for docnum in sorted(res, key=res.get, reverse=True)[:50]:
            #     # Look up our docID
            #     stored = reader.stored_fields(docnum)
            #     # Write `docID Q0 queryID score` into output file
            #     outfile.write(query['id']+ " Q0 " + stored['id'] + " " + str(res[docnum]) + "\n")
        outfile.close()
    ix.close()


def test():
    queries = load_queries()

    ix = index.open_dir(index_dir)
    qp = qparser.QueryParser('content', ix.schema)
    q = qp.parse("id")
    with ix.searcher(weighting=scoring.TF_IDF()) as searcher_tfidf:
        scoring.TFIDF().scorer(searcher_tfidf, 'body', 'algebra').score(q.matcher(searcher_tfidf))
    with ix.searcher(weighting=scoring.BM25F()) as searcher_bm25f:
        scoring.BM25F().scorer(searcher_bm25f, 'body', 'algebra').score(q.matcher(searcher_bm25f))

    #pos_weighting = scoring.FunctionWeighting(pos_score_fn)
    #with myindex.searcher(weighting=pos_weighting) as s:


def test2():
    queries = load_queries()

    ix = index.open_dir(index_dir)
    mysearcher = Searcher(ix)
    #mysearcher = ix.searcher(weighting=scoring.BM25F())
    for query in queries:
        print("Processing query number", query['id'])
        results = mysearcher.search(query['text'], limit=10)
        print(results)


def get_score(searcher, qp, query):
    q = qp.parse(query)  # we contatenate query terms
    results = searcher.search(q)
    for r in results:
        print(r['id'], str(r.score)[0:6])
    # ix.close()
    return results

if __name__ == '__main__':
    score_to_file()
