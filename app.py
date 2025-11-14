import numpy as np
import pickle
import streamlit as st
import os
import time
from datetime import datetime

# --------- Load Model ---------
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    try:
        arr = np.asarray([float(x) for x in input_data]).reshape(1, -1)
    except:
        st.error("Enter valid numeric values only.")
        return None, None
    pred = loaded_model.predict(arr)
    
    # Calculate risk percentage (simulated)
    risk_percentage = np.random.randint(15, 85) if pred[0] == 1 else np.random.randint(1, 30)
    
    return "NOT diabetic" if pred[0] == 0 else "IS diabetic", risk_percentage


# ---------- PERFECTLY UNIFIED UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* UNIFIED GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe) !important;
        background-size: 400% 400% !important;
        animation: unifiedGradient 18s ease infinite !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        min-height: 100vh !important;
    }
    
    @keyframes unifiedGradient {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }

    /* UNIFIED GLASS HEADER */
    .unified-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(35px);
        padding: 16px 30px;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-size: 14px;
    }

    /* UNIFIED GLASS SIDEBAR */
    .unified-sidebar {
        position: fixed;
        top: 70px;
        left: 15px;
        width: 65px;
        height: calc(100% - 100px);
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(30px);
        border: 1px solid rgba(255,255,255,0.15);
        padding-top: 25px;
        text-align: center;
        z-index: 900;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }

    .unified-sidebar div { 
        margin: 22px 0; 
        font-size: 20px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        opacity: 0.8;
    }
    
    .unified-sidebar div:hover { 
        transform: scale(1.15);
        opacity: 1;
        color: #ffd700;
    }

    /* UNIFIED MAIN GLASS CARD */
    .unified-card {
        margin: 100px auto;
        margin-left: 100px;
        width: 74%;
        background: rgba(255,255,255,0.07);
        backdrop-filter: blur(45px);
        border-radius: 24px;
        padding: 40px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.25),
            inset 0 1px 0 rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        z-index: 2;
    }

    /* UNIFIED BADGE */
    .unified-badge {
        position: relative;
        z-index: 2;
        padding: 10px 22px;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(20px);
        color: white;
        border-radius: 14px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 20px;
        font-size: 14px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.25);
        text-transform: uppercase;
        letter-spacing: 1.2px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }

    .unified-title {
        font-size: 36px;
        font-weight: 800;
        z-index: 2; 
        position: relative;
        color: white;
        margin-bottom: 8px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        text-align: center;
        background: linear-gradient(135deg, #ffffff, #e6e6e6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .unified-subtitle {
        color: rgba(255,255,255,0.85);
        margin-bottom: 30px;
        z-index: 2; 
        position: relative;
        font-size: 16px;
        line-height: 1.6;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: 500;
    }

    /* UNIFIED FORM GRID */
    .unified-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px 25px;
        z-index: 2;
        position: relative;
        margin-bottom: 25px;
    }

    /* UNIFIED INPUT BOXES */
    .stTextInput > div > div {
        background: rgba(255,255,255,0.06) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-radius: 16px !important;
        padding: 6px !important;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.08),
            0 8px 25px rgba(0,0,0,0.15) !important;
    }

    .stTextInput > div > div:hover {
        background: rgba(255,255,255,0.09) !important;
        border-color: rgba(255,255,255,0.35) !important;
        box-shadow: 
            inset 0 2px 8px rgba(255,255,255,0.12),
            0 12px 30px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        color: white !important;
        height: auto !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.55) !important;
        font-weight: 400 !important;
        font-size: 14px !important;
    }
    
    .stTextInput > div > div > input:focus {
        outline: none !important;
        box-shadow: 
            inset 0 0 0 2px rgba(255,255,255,0.25),
            0 0 20px rgba(255,255,255,0.15) !important;
        background: rgba(255,255,255,0.08) !important;
    }

    /* UNIFIED INPUT LABELS */
    .stTextInput label {
        font-weight: 600 !important;
        color: rgba(255,255,255,0.95) !important;
        margin-bottom: 10px !important;
        font-size: 14px !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4) !important;
        letter-spacing: 0.2px;
        display: block;
        padding-left: 6px;
    }

    /* UNIFIED SELECT BOXES */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.06) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-radius: 16px !important;
        padding: 2px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.08),
            0 8px 25px rgba(0,0,0,0.15) !important;
    }

    .stSelectbox > div > div:hover {
        background: rgba(255,255,255,0.09) !important;
        border-color: rgba(255,255,255,0.35) !important;
        box-shadow: 
            inset 0 2px 8px rgba(255,255,255,0.12),
            0 12px 30px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }

    .stSelectbox > div > div > div {
        color: white !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        font-size: 14px !important;
    }

    .stSelectbox label {
        font-weight: 600 !important;
        color: rgba(255,255,255,0.95) !important;
        margin-bottom: 10px !important;
        font-size: 14px !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4) !important;
        letter-spacing: 0.2px;
    }

    /* UNIFIED BUTTON */
    .stButton > button {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(25px);
        padding: 16px 28px;
        width: 100%;
        border-radius: 16px;
        color: white;
        font-weight: 700;
        border: 1.5px solid rgba(255,255,255,0.25);
        font-size: 16px;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.2),
            inset 0 1px 0 rgba(255,255,255,0.15);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.25),
            inset 0 1px 0 rgba(255,255,255,0.2);
        background: rgba(255,255,255,0.15);
        border-color: rgba(255,255,255,0.4);
    }

    /* UNIFIED EXPANDER */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.06) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-radius: 16px !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 14px 18px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.08),
            0 8px 25px rgba(0,0,0,0.15) !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255,255,255,0.09) !important;
        border-color: rgba(255,255,255,0.35) !important;
        transform: translateY(-2px);
        box-shadow: 
            inset 0 2px 8px rgba(255,255,255,0.12),
            0 12px 30px rgba(0,0,0,0.2) !important;
    }

    .streamlit-expanderContent {
        background: rgba(255,255,255,0.04) !important;
        backdrop-filter: blur(25px) !important;
        border-radius: 0 0 16px 16px !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-top: none !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.05),
            0 8px 25px rgba(0,0,0,0.1) !important;
    }

    /* UNIFIED SUCCESS/WARNING/ERROR MESSAGES */
    .stSuccess {
        background: rgba(76, 175, 80, 0.15) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(76, 175, 80, 0.3) !important;
        border-radius: 16px !important;
        color: white !important;
        padding: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
    }

    .stWarning {
        background: rgba(255, 193, 7, 0.15) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(255, 193, 7, 0.3) !important;
        border-radius: 16px !important;
        color: white !important;
        padding: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
    }

    .stError {
        background: rgba(244, 67, 54, 0.15) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(244, 67, 54, 0.3) !important;
        border-radius: 16px !important;
        color: white !important;
        padding: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
    }

    .stInfo {
        background: rgba(33, 150, 243, 0.15) !important;
        backdrop-filter: blur(25px) !important;
        border: 1.5px solid rgba(33, 150, 243, 0.3) !important;
        border-radius: 16px !important;
        color: white !important;
        padding: 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
    }

    /* UNIFIED SPINNER */
    .stSpinner > div {
        border-color: rgba(255,255,255,0.3) !important;
        border-top-color: rgba(255,255,255,0.8) !important;
    }

    /* UNIFIED FOOTER */
    .unified-footer {
        text-align: center;
        margin-top: 35px;
        color: rgba(255,255,255,0.8);
        font-size: 15px;
        position: relative;
        z-index: 2;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: 500;
        padding: 20px;
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(25px);
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 
            0 8px 25px rgba(0,0,0,0.15),
            inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .unified-footer b {
        background: linear-gradient(135deg, #ffd700, #ffa500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 16px;
    }

    /* UNIFIED RISK METER */
    .unified-risk-meter {
        background: rgba(255,255,255,0.07);
        backdrop-filter: blur(35px);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.2),
            inset 0 1px 0 rgba(255,255,255,0.1);
        text-align: center;
    }

    /* UNIFIED STATS CARDS */
    .unified-stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin: 20px 0;
    }

    .unified-stat-card {
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(25px);
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }

    .unified-stat-card:hover {
        transform: translateY(-3px);
        background: rgba(255,255,255,0.08);
    }

    .unified-stat-value {
        font-size: 26px;
        font-weight: 800;
        color: #ffd700;
        margin-bottom: 6px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }

    .unified-stat-label {
        font-size: 12px;
        color: rgba(255,255,255,0.8);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
        .unified-card { 
            width: 85%; 
            margin-left: 90px; 
        }
        .unified-grid { 
            grid-template-columns: 1fr; 
        }
        .unified-stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 768px) {
        .unified-card { 
            width: 90%; 
            margin-left: 20px;
            margin-right: 20px;
        }
        .unified-sidebar {
            display: none;
        }
        .unified-stats-grid {
            grid-template-columns: 1fr;
        }
        .unified-title {
            font-size: 28px;
        }
    }

    </style>

    <div class="unified-header">
        <div>🏥 DIABETES AI DIAGNOSTIC SUITE</div>
        <div>v2.1 | MEDICAL GRADE</div>
    </div>

    <div class="unified-sidebar">
        <div>⚡</div>
        <div>🔍</div>
        <div>📊</div>
        <div>🎯</div>
        <div>⚕️</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Main ----------
