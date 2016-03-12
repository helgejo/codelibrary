Practicum 4
===========

Learning objectives:

  - Introduction to scikit-learn
  - Using and comparing various classification algorithms in scikit-learn
  - Computing classification metrics (accuracy, error rate, F1-measure)
  

## Task 0. Scikit-learn introduction

  - Different machine learning tasks
  - Loading example datasets
  

## Task 1. Running a decision tree classifier on the Iris dataset
 
  - Divide the Iris dataset to 2/3 training and 1/3 test sets
  - Train a decision tree classifier and apply it on the test data
  - See [this document](http://scikit-learn.org/stable/modules/tree.html#tree-classification) for help
  - Evaluate the predictions: compute accuracy and error rate

[Solution on DataJoy](https://www.getdatajoy.com/examples/55fc6a7afe8ed5175c3f9df6)  

See also the data folder for the generated decision tree in pdf format.

  
## Task 2. Comparing different classifiers on the Iris dataset

  - Using the previous 2/3-1/3 splits, train different classifiers and compare their performance by filling in the following table:

| Method            | Accuracy | Error rate |
| ----------------- | -------- | ---------- |
| Decision tree     |          |            |
| Nearest Neighbors |          |            |
| Naive Bayes       |          |            |
| SVM               |          |            |
| Random Forest     |          |            |

  - Documentation for the classifiers can be found here:
    * [Decision trees](http://scikit-learn.org/stable/modules/tree.html)
    * [Nearest Neighbors](http://scikit-learn.org/stable/modules/neighbors.html)
    * [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)
    * [SVM](http://scikit-learn.org/stable/modules/svm.html)
    * [Random Forest](http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)
  
[Solution on DataJoy](https://www.getdatajoy.com/examples/55fc6cc2fe8ed5175c3f9df8)  


## Task 3. Performing classification on the Cylinder Bands dataset

  - Download the Cylinder Bands dataset from the mldata.org repository
    * See [this document](http://scikit-learn.org/stable/datasets/index.html#downloading-datasets-from-the-mldata-org-repository) for help
    * [Cylinder Bands dataset on mldata.org](http://mldata.org/repository/data/viewslug/uci-20070111-cylinder-bands/)
    * [Dataset description](https://archive.ics.uci.edu/ml/datasets/Cylinder+Bands)
  - The dataset requires preprocessing
    * Nominal attributes need to be binarized
    * Missing values need to be handled for numerical attributes (e.g., replaced by the mean value for that attribute)
  - Train a classifier (any classifier) and evaluate its performance using cross-validation
    * See [this document](http://scikit-learn.org/stable/modules/cross_validation.html) for help

[Solution on DataJoy](https://www.getdatajoy.com/examples/55fc85c0fe8ed5175c3f9dfa)  
  

## Task 4. Comparing two classifiers on the Cylinder Bands dataset

  - Divide the Cylinder Bands dataset into 80% training and 20% test sets randomly
  - Compare the performance of two classifiers in terms of F1-measure (by increasing the amount of training data incrementally)
  - Plot performance as a function of training data available
    * Use 20%, 40%, ..., 100% of your training data for training
    * For each, evaluate the performance of both models in terms of the F1-measure
    * Make a plot with training data size on the X-axis and F1-score on the Y-axis

[Solution on DataJoy](https://www.getdatajoy.com/examples/55fc8f65896c84651dfcffa9)  

  
## References

  - Scikit-learn
    * [Tutorial](http://scikit-learn.org/stable/tutorial/index.html)
    * [Supervised learning](http://scikit-learn.org/stable/supervised_learning.html)
    * [Class and function reference](http://scikit-learn.org/stable/modules/classes.html)
    * [Dataset loading utilities](http://scikit-learn.org/stable/datasets/index.html)
  - [Scikit-learn tutorial video](https://vimeo.com/53062607) and [online material](http://www.astroml.org/sklearn_tutorial/)
  