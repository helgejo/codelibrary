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

# Generate a vector with random values.
values = generate_values(1000)

# Create a histogram from the original values.
plt.clf()  # this is needed to clear the current figure (prevents multiple labels)
plt.hist(values, bins=11, normed=1, facecolor='green')
plt.show()

# Perform normalization.
# TODO
