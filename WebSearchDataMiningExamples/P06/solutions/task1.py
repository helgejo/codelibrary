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

# Init clustering method
clustering = KMeans(n_clusters=3, max_iter=10, init="random")
# Fit model to the data
clustering.fit(points)
# Predict cluster for each data point
labels = clustering.predict(points)
# Get the centroids
centroids = clustering.cluster_centers_

# Visualize the resulting clusters and cluster centroids
plt.clf()
plt.title('K-Means using K=3, 10 iterations, and random centroid selection')
# Data points
plt.scatter([x[0] for x in points], [x[1] for x in points], c=labels, marker='o', s=50)
# Centroids
plt.scatter([x[0] for x in centroids], [x[1] for x in centroids], c=range(len(centroids)), marker="+", s=250)
plt.show()


# ## K-Means clustering with configuration 2 (K=6, 3 iterations, and providing the initial centroids manually)

# Define the centroids manually
K = 6
centr_init = []
for i in range(K):
    centr_init.append([-3 + i, 6 - i])

# Init clustering method.
# Since we provide the centroids manually, we set the n_init (the number of time the k-means algorithm will be run
# with different centroid seeds) to 1.
clustering = KMeans(n_clusters=K, max_iter=3, n_init=1, init=np.array(centr_init))
# Fit model to the data
clustering.fit(points)
# Predict cluster for each data point
labels = clustering.predict(points)
# Get the centroids
centroids = clustering.cluster_centers_

# Visualize the resulting clusters and cluster centroids
plt.clf()
plt.title('K-Means using K=6, 3 iterations, and manual centroid selection')
plt.scatter([x[0] for x in points], [x[1] for x in points], c=labels, marker='o', s=50)
# Initial (manually provided) centroids (marked as x)
plt.scatter([x[0] for x in centr_init], [x[1] for x in centr_init], c=range(len(centr_init)), marker="x", s=50)
# Updated centroids (marked as +)
plt.scatter([x[0] for x in centroids], [x[1] for x in centroids], c=range(len(centroids)), marker="+", s=250)
plt.show()
