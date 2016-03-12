# Visualizing Adult data
# ======================

# Task
# ----
#   - This is an open-ended task. Explore the dataset using various visualizations. Time to unleash your creativity :)
#   - Some ideas:
#     * Create histograms for the categorical attributes.
#     * Discretize the `age` attribute and display it on a histogram. Experiment with different bin sizes.
#     * Create scatter plots with various pairs of continuous attributes (e.g., capital-gain vs. capital-loss).
#     * Try to add a 3rd or 4th attribute to the scatter plot by using different symbols/shapes, colors, sizes, etc.
#     * The adventurous ones can even try [Star plots](http://matplotlib.org/examples/api/radar_chart.html) or [Chernoff faces](http://healthyalgorithms.com/2012/11/12/dataviz-in-python-chernoff-faces-with-matplotlib/)

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# There are standard imports by now.
import csv
import numpy as np
import matplotlib.pyplot as plt

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
    return records


adult_data = load_adult_data("../data/adult.data")


# ## Visualizations
# These are just two simple examples. You should do some more.

# ### Box plot for comparing hours-per-week across various types of education
plotdata = []  # this is a list of lists holding the data for the boxplot

# Get different education types
edu_types = set(x['education'] for x in adult_data)

# Get the hours-per-week for each education type
for edu in sorted(edu_types):
    hpw = [x['hours-per-week'] for x in adult_data if x['education'] == edu]
    plotdata.append(hpw)

plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.boxplot(plotdata)
plt.title("Distribution of hours-per-week based for different types of education")
plt.xlabel("Education")
plt.ylabel("Hours per week")
plt.xticks(range(1, len(edu_types) + 1), sorted(edu_types), rotation='vertical')  # rotate the labels
plt.show()

# ### Age histrogram break down by gender
age_male = [x['age'] for x in adult_data if x['sex'] == "Male"]
age_female = [x['age'] for x in adult_data if x['sex'] == "Female"]
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.hist([age_male, age_female], normed=1, color=["blue", "red"], label=["Male", "Female"])
plt.legend()
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
