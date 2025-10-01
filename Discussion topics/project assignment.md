# Project assignment

We'll be investigating two different datasets. You are in a team of three, so simply saying "you'll do A, I'll do B" won't work. It's ok to split up the work, but everybody in the group should be able to explain what is happening in the different notebooks, even if they weren't the ones making it (so explain what everything does among the group).

## Dataset 1: UK housing

[Download from Kaggle](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid/data)

Contains all housing prices in the England/Wales between 1995 and 2017. The dataset is very large (2gb). You could work on a subset (in time, in location, ...) or a summary (combine prices per location per month). You could also do a stratified extraction, use this to tune the best possible model and apply the parameters you've learned in this way to the full model.

## Dataset 2: UK Historic Electricity Demand Data

[Download from Neso](https://www.neso.energy/data-portal/historic-demand-data?page=0)
    
Electricity demand in England/Wales between 2001 and 2025. Comes in many files, so combining them will be required.

## Final upload

Your final upload will be a link to your github repo. Upload is on canvas, and the deadline is...

$${\color{red}Monday \space 24 \space November \space 2025}$$

As I already have this link you might wonder why an upload is required. It is to clearly state that you have finished working and still want to participate in the presentations.

# Project parts

## Prepare

* Choose a cool name for your group. Something you can identify with.
* Create your github repo.
* If the repo is private: invite the github user "mjochen".
* If the repo is public: send the link to the repo using teams.
* Invite your teammembers as collaborators.
* Create a README.md-file containing:
    * Name of your group
    * Names of all people in the group
* Build the basic structure of your project.
    * One folder per dataset
    * Numbered naming-system for jupyter notebooks to run them in the right order (scrape, clean, predict, deploy)

You'll fill up the folders with a bunch of jupyter notebooks. Start every notebook by stating who worked on it and roughly what they did. Also make sure you have markdown-blocks explaining what you are doing in the following code-block.

(Remember, during the oral exam you may be asked "what does this code do?". Having that explanation just above really helps a lot in that case.)

## Clean and explore

### Clean the data

This is very important on both datasets as you don't control the field-names yourself.

* Rename columns to remove spaces from the name and make them all lowercase.
* Look for the Na-values. Fix them if possible, using a couple of techniques before deciding which is best.
* Look for the Outliers. Fix them if needed, using a couple of techniques before deciding which is best.
* Look for (ordered) categoricals and label them as such.

### Exploratory data analysis

* Show the outliers and try to explain them.
* Draw some graphs about features you find interesting.
* Look for correlations in your data.

### Repeat

Both phases (cleaning and exploring) aren't two different steps in a process, but rather one large fuzzy mess of code. Something like:

* I'll give all the Na's the mean value.
* My graphs look strange, what is this peak doing at the mean?
* Is there a correlation between the value that has a lot of Na's and another column?
* Let's use the other column to fill in the Na's!

In the upcoming steps of this project you'll put all the really good code together to make one final import, but for now poke the data and see what happens.

### Final loading and preparing

Once you've cleaning and exploring and cleaning and exploring you'll lose track of the necessary steps and the optional steps. It's also possible that you did some cleaning that wasn't needed (e.g predict a field that should have been left empty).

So end up your cleaning by creating a notebook that contains all the code to go from rough data to prepared data without any of the graphs.

This has to be done for all both datasets.

## Building models

The previous part ended with a single notebook (per dataset) that would prepare your data for predicting. Next is building a couple of models and actually predicting something.

Which models will you need?
* A quick first model. This won't be a good one, but with this you can start working on the deployment (next step) while still tuning the model.
* Use PyCaret (or another automated ML comparison) on both datasets.
* Create and tune a model on both your datasets. Explain why you choose this particular model and perhaps train a second model to validate this choice.
* Create and tune a model on AWS.

Make sure to keep all the metrics on the models you made and compare these to show which model performed best.

## Deploy

You also need to deploy your models. This part will only be covered in class minimally as it's the sort of thing any AI can help you with. If you have questions don't hesitate to ask though.

You need:

### A frontend

Streamlit will do, but you could also build a custom webpage that listens to an API.

### A backend

Some code that uses the model you made earlier and makes predictions based on some user input. Don't shy away from languages you've never used before (go, rust, julia, ...)

### A pipeline

In a company you'd have the webdepartment responsible for the front- and backend and the ML-department building a model. When the webdepartment is ready the ML department will keep on building better models based on new data. Make sure the ML-department has an automated pipeline that updates the model everytime new code is pushed to github.

### Hosting

You'll need to host this code somewhere. The frontend normally won't be a problem but the backend may prove to be trickier. You can host it at home on a raspberry Pi or a virtual machine and you don't need a fancy URI. What you do need is a working model of a setup that would bring this ML-model out of the PC of the developer and into the hands of the general public.

# Upload and presentation

## Upload

When all the models have been compared it's time for the final upload and presentation. Check that you have the following files:

* EDA: multiple notebooks. Contain **cleaning** and **graphs** as well the explanation of both.
* Final import: One notebook with a summarized version of all cleaning you found interesting.
* Models: One file per model per dataset.
    * If your computer took a long time building a model, don't remove the output of the code blocks and/or include screenshots of them.
    * If you stored your models in a pickle-file, which is a good idea, remember that github only allows files smaller than 100MB. Remove them if they are bigger before committing. (Use .gitignore)
    * For AWS-models, download the notebook you used on sagemaker locally to include in the github repo.
* Comparison of models: One notebook (per dataset) that gathers the metrics of the models and does a deep down comparison. Also include your conclusions.

## Presentation

Finally your presentation. You'll have 25 minutes per team, but that is including the questions for the oral exam. The structure is as follows:

* Who's who in your team (company presentation)
* EDA: what did you found out? What did you [not] expect?
* Models: Which was easier to train? Which gave the best result?
* Conclusion

* (Questions on your models will be asked during the previous presentation.)
* Questions on the code present in the notebooks that you have worked on.
* Each student will give a random number. Based on this number you'll get one of the discussion topics as an oral question and you should immediately answer them. If you're stuck a teammate can help out.
* If you really don't know the answer you can get another question.

The presentations will be held during classes on 28 November. An exact timing will be shared on canvas. Only the presenting group is present during the presentations. (When you don't have presentation you don't have to be at school.)



