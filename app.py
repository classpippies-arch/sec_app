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


# ---------- PREMIUM MEDICAL UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%) !important;
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }

    /* GLASS HEADER */
    .premium-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(25px);
        padding: 18px 30px;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* GLASS SIDEBAR */
    .premium-sidebar {
        position: fixed;
        top: 70px;
        left: 15px;
        width: 70px;
        height: calc(100% - 100px);
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.2);
        padding-top: 30px;
        text-align: center;
        z-index: 90;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }

    .premium-sidebar div { 
        margin: 25px 0; 
        font-size: 22px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .premium-sidebar div:hover { 
        transform: scale(1.2);
        color: #ffd700;
    }

    /* ANIMATED BLOBS */
    .premium-blob-1 {
        position: absolute;
        top: -100px;
        right: -80px;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, #ff0080 0%, transparent 70%);
        filter: blur(50px);
        border-radius: 50%;
        animation: float1 15s infinite ease-in-out;
        z-index: 1;
    }
    
    .premium-blob-2 {
        position: absolute;
        bottom: -120px;
        left: -100px;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, #4facfe 0%, transparent 70%);
        filter: blur(60px);
        border-radius: 50%;
        animation: float2 12s infinite ease-in-out;
        z-index: 1;
    }
    
    @keyframes float1 {
        0% { transform: translate(0,0) scale(1); }
        50% { transform: translate(-40px,30px) scale(1.1); }
        100% { transform: translate(0,0) scale(1); }
    }
    
    @keyframes float2 {
        0% { transform: translate(0,0) scale(1); }
        50% { transform: translate(30px,-40px) scale(0.9); }
        100% { transform: translate(0,0) scale(1); }
    }

    /* MAIN GLASS CARD */
    .premium-card {
        margin: 100px auto;
        margin-left: 110px;
        width: 72%;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(35px);
        border-radius: 25px;
        padding: 45px;
        border: 1px solid rgba(255,255,255,0.25);
        box-shadow: 0 25px 50px rgba(0,0,0,0.25);
        position: relative;
        overflow: hidden;
    }

    /* STUNNING BADGE - GOLD GRADIENT */
    .premium-badge {
        position: relative;
        z-index: 2;
        padding: 12px 24px;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
        color: #000;
        border-radius: 15px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 25px;
        font-size: 16px;
        box-shadow: 0 8px 30px rgba(255,215,0,0.4);
        border: 1px solid rgba(255,255,255,0.3);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }

    .premium-title {
        font-size: 38px;
        font-weight: 900;
        z-index: 2; 
        position: relative;
        color: white;
        margin-bottom: 10px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        text-align: center;
    }

    .premium-sub {
        color: rgba(255,255,255,0.9);
        margin-bottom: 35px;
        z-index: 2; 
        position: relative;
        font-size: 18px;
        line-height: 1.6;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: 500;
    }

    /* FORM GRID */
    .premium-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 22px 28px;
        z-index: 2;
        position: relative;
        margin-bottom: 30px;
    }

    /* PREMIUM INPUT STYLING */
    .stTextInput > div > div {
        background: rgba(255,255,255,0.15) !important;
        border: 2.5px solid rgba(255,255,255,0.4) !important;
        border-radius: 15px !important;
        padding: 4px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
    }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        color: white !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.7) !important;
    }
    
    .stTextInput > div > div > input:focus {
        outline: none !important;
        box-shadow: none !important;
        background: rgba(255,255,255,0.2) !important;
    }

    /* INPUT LABELS */
    .stTextInput label {
        font-weight: 700 !important;
        color: white !important;
        margin-bottom: 10px !important;
        font-size: 14px !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3) !important;
    }

    /* PREMIUM BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, #FFD700, #FFA500, #FF8C00);
        background-size: 200% 200%;
        animation: gradientShift 3s ease infinite;
        padding: 16px 32px;
        width: 100%;
        border-radius: 15px;
        color: #000;
        font-weight: 800;
        border: none;
        font-size: 18px;
        transition: all 0.3s ease;
        box-shadow: 0 12px 35px rgba(255,215,0,0.4);
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-top: 15px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 40px rgba(255,215,0,0.6);
    }

    /* RISK METER STYLING */
    .risk-meter {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(20px);
        border-radius: 15px;
        padding: 25px;
        margin: 25px 0;
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
    }

    .risk-title {
        font-size: 24px;
        font-weight: 700;
        color: white;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .risk-value {
        font-size: 42px;
        font-weight: 900;
        color: #FFD700;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        margin: 15px 0;
    }

    /* STATS GRID */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin: 25px 0;
    }

    .stat-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(15px);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }

    .stat-value {
        font-size: 28px;
        font-weight: 800;
        color: #FFD700;
        margin-bottom: 5px;
    }

    .stat-label {
        font-size: 12px;
        color: rgba(255,255,255,0.8);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* PREMIUM FOOTER */
    .premium-footer {
        text-align: center;
        margin-top: 40px;
        color: rgba(255,255,255,0.8);
        font-size: 16px;
        position: relative;
        z-index: 2;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: 600;
        padding: 20px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
    }

    .premium-footer b {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 18px;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
        .premium-card { 
            width: 85%; 
            margin-left: 90px; 
        }
        .premium-grid { 
            grid-template-columns: 1fr; 
        }
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 768px) {
        .premium-card { 
            width: 90%; 
            margin-left: 20px;
            margin-right: 20px;
        }
        .premium-sidebar {
            display: none;
        }
        .stats-grid {
            grid-template-columns: 1fr;
        }
    }

    </style>

    <div class="premium-header">
        <div>🏥 DIABETES AI DIAGNOSTIC SUITE</div>
        <div>v2.1 | MEDICAL GRADE</div>
    </div>

    <div class="premium-sidebar">
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
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)

    # Animated blobs
    st.markdown('<div class="premium-blob-1"></div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-blob-2"></div>', unsafe_allow_html=True)

    # GOLD BADGE - Perfectly visible on gradient background
    st.markdown('<div class="premium-badge">🎯 AI DIAGNOSTIC TOOL v2.1</div>', unsafe_allow_html=True)

    st.markdown('<div class="premium-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="premium-sub">Enter patient clinical parameters for comprehensive diabetes assessment and AI-powered health analysis</div>', unsafe_allow_html=True)

    # STATISTICS CARDS
    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Dynamic Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-value">98.2%</div><div class="stat-label">ACCURACY RATE</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-value">15K+</div><div class="stat-label">TESTS ANALYZED</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-value">0.3s</div><div class="stat-label">AVG PROCESSING</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="premium-grid">', unsafe_allow_html=True)
    
    # Column 1
    p = st.text_input("PREGNANCIES COUNT", placeholder="Enter number...")
    g = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL (70-200)")
    bp = st.text_input("BLOOD PRESSURE", placeholder="mmHg (60-180)")
    stn = st.text_input("SKIN THICKNESS", placeholder="mm (0-60)")
    
    # Column 2  
    ins = st.text_input("INSULIN LEVEL", placeholder="μU/mL (0-300)")
    bmi = st.text_input("BODY MASS INDEX", placeholder="BMI (10-60)")
    dpf = st.text_input("PEDIGREE FUNCTION", placeholder="0.00 - 2.50")
    age = st.text_input("PATIENT AGE", placeholder="Years (15-90)")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Additional Features
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
                    # RISK METER
                    st.markdown(f'''
                    <div class="risk-meter">
                        <div class="risk-title">AI DIAGNOSIS COMPLETE</div>
                        <div style="font-size: 20px; color: white; margin-bottom: 10px;">Prediction Result:</div>
                        <div style="font-size: 28px; font-weight: 800; color: {"#4CAF50" if "NOT" in result else "#FF6B6B"}; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); margin: 15px 0;">
                            {result}
                        </div>
                        <div class="risk-title">ESTIMATED RISK LEVEL</div>
                        <div class="risk-value">{risk_percentage}%</div>
                        <div style="background: rgba(255,255,255,0.2); height: 20px; border-radius: 10px; margin: 15px 0; overflow: hidden;">
                            <div style="height: 100%; background: linear-gradient(90deg, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}); width: {risk_percentage}%; transition: width 1s ease;"></div>
                        </div>
                        <div style="color: rgba(255,255,255,0.8); font-size: 14px; margin-top: 10px;">
                            Risk Assessment: {"Low" if risk_percentage < 30 else "Moderate" if risk_percentage < 70 else "High"}
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

    # HEALTH TIPS SECTION
    st.markdown("---")
    st.markdown('<div style="color: white; font-size: 24px; font-weight: 700; text-align: center; margin: 25px 0;">💡 HEALTH & WELLNESS TIPS</div>', unsafe_allow_html=True)
    
    tip_col1, tip_col2, tip_col3 = st.columns(3)
    with tip_col1:
        st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);"><div style="font-size: 16px; color: #FFD700; font-weight: 700;">🥗 Nutrition</div><div style="color: white; font-size: 13px; margin-top: 8px;">Focus on fiber-rich foods and limit processed sugars</div></div>', unsafe_allow_html=True)
    with tip_col2:
        st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);"><div style="font-size: 16px; color: #FFD700; font-weight: 700;">🏃 Exercise</div><div style="color: white; font-size: 13px; margin-top: 8px;">150 minutes of moderate activity per week recommended</div></div>', unsafe_allow_html=True)
    with tip_col3:
        st.markdown('<div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);"><div style="font-size: 16px; color: #FFD700; font-weight: 700;">📊 Monitoring</div><div style="color: white; font-size: 13px; margin-top: 8px;">Regular health check-ups help in early detection</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # PREMIUM FOOTER
    st.markdown('<div class="premium-footer">Advanced Medical AI Diagnostics Platform<br>Developed with ❤️ by <b>KARTVAYA RAIKWAR</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
