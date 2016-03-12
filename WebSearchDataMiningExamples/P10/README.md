Practicum 10
============

Learning objectives:

  - Implementing various retrieval methods


## Task 0. Index the toy document colletion

  - Build an index of a toy document collection using Whoosh.
  - The code is written, you just need to run it.
  

## Task 1. Understanding TFIDF scoring

  - Rank the toy document set for the given query by implementing TFIDF scoring.
  - Compare with the document ranking you get using the TFIDF scorer implemented in Whoosh.
  
  
## Task 2. Understanding BM25 scoring
  
  - Rank the toy document set for the given query by implementing BM25 scoring.
  - Compare with the document ranking you get using the BM25 scorer implemented in Whoosh.
  - Check the document rankings with different parameter settings.


## Task 3. Understanding LM scoring
  
  - Rank the toy document set for the given query by implementing LM scoring.
    * Note: this implementation is not entirely correct; LM scoring would require some modifications to `MyBaseScorer`. Currently, `MyBaseScorer` only scores terms that are in the document.  When LM scoring is used, documents get a score after each query term, even if even if they are not present in the document, because of smoothing. 
    
