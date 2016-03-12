Executing a retrieval experiment
============

This project is about executing a retrieval experiment.

### Retrieval experiment

YImplement a baseline retrieval system and an improved version of the system.
Use any **baseline system** that does ranked retrieval and achieves a **minimum NDCG@10 of 0.3** on the given test collection. The **improved system** can be anything as long as it improves at least **10% over your own baseline**.

Later in this document you can find a list of ideas for baseline and improved systems.

### Report

Write a short (1-2 pages) report that includes the following sections.

  - **Collection and query processing**
    * How did you process documents and queries? Issues to cover include text extraction from HTML, tokenization, stemming, etc. 
  - **Baseline and improved retrieval systems**: 
    * Detail the baseline system (retrieval model and parameter settings).
    * Discuss how the improved system different is from the baseline system.
  - **Results** 
    * Include the following table with effectiveness results for the baseline and improved systems.
    
| System      |   P@5   |  P@10   |   MRR   |   MAP   | NDCG@10 |
| ----------- | ------- | ------- | ------- | ------- | ------- | 
| Baseline    |         |         |         |         |         |
| Improved    |         |         |         |         |         |
        
  - **Analysis**
    * Compare the baseline and improved systems on the query level. Create a plot that visualizes which queries improved and which degraded in the improved system, with respect to the baseline (use NDCG@10 as the basis of comparison). Identify the top 2-2 specific queries (with queryID and query content) that improved and degraded the most.

The document must be in pdf format and placed under the `report` folder.



## Data

### Document collection

The document collection is ~350MB compressed (4.2GB uncompressed!) and therefore it is not posted on GitHub. 


The document collection is a crawl of an organization's (CSIRO) intranet. It's split into a number of files (267 to be exact), where each file contains a number of documents in between `<DOC>` and `</DOC>`, where each document has the following structure:

```
<DOC>
<DOCNO>CSIROxxx-yyyyyyy</DOCNO>
<DOCHDR>
  /* document metadata */
</DOCHDR>
  /* HTML source  */
</DOC>
```

Mind that this is *not an XML file* and you should not attempt to parse it as such. You can simply read the file line-by-line, collect the lines in between `</DOCHDR>` and `</DOC>` and extract the textual content from it (e.g., using BeautifulSoup or any other technique you used for Assignment 2). You will also need to extract the document identifier inside `<DOCNO>..</DOCNO>`.

Indexing the collection is <70 lines of python code (a bit more if you also extract document titles), but it will take 6-9 hours on an average laptop. The index size is ~920MBs for a content-only index (i.e., without indexing document titles).


### Queries

The file `queries.xml` contains 50 queries. These are short, typical of what people use in search engines today.  The `id` attribute contains what we refer to as queryID below. 


### Relevance judgments

The `data/qrels.txt` file contains the relevance judgments for all the manually judged documents.  The format of the file is `queryID Q0 docID rel`, where

  - `queryID` is the query identifier (1 to 50)
  - the string `Q0` (that carries no meaning here)
  - `docID` is the document identifier (CSIROxxx-yyyyyyyy)
  - `rel` is the relevance level. Documents are graded on a three-point scale: (0) non-relevant, (1) somewhat relevant, (2) relevant.  
  
Note that the qrels file only contains the manually judged documents; all documents that are not explicitly listed for the given query are considered non-relevant.


### Result file

The retrieval results (document rankings) for all queries are to be written in a single file that has the following format: `queryID Q0 docID score`.

  - You can return **at most 50 results per query** (i.e., top 50 documents).
  - Documents need to be ordered by relevance (from more to less relevant).
  - The actual score values do not matter, the evaluation script only considers the ordering.

Put the two result files in the `output` folder: `baseline.out` and `improved.out`, corresponding to your baseline and improved retrieval systems.


### Evaluation script

An evaluation script is provided that compares the system generated ranking with the ground truth and computes effectiveness metrics. Note that the relevance judgments and result files follow the exact same format we used in Practicum 8. The evaluation script is also taken from Practicum 8, but has been extended to handle graded relevance judgments and to compute NDCG@10. For the metrics that take relevance to be binary (that is, all metrics except NDCG), all relevance levels >=1 count as relevant.

For example, evaluating your baseline ranking goes as follows from the command line:

```
python eval.py data/qrels.txt output/baseline.out
```

## Hints for the retrieval experiment

  - Using standard text preprocessing (HTML content removal and using the default analysis in Whoosh) and a Vector Space Model with TF-IDF term weighting should give you an NDCG@10 of about 0.34. Ranking using the BM25 model (default choice in Whoosh) should give you an NDCG@10 of about 0.65.
  -  Possibilities for getting improvements include, but are not limited to, the following:
    * **Different collection preprocessing** (e.g., stemming, collection-specific stopwords removal, etc.). 
        - It is the easiest option in terms of implementation, but it can be quite time-consuming as you will need to index the collection several times. Also, it is not guaranteed that you can get the 10% improvement using this method. 
    * **Different retrieval method** Compare two different retrieval methods. Hint: use the Vector Space Model with TF-IDF term weighting as your baseline (that is, choose a weak baseline). Then, for the improved model, you can use the BM25 model out-of-the box (it is shipped with Whoosh) or implement Language Models yourself. (We will cover these models in Lecture 9.) 
        - Implementing Language Models will give you a great learning experience, highly recommended. The 10% improvement over TF-IDF is guaranteed.
    * **Fielded retrieval model** Extract document titles and add them as a separate field to the index. Use a fielded extension of BM25 or Language Modeling. (We will cover these techniques in Lecture 9.)
        - Relatively easy to do and useful in practice. It should get you the required improvement (but this has not been tested).
    * **Document priors** Not all documents are equally important in the collection. You can detect specific document types (e.g., media releases or research highlight pages) using simple rules and assign more prior importance to these types of pages. (We will cover these techniques in Lecture 9.)
        - Relatively easy to do; might need to be combined with some of the other techniques though to get the required overall improvement.
    * **Query modeling** Use relevance feedback. (We will cover these techniques in Lecture 10.)
        - This is for maximum learning experience.
  - Note that you can combine multiple techniques. If you're serious about winning as many queries as possible, you should really try to stack up things. E.g., use a fielded model, tune the parameters, use document priors, and even relevance feedback.
