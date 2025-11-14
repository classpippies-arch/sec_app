import numpy as np
import pickle
import streamlit as st
import os

# -------- Load model ----------
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    # convert inputs to floats safely
    try:
        arr = np.asarray([float(x) for x in input_data], dtype=float).reshape(1, -1)
    except Exception:
        # if conversion fails, raise a friendly error (Streamlit will show it)
        st.error("Please enter valid numeric values for all fields.")
        return None
    pred = loaded_model.predict(arr)
    return "NOT diabetic" if pred[0] == 0 else "IS diabetic"


# -------- CSS for premium white + liquid-glass ----------
def load_css():
    st.markdown(
        """
        <style>
        /* App background - premium white */
        .stApp {
            background: #ffffff;
            color: #111111;
            font-family: 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
            overflow-x: hidden;
        }

        /* Top navbar - subtle glass on white */
        .top-nav {
            width: 100%;
            padding: 16px 28px;
            background: rgba(255,255,255,0.85);
            border-bottom: 1px solid rgba(17,17,17,0.06);
            position: fixed;
            top: 0;
            z-index: 12;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 6px 18px rgba(17,17,17,0.04);
        }
        .top-nav .brand { font-weight: 800; font-size: 18px; color: #0f1724; }
        .top-nav .tag { font-size: 13px; color: #6b7280; }

        /* Left sidebar (Bank section) - DO NOTHING to change visuals */
        .side-menu {
            position: fixed;
            top: 72px;
            left: 16px;
            width: 72px;
            height: calc(100% - 88px);
            background: rgba(17,24,39,0.02); /* very subtle on white */
            border-right: 1px solid rgba(17,17,17,0.02);
            padding-top: 24px;
            text-align: center;
            color: #111827;
            font-size: 13px;
            z-index: 10;
            border-radius: 12px;
        }

        /* Soft pastel liquid blob (very subtle on white) */
        .blob {
            position: fixed;
            right: -120px;
            top: -140px;
            width: 520px;
            height: 520px;
            background: radial-gradient(circle at 30% 30%, #ffedd5aa, #fff7ed66, transparent);
            filter: blur(80px);
            border-radius: 50%;
            animation: blobMove 14s ease-in-out infinite;
            z-index: -1;
        }
        @keyframes blobMove {
            0% { transform: translate(0,0) scale(1); }
            50% { transform: translate(-90px,100px) scale(1.08); }
            100% { transform: translate(0,0) scale(1); }
        }

        /* Main card container - premium glass on white */
        .card {
            margin: 120px auto;
            width: 820px;
            max-width: calc(100% - 64px);
            padding: 34px;
            border-radius: 18px;
            background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.92));
            box-shadow: 0 12px 40px rgba(15,23,36,0.06);
            border: 1px solid rgba(17,24,39,0.04);
        }

        /* FIR Tax badge above the card */
        .fir-badge {
            width: 820px;
            max-width: calc(100% - 64px);
            margin: 72px auto 6px;
            padding: 6px 12px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255,126,54,0.08);
            color: #b45309;
            font-weight: 700;
            font-size: 14px;
            border: 1px solid rgba(249,115,22,0.10);
            box-shadow: 0 6px 18px rgba(249,115,22,0.03);
        }

        /* Title inside card */
        .card-title {
            font-size: 28px;
            font-weight: 800;
            color: #0f1724;
            margin-bottom: 8px;
        }
        .card-sub {
            color: #6b7280;
            margin-bottom: 20px;
        }

        /* Inputs layout: create two-column grid */
        .inputs-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px 18px;
            margin-bottom: 18px;
        }

        /* Full width predict button */
        .stButton > button {
            background: linear-gradient(90deg,#ff7a1a,#ff9c42);
            color: #ffffff;
            border: none;
            padding: 12px 16px;
            border-radius: 12px;
            width: 100%;
            font-weight: 700;
            font-size: 15px;
            box-shadow: 0 10px 30px rgba(255,122,26,0.12);
        }
        .stButton > button:hover { transform: translateY(-2px); }

        /* Result styling (success) */
        .stSuccess, .stAlert { margin-top: 12px; }

        /* Make sure Streamlit default containers don't show an extra box below */
        .block-container { padding-top: 92px; }

        /* Responsive tweaks */
        @media (max-width: 880px) {
            .inputs-grid { grid-template-columns: 1fr; }
            .fir-badge, .card { margin-left: 20px; margin-right: 20px; width: auto; }
        }
        </style>

        <div class="top-nav">
            <div class="brand">Afterwork CRM — Dashboard</div>
            <div class="tag">Premium • Clean • White</div>
        </div>

        <!-- Left sidebar (Bank section) - unchanged -->
        <div class="side-menu">
            <div style="margin-top:8px;">🏦</div>
            <div style="margin-top:28px;">📊</div>
            <div style="margin-top:28px;">🧾</div>
            <div style="margin-top:28px;">⚙️</div>
        </div>

        <div class="blob"></div>
        """,
        unsafe_allow_html=True,
    )


# -------- Main app ----------
def main():
    load_css()

    # FIR Tax badge placed above the main card (as requested)
    st.markdown('<div class="fir-badge">FIR Tax • Apply/Check Here</div>', unsafe_allow_html=True)

    # Main card
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="card-title">🩺 Diabetes Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-sub">Enter patient metrics below — premium & minimal UI</div>', unsafe_allow_html=True)

    # Create inputs in a neat two-column grid
    st.markdown('<div class="inputs-grid">', unsafe_allow_html=True)
    p = st.text_input("Number of Pregnancies")
    g = st.text_input("Glucose Level")
    bp = st.text_input("Blood Pressure")
    stn = st.text_input("Skin Thickness")
    ins = st.text_input("Insulin Level")
    bmi = st.text_input("BMI")
    dpf = st.text_input("Diabetes Pedigree Function")
    age = st.text_input("Age")
    st.markdown('</div>', unsafe_allow_html=True)

    # Single Predict button (no extra boxes below)
    if st.button("Predict"):
        inputs = [p, g, bp, stn, ins, bmi, dpf, age]
        result = diabetes_prediction(inputs)
        if result is not None:
            if "NOT" in result:
                st.success(f"✔ Result: The person is {result}")
            else:
                st.error(f"✖ Result: The person {result}")

    st.markdown('</div>', unsafe_allow_html=True)  # close card


if __name__ == "__main__":
    main()
