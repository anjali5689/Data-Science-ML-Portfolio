import joblib
import streamlit as st
import pandas as pd


# Load trained model
model = joblib.load('calorie_model.pkl')

st.set_page_config(page_title="Calorie Burn Predictor", layout="centered")
st.title("🔥 Calorie Burn Predictor")

st.markdown("Enter your workout details below to estimate calories burned.")

with st.form("calorie_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    age = st.slider("Age", 10, 100, 25)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=65.0)
    duration = st.number_input("Workout Duration (minutes)", min_value=1.0, max_value=180.0, value=30.0)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=60.0, max_value=200.0, value=120.0)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

    submitted = st.form_submit_button("Predict Calories Burned")

# Run prediction only when form is submitted
if submitted:
    input_df = pd.DataFrame([{
        'Gender': gender,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Duration': duration,
        'Heart_Rate': heart_rate,
        'Body_Temp': body_temp
    }])
    
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Calories Burned: **{prediction:.2f} kcal**")