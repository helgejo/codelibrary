# Finding k-nearest neighbors using Eucledian distance
# ====================================================

# Task
# ----
#  - Generate n=100 random points in a two dimensional space. Let both
#    the x and y attributes be int values between 1 and 100.
#  - Display these points on a scatterplot.
#  - Select one of these points randomly (i.e., pick a random index).
#  - Find the k closest neighbors of the selected record (i.e., the k records
#    that are most similar to it) using the Eucledian distance.
#    The value of k is given (i.e., hard-coded).
#  - Display the selected record and its k closest neighbors in a distinctive
#    manner on the plot (e.g., using different colors).

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We import the matplotlib submodule **pyplot**, to plot 2d graphics;
# following a widely used convention, we use the `plt` alias.
# We also need the **random** module for generating random numbers and the **math** module
# for computing `sqr` and `pow`.
import matplotlib.pyplot as plt
import random
import math

# The number of random points we want.
n = 100

# The number of nearest neighbors.
k = 5

# Compute Eucledian distance between two points.
# The points are given by their indices in the x and y arrays.
# Their distance then is computed as follows:
# $d = \sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$
# where $x_1$ and $y_1$ are the coordinates of the first point (given by index i1)
# and $x_2$ and $y_2$ are the coordinates of the second point (given by index i2)

def dist_eucledian(i1, i2):
    return math.sqrt(math.sqrt(math.pow(x[i1]-x[i2], 2) + math.pow(y[i1]-y[i2], 2)))

# Generate random points with x and y coordinates and set them to the default color (blue).
x = []
y = []
c = []
for i in range(n):
    x.append(random.randint(1, 100))
    y.append(random.randint(1, 100))
    c.append("blue")

# Pick a selected point (random point index) and set it to a different color (red).
sel = random.randint(0, n - 1)
c[sel] = "red"

# Compute the distances between the selected point and all other points.
# The results are stored in a dictionary where the key is the index of the point
# (in the x, y, and c lists) and the value is its distance from the selected point.
d = {}
for i in range(n):
    if i != sel:
        d[i] = dist_eucledian(i, sel)

# Find k-nearest neighbors. We sort dictionary d by value (which holds the distances)
# and use `[:k]` to pick the first k elements. We print the index and distance of
# these points and color them (to cyan).
for w in sorted(d, key=d.get)[:k]:
    print w, d[w]
    c[w] = "cyan"

# Plot data.
# The selected point is displayed in red. The k nearest neighbors are shown in cyan.
# All other points are blue.
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.scatter(x, y, c=c)
plt.show()
