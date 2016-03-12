Practicum 8
===========

Learning objectives:

  - Indexing a document collection using Whoosh
  - Evaluating retrieval using various search effectiveness metrics


## Task 0. Installing Whoosh

  - We will be using the [Whoosh](https://pypi.python.org/pypi/Whoosh/) full-text indexing and searching Python library.
  - You can download and install it using `easy_install Whoosh` or `pip install Whoosh`.


## Task 1. Indexing documents with Whoosh

  - Build an index of a toy document collection using Whoosh.
    * Add `title` and `content` as indexed
    * See [this page](http://whoosh.readthedocs.org/en/latest/schema.html) for details on how to design the index schema
  - Load the index and check whether everything was done correctly by requesting the following information from it:
    * Number of documents the index contains
    * Number of times the term `document` appears in the title and content fields (i.e., term frequency)
    * Number of documents the term `document` appears in the title and content fields (i.e., document frequency)
    * Total length (number of terms) in the title and content fields
    * The posting list for the term `document` for the content field
  - See the [IndexReader](http://whoosh.readthedocs.org/en/latest/api/reading.html) and the [Whoosh recipes](http://whoosh.readthedocs.org/en/latest/recipes.html) pages for help.
  

## Task 2. Indexing the CACM collection with Whoosh

  - The CACM collection in `data/cacm.xml` contains 3024 documents.
  - Build an index of this collection using Whoosh by selecting the appropriate [Analyzer](http://whoosh.readthedocs.org/en/latest/api/analysis.html).
  - Check index statistics (see Task 1 for ideas).


## Task 3. Retrieval using the Vector Space Model

  - Take Task 4 from the last practicum (P07) and update the code such that the term statistics are taken from the Whoosh index we built in Task 2


## Task 4. Generate retrieval results in "batch mode"

 - Using the retrieval algorithm from Task 3, process the queries in `data/cacm.query.xml` and output the top 10 results to a single file, `data/cacm.out`, in the following format (one result per line) `queryID Q0 docID score`


## Task 5. Evaluate retrieval effectiveness

  - The ground truth is in `data/cacm.rel`. The format is `queryID Q0 docID rel` where `rel` is 1 if the document is relevant and 0 otherwise. 
    * This file contains only the relevant documents so the value will always be 1. This means that everything that is not in this file counts as non-relevant.
  - Write a script that computes P@5, P@10, Average Precision, and Reciprocal Ranks for each query as well as the averages over the entire query set for the output file generated in Task 4.


## References

  - [Whoosh documentation](http://whoosh.readthedocs.org/en/latest/)
  - [Whoosh recipes](http://whoosh.readthedocs.org/en/latest/recipes.html)
