import numpy as np
import pickle
import streamlit as st
import os

# --------- Load Model ----------
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)


# --------- Prediction Function ----------
def diabetes_prediction(input_data):
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return "The person is NOT diabetic" if prediction[0] == 0 else "The person IS diabetic"


# --------- Custom Modern UI CSS ----------
def load_css():
    st.markdown("""
        <style>
        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            font-family: 'Inter', sans-serif;
        }

        /* Title styling */
        .title {
            font-size: 42px;
            font-weight: 800;
            background: linear-gradient(90deg, #FF7A1A, #ff9b4a);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            padding-bottom: 10px;
        }

        /* Glassmorphism card */
        .glass-card {
            backdrop-filter: blur(14px) saturate(140%);
            -webkit-backdrop-filter: blur(14px) saturate(140%);
            background-color: rgba(255, 255, 255, 0.35);
            border-radius: 25px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            animation: fadeIn 0.8s ease-in-out;
        }

        /* Smooth fade animation */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Predict Button */
        .stButton > button {
            background: linear-gradient(90deg, #FF7A1A, #ff9442);
            border: none;
            padding: 12px 25px;
            border-radius: 15px;
            color: white;
            font-size: 18px;
            font-weight: 600;
            transition: 0.2s ease-in-out;
        }
        .stButton > button:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 20px rgba(255, 122, 26, 0.4);
        }

        </style>
    """, unsafe_allow_html=True)


# --------- Main App ----------
def main():
    load_css()

    st.markdown("<div class='title'>🩺 Diabetes Prediction</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    st.write("### Enter Patient Details")

    labels = [
        "Number of Pregnancies","Glucose Level","Blood Pressure",
        "Skin Thickness","Insulin Level","BMI",
        "Diabetes Pedigree Function","Age"
    ]

    inputs = [st.text_input(label) for label in labels]

    if st.button("Predict"):
        output = diabetes_prediction(inputs)

        st.success(f"### 🔍 Result: **{output}**")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
