# Implementing K-Means clustering
# ===============================

# Task
# ----
#   - A set of 2D data points are given (generated artificially)
#   - Select the centroids initially randomly from the data points
#   - Repeat until the cluster assignments change for less than 1% of the data points
#   - Visualize the cluster assignments and centroids after each iteration

# Solution
# --------

from __future__ import division

import math
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs


# Compute Eucledian distance between two points given as vectors (lists)
def dist(p1, p2):
    s = 0
    for i in range(len(p1)):
        s += math.pow(p1[i] - p2[i], 2)
    return math.sqrt(s)


# Perform K-Means clustering on a set of data points given the user-specified parameter k
def kmeans(k, points):
    # TODO Algorithm
    # 1. select K points as initial centroids
    # 2. repeat
    #    3. Form K clusters by assigning each point to its closest centroid
    #    4. Recompute the centroid of each cluster
    #    (visualize the cluster assignments and centroids)
    # 5. until the cluster assignments change for less than 1% of the data points
    pass


# Data points (generated randomly)
N = 200
points, clusters = make_blobs(n_samples=N, centers=3, n_features=2, cluster_std=0.8, random_state=0)

# Visualize the initial data points with the 'true' clusters
plt.clf()
plt.scatter(points[:, 0], points[:, 1], c=clusters, marker='o', s=50)
plt.title('True cluster assignments')
plt.show()

# Call clustering method
kmeans(3, points)
