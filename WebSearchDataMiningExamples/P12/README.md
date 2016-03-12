Practicum 12
============

Learning objectives:

  - Understanding DBpedia
  - Performing entity retrieval using DBpedia
  - Performing entity linking using DBpedia


## Task 0. Understanding DBpedia

  - DBpedia is a "structured version" of Wikipedia
  - Check a couple of Wikipedia pages and their counterparts in DBpedia, e.g.,
    * Japan in [Wikipedia](https://en.wikipedia.org/wiki/Japan) and in [DBpedia](http://dbpedia.org/resource/Japan)
    * Whiplash (2014 film) in [Wikipedia](https://en.wikipedia.org/wiki/Whiplash_(2014_film)) and in [DBpedia](http://dbpedia.org/page/Whiplash_(2014_film))
    * New York City in [Wikipedia](https://en.wikipedia.org/wiki/New_York_City) and in [DBpedia](http://dbpedia.org/page/New_York_City)
  - Check the [DBpedia download pages](http://oldwiki.dbpedia.org/Downloads39) to see how the data is divided along various predicate types
  - Check the [DBpedia ontology](http://oldwiki.dbpedia.org/Ontology2014)
    * There is a [browsable version](http://mappings.dbpedia.org/server/ontology/classes/) with all the classes
  - Understanding redirects
    * If upon opening Wikipedia page A you are redirected to Wikipedia page B, then page B is a redirect of page A. It means that "A" is one of the names entity _B_ is frequently referred to (i.e., "A" is an alias for entity _B_).
    * For example, [NYC](https://en.wikipedia.org/wiki/NYC) redirects to [New York City](https://en.wikipedia.org/wiki/New_York_City), therefore, "NYC" is a redirect (or alias) for the entity _New York City
  
  
## Task 1. Performing entity retrieval using DBpedia
  
  - Build an entity index with the following fields:
    * _names_: entity names from `labels_en.nt`
    * _abstract_: short description (abstract) from `short_abstracts_en.nt`
    * _categories_: associated Wikipedia categories from `article_categories_en.nt`
  - Perform entity retrieval using a fielded model (BM25F). Compare different configurations:
    * Using only the names
    * Using names and abstract
    * Using names, abstract, and categories


## Task 2. Performing entity linking using DBpedia

  - Build a simple dictionary-based entity linker for a sample of entities.
    * Given an input query, identify all the entity mentions in the query and list candidate entities (i.e., entities that the mention might be referring to) for each mention.
  - Use the "primary" entity names from the `labels_en.nt` file.
  - Homework: extend the dictionary with redirect pages.
