Practicum 7
===========

Learning objectives:

  - Building an inverted index and a document (meta)data store
  - Retrieval using the Boolean and Vector Space Models


## Notes

  - Since we work with small data, we will keep everything in memory during these exercises (the inverted index and the document metadata store)
  - The `indexer.py` file will be extended incrementally throughout Tasks 1--4. The solution shared on GitHub and on DataJoy shows the final outcome.


## Task 1. Creating an inverted index

  - Create an inverted index from a subset of the Reuters-21578 document collection given in `data/reuters21578-000.xml`
    * A skeleton that parses the XML file is already given
    * Extract index terms by preprocessing the text (tokenize, lowercase, remove stopwords -- see Practicum 6)
    * [The Reuters-21578 data collection](http://www.daviddlewis.com/resources/testcollections/reuters21578/)
  - Create an inverted index with the term frequencies stored
  - Save the inverted index in a text file. E.g., `termID docID1:freq1 docID2:freq2 ...`
  
  
## Task 2. Creating a document metadata store

  - For the retrieval part, we will also need document metadata: the length, date, and title of each document. Extend the indexing process (i.e., `indexer.py`) such that it also generates a document (meta)data store.
  - Save the document metadata in a separate text file. E.g., `docID length date title` tab-separated.


## Task 3. Retrieval using the Boolean model

  - Load the index from the disk that was created in Tasks 1 and 2.
  - Compose a boolean query by combining terms with operators AND, OR, NOT. 
    * Hint: a single term query is the atomic unit (TermQuery class); operators should combine one or more term queries (i.e., classes that take one or more term queries as parameters)
  - Try to create the following (or similar) queries:
    * "states"
    * "NOT washington"
    * "united AND states"
    * "(us OR (united AND states)) AND NOT washington"
  - Retrieve matching documents
    * Display the number of matching documents
    * If there are less than 20 matching documents, list the titles of the matches
  - Extend `indexer.py` with the necessary methods
    * Hint: you will need a method that returns the set of documents that contain a given term
  - Homework: Write a query parser that supports AND, OR, and NOT operators and grouping using (). E.g., be able to handle the query "(us OR (united AND states)) AND NOT washington"


## Task 4. Retrieval using the Vector Space Model

  - Load the index from the disk that was created in Tasks 1 and 2.
  - Rank documents using keyword queries (e.g., "united states") using the Vector Space Model
    * Use TF-IDF term weighting and cosine similarity
  - Display a ranked list of the top 10 matching documents, along with the corresponding relevance scores
  - Extend `indexer.py` with the necessary methods
    * Hint: you will need a method that returns the posting list for a given term
  - Homework: try some of the [different variants for TF and IDF weights](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
    