**GenAI Disclosure** → check GenAI policy on how to use GenAI tools

# Machine Learning/cloud AI challenge


We'll be investigating two different datasets. This the theme is "Going green."


## Dataset 1: Secondary Mushroom

[Download from UCI](https://archive.ics.uci.edu/dataset/848/secondary+mushroom+dataset)

This dataset includes 61.069 hypothetical mushrooms based on 173 species (353 mushrooms
per species). Each mushroom is identified as definitely edible, definitely poisonous, or of
unknown edibility and not recommended (the latter class was combined with the poisonous class).

The dataset isn't huge, so make sure to use each row optimally. It's also quite obvious what should be predicted (although you can diverge from the beaten path, but talk this trough first). It does, however, lend itself very nicely to a clean inference-interface.

## Dataset 2: NYC Citi Bike System Data

[Download from citibikenyc](https://citibikenyc.com/system-data)
    
A rather large dataset of all trips using City Bikes in New York.

The files are too large to store inside of the github repo. Make sure they are downloaded, unpacked and assembled with code (don't do this manually!) Analysis will therefore be less straightforward than the mushrooms. This means:

- Exploratory Data Analysis: What can the dataset tell you that is actually supported by the data?
    - And can you back this up with statistical evidence?
- Aggregation: Try out some aggregations and visualize them
- Testable Hypothesis: Before building a predictive model, formulate at least one testable hypothesis and use the data to establish that there is actually a meaningful pattern to predict.

After all this, make a decision and deploy the best possible model.

## Final upload

Your final upload will be a link to your github repo. Upload is on canvas, and the deadline is...

$${\color{red}Thursday \space 15 \space October \space 2026}$$

As I already have this link you might wonder why an upload is required. It is to clearly state that you have finished working and still want to participate in the presentations.

# Groups

We'll be investigating two different datasets. You are in a team of three, so simply saying "you'll do A, I'll do B" won't work. It's ok to split up the work, but everybody in the group should be able to explain what is happening in the different notebooks, even if they weren't the ones making it (so explain what everything does among the group).

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

As always, clean and explore the data. Apply all that you can think of to make this a useable dataset. Also check if what you changed actually improves the data.

This includes (but isn't limited to):

- Column names
- Na-values
- Outliers
- (Ordered) categoricals

Once you've cleaning and exploring and cleaning and exploring you'll lose track of the necessary steps and the optional steps. It's also possible that you did some cleaning that wasn't needed (e.g predict a field that should have been left empty).

So end up your cleaning by creating a notebook that contains all the code to go from rough data to prepared data without any of the graphs.

This has to be done for both datasets.

## Building models

The previous part ended with a single notebook (per dataset) that would prepare your data for predicting. Next is building a couple of models and actually predicting something.

Which models will you need?
* A quick first model. This won't be a good one, but with this you can start working on the deployment (next step) while still tuning the model.
* Use PyCaret (or another automated ML comparison) on both datasets.
* Create and tune multiple models on both your datasets. Explain why you choose the models and compare the results.
* **Create and tune at least one model on AWS.**

Make sure to keep all the metrics on the models you made and compare these to show which model performed best.

## Deploy

You also need to deploy your models. This part will only be covered in class minimally. If you have questions don't hesitate to ask though.

You need:

* A frontend: Build a custom webpage that listens to an API.
* A backend: Some code that uses the model you made earlier and makes predictions based on some user input. Don't shy away from languages you've never used before (go, rust, julia, ...)
* A pipeline: In a company you'd have the webdepartment responsible for the front- and backend and the ML-department building a model. When the webdepartment is ready the ML department will keep on building better models based on new data. Make sure the ML-department has an automated pipeline that updates the model everytime new code is pushed to github.
* Hosting: You'll need to host this code somewhere. The frontend normally won't be a problem but the backend may prove to be trickier.
    * You can host it at home on a raspberry Pi or a virtual machine and you don't need a fancy URI.
    * What you do need is a working model of a setup that would bring this ML-model out of the PC of the developer and into the hands of the general public.
    * It only has to run when I'm evaluating the model, which will be two week max. You have to be able to turn it back on later.
    * Tip: look into Oracle. They have a pretty decent free tier, but beware where you start it (the free tier is limited to datacenters where they have 'space left').

# Upload and presentation

## Upload

When all the models have been compared it's time for the final upload and presentation. Check that you have the following files:

* EDA: multiple notebooks. Contain **cleaning** and **graphs** as well the explanation of both.
* Final data preparation notebook: One notebook with a summarized version of all cleaning you found interesting.
* Models: One file per model per dataset.
    * If your computer took a long time building a model, don't remove the output of the code blocks and/or include screenshots of them.
    * If you stored your models in a pickle-file, which is a good idea, remember that github only allows files smaller than 100MB. Remove them if they are bigger before committing. (Use .gitignore)
    * For AWS-models, download the notebook you used on sagemaker locally to include in the github repo.
* Comparison of models: One notebook (per dataset) that gathers the metrics of the models and does a deep down comparison. Also include your conclusions.

## Presentation

Finally your presentation. Each team has a 25-minute slot, including the oral-exam questions. The structure is as follows:

* Who's who in your team (company presentation)
* EDA: what did you found out? What did you [not] expect?
* Models: Which was easier to train? Which gave the best result?
* Conclusion

* (Questions on your models will be asked during the previous presentation.)
* Questions on the code present in the notebooks that you have worked on.
* Questions on topics related to what you did in the notebooks.
    * Possible: You've used XGBoost. This is a tree-based model. What others are there?

The presentations will be held during classes on 23 October. An exact timing will be shared on canvas. Only the presenting group is present during the presentations. (When you don't have presentation you don't have to be at school.)

# Grading

## Minimum viable product

The minimum viable product entails the following for both datasets:

* Loading and cleaning the data
* EDA with graphs and statistical analysis
* Using PyCaret for automated model comparison
* Training at least 2 additional models
* Using an appropriate split of the data
* Deploying at least one model in a web interface for inference
* Training and tuning at least one model using AWS

## Extensions

Extensions can include (but are not limited to):

* EDA that tells an actual story, rather than just presenting a collection of graphs
* Training additional models
* Tuning models and improving their performance
* More advanced feature engineering
* More thorough model comparison and error analysis
* Hosting the model in a different language than the one it was trained in
* A more advanced or automated deployment pipeline
* ...

In both the MVP and the extensions, keep in mind:

> Everyone can generate a lot of code. It takes skill to keep only the code that adds to the story you are trying to tell and the goal you are trying to achieve.

**Quantity will not get you grades; quality will.**

However, this does not mean that you should hide experiments that did not work. If you choose not to follow a particular path — for example, not to train a certain model or not to investigate a particular graph — explain why you made that decision.

Good ML work is not about trying everything. It is about making informed choices and being able to explain them.

## Evaluation & Grading Rubric

| Criterion  |        % | Formative Checkpoints *(Process & Iteration)*      |Final Oral Defense *(Mastery & Ownership)*   |
| ---- | ----: | ------ | ------ |
| **Data & EDA**                       |  **20%** | Clean, reproducible data preparation; meaningful EDA; appropriate handling of missing values, outliers and categoricals; hypotheses for Citi Bike. | Explains important patterns and cleaning decisions, and how findings influenced the ML problem and modelling.                    |
| **Modelling & Fine-Tuning**          |  **30%** | Baseline + AutoML comparison + tuned models; appropriate validation and metrics; AWS model; systematic experimentation.                            | Explains model choices, validation, metrics and tuning; can explain why the final model performs as it does.                     |
| **Evaluation & Error Analysis**      |  **15%** | Compares models using meaningful metrics; investigates poor or unexpected predictions and iterates accordingly.                                    | Diagnoses concrete errors and limitations; distinguishes genuine improvements from misleading metrics or experimental artefacts. |
| **End-to-End Pipeline & Deployment** |  **20%** | Working data → preprocessing → model → API → frontend pipeline; hosted application; automated model update/retraining.                             | Explains the architecture and data flow, and can justify the deployment and automation choices.                                  |
| **Code & Project Quality**           |  **10%** | Reproducible notebooks, clear repository structure, documented code and sensible Git workflow.                                                     | Can walk through their code and explain implementation choices; demonstrates that all team members understand the project.       |
| **Process & AI Ownership**           |   **5%** | Responds to feedback, iterates on the project, and uses AI tools critically and transparently.                                                     | Demonstrates individual ownership; can defend implementation and modelling decisions without relying on AI assistance.           |
| **Total**                            | **100%** |                                                                                                                                                    |                                                                                                                                  |


# Gen AI disclaimer

Generative AI was used in the formation of this document. It was used to suggest datasets and project ideas, proofread and improve the wording of the assignment, and help structure and check the grading criteria for completeness and fairness.

The final assignment, requirements and grading criteria were reviewed and decided upon by the lecturer.