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


# ---------- MEDICAL PROFESSIONAL UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* CLEAN MEDICAL THEME BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }

    /* PROFESSIONAL HEADER */
    .medical-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(20px);
        padding: 20px 30px;
        border-bottom: 1px solid rgba(0,0,0,0.08);
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        color: #1a73e8;
        box-shadow: 0 2px 20px rgba(0,0,0,0.08);
    }

    /* MEDICAL SIDEBAR */
    .medical-sidebar {
        position: fixed;
        top: 80px;
        left: 0;
        width: 70px;
        height: calc(100% - 80px);
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(0,0,0,0.06);
        padding-top: 30px;
        text-align: center;
        z-index: 90;
        border-radius: 0 16px 16px 0;
        box-shadow: 3px 0 15px rgba(0,0,0,0.04);
    }

    .medical-sidebar div { 
        margin: 25px 0; 
        font-size: 20px;
        opacity: 0.7;
        transition: opacity 0.3s;
    }
    
    .medical-sidebar div:hover { 
        opacity: 1;
        transform: scale(1.1);
    }

    /* MEDICAL GRADIENT BLOB */
    .medical-blob {
        position: absolute;
        top: -80px;
        right: -60px;
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, #e3f2fd 0%, #bbdefb 50%, transparent 70%);
        filter: blur(40px);
        border-radius: 50%;
        animation: float 8s infinite ease-in-out;
        z-index: 1;
    }
    
    @keyframes float {
        0% { transform: translate(0,0) scale(1); }
        50% { transform: translate(-20px,15px) scale(1.05); }
        100% { transform: translate(0,0) scale(1); }
    }

    /* PROFESSIONAL MEDICAL CARD */
    .medical-card {
        margin: 120px auto;
        margin-left: 100px;
        width: 70%;
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(25px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }

    /* MEDICAL BADGE */
    .medical-badge {
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

    .card-title {
        font-size: 32px;
        font-weight: 800;
        z-index: 2; 
        position: relative;
        color: #1a237e;
        margin-bottom: 8px;
        background: linear-gradient(135deg, #1a237e, #283593);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .sub {
        color: #5f6368;
        margin-bottom: 30px;
        z-index: 2; 
        position: relative;
        font-size: 16px;
        line-height: 1.5;
    }

    /* FORM GRID */
    .medical-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px 25px;
        z-index: 2;
        position: relative;
        margin-bottom: 25px;
    }

    /* ENHANCED INPUT STYLING */
    .stTextInput > div > div > input {
        background: rgba(248, 249, 250, 0.8);
        border: 1.5px solid #e0e0e0;
        border-radius: 12px;
        padding: 12px 16px;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1a73e8;
        box-shadow: 0 0 0 2px rgba(26,115,232,0.1);
        background: white;
    }

    /* MEDICAL BUTTON */
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
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(26,115,232,0.35);
        background: linear-gradient(135deg, #1669d6, #3367d6);
    }

    /* SUCCESS MESSAGE STYLING */
    .stSuccess {
        background: linear-gradient(135deg, #34a853, #4caf50);
        color: white;
        border-radius: 12px;
        padding: 20px;
        border: none;
        font-weight: 600;
    }

    /* FOOTER */
    .medical-footer {
        text-align: center;
        margin-top: 35px;
        color: #5f6368;
        font-size: 14px;
        position: relative;
        z-index: 2;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
        .medical-card { 
            width: 85%; 
            margin-left: 80px; 
        }
        .medical-grid { 
            grid-template-columns: 1fr; 
        }
    }
    
    @media (max-width: 768px) {
        .medical-card { 
            width: 90%; 
            margin-left: 20px;
            margin-right: 20px;
        }
        .medical-sidebar {
            display: none;
        }
    }

    </style>

    <div class="medical-header">
        <div>🏥 Diabetes Diagnostic Assistant</div>
        <div>Medical Intelligence Platform</div>
    </div>

    <div class="medical-sidebar">
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
    st.markdown('<div class="medical-card">', unsafe_allow_html=True)

    # Medical gradient blob
    st.markdown('<div class="medical-blob"></div>', unsafe_allow_html=True)

    # Professional medical badge
    st.markdown('<div class="medical-badge">AI DIAGNOSTIC TOOL</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-title">Diabetes Risk Assessment</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Enter patient clinical parameters for AI-powered diabetes risk prediction</div>', unsafe_allow_html=True)

    st.markdown('<div class="medical-grid">', unsafe_allow_html=True)
    
    # Column 1
    p = st.text_input("Pregnancies", placeholder="e.g., 2")
    g = st.text_input("Glucose Level (mg/dL)", placeholder="e.g., 120")
    bp = st.text_input("Blood Pressure (mmHg)", placeholder="e.g., 80")
    stn = st.text_input("Skin Thickness (mm)", placeholder="e.g., 25")
    
    # Column 2  
    ins = st.text_input("Insulin Level (μU/mL)", placeholder="e.g., 80")
    bmi = st.text_input("BMI", placeholder="e.g., 25.5")
    dpf = st.text_input("Diabetes Pedigree Function", placeholder="e.g., 0.5")
    age = st.text_input("Age (years)", placeholder="e.g., 35")
    
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔍 Analyze Diabetes Risk"):
        if all([p, g, bp, stn, ins, bmi, dpf, age]):
            result = diabetes_prediction([p, g, bp, stn, ins, bmi, dpf, age])
            if result:
                st.success(f"**Analysis Result:** Patient {result}")
        else:
            st.warning("Please fill in all fields before analysis.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="medical-footer">Developed by <b>Medical AI Research Team</b> | Secure & Confidential</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
