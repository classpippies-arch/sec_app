import numpy as np
import pickle
import streamlit as st
import os

# Load Model
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    pred = loaded_model.predict(input_data)
    return "The person is NOT diabetic" if pred[0] == 0 else "The person IS diabetic"


# ---------------- LIQUID GLASS UI CSS --------------------
def load_css():
    st.markdown("""
    <style>

    /* Global */
    .stApp {
        background: #0f0f0f;
        font-family: 'Inter', sans-serif;
        overflow: hidden;
    }

    /* TOP NAVBAR */
    .top-nav {
        width: 100%;
        padding: 18px 25px;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255,255,255,0.1);
        position: fixed;
        top: 0;
        z-index: 10;
        font-size: 20px;
        font-weight: 700;
        color: white;
        display: flex;
        justify-content: space-between;
    }

    /* LEFT SIDEBAR */
    .side-menu {
        position: fixed;
        top: 70px;
        left: 0;
        width: 80px;
        height: 100%;
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(18px);
        border-right: 1px solid rgba(255,255,255,0.1);
        padding-top: 40px;
        text-align: center;
        color: white;
        font-size: 12px;
    }

    /* LIQUID BLOB BACKGROUND */
    .blob {
        position: fixed;
        top: -200px;
        right: -150px;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle at 30% 30%, #ff7a1a55, #ff7a1a22, transparent);
        filter: blur(100px);
        border-radius: 50%;
        animation: moveBlob 13s ease-in-out infinite;
        z-index: -1;
    }

    @keyframes moveBlob {
        0% { transform: translate(0,0) scale(1); }
        50% { transform: translate(-150px,100px) scale(1.4); }
        100% { transform: translate(0,0) scale(1); }
    }

    /* CENTER GLASS CARD */
    .card {
        margin: 140px auto;
        width: 60%;
        padding: 40px;
        border-radius: 25px;
        background: rgba(255, 255, 255, 0.11);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 12px 35px rgba(0,0,0,0.45);
        animation: fadeUp 0.7s ease;
    }

    @keyframes fadeUp {
        0% {opacity: 0; transform: translateY(30px);}
        100% {opacity: 1; transform: translateY(0);}
    }

    /* Title */
    .card-title {
        font-size: 33px;
        font-weight: 800;
        background: linear-gradient(90deg, #ff7a1a, #ffb06b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 25px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #ff7a1a, #ff9c42);
        border: none;
        color: white;
        font-size: 18px;
        padding: 12px;
        border-radius: 14px;
        width: 100%;
        transition: 0.25s;
    }
    .stButton > button:hover {
        transform: scale(1.04);
        box-shadow: 0px 8px 20px #ff7a1a55;
    }

    </style>

    <div class="top-nav">
        <div>Afterwork CRM — Dashboard</div>
        <div>⚡ Powered by AI</div>
    </div>

    <div class="side-menu">
        🏠<br><br>
        📊<br><br>
        🧪<br><br>
        ⚙️
    </div>

    <div class="blob"></div>

    """, unsafe_allow_html=True)



# ------------------ MAIN ---------------------
def main():
    load_css()

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<div class='card-title'>🩺 Diabetes Prediction</div>", unsafe_allow_html=True)

    labels = [
        "Number of Pregnancies","Glucose Level","Blood Pressure",
        "Skin Thickness","Insulin Level","BMI",
        "Diabetes Pedigree Function","Age"
    ]

    inputs = [st.text_input(label) for label in labels]

    if st.button("Predict"):
        result = diabetes_prediction(inputs)
        st.success(f"### ✔ Result: {result}")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
