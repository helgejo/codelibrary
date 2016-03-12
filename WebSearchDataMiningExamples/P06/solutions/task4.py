# Hierarchical Agglomerative Clustering of documents using scikit-learn
# =====================================================================

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

# ## A) Hierarchical agglomerative clustering using scikit-learn
# Notes for the scikit-learn agglomerative clustering implementation
# - Only three cluster proximity methods are supported (ward, average, complete), single link, for example is not
# - When cosine similarity is used, there are only two: average and complete
# - It is not possible to get the distances between the clusters (or would be cumbersome to have them returned, see
#   http://stackoverflow.com/questions/26851553/sklearn-agglomerative-clustering-linkage-matrix)
# - It is not possible to get the information needed for generating a dendrogram
for linkage in ("average", "complete"):
    clustering = AgglomerativeClustering(linkage=linkage, affinity="cosine", n_clusters=3)
    clustering.fit(dtm)
    print linkage, clustering.labels_

# ## B) Hierarchical agglomerative clustering using scipy
# (See http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.cluster.hierarchy.linkage.html)
for linkage in ("average", "single", "complete"):
    # `z` containts the linkage matrix which includes the distances of the merged clusters
    # (shown as the value on the y-axis of the dendrograms)
    # See the link above on the format of matrix `z`.
    z = hac.linkage(dtm, method=linkage, metric="cosine")
    plt.clf()
    plt.title("HAC " + linkage + " linkage")
    hac.dendrogram(z,
               color_threshold=1,
               labels=range(len(docs)),
               show_leaf_counts=True)
    plt.show()
