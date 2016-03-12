# Perform K-Means clustering using scikit-learn
# =============================================

# Task
# ----
#   - A set of 2D data points are given (generated artificially)
#   - Perform K-means clustering using scikit-learn using the following two configurations:
#     * K=3, 10 iterations, and random centroid selection
#     * K=6, 3 iterations, and providing the initial centroids manually
#   - Visualize the resulting clusters and the cluster centroids
#   - See [this document](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) for help

# Solution
# --------

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


# Data points (generated randomly)
N = 200
points, clusters = make_blobs(n_samples=N, centers=3, n_features=2, cluster_std=0.8, random_state=0)
points = np.array(points).tolist()

# Visualize the 'true' clusters
plt.clf()
plt.title('True cluster assignments')
plt.scatter([x[0] for x in points], [x[1] for x in points], c=clusters, marker='o', s=50)
plt.show()


# ## K-Means clustering with configuration 1 (K=3, 10 iterations, and random centroid selection)

# Perform clustering
# TODO

# Visualize the resulting clusters and cluster centroids
plt.clf()
plt.title('K-Means using K=3, 10 iterations, and random centroid selection')
# TODO
plt.show()


# ## K-Means clustering with configuration 2 (K=6, 3 iterations, and providing the initial centroids manually)

# Define the centroids manually
K = 6
# TODO

# Perform clustering
# TODO

# Visualize the resulting clusters and cluster centroids
plt.clf()
plt.title('K-Means using K=6, 3 iterations, and manual centroid selection')
# TODO
plt.show()
