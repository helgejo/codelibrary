# Implementing Bisecting K-Means clustering
# =========================================

# Task
# ----
#   - Solve the previous task using the bisecting variant of K-Means
#   - Measure the quality of the resulting clustering in terms of Sum of Squared Error (SSE)
#     * How does it compare to the SSE of the 'true' clustering?

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


# Compute Sum of Squared Error (SSE) for a clustering.
# The variable clusters is a list (clusters) of lists (points).
# The variable centroids contains the cluster centroids.
# I.e., for cluster i, clusters[i] is the list of points assigned to that cluster
# and centroids[i] is the centroid of the cluster.
def sse(clusters, centroids):
    sse = 0
    for i in range(len(clusters)):
        for x in clusters[i]:
            sse += dist(x, centroids[i])
    return sse


# Perform K-means clustering
def kmeans(k, points):
    # TODO This is to be copied from Task 1
    pass


# Perform Bisecting K-Means clustering on a set of data points given the user-specified parameter k
def bikmeans(k, points):
    # TODO Algorithm
    # 1. Initial cluster contains all data points
    # 2. repeat
    #    3. Select a cluster to split
    #    4. for a number of trials
    #       5. Bisect the selected cluster using basic K-means
    #    6. end for
    #    7. Select the clusters from the bisection with the lowest total SSE
    # 8. until we have K clusters
    pass


# Data points (generated randomly)
N = 200
points, clusters = make_blobs(n_samples=N, centers=3, n_features=2, cluster_std=0.8, random_state=0)

# Visualize the initial data points with the 'true' clusters
plt.clf()
plt.scatter(points[:, 0], points[:, 1], c=clusters, marker='o', s=50)
plt.title('True cluster assignments')
plt.show()

# Compute the SSE for the 'true' clusters
# TODO

# Call clustering method
bikmeans(3, points)
