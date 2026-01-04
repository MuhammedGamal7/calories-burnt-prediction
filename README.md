# Calories Burnt Prediction App

A machine learning–powered web application that estimates the number of calories burnt during physical activity based on personal and exercise-related inputs.  
The application provides instant predictions through an interactive Streamlit interface.

---

## Overview

Accurately estimating calories burnt is important for fitness tracking, weight management, and exercise planning.  
This project uses a trained machine learning model to predict calorie expenditure using physiological and activity-related features such as age, gender, body measurements, exercise duration, heart rate, and body temperature.

The model is deployed as a lightweight and user-friendly web app using Streamlit.

---

## Problem Statement

Most calorie estimations rely on generic formulas that do not adapt well to individual body characteristics or real-time exercise conditions.  
This project aims to provide a more personalized calorie estimation using machine learning, improving accuracy and usability.

---

## Solution Approach

- A regression-based machine learning model is trained using physiological and exercise data.
- The trained model is saved and loaded using `joblib`.
- A Streamlit web interface allows users to enter their data and receive real-time predictions.
- Gender is encoded numerically to be compatible with the trained model.

---

## Features

- Interactive web-based interface
- Real-time calorie burn prediction
- Simple and clean user input flow
- Lightweight deployment using Streamlit
- Pre-trained model for fast inference

---

## Tech Stack

- **Python**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Joblib**
- **Jupyter Notebook**

---

## Project Structure

