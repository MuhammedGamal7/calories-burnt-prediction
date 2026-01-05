import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("calories_model.pkl")

st.title("Calories Burnt Prediction App")

st.write("Enter your details below:")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=10, max_value=100, value=25)
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
duration = st.number_input("Exercise Duration (min)", min_value=1, max_value=300, value=60)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=80)
body_temp = st.number_input("Body Temp (°C)", min_value=35.0, max_value=42.0, value=37.0)

# Convert gender
gender = 1 if gender == "Male" else 0

# Prediction
if st.button("Predict Calories Burnt"):
    features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(features)
    st.success(f"Estimated Calories Burnt: {prediction[0]:.2f}")
