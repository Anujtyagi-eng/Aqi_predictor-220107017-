import streamlit as st
import joblib
import numpy as np

# Load the trained model pipeline
model = joblib.load('model_pipeline.pkl')

# AQI category function
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

# Streamlit app
st.title("🌍 AQI Predictor")

st.write("Enter pollutant levels and your city to predict AQI:")

# Input fields
no2 = st.number_input("NO2 AQI", min_value=0.0)
ozone = st.number_input("Ozone AQI", min_value=0.0)
co = st.number_input("CO AQI", min_value=0.0)
pm25 = st.number_input("PM2.5 AQI", min_value=0.0)
city = st.text_input("City")
country = st.text_input("Country")

# Predict button
if st.button("Predict AQI"):
    input_data = np.array([[no2, ozone, co, pm25, city, country]])
    prediction = model.predict(input_data)[0]
    category = get_aqi_category(prediction)

    st.success(f"🌡️ Predicted AQI: **{round(prediction, 2)}**")
    st.info(f"🏷️ Air Quality Category: **{category}**")
