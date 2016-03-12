Practicum 2
===========

Learning objectives:

  - Loading small data sets
  - Computing summary statistics (mean, median, range, variance, etc.)
  - Visualization (histograms, scatter plots, box plots)
  - Setting up local environment
  

## Task 1. Computing summary statistics on the Iris dataset
 
  - Load the Iris dataset (`data/iris.data`)
  - Answer the following questions:
    * What is the mean `sepal length` for Iris Setosa?
    * What is the median `petal length` for Iris Virginica?
    * What is the range of `sepal width` for Iris Versicolour?
    * Which class (Setosa/Versicolour/Virginica) shows the highest variance in `petal width`?
    * What is the 70% percentile for `sepal length` and `sepal width` (for all classes together)?
    * Compute Absolute Average Deviation (AAD), Median Absolute Deviation (MAD), and Interquartile Range (IQR) for `petal length` (for all classes together).
  
[Solution on DataJoy](https://www.getdatajoy.com/examples/55e9df6a896c84651dfcfeb6)  

  
## Task 2. Computing summary statistics using numpy

  - Load the Iris dataset into a 4x150 numpy array.
  - Answer the questions from Task 1 (except the last one) using numpy.
  - See reference at the bottom of the document.

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e9e231fe8ed5175c3f9d41)  


## Task 3. Visualizing Iris data

  - Create two scatter plots: sepal length vs. width and petal length vs. width. Use different color/symbols for the different classes (Setosa/Versicolour/Virginica).
  - Create box plots for comparing the four attributes (for all classes). I.e., 4 box plots, one for each attribute.
  - Create box plots for comparing one of the attributes (e.g., sepal length) across the three classes. I.e., 3 box plots, one for each class.

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e9e479fe8ed5175c3f9d45)  


## Task 4. Setting up local environment

  - Install python and an IDE on your local computer and run the code from Practicum 1 and earlier today.
  - The next two tasks should be done on your local machine.
  

## Task 5. Computing statistics on the Adult dataset

  - Compute frequency and mode for a selected categorical attribute.
  - Compute mean, median, and variance for a selected continuous attribute, for each of the two classes (>50K, <=50K).

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e9e70a896c84651dfcfec7)  


## Task 6. Visualizing Adult data

  - This is an open-ended task. Explore the dataset using various visualizations. Time to unleash your creativity :)
  - Some ideas:
    * Create histograms for the categorical attributes.
    * Discretize the `age` attribute and display it on a histogram. Experiment with different bin sizes.
    * Create scatter plots with various pairs of continuous attributes (e.g., capital-gain vs. capital-loss).
    * Try to add a 3rd or 4th attribute to the scatter plot by using different symbols/shapes, colors, sizes, etc.
    * The adventurous ones can even try [Star plots](http://matplotlib.org/examples/api/radar_chart.html) or [Chernoff faces](http://healthyalgorithms.com/2012/11/12/dataviz-in-python-chernoff-faces-with-matplotlib/)

[Solution on DataJoy](https://www.getdatajoy.com/examples/55e9e8befe8ed5175c3f9d4b)  


## References

  - [Numpy arrays](http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array)
  - [Numpy statistics](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)
  - [Matplotlib plotting framework](http://matplotlib.org/api/pyplot_api.html)
  - [Plotting examples on DataJoy](https://www.getdatajoy.com/examples/549f08816e8e238a185a9056)
  - [BoxPlot examples on DataJoy](https://www.getdatajoy.com/examples/54ea09826e8e238a185a9068)
  - [How to make beautiful data visualizations in Python with matplotlib](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
    