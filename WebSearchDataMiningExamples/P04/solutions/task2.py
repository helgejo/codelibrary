# Comparing different classifiers on the Iris dataset
# ===================================================

# Task
# ----
#   - Using the previous 2/3-1/3 splits, train different classifiers and compare their performance
#     by filling in the following table:
#
# | Method                  | Accuracy | Error rate |
# | ----------------------- | -------- | ---------- |
# | Decision tree           |     0.86 |       0.14 |
# | Nearest Neighbors (k=3) |     0.98 |       0.02 |
# | Naive Bayes (Gaussian)  |     1.00 |       0.00 |
# | SVM (linear kernel)     |     0.98 |       0.02 |
# | Random Forest           |     0.94 |       0.06 |
#
#   - Documentation for the classifiers can be found here:
#     * [Decision trees](http://scikit-learn.org/stable/modules/tree.html)
#     * [Nearest Neighbors](http://scikit-learn.org/stable/modules/neighbors.html)
#     * [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)
#     * [SVM](http://scikit-learn.org/stable/modules/svm.html)
#     * [Random Forest](http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)

# Solution
# --------

from __future__ import division

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


# ### Evaluating predictions
# This function evaluates the predictions by comparing them to the true labels
def evaluate(predictions, true_labels):
    correct = 0
    incorrect = 0
    for i in range(len(predictions)):
        if predictions[i] == true_labels[i]:
            correct += 1
        else:
            incorrect += 1

    print "Accuracy:   ", correct / len(predictions)
    print "Error rate: ", incorrect / len(predictions)

    return 0


# Import the Iris dataset
iris = datasets.load_iris()

# ### Split the data into training and test sets
# (we don't do a random split so that we have the same splits for all experiments)
train_x = []  # train attributes
train_y = []  # train class labels
test_x = []  # test attributes
test_y = []  # test class labels

for i in range(len(iris.data)):
    if i % 3 == 0:  # test instance
        test_x.append(iris.data[i])
        test_y.append(iris.target[i])
    else:  # train instance
        train_x.append(iris.data[i])
        train_y.append(iris.target[i])

# ### Decision tree
print "Decision tree"
clf = DecisionTreeClassifier()
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)
# Accuracy:    0.86
# Error rate:  0.14

# ### Nearest Neighbors
print "Nearest Neighbors"
k = 3
clf = KNeighborsClassifier(k)
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)
# Accuracy:    0.98
# Error rate:  0.02

# ### Naive Bayes
print "Naive Bayes"
clf = GaussianNB()
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)
# Accuracy:    1.0
# Error rate:  0.0

# ### SVM
print "SVM"
clf = SVC(kernel='linear')
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)
# Accuracy:    0.98
# Error rate:  0.02

# ### Random Forest
print "Random Forest"
trees = 10  # number of trees in the forest
max_features = 2  # maximum number of features in each tree
clf = RandomForestClassifier(n_estimators=trees, max_features=max_features)
clf.fit(train_x, train_y)
predictions = clf.predict(test_x)
evaluate(predictions, test_y)
# Accuracy:    0.94
# Error rate:  0.06
