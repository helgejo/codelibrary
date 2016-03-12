Practicum 6
===========

Learning objectives:

  - Using clustering algorithms in scikit-learn
  - Text preprocessing
  - Document similarity calculation
  

## Task 1. K-Means clustering using scikit-learn

  - A set of 2D data points are given (generated artificially)
  - Perform K-means clustering using scikit-learn using the following two configurations:
    * K=3, 10 iterations, and random centroid selection
    * K=6, 3 iterations, and providing the initial centroids manually
  - Visualize the resulting clusters and the cluster centroids
  - See [this document](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) for help

[Solution on DataJoy](https://www.getdatajoy.com/examples/560ec3d4896c84651dfd0017)  


## Task 2. Text preprocessing and document similarity

  - Write a function that creates (and prints out) the document-term matrix from an input set of documents
  - Apply the following preprocessing steps:
    * Tokenization
    * Lowercasing
    * Stopword removal
    * Suffix-s stemming
  - Implement a function that computes the Jaccard similarity of two term vectors
  - Implement a function that computes the cosine similarity of two term vectors

[Solution on DataJoy](https://www.getdatajoy.com/examples/560ec51dfe8ed5175c3f9e58)  


## Task 3. Text preprocessing using scikit-learn
  
  - Create the document-term matrix from Task 2 using scikit-learn
  - See [this document](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)

[Solution on DataJoy](https://www.getdatajoy.com/examples/560ec5bf896c84651dfd001c)  


## Task 4. Hierarchical Agglomerative Clustering of documents using scikit-learn

  - Cluster the documents from Task 2 using Hierarchical Agglomerative Clustering with scikit-learn
  - Use cosine similarity
  - Compare the different available cluster proximity methods available
  - Visualize the different clusterings using dendrograms
  - See [this document](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html) for help
  - Can you introduce a similarity threshold for merging clusters? Or, in other words, can you extract the distance between clusters? 
    
[Solution on DataJoy](https://www.getdatajoy.com/examples/560ec7b1896c84651dfd001e)  


## References

  - [Clustering in scikit-learn](http://scikit-learn.org/stable/modules/clustering.html)
    