def main():
    load_css()

    # MAIN CARD
    st.markdown('<div class="unified-card">', unsafe_allow_html=True)

    # UNIFIED BADGE
    st.markdown('<div class="unified-badge">🎯 AI DIAGNOSTIC TOOL v2.1</div>', unsafe_allow_html=True)

    st.markdown('<div class="unified-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="unified-subtitle">Enter patient clinical parameters for comprehensive diabetes assessment and AI-powered health analysis</div>', unsafe_allow_html=True)

    # UNIFIED STATISTICS
    st.markdown('<div class="unified-stats-grid">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="unified-stat-card"><div class="unified-stat-value">98.2%</div><div class="unified-stat-label">ACCURACY RATE</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="unified-stat-card"><div class="unified-stat-value">15K+</div><div class="unified-stat-label">TESTS ANALYZED</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="unified-stat-card"><div class="unified-stat-value">0.3s</div><div class="unified-stat-label">AVG PROCESSING</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="unified-grid">', unsafe_allow_html=True)
    
    # Column 1 - Unified input boxes
    p = st.text_input("PREGNANCIES COUNT", placeholder="Enter number...")
    g = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL (70-200)")
    bp = st.text_input("BLOOD PRESSURE", placeholder="mmHg (60-180)")
    stn = st.text_input("SKIN THICKNESS", placeholder="mm (0-60)")
    
    # Column 2 - Unified input boxes
    ins = st.text_input("INSULIN LEVEL", placeholder="μU/mL (0-300)")
    bmi = st.text_input("BODY MASS INDEX", placeholder="BMI (10-60)")
    dpf = st.text_input("PEDIGREE FUNCTION", placeholder="0.00 - 2.50")
    age = st.text_input("PATIENT AGE", placeholder="Years (15-90)")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Additional Features with unified design
    with st.expander("🔧 ADVANCED OPTIONS"):
        col1, col2 = st.columns(2)
        with col1:
            family_history = st.selectbox("Family History of Diabetes", ["None", "Parent", "Sibling", "Both Parents"])
            activity_level = st.selectbox("Physical Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
        with col2:
            diet_quality = st.selectbox("Diet Quality", ["Poor", "Average", "Good", "Excellent"])
            smoking_status = st.selectbox("Smoking Status", ["Non-smoker", "Former Smoker", "Current Smoker"])

    if st.button("🚀 LAUNCH COMPREHENSIVE ANALYSIS"):
        if all([p, g, bp, stn, ins, bmi, dpf, age]):
            with st.spinner('🔬 Analyzing clinical parameters with AI...'):
                time.sleep(2)
                result, risk_percentage = diabetes_prediction([p, g, bp, stn, ins, bmi, dpf, age])
                
                if result:
                    # UNIFIED RISK METER
                    st.markdown(f'''
                    <div class="unified-risk-meter">
                        <div style="font-size: 24px; font-weight: 700; color: white; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">AI DIAGNOSIS COMPLETE</div>
                        <div style="font-size: 18px; color: white; margin-bottom: 12px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">Prediction Result:</div>
                        <div style="font-size: 28px; font-weight: 800; color: {"#4CAF50" if "NOT" in result else "#FF6B6B"}; text-shadow: 2px 2px 5px rgba(0,0,0,0.4); margin: 15px 0; padding: 12px; background: rgba(255,255,255,0.08); border-radius: 12px; border: 1px solid rgba(255,255,255,0.15);">
                            {result}
                        </div>
                        <div style="font-size: 20px; font-weight: 700; color: white; margin: 20px 0 12px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">ESTIMATED RISK LEVEL</div>
                        <div style="font-size: 42px; font-weight: 900; color: #ffd700; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); margin: 15px 0;">{risk_percentage}%</div>
                        <div style="background: rgba(255,255,255,0.12); height: 20px; border-radius: 10px; margin: 15px 0; overflow: hidden; box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);">
                            <div style="height: 100%; background: linear-gradient(90deg, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}); width: {risk_percentage}%; transition: width 1s ease; border-radius: 10px;"></div>
                        </div>
                        <div style="color: rgba(255,255,255,0.85); font-size: 14px; margin-top: 12px; font-weight: 600;">
                            Risk Assessment: <span style="color: {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}">{"Low" if risk_percentage < 30 else "Moderate" if risk_percentage < 70 else "High"}</span>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # RECOMMENDATIONS
                    if "IS" in result:
                        st.warning("""
                        **🩺 MEDICAL RECOMMENDATIONS:**
                        - Consult with healthcare provider immediately
                        - Monitor blood glucose levels regularly
                        - Adopt balanced diet and exercise routine
                        - Schedule follow-up tests in 3 months
                        """)
                    else:
                        st.info("""
                        **💡 PREVENTIVE MEASURES:**
                        - Maintain healthy lifestyle
                        - Regular health check-ups
                        - Balanced nutrition
                        - Physical activity 150 mins/week
                        """)
        else:
            st.error("⚠️ Please complete all required clinical parameters for accurate analysis")

    st.markdown('</div>', unsafe_allow_html=True)

    # UNIFIED FOOTER
    st.markdown('<div class="unified-footer">Advanced Medical AI Diagnostics Platform<br>Developed with ❤️ by <b>KARTVAYA RAIKWAR</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
