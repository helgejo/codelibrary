# Performing classification on the Cylinder Bands dataset
# =======================================================

# Task
# ----
#   - Download the Cylinder Bands dataset from the mldata.org repository
#     * See [this document](http://scikit-learn.org/stable/datasets/index.html#downloading-datasets-from-the-mldata-org-repository) for help
#     * [Cylinder Bands dataset on mldata.org](http://mldata.org/repository/data/viewslug/uci-20070111-cylinder-bands/)
#     * [Dataset description](https://archive.ics.uci.edu/ml/datasets/Cylinder+Bands)
#   - The dataset requires preprocessing
#     * Nominal attributes need to be binarized
#     * Missing values need to be handled for numerical attributes (e.g., replaced by the mean value for that attribute)
#   - Train a classifier (any classifier) and evaluate its performance using cross-validation
#     * See [this document](http://scikit-learn.org/stable/modules/cross_validation.html) for help

# Solution
# --------

from __future__ import division

import csv

# Scikit-learn packages needed
from sklearn.datasets import fetch_mldata  # to download the dataset directly from the mldata.org repository
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import Imputer
from sklearn.feature_extraction import DictVectorizer
from sklearn import cross_validation


# Numpy needed for data preprocessing
import numpy as np


# ## Load data
# We load data from the CSV file directly.
filename = "../data/uci-20070111-cylinder-bands.csv"

# Alternatively, using the mldata loader should also be an option:
# cylinder_data = fetch_mldata('uci-20070111-cylinder-bands')
# See http://scikit-learn.org/stable/datasets/index.html#downloading-datasets-from-the-mldata-org-repository for further info

# We store nominal and numerical attributes separately, as we will need to preprocess them differently.
data_x_nominal = []  # nominal attributes are list of feature-value pairs
data_x_numeric = []  # numerical attributes are a list of lists
data_y = []  # target class label are a list of 0/1 values

# These two array contains the indexes of nominal and numerical attributes.
# Attributes 1-20 are nominal, attributes 21-39 are numeric.
# See the list of attributes here: https://archive.ics.uci.edu/ml/datasets/Cylinder+Bands
# (Note that we index from 0 here, so all indices are "one off" compared to the list on the above URL.)
ids_nominal = range(20)
ids_numerical = range(20, 39)

with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            data_x_nominal.append({i: row[i] for i in ids_nominal})  # extract nominal attributes (key-value pairs; we use the attribute id as the key)
            data_x_numeric.append([float(row[i]) for i in ids_numerical])  # extract numerical attributes (list of values)
            data_y.append(1 if row[-1] == "band" else 0)  # last element is the class label; we make it binary


# ## Data preprocessing
# Scikit-learn requires that all attributes are numeric and that there are no missing values.
# Unlike the Iris dataset, the Cylinder Bands dataset is not like that, we need to do some preprocessing.

# ### Nominal attributes
# Categorical values need to be translated to numbers.
# We binarize categorical values as follows: each categorical feature with m possible values is turned into m binary
# features, with only one active.
# We use the DictVectorizer class to achieve exactly this; it transforms lists of feature-value mappings to vectors.
# See 4.2.1 here: http://scikit-learn.org/stable/modules/feature_extraction.html
vec = DictVectorizer()
data_x_nominal = vec.fit_transform(data_x_nominal).toarray()  # mind that this is a numpy array

# ### Numeric attributes
# We use the Imputer class for substituting missing attribute values with the mean.
# See 4.3.5. here: http://scikit-learn.org/stable/modules/preprocessing.html

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data_x_numeric)
data_x_numeric = imp.transform(data_x_numeric)  # mind that this is a numpy array

# Create train vector by concatenating vectorized nominal and numeric attributes.
# Note that both data_x_nominal and data_x_numeric are numpy arrays, so we need to use numpy to concatenate them.
# The resulting (numpy) array can directly be used for model building.
train_x = np.concatenate((data_x_nominal, data_x_numeric), axis=1)


# ## Model
# We use a decision tree classifier
clf = DecisionTreeClassifier()

# ## Evaluate the model using cross-validation
# See http://scikit-learn.org/stable/modules/cross_validation.html
scores = cross_validation.cross_val_score(clf, train_x, data_y, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
