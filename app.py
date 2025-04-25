import streamlit as st
import joblib
import pandas as pd

# Load the trained pipeline model
pipeline = joblib.load('model_pipeline.pkl')

st.title("AQI Predictor")

# Inputs for the user to enter
no2 = st.number_input("NO2 AQI Value", min_value=0.0, step=1.0)
ozone = st.number_input("Ozone AQI Value", min_value=0.0, step=1.0)
co = st.number_input("CO AQI Value", min_value=0.0, step=1.0)
pm25 = st.number_input("PM2.5 AQI Value", min_value=0.0, step=1.0)
city = st.text_input("City Name")
country = st.text_input("Country Name")

if st.button("Predict AQI"):
    # Creating a DataFrame for prediction
    input_data = pd.DataFrame([{
        "NO2 AQI Value": no2,
        "Ozone AQI Value": ozone,
        "CO AQI Value": co,
        "PM2.5 AQI Value": pm25,
        "City": city,
        "Country": country
    }])

    # Making the prediction
    prediction = pipeline.predict(input_data)[0]

    # Displaying the result
    st.write(f"Predicted AQI: {prediction:.2f}")
