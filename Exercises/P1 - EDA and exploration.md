
# The project step 1 - Data science, data exploration

## Titanic

The 'toy'-dataset is Titanic. It's the hello world of machine learning, so you'll find more examples of analyzing this data than you can process. You need to present a project on this dataset where you do an analysis on the titanic dataset, but explain everything you see.

The first step in machine learning is data science. This week you'll be doing data science and analyzing the titanic data. The following exercise is more of a guideline than an actual list you need to follow. Make good visualisations that you can explain and that actually teach us something new.

Download the Titanic dataset from [Kaggle](https://www.kaggle.com/datasets/vinicius150987/titanic3).

First import the data and clean it up:

* Rename columns to remove space from the name and make them all lowercase.
* Look for the Na-values. Fix them if possible, using a couple of techniques before deciding which is best.
* Look for the Outliers. Fix them if needed, using a couple of techniques before deciding which is best.
* Look for (ordered) categoricals and label them as such.

Next do an exploratory data analysis:

* Show the outliers and try to explain them.
* Draw some graphs about features you find interesting.
* Look for correlations in your data.

Both phases (cleaning and exploring) aren't two different steps in a process, but rather one large fuzzy mess of code. Something like:

* I'll give all the Na's the mean value.
* My graphs look strange, what is this peak doing at the mean?
* Is there a correlation between the value that has a lot of Na's and another column?
* Let's use the other column to fill in the Na's!

In the second step of this project you'll put all the really good code together to make one final import, but for now poke the data an see what happens.


## Crop dataset.

The 'difficult' dataset is a dataset about crops. You can find it in the zip-file called 'food-twentieth-century-crop-statistics-1900-2017-xlsx'. Besides the actual data it also contains a pdf-file describing what all the fields stand for.

Take this week to start exploring this dataset. Remember the steps:

- Import and clean your data (dates, categoricals, ...)
- Draw a graph
- Try to see a pattern or an interesting outlier
- Draw another graph to confirm this suspicion
- Try to see a pattern or an interesting outlier
- Draw another graph to confirm this suspicion
- Try to see a pattern or an interesting outlier
- Draw another graph to confirm this suspicion
- ...

The final project will be partly graded on building a model based on this data, but also on the exploration of the data. Doing this step thorough will also greatly increase the quality of your model.