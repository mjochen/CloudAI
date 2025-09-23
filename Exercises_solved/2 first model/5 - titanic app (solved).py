import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# import the files, only needed for ranges in sliders
df = pd.read_excel('files/titanic3.xlsx', engine='openpyxl')


def calculate_survival():
    random_person_dict = {
        'pclass': class_option,
        'age': age_slider,
        'sibsp': sibsps_slider, # SibSp is the number of siblings or spouse of a person onboard.
        'parch': parch_slider, # Similar to the SibSp, this feature contained the number of parents or children each passenger was touring with.
        'fare': fare_option,
        'male': (gender_option == "male"),
        'Q': (embarked_option == "Q"),
        'S': (embarked_option == "S")
    }

    random_person = pd.DataFrame(random_person_dict, index=[0])
    
    with open('files/titanic_model.pkl', 'rb') as file: 
        model = pickle.load(file) 

    return model.predict(random_person)[0]

# Using object notation
class_option = st.sidebar.selectbox("Which class were you in?", (1,2,3))
age_slider = st.sidebar.slider("How old are you?", df.age.min(), df.age.max(), df.age.mean())
sibsps_slider = st.sidebar.slider("How many siblings or spouse do you have?", df.sibsp.min(), df.sibsp.max(), int(df.sibsp.mean()))
parch_slider = st.sidebar.slider("How many parents or children do you have?", df.parch.min(), df.parch.max(), int(df.parch.mean()))
fare_option = st.sidebar.selectbox("What was the fare you paid?", list(df.fare.quantile([0.25, 0.5, 0.75, 1])))
gender_option = st.sidebar.selectbox("What is your gender?", ("male", "female"))
embarked_option = st.sidebar.selectbox("Where did you embark?", ("Q", "S", "C"))
# displ_slider = st.sidebar.slider("Displacement",mpg.displ.min(), mpg.displ.max(), 2.8)
# cyl_dropdown = st.sidebar.selectbox("Cylinders", mpg.cyl.sort_values().unique(), 2)
# year_slider = st.sidebar.slider("Year", mpg.year.min(), mpg.year.max(), 1999)
ok_button = st.sidebar.button("OK")

# Bing AI, "could you please write an intro text for a website that uses machine learning to predict surviving the titanic. Not to long."
st.markdown("""
# **Predicting Titanic Survival with Machine Learning**

Welcome to our Titanic Survival Prediction platform! 🚢

Our cutting-edge machine learning algorithms analyze historical data from the ill-fated RMS Titanic to forecast the likelihood of passengers surviving the tragic voyage. By considering factors such as passenger class, age, gender, and cabin location, our models provide accurate predictions.

Embark on this journey with us as we unravel the mysteries of the Titanic's destiny. 🌊
""")

if ok_button:
    living = calculate_survival()
    if living == 1:
        st.markdown(f"**You would have survived the Titanic.**")
    else:
        st.markdown(f"**You would have died on the Titanic.**")
    