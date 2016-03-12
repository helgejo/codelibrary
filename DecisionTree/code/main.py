from __future__ import division
import csv
from id3 import *
from eval import *
import numpy as np

__author__ = 'Helge Bjorland'

def load_adult_data(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 15:  # if we have all fields in that line
                records.append({
                    "age": int(row[0].strip()),
                    "workclass": row[1].strip(),
                    "fnlwgt": int(row[2].strip()),
                    "education": row[3].strip(),
                    "education-num": int(row[4].strip()),
                    "marital-status": row[5].strip(),
                    "occupation": row[6].strip(),
                    "relationship": row[7].strip(),
                    "race": row[8].strip(),
                    "sex": row[9].strip(),
                    "capital-gain": int(row[10].strip()),
                    "capital-loss": int(row[11].strip()),
                    "hours-per-week": int(row[12].strip()),
                    "native-country": row[13].strip(),
                    "class": row[14].strip()
                })
            elif len(row) == 14:  # if we have all fields in that line
                records.append({
                    "age": int(row[0].strip()),
                    "workclass": row[1].strip(),
                    "fnlwgt": int(row[2].strip()),
                    "education": row[3].strip(),
                    "education-num": int(row[4].strip()),
                    "marital-status": row[5].strip(),
                    "occupation": row[6].strip(),
                    "relationship": row[7].strip(),
                    "race": row[8].strip(),
                    "sex": row[9].strip(),
                    "capital-gain": int(row[10].strip()),
                    "capital-loss": int(row[11].strip()),
                    "hours-per-week": int(row[12].strip()),
                    "native-country": row[13].strip(),
                })
    return records

def removeCont(adult):
    for row in adult:
        del row["age"]
        del row["fnlwgt"]
        del row["education-num"]
        del row["capital-gain"]
        del row["capital-loss"]
        del row["hours-per-week"]

def preProcess(adult):
    for row in adult:
        del row["native-country"]
        del row["fnlwgt"]
        del row["education-num"]
        del row["marital-status"]

def descritize(adult):

    #handle age (max:90, min: 17)
    ageBin = np.linspace(15.0, 91.0, num=11)

    # handle capital-gain (Max: 99999, min 0 )
    CapGBin = np.linspace(0.0, 100000.0, num=1500)

    #handle capital-loss (4356, 0)
    CapLBin = np.linspace(0.0, 4400.0, num=500)

    #handle hours-per-week (99, 1)
    Hbin = np.linspace(0.0, 100.0, num=2)

    age = descr(adult, "age", ageBin)
    CapG = descr(adult, "capital-gain", CapGBin)
    CapL = descr(adult, "capital-loss", CapLBin)
    hpw = descr(adult, "hours-per-week", Hbin)

def descr(data, col, bins):
    dic = {}
    values = np.array([record[col] for record in data])
    inds = np.digitize(values, bins)
    for i in range(values.size):
        dic[values[i]] = str(bins[inds[i]])

    for row in data:
        row[col] = dic[row[col]]
    return dic

def splitData(data, mod):
    for i in range(len(data)):
        if mod == -1:
            train.append(data[i])
        elif i % mod == 0:  # test instance
            test.append(data[i])
        else:  # train instance
            train.append(data[i])

def create_decision_tree(data, attributes, target_attr, func):

    def unique(seq):
        # Method to find unique values in list
         seen = set()
         seen_add = seen.add
         return [ x for x in seq if not (x in seen or seen_add(x))]

    def count(vals):
        # Count instances of value in list
        hig_val = 0
        res = ""
        instances = unique(vals)
        for val in instances:
            z = 0
            for row in data:
                z += sum( x == val for x in row.values() )
            if z >= hig_val:
                res = val
                hig_val = z
        return res

    def get_values(data, attr):
        # Returns a list of unique values for attr in data
        data = data[:]
        return unique([record[attr] for record in data])

    def get_examples(data, attr, value):
        # Returns a list of all the rows in data
        # where the value of attr matches value.

        data = data[:]
        rtn_lst = []

        if not data:
            return rtn_lst
        else:
            for row in data:
                if row[attr] == value:
                    rtn_lst.append(row)
        return rtn_lst

    def choose_attribute(data, attributes, target_attr, func):
        #Find the attribute with the highest gain
        data = data[:]
        best_gain = 0.0
        best_attr = None

        for attr in attributes:

            gain = func(data, attr, target_attr)
            if (gain >= best_gain and attr != target_attr):
                best_gain = gain
                best_attr = attr

        return best_attr

    # copy the dataset
    data = data[:]
    # list of target values in dataset
    vals = [record[target_attr] for record in data]

    default = count(vals)

     # If training or attribute set is empty, return default;
    if not data or (len(attributes) - 1) <= 0:
            return default

    # If S consists of records all with the same value for
	#the categorical attribute, return default;
    elif vals.count(vals[0]) == len(vals):
        return vals[0]

        # Let D be the attribute with largest Gain(D,S)
	#    among attributes in set of attributes;
	# Let {dj| j=1,2, .., m} be the values of attribute D;
	# Let {Sj| j=1,2, .., m} be the subsets of S consisting
	#    respectively of records with value dj for attribute D;
	# Return a tree with root labeled D and arcs labeled
	#    d1, d2, .., dm going respectively to the trees
    #
	#      ID3(R-{D}, C, S1), ID3(R-{D}, C, S2), .., ID3(R-{D}, C, Sm);
    else:
        # Choose the best attribute to best classify our data
        best = choose_attribute(data, attributes, target_attr, func)

        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object
        tree = {best:{}}

        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in get_values(data, best):
            # Create a subtree for the current value under the "best" field
            subtree = create_decision_tree(get_examples(data, best, val),
            [attr for attr in attributes if attr != best], target_attr, func)

            # Add the new subtree to the empty dictionary object
            tree[best][val] = subtree

    return tree

def get_classification(row, tree):
    """
    This function recursively traverses the decision tree and returns a
    classification for the given record.
    """
    # If the current node is a string, then we've reached a leaf node and
    # we can return it as our answer
    if type(tree) == type("string"):
        return tree

    # Traverse the tree further until a leaf node is found.
    else:
        try:
            attr = tree.keys()[0]
            t = tree[attr][row[attr]]
        except KeyError:
            return "<=50K"
        return get_classification(row, t)

def classify(tree, data):
    """
    Returns a list of classifications for each of the records in the data
    list as determined by the given decision tree.
    """
    data = data[:]
    classification = []

    for row in data:
        classification.append(get_classification(row, tree))

    return classification

def classifyTest(tree, test):
    # Classify the records and evaluate
    classification = classify(tree, test)
    file = open("eval_pred", 'w')
    for i in classification:
        file.write(i + "\n")
    file.close()

    file2 = open("fasit", 'w')
    for row in test:
        x = row["class"]
        file2.write(x + "\n")
    file2.close()

    eval("fasit", "eval_pred")

def classifyOUT(tree):
    # Classify the records and evaluate
    adult_test = load_adult_data("../data/adult.test")
    preProcess(adult_test)
    descritize(adult_test)

    classification = classify(tree, adult_test)
    file = open("../output/task1.out", 'w')
    file.write("Id" + "," + "Target"+ "\n")
    z = 1
    for i in classification:
        file.write(str(z) + "," + i + "\n")
        z += 1
    file.close()

def main(type):
    adult_data = load_adult_data("../data/adult.data")
    preProcess(adult_data)
    descritize(adult_data)

    if type == 0:
        splitData(adult_data, 3)
    else:
        splitData(adult_data, -1) #Use to train on entire dataset

    attributes = train[0].keys()
    tree = create_decision_tree(train, attributes, "class", gain)

    if type == 0:
        classifyTest(tree, test)
    else:
        classifyOUT(tree)

train = []  # list to be filled with training data
test = []  # list to be filled with test data
main(-1) #0 to run test/train set and -1 to train on entire dataset and writh to task1 file