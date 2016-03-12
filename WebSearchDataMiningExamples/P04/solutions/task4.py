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
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(len(predictions)):
        if true_labels[i] == 1:  # actual class is positive
            if predictions[i] == 1:  # predicted class is positive
                tp += 1  # true positive
            else:
                fn += 1  # false negative
        else:  # actual class is negative
            if predictions[i] == 1:  # predicted class is positive
                fp += 1  # false positive
            else:
                tn += 1  # true negative

    p = tp / (tp + fp)  # precision
    r = tp / (tp + fn)  # recall

    return 2 * p * r / (r + p)  # F1-measure


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

# ## Split data to 80% train and 20% test
# We can use the train_test_split method of the cross-validation package, see:
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.train_test_split.html
train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.2)


# ## Train and test models

# The first model is SVM with rbf kernel
clf1 = SVC(kernel='rbf')

# The second model is a Random Forest classifier
trees = 20  # number of trees in the forest
max_features = 10  # maximum number of features in each tree
clf2 = RandomForestClassifier(n_estimators=trees, max_features=max_features)

# We incrementally increase the amount of training data, make predictions, and evaluate the model
f1_1 = []  # F1 scores of the first classifier
f1_2 = []  # F2 scores of the first classifier

for i in range(20, 120, 20):  # we use 20, 40, ... 100% of the training instances for training
    idx = int(math.floor(len(train_x) * i / 100))  # index of the last training instance used for training
    # Train and test using the first model
    clf1.fit(train_x[:idx], train_y[:idx])
    predictions = clf1.predict(test_x)
    f1_1.append(f1(predictions, test_y))
    # Train and test using the second model
    clf2.fit(train_x[:idx], train_y[:idx])
    predictions = clf2.predict(test_x)
    f1_2.append(f1(predictions, test_y))

# ## Plot results
plt.clf()

x = range(20, 120, 20)  # x values for the plot
plt.plot(x, f1_1, 'darkgreen', linewidth=3, label='SVM')
plt.plot(x, f1_2, 'darkmagenta', linewidth=3, label='Random Forest')

plt.title('Comparison of classifiers')
plt.xlabel('Fraction of training data used')
plt.ylabel('F1-measure')
legend = plt.legend(loc='lower right', fontsize='small')

plt.show()
