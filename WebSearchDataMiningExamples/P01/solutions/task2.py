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
    record_bin = []
    # Gender: either 0 or 1.
    if record['gender'] == "female":
        record_bin.append(0)
    else:
        record_bin.append(1)
        
    # Age: 6 bits.
    age_vect = [0, 0, 0, 0, 0, 0]
    for idx, val in enumerate(age):
        if record['age'] == val:
            age_vect[idx] = 1
    record_bin = record_bin + age_vect
    
    # Income: 3 bits.
    income_vect = [0, 0, 0]
    for idx, val in enumerate(income):
        if record['income'] == val:
            income_vect[idx] = 1
    record_bin = record_bin + income_vect
    
    return record_bin


# ### Computing similarity
# Let $x$ and $y$ be two objects (records) that consist of binary attributes.
# We define the following 4 quantities
#  - $f_{01}$ = the number of attributes where $x$ was 0 and $y$ was 1
#  - $f_{10}$ = the number of attributes where $x$ was 1 and $y$ was 0
#  - $f_{00}$ = the number of attributes where $x$ was 0 and $y$ was 0
#  - $f_{11}$ = the number of attributes where $x$ was 1 and $y$ was 1

# #### Simple Matching Coefficient
# Compute (f_11 + f_00) / (f_01 + f_10 + f_11 + f_00).
# In simple terms, it is the number of matching attributes divided by the number of all attributes.
def sim_smc(x, y):
    matches = 0
    for idx, val in enumerate(x):
        if x[idx] == y[idx]:
            matches += 1
    return matches / len(x)

# #### Jaccard Coefficient
# Compute (f_11) / (f_01 + f_10 + f_11).
# In simple terms, it is the number of matching attributes divided by the number of all attributes,
# **excluding** cases where both attributes are 0.
def sim_jaccard(x, y):
    matches = 0
    nonzeros = 0
    for idx, val in enumerate(x):
        if x[idx] + y[idx] > 0:
            nonzeros += 1
            if x[idx] == y[idx]:
                matches += 1
    return matches / nonzeros


# ### Main

# Read input data into `records`.
records = load_data("data/task2_data.txt")

# Print records.
print(records)

# Binarize all records.
records_bin = []
for record in records:
    records_bin.append(binarize(record))

# Print the binarized version of records.
print(records_bin)

# Find the two most similar records using SMC and Jaccard.
max_smc = 0
max_smc_names = ""
max_jacc = 0
max_jacc_names = ""

for i1 in range(len(records)):
    for i2 in range(i1+1, len(records)):
        s_smc = sim_smc(records_bin[i1], records_bin[i2])
        s_jacc = sim_jaccard(records_bin[i1], records_bin[i2])
        # print records[i1]['id'], records[i2]['id'], s_smc, s_jacc
        if s_smc > max_smc:
            max_smc = s_smc
            max_smc_names = records[i1]['id'] + " - " + records[i2]['id']
        if s_jacc > max_jacc:
            max_jacc = s_jacc
            max_jacc_names = records[i1]['id'] + " - " + records[i2]['id']

print "Most similar pair using SMC: "
print "\t", max_smc_names
print "\tsimilarity: ", max_smc
print "Most similar pair using Jaccard: "
print "\t", max_jacc_names
print "\tsimilarity: ", max_jacc
