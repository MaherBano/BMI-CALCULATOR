import streamlit as st

st.title("***BMI CALCULATOR***")

# Input sliders
height = st.slider("Enter your height (in cm):", 100, 250, 150)
weight = st.slider("Enter your weight (in kg):", 20, 150, 50)

# Convert height to meters
height_m = height / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

st.write(f"Your BMI is: **{bmi:.2f}**")

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

st.write(f"Category: **{category}**")