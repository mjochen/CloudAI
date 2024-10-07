# Project overview

For this course you'll need to do a project. You'll be doing this project in a team of about 3 people. The project will consist of 3 datasets:

## Titanic

Our toy-dataset. You'll find so much machine learning notebooks on this dataset that it is hard not to get good results. Use this as a learning opportunity and to test out Sagemaker on AWS.

## UK Housing

[The link](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid/data)

This is a huge dataset. You can choose to work with the full dataset or a subset of the data. **When working with the full dataset, do not upload it to github.** You don't have 2.5gb of storage there.

## Stock prices

Third dataset is time related. Pick two companies (Microsoft and Apple? Opel and Volkswagen?) and download their stock value for as long as you can find them. Then start by comparing them and predicting the upcoming value.

Note: we're not investing actual money here, so don't predict the future but the near past. That way you'll have the data from company A to help predict company B and you'll be able to check your predictions vs the actual value of the stock.

## Final upload

Your final upload will be a zip-files containing all the files from your github repo. Upload is on canvas, and the deadline is...

$${\color{red}Thursday \space 28 \space November \space 2024}$$

The following is roughly ordered chronologically, but some steps may be executed concurrently (like scraping the stocks and cleaning titanic). The first step (prepare) should be finished by the first week but for the others parts you get to decide [your time-line all by yourself](https://www.timeanddate.com/countdown/boxing?iso=20241128T11&p0=337&msg=Deadline+for+the+Cloud+AI+project&ud=1&font=cursive).



# Prepare

* Choose a cool name for your group. Something you can identify with.
* Create your github repo.
* If the repo is private: invite the github user "mjochen".
* If the repo is public: send the link to the repo using teams.
* Invite your team as collaborators.
* Create a README.md-file containing:
    * Name of your group
    * Names of all people in the group
    * Which companies you'll be tracking for the stock-task
* Build the basic structure of your project.
    * One folder per dataset
    * Numbered naming-system for jupyter notebooks to run them in the right order (scrape, clean, predict)

You'll fill up the folders with a bunch of jupyter notebooks. Start every notebook by stating who worked on it and roughly what they did. Also make sure you have markdown-blocks explaining what you are doing in the following code-block.

(Remember, during the oral exam you may be asked "what does this code do?". Having that explanation just above really helps a lot in that case.)

# Scrape

All three projects require some amount of scraping:

* Titanic is easy. There are CSV's on kaggle you can use. If they contain the "boat" and "body"-columns don't forget to remove these before starting to make predictions (if you're in a lifeboat you had a good chance of surviving, if they found your body you died). Include a link in your first notebook.
* The link for UK housing was given, but you still have to solve the 2.5gb-problem. Look into it. Explain your solution in your first notebook.
* The stocks are real scraping-example. Create a separate notebook for this task.

# Clean and explore

## Clean the data

This is very important on Titanic and UK housing as you don't control the field-names yourself there.

* Rename columns to remove spaces from the name and make them all lowercase.
* Look for the Na-values. Fix them if possible, using a couple of techniques before deciding which is best.
* Look for the Outliers. Fix them if needed, using a couple of techniques before deciding which is best.
* Look for (ordered) categoricals and label them as such.

## Exploratory data analysis

Once again more important for Titanic and UK housing than for the stock-prices. Don't skip them entirely though as a good exploratory data analysis will allow you to check the data you've downloaded. There may also be outliers that you want to know about before moving on.

* Show the outliers and try to explain them.
* Draw some graphs about features you find interesting.
* Look for correlations in your data.

## Repeat

Both phases (cleaning and exploring) aren't two different steps in a process, but rather one large fuzzy mess of code. Something like:

* I'll give all the Na's the mean value.
* My graphs look strange, what is this peak doing at the mean?
* Is there a correlation between the value that has a lot of Na's and another column?
* Let's use the other column to fill in the Na's!

In the upcoming steps of this project you'll put all the really good code together to make one final import, but for now poke the data an see what happens.

## Final loading and preparing

Once you've cleaning and exploring and cleaning and exploring you'll lose track of the necessary steps and the optional steps. It's also possible that you did some cleaning that wasn't needed (e.g predict a field that should have been left empty).

So end up your cleaning by creating a notebook that contains all the code to go from rough data to prepared data without any of the graphs.

This has to be done for all three datasets.

# Building models

The previous part ended with a single notebook (per dataset) that would prepare your data for predicting. Next is building a couple of models and actually predicting something.

For both Titanic and the housing-dataset you need at least a model using **AWS** and another model that **PyCaret** suggested. Thirdly you'll also need a model that you manually implemented, along with the reason you choose this exact model.

When the models are done, gather the metrics that describe these models. Export them (CSV, Pickle, ...) and put them together in a single notebook. There you can do a deep analysis on which of the models performed better.

# Upload and presentation

## Upload

When all the models have been compared it's time for the final upload and presentation. Check that you have the following files:

* EDA: multiple notebooks. Contain **cleaning** and **graphs** as well the explanation of both.
* Final import: One notebook with a summarized version of all cleaning you found interesting.
* Models: One file per model per dataset.
    * If your computer took a long time building a model, don't remove the output of the code blocks and/or include screenshots of them.
    * If you stored your models in a pickle-file, which is a good idea, remember that github only allows files smaller than 100MB. Remove them if they are bigger before committing. (Use .gitignore)
* Comparison of models: One notebook (per dataset) that gathers the metrics of the models and does a deep down comparison. Also include your conclusions.

## Presentation

Finally your presentation. You'll have 25 minutes per team, but that is including the questions for the oral exam. The structure is as follows:

* Who's who in your team (company presentation)
* EDA: what did you found out? What did you [not] expect?
* Models: Which was easier to train? Which gave the best result?
* Conclusion

* (Questions on your models will be asked during the previous presentation.)
* Questions on the code present in the notebooks that you have worked on.
* Each student will give a random number. Based in this number you'll get one of the discussion topics as an oral question and you should immediately answer them. If you're stuck a teammate can help out.
* If you really don't know the answer you can get another question.

The presentations will be held during classes on 9 or 16 December. An exact timing will be shared on canvas. Only the presenting group is present during the presentations. (When you don't have presentation you don't have to be at school.)