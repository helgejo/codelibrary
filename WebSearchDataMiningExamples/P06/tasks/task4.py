# Perform Hierarchical Agglomerative Clustering of documents using scikit-learn
# =============================================================================

# Task
# ----

# - Cluster the documents from Task 2 using Hierarchical Agglomerative Clustering with scikit-learn
# - Use cosine similarity
# - Compare the different available cluster proximity methods available
# - Visualize the different clusterings using dendrograms
# - See [this document](scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html) for help
# - Can you introduce a similarity threshold for merging clusters? Or, in other words, can you extract the distance between clusters?

# Solution
# --------

from __future__ import division

import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

from task2 import docs, doc_term_matrix

# Create document-term matrix
dtm = doc_term_matrix(docs, display=False)

# Hierarchical agglomerative clustering using scikit-learn

# TODO perform clustering

# TODO visualize clusterings using dendograms

# TODO extract distances between clusters
