# Computing statistics on the Adult dataset
# =========================================

# Task
# ----
#  - Compute frequency and mode for a selected categorical attribute.
#  - Compute mean, median, and variance for a selected continuous attribute, for each of the two classes (>50K, <=50K).

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# There are standard imports by now.
import csv
import numpy as np


# The data set is stored in a comma-separated text file.
# The delimiter is actually ", ", therefore we'll need to strip the spaces from the values.
# We read it and store it as a list of records, where each record is represented using a dict.
def load_adult_data(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 15:  # if we have 4 fields in that line
                records.append({
                    "age": row[0].strip(),
                    "workclass": row[1].strip(),
                    "fnlwgt": row[2].strip(),
                    "education": row[3].strip(),
                    "education-num": row[4].strip(),
                    "marital-status": row[5].strip(),
                    "occupation": row[6].strip(),
                    "relationship": row[7].strip(),
                    "race": row[8].strip(),
                    "sex": row[9].strip(),
                    "capital-gain": row[10].strip(),
                    "capital-loss": row[11].strip(),
                    "hours-per-week": int(row[12].strip()),
                    "native-country": row[13].strip(),
                    "class": row[14].strip()
                })
    return records


adult_data = load_adult_data("../data/adult.data")

# Compute the frequency for the categorical attribute `workclass`
workclass = [x['workclass'] for x in adult_data]

# We make a dictionary out of it, with category label as key and frequency as value
freq = {}
for wc in workclass:
    if wc in freq:
        freq[wc] += 1
    else:
        freq[wc] = 1

# We need to normalize the frequencies (i.e., divide by the number of elements)
for wc in freq:
    freq[wc] /= len(workclass)

# Print frequencies
print(freq)

# The mode is the label of the most frequent category
sorted_freq = sorted(freq, key=freq.get, reverse=True)
# Answer: Private
print(sorted_freq[0])


# Compute mean, median, and variance for the continuous attribute `hours-per-week`, for the two classes (>50K, <=50K).
over50_hpw = [x['hours-per-week'] for x in adult_data if x['class'] == ">50K"]
under50_hpw = [x['hours-per-week'] for x in adult_data if x['class'] == "<=50K"]

# Mean >50K: 45.47
print(np.mean(over50_hpw))
# Mean <=50K: 38.84
print(np.mean(under50_hpw))

# Median >50K: 40
print(np.median(over50_hpw))
# Median <=50K: 40
print(np.median(under50_hpw))

# Variance >50K: 121.27
print(np.var(over50_hpw))
# Variance <=50K: 151.75
print(np.var(under50_hpw))
