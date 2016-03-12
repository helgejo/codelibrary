# Implementing Hierarchical Agglomerative Clustering
# ==================================================

# Task
# ----
#   - Cluster the "Italian cities" dataset (from Lecture 5) using Hierarchical Agglomerative Clustering
#   - Implement the Single link (MIN), Complete link (MAX), and Group average methods for comparing cluster proximities
#   - Bonus: visualize the different clusterings using dendograms

# Solution
# --------

from __future__ import division

# There imports are needed for visualizing the clustering using dendograms
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt
import numpy as np

# Cities
cities = ["BA", "FI", "MI", "NA", "RM", "TO"]

# Distances between the cities
dist = [[0, 662, 877, 255, 412, 996],
        [662, 0, 295, 468, 268, 400],
        [877, 295, 0, 754, 564, 138],
        [255, 468, 754, 0, 219, 869],
        [412, 268, 564, 219, 0, 669],
        [996, 400, 138, 869, 669, 0]]


# Perform Hierarchical Agglomerative Clustering
# - dist is a distance matrix
# - linkage can be "min" (single link), "max" (complete link), or "avg" (group average)
def hac(dist, linkage):
    # TODO Algorithm
    # 1. Compute the proximity matrix
    # 2. repeat
    #    3. Merge the closest two clusters
    #    4. Update the proximity matrix
    # 5. until only one cluster remains

    # TODO return the linkages for visualization
    pass


# Cluster data
linkages = hac(dist, "min")


# Bonus visualize the clusterings using dendograms
# See http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
# on how to construct the linkage matrix.
"""
linkage = [[0, 2, 10, 2],
           [1, 3, 20, 3]]
linkage_matrix = np.array(linkage)
plt.title("Single link")
dendrogram(linkage_matrix.astype(float),
           color_threshold=1,
           labels=cities,
           show_leaf_counts=True)
plt.show()
"""