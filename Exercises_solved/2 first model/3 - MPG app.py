import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# import the files, only needed for ranges in sliders
mpg = pd.read_csv('files/mpg.csv', index_col=0)


def calculate_hwy():
    new_car = pd.DataFrame(data = [[displ_slider, year_slider, cyl_dropdown]], columns = ['displ', 'year', 'cyl'])
    with open('files/mpg_model.pkl', 'rb') as file: 
        model_3 = pickle.load(file) 

    return round(model_3.predict(new_car)[0],4)

# Using object notation
displ_slider = st.sidebar.slider("Displacement",mpg.displ.min(), mpg.displ.max(), 2.8)
cyl_dropdown = st.sidebar.selectbox("Cylinders", mpg.cyl.sort_values().unique(), 2)
year_slider = st.sidebar.slider("Year", mpg.year.min(), mpg.year.max(), 1999)
ok_button = st.sidebar.button("OK")

# Bing AI, "could you write a welcome text for a website that predict the miles per gallon a car can do based on displacement, year and nr of cylinders?"
st.markdown("""
# Welcome to MPG Predictor!
At MPG Predictor, we’re passionate about helping you estimate the fuel efficiency of your car. Whether you’re a car enthusiast, a prospective buyer, or simply curious, our powerful prediction models can provide valuable insights.

## How It Works
1. Input Your Car Details: Tell us about your vehicle. Enter the displacement, model year, and the number of cylinders in your car.
1. Predict MPG: Our sophisticated algorithms analyze historical data from various makes and models. Using this information, we predict the miles per gallon (MPG) your car is likely to achieve.
1. Explore Insights: Discover how different factors impact fuel efficiency. Is a larger displacement better for MPG? Does the model year play a significant role? We’ve got answers!

## Why Choose MPG Predictor?

* Accuracy: Our models are trained on real-world data, ensuring reliable predictions.
* User-Friendly: Our intuitive interface makes it easy to input your car details and get instant results.
* Educational: Learn about the relationship between car features and fuel efficiency.

## Get Started
Ready to explore? Enter your car’s details and let MPG Predictor do the rest! 🚗💨

(The default values of 2.8 liters, 6 cylinders and year 1999 are of the audi A4 and should give about 26 miles per gallon.)""")

if ok_button:
    hwy = calculate_hwy()
    st.markdown(f"**Your car will do an average of {hwy} miles per gallon on the highway.**")

# Run using
# streamlit run '.\4.3 - MPG app.py'