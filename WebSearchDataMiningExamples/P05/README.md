Practicum 5
===========

Learning objectives:

  - Implementing K-Means and Bisecting K-Means clustering algorithms
  - Implementing Hierarchical Agglomerative Clustering using different cluster proximities
  - Visualizing clusters (scatterplots and dendrograms)
  

## Task 1. Implementing K-Means clustering
 
  - A set of 2D data points are given (generated artificially)
  - Select the centroids initially randomly from the data points
  - Repeat until the cluster assignments change for less than 1% of the data points
  - Visualize the cluster assignments and centroids after each iteration

[Solution on DataJoy](https://www.getdatajoy.com/examples/560528d1fe8ed5175c3f9e26)  


## Task 2. Implementing Bisecting K-Means clustering
  
  - Solve the previous task using the bisecting variant of K-Means
  - Measure the quality of the resulting clustering in terms of Sum of Squared Error (SSE)
    * How does it compare to the SSE of the 'true' clustering?

[Solution on DataJoy](https://www.getdatajoy.com/examples/56080339896c84651dfcffe1)  


## Task 3. Implementing Hierarchical Agglomerative Clustering

  - Cluster the "Italian cities" dataset (from Lecture 5) using Hierarchical Agglomerative Clustering
  - Implement the Single link (MIN), Complete link (MAX), and Group average methods for comparing cluster proximities
  - Bonus: visualize the different clusterings using dendrograms

[Solution on DataJoy](https://www.getdatajoy.com/examples/56080495fe8ed5175c3f9e33)  
