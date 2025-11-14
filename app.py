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


# ---------- BOX-STYLE UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* CLEAN BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }

    /* HEADER */
    .box-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(20px);
        padding: 20px 30px;
        border-bottom: 1px solid rgba(0,0,0,0.1);
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        color: #1a73e8;
        box-shadow: 0 2px 20px rgba(0,0,0,0.1);
    }

    /* SIDEBAR */
    .box-sidebar {
        position: fixed;
        top: 80px;
        left: 0;
        width: 70px;
        height: calc(100% - 80px);
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(0,0,0,0.1);
        padding-top: 30px;
        text-align: center;
        z-index: 90;
        border-radius: 0 16px 16px 0;
        box-shadow: 3px 0 15px rgba(0,0,0,0.08);
    }

    .box-sidebar div { 
        margin: 25px 0; 
        font-size: 20px;
        opacity: 0.7;
        transition: opacity 0.3s;
    }
    
    .box-sidebar div:hover { 
        opacity: 1;
        transform: scale(1.1);
    }

    /* MAIN CARD */
    .box-card {
        margin: 120px auto;
        margin-left: 100px;
        width: 70%;
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(0,0,0,0.1);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        position: relative;
        overflow: hidden;
    }

    /* BADGE */
    .box-badge {
        position: relative;
        z-index: 2;
        padding: 8px 16px;
        background: linear-gradient(135deg, #1a73e8, #4285f4);
        color: white;
        border-radius: 12px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 20px;
        font-size: 14px;
        box-shadow: 0 4px 15px rgba(26,115,232,0.2);
    }

    .box-title {
        font-size: 32px;
        font-weight: 800;
        z-index: 2; 
        position: relative;
        color: #1a237e;
        margin-bottom: 8px;
    }

    .box-sub {
        color: #5f6368;
        margin-bottom: 30px;
        z-index: 2; 
        position: relative;
        font-size: 16px;
        line-height: 1.5;
    }

    /* FORM GRID WITH BOX STYLING */
    .box-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px 25px;
        z-index: 2;
        position: relative;
        margin-bottom: 25px;
    }

    /* ENHANCED BOX-STYLE INPUTS */
    .stTextInput > div > div {
        background: white !important;
        border: 2.5px solid #1a73e8 !important;
        border-radius: 12px !important;
        padding: 4px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(26,115,232,0.15) !important;
    }

    /* DIFFERENT BORDER COLORS FOR EACH INPUT */
    .stTextInput:nth-child(1) > div > div { border-color: #1a73e8 !important; }
    .stTextInput:nth-child(2) > div > div { border-color: #34a853 !important; }
    .stTextInput:nth-child(3) > div > div { border-color: #ea4335 !important; }
    .stTextInput:nth-child(4) > div > div { border-color: #fbbc05 !important; }
    .stTextInput:nth-child(5) > div > div { border-color: #4285f4 !important; }
    .stTextInput:nth-child(6) > div > div { border-color: #8e44ad !important; }
    .stTextInput:nth-child(7) > div > div { border-color: #e74c3c !important; }
    .stTextInput:nth-child(8) > div > div { border-color: #2ecc71 !important; }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        color: #333 !important;
    }
    
    .stTextInput > div > div > input:focus {
        outline: none !important;
        box-shadow: none !important;
        background: rgba(26,115,232,0.05) !important;
    }

    /* INPUT LABELS */
    .stTextInput label {
        font-weight: 600 !important;
        color: #1a237e !important;
        margin-bottom: 8px !important;
        font-size: 14px !important;
    }

    /* BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, #1a73e8, #4285f4);
        padding: 14px 28px;
        width: 100%;
        border-radius: 12px;
        color: white;
        font-weight: 600;
        border: none;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(26,115,232,0.25);
        margin-top: 10px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(26,115,232,0.35);
        background: linear-gradient(135deg, #1669d6, #3367d6);
    }

    /* SUCCESS MESSAGE */
    .stSuccess {
        background: linear-gradient(135deg, #34a853, #4caf50);
        color: white;
        border-radius: 12px;
        padding: 20px;
        border: none;
        font-weight: 600;
        text-align: center;
        margin-top: 20px;
    }

    /* FOOTER */
    .box-footer {
        text-align: center;
        margin-top: 35px;
        color: #5f6368;
        font-size: 14px;
        position: relative;
        z-index: 2;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
        .box-card { 
            width: 85%; 
            margin-left: 80px; 
        }
        .box-grid { 
            grid-template-columns: 1fr; 
        }
    }
    
    @media (max-width: 768px) {
        .box-card { 
            width: 90%; 
            margin-left: 20px;
            margin-right: 20px;
        }
        .box-sidebar {
            display: none;
        }
    }

    </style>

    <div class="box-header">
        <div>🏥 Diabetes Prediction Web App</div>
        <div>Medical Diagnostic Tool</div>
    </div>

    <div class="box-sidebar">
        <div>🩺</div>
        <div>📊</div>
        <div>📈</div>
        <div>⚕️</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Main ----------
def main():
    load_css()

    # MAIN CARD
    st.markdown('<div class="box-card">', unsafe_allow_html=True)

    # Badge
    st.markdown('<div class="box-badge">AI DIAGNOSTIC TOOL</div>', unsafe_allow_html=True)

    st.markdown('<div class="box-title">Diabetes Prediction Web App</div>', unsafe_allow_html=True)
    st.markdown('<div class="box-sub">Enter patient clinical parameters for diabetes risk assessment</div>', unsafe_allow_html=True)

    st.markdown('<div class="box-grid">', unsafe_allow_html=True)
    
    # Column 1 - Each input has different colored border
    p = st.text_input("Number of Pregnancies", placeholder="e.g., 2")
    g = st.text_input("Glucose Level", placeholder="mg/dL")
    bp = st.text_input("Blood Pressure value", placeholder="mmHg")
    stn = st.text_input("Skin Thickness value", placeholder="mm")
    
    # Column 2 - Each input has different colored border  
    ins = st.text_input("Insulin Level", placeholder="μU/mL")
    bmi = st.text_input("BMI value", placeholder="Body Mass Index")
    dpf = st.text_input("Diabetes Pedigree Function value", placeholder="0.00 - 2.00")
    age = st.text_input("Age of the Person", placeholder="Years")
    
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Predict"):
        if all([p, g, bp, stn, ins, bmi, dpf, age]):
            result = diabetes_prediction([p, g, bp, stn, ins, bmi, dpf, age])
            if result:
                st.success(f"**Diabetes Test Result**\n\nThe person is {result.lower()}")
        else:
            st.warning("Please fill in all fields before prediction.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="box-footer">Developed by <b>Kartvaya Raikwar</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
