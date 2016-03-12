# Computing summary statistics on the Iris dataset
# ================================================

# Task
# ----
#   - Load the Iris dataset (`data/iris.data`)
#   - Answer the following questions:
#     * What is the mean `sepal length` for Iris Setosa?
#     * What is the median `petal length` for Iris Virginica?
#     * What is the range of `sepal width` for Iris Versicolour?
#     * Which class (Setosa/Versicolour/Virginica) shows the highest variance in `petal width`?
#     * What is the 70% percentile for `sepal length` and `sepal width` (for all classes together)?
#     * Compute Absolute Average Deviation (AAD), Median Absolute Deviation (MAD), and Interquartile
#       Range (IQR) for `petal length` (for all classes together).

# Hint: you can exploit the fact that the input is ordered by class: the first 50 records are Iris Setosa,
# records 51-100 are Iris Versicolour, and records 101-150 are Iris Virginica.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We will use the **csv** module for reading in data from a file.
import csv

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

# Compute the mean
def mean(elements):
    s = 0  # holds sum
    for x in elements:
        s += x
    return s / len(elements)

# Compute the median
def median(elements):
    # sort elements (we make a copy so that the original order of elements is not affected)
    es = sorted(elements)
    if len(elements) % 2 == 0:
        mid = int(len(elements) / 2)
        return (es[mid-1] + es[mid]) /2
    else:
        mid = int((len(elements) - 1) / 2)
        return es[mid]

# Compute the range
def range(elements):
    return max(elements) - min(elements)

# Compute the variance
def variance(elements):
    s = 0  # holds sum
    m = mean(elements)
    for x in elements:
        s += (x-m) * (x-m)
    return (1 / len(elements)) * s

# Compute the pth percentile
def percentile(elements, p):
    # sort elements (we make a copy so that the original order of elements is not affected)
    es = sorted(elements)
    i = int(len(elements) * (p/100))
    return es[i]

# Compute the Absolute Average Deviation (AAD)
def aad(elements):
    s = 0  # holds sum
    m = mean(elements)
    for x in elements:
        s += abs(x-m)
    return (1 / len(elements)) * s

# Compute the Median Absolute Deviation (MAD)
def mad(elements):
    diffs = []
    m = mean(elements)
    for x in elements:
        diffs.append(abs(x-m))
    return median(diffs)

# Compute the Interquartile Range (IQR)
def iqr(elements):
    return percentile(elements, 75) - percentile(elements, 25)


iris_data = load_iris_data("../data/iris.data")

# Hints:
# Get a slice of the list, e.g., all Iris Versicolour records: iris_data[50:100]
# Get a given attribute as a list, e.g., sepal with: attr = [x['sepal_width'] for x in iris_data]

setosa = iris_data[0:50]
versicolour = iris_data[50:100]
virginica = iris_data[100:150]

# ## Answers to questions

# What is the mean `sepal length` for Iris Setosa?
attr_sl_is = [x['sepal_length'] for x in setosa]
# Answer: 5.006
print(mean(attr_sl_is))


# What is the median `petal length` for Iris Virginica?
attr_pl_iv = [x['petal_length'] for x in virginica]
# Answer: 5.55
print(median(attr_pl_iv))


# What is the range of `sepal width` for Iris Versicolour?
attr_sw_iv = [x['sepal_width'] for x in versicolour]
# Answer: 1.4
print(range(attr_sw_iv))


# Which class (Setosa/Versicolour/Virginica) shows the highest variance in `petal width`?
print(variance([x['petal_width'] for x in setosa]))  # Setosa
print(variance([x['petal_width'] for x in versicolour]))  # Versicolour
print(variance([x['petal_width'] for x in virginica]))  # Virginica
# Answer: Virginica (0.0739)


# What is the 70% percentile for `sepal length` and `sepal width` (for all classes together)?
# Answer: 6.3 for sepal length
print(percentile([x['sepal_length'] for x in iris_data], 70)) 
# Answer: 3.2 for sepal width
print(percentile([x['sepal_width'] for x in iris_data], 70)) 


# Compute Absolute Average Deviation (AAD), Median Absolute Deviation (MAD), and Interquartile
# Range (IQR) for `petal length` (for all classes together).
# Answer: AAD: 1.56192
print(aad([x['petal_length'] for x in iris_data])) 
# Answer: MAD: 1.7913
print(mad([x['petal_length'] for x in iris_data]))
# Answer: IQR: 3.5
print(iqr([x['petal_length'] for x in iris_data]))

