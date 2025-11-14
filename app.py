import numpy as np
import pickle
import streamlit as st
import os

# --------- Load Model ---------
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    try:
        arr = np.asarray([float(x) for x in input_data]).reshape(1, -1)
    except:
        st.error("Enter valid numeric values only.")
        return None
    pred = loaded_model.predict(arr)
    return "NOT diabetic" if pred[0] == 0 else "IS diabetic"


# ---------- PREMIUM LIQUID WHITE UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* FULL WHITE CLEAN BACKGROUND */
    .stApp {
        background: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }

    /* TOP NAVBAR (APPLE STYLE) */
    .top-nav {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.75);
        backdrop-filter: blur(18px);
        padding: 18px 26px;
        border-bottom: 1px solid rgba(0,0,0,0.06);
        z-index: 100;
        display: flex;
        justify-content: space-between;
        font-weight: 700;
        color: #111;
    }

    /* LEFT BANK SIDEBAR – FIXED */
    .sidebar {
        position: fixed;
        top: 75px;
        left: 0;
        width: 80px;
        height: calc(100% - 80px);
        background: rgba(255,255,255,0.55);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(0,0,0,0.08);
        padding-top: 35px;
        text-align: center;
        z-index: 90;
        border-radius: 0 16px 16px 0;
        box-shadow: 4px 0 20px rgba(0,0,0,0.05);
        font-size: 22px;
    }

    .sidebar div { margin: 28px 0; }

    /* LIQUID BLOB INSIDE MAIN CARD */
    .liquid {
        position: absolute;
        top: -60px;
        left: -40px;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, #ffefe2bb, #fff4ecc2, transparent);
        filter: blur(55px);
        border-radius: 50%;
        animation: float 10s infinite ease-in-out;
        z-index: 1;
    }
    @keyframes float {
        0% { transform: translate(0,0) scale(1); }
        50% { transform: translate(40px,20px) scale(1.1); }
        100% { transform: translate(0,0) scale(1); }
    }

    /* PURE LIQUID GLASS CARD */
    .card {
        margin: 130px auto;
        margin-left: 120px;
        width: 65%;
        background: rgba(255,255,255,0.55);
        backdrop-filter: blur(22px);
        border-radius: 24px;
        padding: 40px;
        border: 1px solid rgba(0,0,0,0.08);
        box-shadow: 0 10px 35px rgba(0,0,0,0.06);
        position: relative;
        overflow: hidden;
    }

    /* FIR TAX LABEL INSIDE CARD */
    .fir-badge {
        position: relative;
        z-index: 2;
        padding: 6px 14px;
        background: #ffefe2;
        color: #b45309;
        border-radius: 10px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 18px;
        border: 1px solid #fcd9b6;
    }

    .card-title {
        font-size: 30px;
        font-weight: 800;
        z-index: 2; position: relative;
        color: #111;
        margin-bottom: 12px;
    }

    .sub {
        color: #666;
        margin-bottom: 20px;
        z-index: 2; position: relative;
    }

    /* FORM GRID */
    .grid {
        display: grid;
        grid-template-columns: repeat(2,1fr);
        gap: 16px 22px;
        z-index: 2;
        position: relative;
        margin-bottom: 20px;
    }

    /* BUTTON */
    .stButton > button {
        background: linear-gradient(90deg, #ff7a1a, #ff9c42);
        padding: 13px;
        width: 100%;
        border-radius: 12px;
        color: white;
        font-weight: 700;
        border: none;
        box-shadow: 0 10px 25px rgba(255,122,26,0.18);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* FOOTER */
    .footer {
        text-align: center;
        margin-top: 28px;
        color: #777;
        font-size: 14px;
    }

    @media(max-width:900px){
        .card { width: 90%; margin-left: 0; }
        .grid { grid-template-columns: 1fr; }
    }

    </style>

    <div class="top-nav">
        <div>Premium CRM Dashboard</div>
        <div>Liquid Glass UI</div>
    </div>

    <div class="sidebar">
        <div>🏦</div>
        <div>📊</div>
        <div>🧾</div>
        <div>⚙️</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Main ----------
def main():
    load_css()

    # MAIN CARD
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Liquid blob inside card
    st.markdown('<div class="liquid"></div>', unsafe_allow_html=True)

    # FIR TAX badge inside the box
    st.markdown('<div class="fir-badge">FIR TAX — Details</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-title">🩺 Diabetes Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Enter patient details below</div>', unsafe_allow_html=True)

    st.markdown('<div class="grid">', unsafe_allow_html=True)
    p = st.text_input("Pregnancies")
    g = st.text_input("Glucose Level")
    bp = st.text_input("Blood Pressure")
    stn = st.text_input("Skin Thickness")
    ins = st.text_input("Insulin Level")
    bmi = st.text_input("BMI")
    dpf = st.text_input("Diabetes Pedigree Function")
    age = st.text_input("Age")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Predict"):
        result = diabetes_prediction([p,g,bp,stn,ins,bmi,dpf,age])
        if result:
            st.success(f"Result: Person is {result}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer">Developed by <b>Kartvaya Raikwar</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
