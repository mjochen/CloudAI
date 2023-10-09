
# The project step 1 - Data science, data exploration

## Titanic

The 'toy'-dataset is Titanic. It's the hello world of machine learning, so you'll find more examples of analyzing this data than you can process. You need to present a project on this dataset where you do an analysis on the titanic dataset, but explain everything you see.

The first step in machine learning is data science. This week you'll be doing data science and analyzing the titanic data. The following exercise is more of a guideline than an actual list you need to follow. Make good visualisations that you can explain and that actually teach us something new.

Download the Titanic dataset from [Kaggle](https://www.kaggle.com/datasets/vinicius150987/titanic3).

Open Sagemaker as a sandbox (at the bottom of your screen in the AWS-canvas-course) or run locally in a virtual environment.

Once you’ve loaded your data, go full data scientist on it:
1.	Perform data preprocessing, which includes handling missing values, converting categorical features to numerical, and feature scaling.
2.	Use feature selection techniques to select the most important features for the models. Try using correlation analysis or feature importance from models like the decision tree or random forest.
3.	Use cross-validation techniques such as k-fold cross-validation to evaluate the models' performance and avoid overfitting.
4.	Use ensemble methods like stacking or blending to combine the predictions from multiple models and improve the overall performance.
5.	Use hyperparameter optimization techniques such as Bayesian optimization or genetic algorithms to find the optimal hyperparameters for the models.
6.	Use techniques like data augmentation or synthetic minority oversampling technique (SMOTE) to handle class imbalance in the target variable.
7.	Use different evaluation metrics like ROC AUC or average precision score to evaluate the models' performance, especially when dealing with imbalanced datasets.
8.	Visualize the models' performance using metrics like confusion matrix, ROC curve, or precision-recall curve to better understand the models' strengths and weaknesses.
9.	Interpret the models' results using techniques like feature importance, partial dependence plots, or SHAP values to understand the factors that contribute to the models' predictions.

These exercises focus more on the data science aspects of supervised machine learning, including data preprocessing, feature selection, cross-validation, hyperparameter optimization, and model interpretation.

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