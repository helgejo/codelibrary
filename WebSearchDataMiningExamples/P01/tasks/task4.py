# Discretization
# ==============

# Task
# ----
#  - Create an ordinal attribute `file size` with the following 5 possible values
#    {tiny, small, medium, large, huge}.
#  - Implement both the equal width and equal frequency methods.
#  - Display the data on a plot.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We import the matplotlib submodule **pyplot**, to plot 2d graphics;
# following a widely used convention, we use the `plt` alias.
import matplotlib.pyplot as plt

# We will use the **csv** module for reading in data from a file.
import csv

# Read data from file.
# The first attribute will be shown on the x dimension, the second on the y dimension.
# We know that the first attribute is the file size. The meaning of the second attribute is
# not important for this exercise.
x = []
y = []
with open("../data/task4_data.txt", 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
    for row in csvreader:
        if len(row) == 2:  # if we have 2 fields in that line
            x.append(row[0])
            y.append(row[1])

# Plot original data.
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.scatter(x, y)
plt.show()

# Discretize data.
# TODO
