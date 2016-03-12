# Variable transformation: normalization by scaling between 0 and 1
# =================================================================

# Task
# ----
#  - Generate a random value that is the sum of rolling two six-sided dice.
#  - Create a vector with n random values.
#  - Plot the distribution of the values on a histogram.
#  - Normalize the values between 0 and 1 using Min-Max normalization.
#  - Plot the distribution of the normalized values on a histogram.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We import the matplotlib submodule **pyplot**, to plot 2d graphics;
# following a widely used convention, we use the `plt` alias.
# We also need the **random** module for generating random numbers.
import matplotlib.pyplot as plt
import random

# The following function generates a vector (list) of size `n` values that are
# the result of the sum of rolling two six-sided dice.
def generate_values(n):
    values = []
    for i in range(n):
        x = random.randint(1, 6) + random.randint(1, 6)
        values.append(x)
    return values

# This function performs the Min-Max normalization.
# For each value x, the normalized value is calculated using $x' = \frac{x-min_x}{max_x-min_x}$.
def norm_minmax(values):
    min_x = min(values)
    max_x = max(values)

    values_norm = []
    for x in values:
        x_norm = (x-min_x) / (max_x-min_x)
        values_norm.append(x_norm)
    return values_norm

# Generate a vector with random values.
values = generate_values(1000)

# Create a histogram from the original values.
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.hist(values, bins=11, normed=1, facecolor='green')
plt.show()

# Perform normalization.
values2 = norm_minmax(values)

# Create a histogram from the normalized values.
plt.clf()
plt.hist(values2, bins=11, normed=1, facecolor='blue')
plt.show()
