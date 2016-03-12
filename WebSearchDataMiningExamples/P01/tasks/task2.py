# Computing the similarity of binary vectors
# ==========================================

# Task
# ----
#  - Create a binary representation of the records that have nominal and ordinal attributes.
#  - Implement the functions that compute the Simple Matching Coefficient and Jaccard Coefficient
#    for a given pair of records.
#  - Find the most similar pair of records according to each similarity measure.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We will use the **csv** module for reading in data from a file.
import csv


# ### Input data

# **Gender** is a nominal attribute and has the following possible values:
gender = ["female", "male"]

# **Age** is a nominal attribute and has the following possible values:
age = ["0-5", "6-17", "18-34", "35-49", "50-64", "65+"]

# **Income** is a nominal attribute and has the following possible values:
income = ["low", "medium", "high"]

# The data set is stored in a tab-separated text file (`task2_data.txt`).
# We read it and store it as a list of records, where each record is represented using a dict.
# The first column in the file is an **id** field, which is a unique identifier.  It is a nominal
# attribute, but it should not be considered when computing the similarities between records.
# The first line of the file is a header with the field names, it should be ignored.
def load_data(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        csvreader.next()  # skip the header line
        for row in csvreader:
            if len(row) == 4:  # if we have 4 fields in that line
                records.append({
                    "id": row[0],
                    "gender": row[1],
                    "age": row[2],
                    "income": row[3]
                })
    return records


# ### Binarization

# This function takes a record as input and returns a binarized record.
# The binarized record is represented as a vector (python list).
def binarize(record):
    # TODO
    record_bin = []
    return record_bin


# ### Computing similarity
# Let $x$ and $y$ be two objects (records) that consist of binary attributes.
# We define the following 4 quantities
#  - $f_{01}$ = the number of attributes where $x$ was 0 and $y$ was 1
#  - $f_{10}$ = the number of attributes where $x$ was 1 and $y$ was 0
#  - $f_{00}$ = the number of attributes where $x$ was 0 and $y$ was 0
#  - $f_{11}$ = the number of attributes where $x$ was 1 and $y$ was 1

# #### Simple Matching Coefficient
# Compute $SMC = \frac{f_{11}+f_{00}}{f_{01}+f_{10}+f_{11}+f_{00}}$
# TODO
def sim_smc(x, y):
    return 0

# #### Jaccard Coefficient
# Compute $J = \frac{f_{11}}{f_{01}+f_{10}+f_{11}}$
# TODO
def sim_jaccard(x, y):
    return 0


# ### Main

# Read input data into `records`.
records = load_data("task2_data.txt")

# Binarize all records.
records_bin = []
for record in records:
    records_bin.append(binarize(record))

# Find the two most similar records using SMC and Jaccard.
# TODO
