# Discussion topics week 2

## Model Quality


1. What is the difference between classification and regression models?
1. Can you give examples of real-world problems that would use classification vs regression?
1. What kind of questions or predictions are best suited for regression models?
1. What are the main types of machine learning? How do they differ?
1. Why do we split the dataset into training and test sets? How does this help in evaluating the model's performance?
1. Why do we split data into training, validation, and test sets?
1. What could go wrong if you don’t properly randomize your data before splitting?
1. What is the role of the validation set when tuning model parameters?
1. How can the sensitivity to the train/test split affect model performance? What strategies can you use to mitigate this sensitivity?
1. Why is it important for a model to generalize to unseen data? What are the risks of a model that doesn't generalize well?
1. What are the signs of overfitting and underfitting in a model? How can you address these issues?
1. What is the bias-variance tradeoff? How do you find the right balance between bias and variance in a model?
1. How do you model more complex patterns in data? What techniques can be used to capture these patterns effectively?
1. Why is it important to start with data exploration before modeling?
1. How do you determine if a model is good? What metrics and methods can you use to evaluate its performance?
1. What does RMSE (Root Mean Square Error) tell us about a model's performance? Why is it important to compare RMSE on both training and test datasets?
1. What does RMSE measure and why is it useful?
1. How does RMSE differ from MAE?
1. What does R² tell us about a regression model?
1. Why do classification metrics not apply to regression problems?
1. What are TP, FP, FN, and TN in a confusion matrix?
1. Give some examples on why you'd want to optimize a model towards more TP (and more FP) or more TN (and more FN).
1. What does sensitivity (recall) measure, and why is it important in medical diagnostics?
1. What does specificity measure, and when is it more important than sensitivity?
1. Can you think of a scenario where high sensitivity is preferred over high specificity, and vice versa?
1. What does the F1-score balance, and when is it most useful?
1. What challenges arise when evaluating multiclass classification models?
1. What parameters can be calculated to assess the quality of multiclass classification models?
1. What is the difference between macro and micro averaging?
1. In multiclass classification, what are macro and micro average? What are the advantages of both?
1. When would you use macro average over micro average?
1. What does changing the classification threshold do to sensitivity and specificity?
1. What is an ROC and the AUC?
1. What does the ROC curve represent?
1. Why is the diagonal line in an ROC curve considered a “random classifier”?
1. How can ROC curves help compare different models?
1. What does AUC-ROC measure and why is it useful?
1. Why might ROC curves be misleading in imbalanced datasets?

## Models

1. What makes a model "generalize well," and why is that more important than just fitting the training data?
1. How can we tell if a model is too simple or too complex for the problem we're trying to solve?
1. Why might a model that performs well on training data still fail in real-world applications?
1. What are the risks of using overly complex models, even if they reduce training error?
1. How does the bias-variance tradeoff influence the choice of model complexity?
1. Why is it important to split data into training, validation, and test sets — and what could go wrong if we don’t?
1. How does the size of your dataset influence how you should split it?
1. Why is it dangerous to tune a model using the test set?
1. What does RMSE really tell us about a model’s performance, and when might it be misleading?
1. How can we model non-linear relationships without resorting to overly complex functions?
1. What are the benefits and drawbacks of using splines or polynomial regression to capture complex patterns?
1. Why is sensitivity to the train/test split (variance) a problem, and how can we detect it?
1. How does cross-validation help us build more reliable models, especially with limited data?
1. Why is stratified splitting important in classification problems, and what happens if we ignore it?
1. What are the trade-offs between bagging and boosting in ensemble learning?
1. Why does combining weak models often result in a strong model?
1. How does bootstrapping help when we don't have enough data?
1. What makes gradient boosting different from random forests, and when might one be preferred over the other?
1. Why is XGBoost often considered better than traditional gradient boosting?
1. What are the risks of using ensemble methods without understanding the individual models involved?
1. How do linear models help us understand relationships in data, even if they’re not the most accurate predictors?
1. What assumptions do linear models make, and how can we check if those assumptions hold?
1. Why might regularization be necessary in linear models, and how does it help?
1. How can linear models be used to remove dominant effects in data to reveal subtler patterns?
1. What makes support vector machines effective in high-dimensional spaces?
1. Why is the choice of kernel so important in SVMs?
1. How does k-nearest neighbors differ from other models in how it “learns”?
1. What are the limitations of k-NN in high-dimensional or noisy datasets?
1. Why does Naive Bayes work well despite its unrealistic assumptions?
1. How do probabilistic models like Naive Bayes differ in philosophy from geometric or distance-based models?
1. How does the ensemble methods stacking differ from bagging and boosting?
1. Why is it important to understand the assumptions behind each model before applying it?
