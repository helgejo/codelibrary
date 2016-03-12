# Comparing two classifiers on the Cylinder Bands dataset
# =======================================================

# Task
# ----
#   - Divide the Cylinder Bands dataset into 80% training and 20% test sets randomly
#   - Compare the performance of two classifiers in terms of F1-measure (by increasing the amount of training data incrementally)
#   - Plot performance as a function of training data available
#     * Use 20%, 40%, ..., 100% of your training data for training
#     * For each, evaluate the performance of both models in terms of the F1-measure
#     * Make a plot with training data size on the X-axis and F1-score on the Y-axis

# Solution
# --------

from __future__ import division

import math
import csv
import numpy as np

# Scikit-learn packages needed
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import Imputer
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split

# For plotting
import matplotlib.pyplot as plt


# ## Computing F1-score
def f1(predictions, true_labels):
    # TODO
    return 0  # F1-measure


# ## Data loading an preprocessing
# This is copy-pasted from Task 3 and the comments are removed. Check Task 3 for an explanation.
filename = "../data/uci-20070111-cylinder-bands.csv"
data_x_nominal = []
data_x_numeric = []
data_y = []
ids_nominal = range(20)
ids_numerical = range(20, 39)

with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            data_x_nominal.append({i: row[i] for i in ids_nominal})
            data_x_numeric.append([float(row[i]) for i in ids_numerical])
            data_y.append(1 if row[-1] == "band" else 0)

vec = DictVectorizer()
data_x_nominal = vec.fit_transform(data_x_nominal).toarray()  # mind that this is a numpy array

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data_x_numeric)
data_x_numeric = imp.transform(data_x_numeric)  # mind that this is a numpy array

data_x = np.concatenate((data_x_nominal, data_x_numeric), axis=1)

# TODO Split data to 80% train and 20% test
# You can use the train_test_split method of the cross-validation package, see:
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.train_test_split.html


# TODO Train and test models


# TODO Plot results

