import streamlit as st
import joblib
import pandas as pd

# Load your saved pipeline
pipeline = joblib.load('model_pipeline.pkl')

# AQI category helper
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

st.title("🌍 AQI Predictor")

# User inputs (names must match training features exactly)
no2   = st.number_input("NO2 AQI Value",   min_value=0.0, step=0.1)
ozone = st.number_input("Ozone AQI Value", min_value=0.0, step=0.1)
co    = st.number_input("CO AQI Value",    min_value=0.0, step=0.1)
pm25  = st.number_input("PM2.5 AQI Value", min_value=0.0, step=0.1)
city    = st.text_input("City",    value="Delhi")
country = st.text_input("Country", value="India")

if st.button("Predict AQI"):
    # Build DataFrame with the exact columns your pipeline expects
    df = pd.DataFrame([{
        "NO2 AQI Value":   no2,
        "Ozone AQI Value": ozone,
        "CO AQI Value":    co,
        "PM2.5 AQI Value": pm25,
        "City":            city,
        "Country":         country
    }])
    # Predict and categorize
    pred     = pipeline.predict(df)[0]
    category = get_aqi_category(pred)

    st.success(f"🌡️ Predicted AQI: **{pred:.2f}**")
    st.info(   f"🏷️ Category: **{category}**")
