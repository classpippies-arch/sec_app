import numpy as np
import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return "The person is NOT diabetic" if prediction[0] == 0 else "The person IS diabetic"

def main():
    st.title("Diabetes Prediction Web App")
    inputs = [st.text_input(label) for label in [
        "Number of Pregnancies","Glucose Level","Blood Pressure",
        "Skin Thickness","Insulin Level","BMI",
        "Diabetes Pedigree Function","Age"
    ]]
    if st.button("Predict"):
        st.success(diabetes_prediction(inputs))

if __name__ == "__main__":
    main()
