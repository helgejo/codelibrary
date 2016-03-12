# Running a decision tree classifier on the Iris dataset
# ======================================================

# Task
# ----
#   - Divide the Iris dataset to 2/3 training and 1/3 test sets
#   - Train a decision tree classifier and apply it on the test data
#   - Evaluate the predictions: compute accuracy and error rate

# Solution
# --------

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

# ### Evaluating predictions
# This function evaluates the predictions by comparing them to the true labels
def evaluate(predictions, true_labels):
    # TODO
    return 0

# import some data to play with
iris = datasets.load_iris()

# ### Split the data into training and test sets
# (we don't do a random split so that we have the same splits for all experiments)
train_x = []  # train attributes
train_y = []  # train class labels
test_x = []  # test attributes
test_y = []  # test class labels
# TODO

# ### Create a decision tree classifier object
clf = DecisionTreeClassifier()

# ### Train the classifier
# TODO

# ### Apply it to the test data
# TODO
predictions = []

# ### Evaluate the predictions
evaluate(predictions, test_y)
