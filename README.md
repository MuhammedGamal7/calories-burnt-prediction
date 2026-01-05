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
│calories-burnt-prediction/

├── app.py # Streamlit application

├── Calories_Burnt_Prediction.ipynb# Model training and experimentation

├── calories_model.pkl # Trained ML model

├── requirements.txt # Project dependencies

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/jimmy70707/calories-burnt-prediction.git
cd calories-burnt-prediction

2.Install dependencies:
pip install -r requirements.txt

3.streamlit run app.py
4.Open the provided local URL in your browser.
```
Input Parameters

Gender

Age

Height (cm)

Weight (kg)

Exercise Duration (minutes)

Heart Rate

Body Temperature (°C)

## 👤 Author
Muhammed Gamal

Machine Learning & AI Engineer

## 🔗 Connect with Me

<p align="center">
<a href="https://www.linkedin.com/in/muhammed-gamal-b0a347244"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="36" height="36"/></a>&nbsp;&nbsp;&nbsp;
<a href="https://github.com/Jimmy70707"><img src="https://img.icons8.com/ios-filled/50/ffffff/github.png" width="36" height="36"/></a>&nbsp;&nbsp;&nbsp;
<a href="mailto:muhammed.gammal00@gmail.com"><img src="https://img.icons8.com/fluency/48/email-open.png" width="36" height="36"/></a>
</p>
