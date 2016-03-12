Practicum 9
===========

Learning objective:

  - Indexing a reasonably large text collection (first part of Assignment 3)
  

## Hints

  - Use a small subset of the collection (e.g., the first two files) during development. Once you're done, run the code on the full collection.
  - As it is written in the assignment's description, the input files are not valid XML files; they are simply HTML files concatenated together and separated by tags. Don't try to parse them as XML.
  - It might be helpful to decide early on if you want to extract only the document content or titles as well; then you don't have to process the collection twice. Extracting titles is easy (e.g., a regular expression to extract the content of `<title>..</title>` tags). 
  - Check the extracted text before you index it. The best way to do it is to pick a few random documents, save them as HTML files, open them in a browser, and then see if the text you extracted makes any sense.
  - Designing the index schema
    * Depending on whether you index titles as well, you need a schema with two (docID, content) or three (docID, content, title) fields. 
    * The docID field has to be of type `ID` and needs to be stored (you'll have look up the docIDs when writing result to the output file).
    * Textual fields are of type `TEXT`. By default these are not stored (and that is fine). The contents by default are processed using the [StandardAnalyzer](http://whoosh.readthedocs.org/en/latest/api/analysis.html#whoosh.analysis.StandardAnalyzer): it lowercases text and removes stopwords. Check the [analysis](http://whoosh.readthedocs.org/en/latest/api/analysis.html) module for other options (e.g., if you want to use stemming).  See `test_analyzers.py` on how to test different analyzers in isolation.
  - Indexing the full collection might take several hours. Make sure you leave enough time for that (e.g., run it overnight).

    
## References

  - [Designing a schema](http://whoosh.readthedocs.org/en/latest/schema.html)
  - [Analysis module](http://whoosh.readthedocs.org/en/latest/api/analysis.html)
