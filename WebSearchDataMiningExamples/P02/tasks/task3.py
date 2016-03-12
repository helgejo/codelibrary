# Visualizing Iris data
# =====================

# Task
# ----
#   - Create two scatter plots: sepal length vs. width and petal length vs. width.
#     Use different color/symbols for the different classes (Setosa/Versicolour/Virginica).
#   - Create box plots for comparing the four attributes (for all classes).
#     I.e., 4 box plots, one for each attribute.
#   - Create box plots for comparing one of the attributes (e.g., sepal length) across the
#     three classes. I.e., 3 box plots, one for each class.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We will use the **csv** module for reading in data from a file.
import csv

# It is common to import **numpy** under the briefer name **np**.
import numpy as np

# We import the matplotlib submodule **pyplot**, to plot 2d graphics;
# following a widely used convention, we use the `plt` alias.
import matplotlib.pyplot as plt


# The data set is stored in a comma-separated text file.
# We read it and store it as a list of records, where each record is represented using a dict.
def load_iris_data(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 5:  # if we have 4 fields in that line
                records.append({
                    "sepal_length": float(row[0]),
                    "sepal_width": float(row[1]),
                    "petal_length": float(row[2]),
                    "petal_width": float(row[3]),
                    "class": row[4]
                })
    return records

iris_data = load_iris_data("../data/iris.data")
