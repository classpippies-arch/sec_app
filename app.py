import numpy as np
import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    pred = loaded_model.predict(input_data)
    return "The person is NOT diabetic" if pred[0] == 0 else "The person IS diabetic"


# --------------- LIQUID GLASS CSS ----------------
def load_css():
    st.markdown("""
    <style>

    /* PAGE BACKGROUND */
    .stApp {
        background: #0f0f0f;
        overflow: hidden;
        position: relative;
        font-family: 'Inter', sans-serif;
    }

    /* LIQUID BLOB ANIMATION */
    .liquid-bg {
        position: fixed;
        top: -200px;
        left: -200px;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle at 30% 30%, #ff7a1a55, #ff7a1a22, transparent);
        filter: blur(80px);
        animation: blobMove 12s infinite ease-in-out;
        z-index: -1;
        border-radius: 50%;
    }

    @keyframes blobMove {
        0%   { transform: translate(0px, 0px) scale(1); }
        50%  { transform: translate(200px, 120px) scale(1.3); }
        100% { transform: translate(0px, 0px) scale(1); }
    }

    /* GLASS CARD */
    .glass-card {
        backdrop-filter: blur(20px) saturate(180%);
        background: rgba(255, 255, 255, 0.12);
        border-radius: 25px;
        padding: 35px;
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 10px 35px rgba(0,0,0,0.4);
        margin-top: 20px;
        animation: fadeInUp 0.9s ease;
    }

    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* TITLE */
    .title {
        font-size: 38px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #ff7a1a, #ffaa56);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }

    /* BUTTON */
    .stButton > button {
        background: linear-gradient(90deg, #ff7a1a, #ff9c42);
        border-radius: 12px;
        padding: 10px 25px;
        font-size: 18px;
        color: white;
        border: none;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px #ff7a1a55;
    }

    </style>

    <div class="liquid-bg"></div>

    """, unsafe_allow_html=True)



# ------------------ MAIN APP ---------------------
def main():
    load_css()

    st.markdown("<div class='title'>🩺 Diabetes Prediction</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    inputs = [
        st.text_input("Number of Pregnancies"),
        st.text_input("Glucose Level"),
        st.text_input("Blood Pressure"),
        st.text_input("Skin Thickness"),
        st.text_input("Insulin Level"),
        st.text_input("BMI"),
        st.text_input("Diabetes Pedigree Function"),
        st.text_input("Age")
    ]

    if st.button("Predict"):
        result = diabetes_prediction(inputs)
        st.success(f"### Result: {result}")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
