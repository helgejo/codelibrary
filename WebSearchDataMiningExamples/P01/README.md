Practicum 1
===========

Learning objectives:

  - Familiarize with the programming environment (Python and DataJoy)
  - Variable transformation (normalization, binarization, discretization)
  - Proximity calculations
  - Simple plotting


See the document on itslearning about the programming environment, etc.
You will need to register on getdatajoy.com to access the solutions documents 
with explanations and output, generated automatically from the source files.
  

## Task 1. Variable transformation: normalization by scaling between 0 and 1
 
  - Generate a random value that is the sum of rolling two six-sided dice.
  - Create a vector with n random values.
  - Plot the distribution of the values on a histogram.
  - Normalize the values between 0 and 1 using Min-Max normalization.
  - Plot the distribution of the normalized values on a histogram.

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e04451896c84651dfcfe41)


## Task 2. Computing the similarity of binary vectors

  - Create a binary representation of the records that have nominal and ordinal attributes.
  - Implement the functions that compute the Simple Matching Coefficient and Jaccard Coefficient for a given pair of records.
  - Find the most similar pair of records according to each similarity measure.

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e04682896c84651dfcfe45)


## Task 3. Computing similarity between documents

  - Compute the similarity between two documents.
  - Represent each document as a vector of binary attributes: if a given word is present in the document or not.
  - You can then use the Jaccard coefficient.

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e048aa896c84651dfcfe4c)


## Task 4. Discretization

  - Create an ordinal attribute "file size" with the following 5 possible values {tiny, small, medium, large, huge}.
  - Implement both the equal width and equal frequency methods.
  - Display the data on a plot. 

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e0498f896c84651dfcfe4e)
  

## Task 5. Finding k-nearest neighbors using Eucledian distance

  - Generate n=100 random points in a two dimensional space. Let both the x and y attributes be int values between 1 and 100.
  - Display these points on a scatterplot.
  - Select one of these points randomly (i.e., pick a random index).
  - Find the k closest neighbors of the selected record (i.e., the k records that are most similar to it) using the Eucledian distance. The value of k is given (i.e., hard-coded).
  - Display the selected record and its k closest neighbors in a distinctive manner on the plot (e.g., using different colors).
  
[Solution on DataJoy](https://www.getdatajoy.com/examples/55e04be4896c84651dfcfe59)


## References

  - [Matplotlib plotting framework](http://matplotlib.org/api/pyplot_api.html)
    