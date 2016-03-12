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

# Load data into a numpy array
arr = np.array([
    [x['sepal_length'] for x in iris_data],
    [x['sepal_width'] for x in iris_data],
    [x['petal_length'] for x in iris_data],
    [x['petal_width'] for x in iris_data],
], float)

# class colors
cc = ["red"] * 50 + ["blue"] * 50 + ["green"] * 50

# Scatter plot: sepal length vs. width
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.scatter(arr[0], arr[1], c=cc)
plt.title("Sepal length vs. width")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()

# Scatter plot: petal length vs. width
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.scatter(arr[2], arr[3], c=cc)
plt.title("Petal length vs. width")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.show()

# Box plot for comparing the four attributes
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
# You can also supply the data as [arr[0],arr[1],arr[2],arr[3]] --  we use the tolist() method ]
# of numpy arrays here to achieve this.
plt.boxplot(arr.tolist())
plt.title("Attribute comparison")
plt.xticks([1, 2, 3, 4], ["sepal length", "sepal width", "petal length", "petal width"])
plt.show()

# Box plot for comparing one attribute (sepal length) across the three classes
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.boxplot([arr[0,0:50], arr[0,50:100], arr[0,100:150]])
plt.title("Sepal length")
plt.xticks([1, 2, 3], ["Setosa", "Versicolor", "Virginica"])
plt.show()
