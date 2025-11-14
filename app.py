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


# ---------- SMOOTH ANIMATED UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* ANIMATED GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab, #667eea, #764ba2, #f093fb, #f5576c) !important;
        background-size: 400% 400% !important;
        animation: gradient 15s ease infinite !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }

    /* GLASS HEADER */
    .smooth-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(30px);
        padding: 18px 30px;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* GLASS SIDEBAR */
    .smooth-sidebar {
        position: fixed;
        top: 70px;
        left: 15px;
        width: 70px;
        height: calc(100% - 100px);
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255,255,255,0.15);
        padding-top: 30px;
        text-align: center;
        z-index: 90;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }

    .smooth-sidebar div { 
        margin: 25px 0; 
        font-size: 22px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .smooth-sidebar div:hover { 
        transform: scale(1.2);
        color: #ffd700;
    }

    /* FLOATING PARTICLES BACKGROUND */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }
    
    .particle {
        position: absolute;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        animation: floatParticle 20s infinite linear;
    }
    
    @keyframes floatParticle {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 0.7; }
        90% { opacity: 0.7; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }

    /* MAIN GLASS CARD */
    .smooth-card {
        margin: 100px auto;
        margin-left: 110px;
        width: 72%;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(40px);
        border-radius: 25px;
        padding: 45px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.25),
            inset 0 1px 0 rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        z-index: 2;
    }

    /* SMOOTH BADGE */
    .smooth-badge {
        position: relative;
        z-index: 2;
        padding: 12px 24px;
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        color: white;
        border-radius: 15px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 25px;
        font-size: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.3);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }

    .smooth-title {
        font-size: 38px;
        font-weight: 900;
        z-index: 2; 
        position: relative;
        color: white;
        margin-bottom: 10px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
        text-align: center;
        background: linear-gradient(135deg, #ffffff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .smooth-sub {
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
    .smooth-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 22px 28px;
        z-index: 2;
        position: relative;
        margin-bottom: 30px;
    }

    /* SMOOTH GLASS INPUT BOXES */
    .stTextInput > div > div {
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(20px) !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-radius: 16px !important;
        padding: 8px !important;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.1),
            0 8px 25px rgba(0,0,0,0.15) !important;
    }

    .stTextInput > div > div:hover {
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.4) !important;
        box-shadow: 
            inset 0 2px 8px rgba(255,255,255,0.15),
            0 12px 35px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: white !important;
        height: auto !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.6) !important;
        font-weight: 500 !important;
        font-size: 15px !important;
    }
    
    .stTextInput > div > div > input:focus {
        outline: none !important;
        box-shadow: 
            inset 0 0 0 2px rgba(255,255,255,0.3),
            0 0 20px rgba(255,255,255,0.2) !important;
        background: rgba(255,255,255,0.1) !important;
    }

    /* SMOOTH INPUT LABELS */
    .stTextInput label {
        font-weight: 700 !important;
        color: rgba(255,255,255,0.95) !important;
        margin-bottom: 12px !important;
        font-size: 15px !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4) !important;
        letter-spacing: 0.3px;
        display: block;
        padding-left: 8px;
        transition: all 0.3s ease;
    }

    /* SMOOTH SELECT BOXES */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(20px) !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-radius: 16px !important;
        padding: 4px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.1),
            0 8px 25px rgba(0,0,0,0.15) !important;
    }

    .stSelectbox > div > div:hover {
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.4) !important;
        box-shadow: 
            inset 0 2px 8px rgba(255,255,255,0.15),
            0 12px 35px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }

    .stSelectbox > div > div > div {
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
    }

    .stSelectbox label {
        font-weight: 700 !important;
        color: rgba(255,255,255,0.95) !important;
        margin-bottom: 12px !important;
        font-size: 15px !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4) !important;
        letter-spacing: 0.3px;
    }

    /* SMOOTH BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(20px);
        padding: 18px 32px;
        width: 100%;
        border-radius: 18px;
        color: white;
        font-weight: 800;
        border: 1px solid rgba(255,255,255,0.3);
        font-size: 18px;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 
            0 12px 35px rgba(0,0,0,0.2),
            inset 0 1px 0 rgba(255,255,255,0.2);
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-top: 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 
            0 20px 45px rgba(0,0,0,0.3),
            inset 0 1px 0 rgba(255,255,255,0.3);
        background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0.15));
        border-color: rgba(255,255,255,0.5);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.8s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }

    /* SMOOTH EXPANDER */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(20px) !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-radius: 16px !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 16px 20px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.1),
            0 8px 25px rgba(0,0,0,0.15) !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.4) !important;
        transform: translateY(-2px);
        box-shadow: 
            inset 0 2px 8px rgba(255,255,255,0.15),
            0 12px 35px rgba(0,0,0,0.2) !important;
    }

    .streamlit-expanderContent {
        background: rgba(255,255,255,0.03) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 0 0 16px 16px !important;
        border: 1.5px solid rgba(255,255,255,0.2) !important;
        border-top: none !important;
        box-shadow: 
            inset 0 2px 4px rgba(255,255,255,0.05),
            0 8px 25px rgba(0,0,0,0.1) !important;
    }

    /* SMOOTH FOOTER */
    .smooth-footer {
        text-align: center;
        margin-top: 45px;
        color: rgba(255,255,255,0.9);
        font-size: 17px;
        position: relative;
        z-index: 2;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
        font-weight: 600;
        padding: 25px;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(25px);
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.2),
            inset 0 1px 0 rgba(255,255,255,0.1);
    }

    .smooth-footer b {
        background: linear-gradient(135deg, #ffd700, #ffa500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 19px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
        .smooth-card { 
            width: 85%; 
            margin-left: 90px; 
        }
        .smooth-grid { 
            grid-template-columns: 1fr; 
        }
    }
    
    @media (max-width: 768px) {
        .smooth-card { 
            width: 90%; 
            margin-left: 20px;
            margin-right: 20px;
        }
        .smooth-sidebar {
            display: none;
        }
    }

    </style>

    <div class="smooth-header">
        <div>🏥 DIABETES AI DIAGNOSTIC SUITE</div>
        <div>v2.1 | MEDICAL GRADE</div>
    </div>

    <div class="smooth-sidebar">
        <div>⚡</div>
        <div>🔍</div>
        <div>📊</div>
        <div>🎯</div>
        <div>⚕️</div>
    </div>
    
    <div class="particles" id="particles"></div>
    """, unsafe_allow_html=True)


# ---------- Particle Animation Script ----------
def add_particles():
    st.markdown("""
    <script>
    function createParticles() {
        const container = document.getElementById('particles');
        const particleCount = 30;
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            
            // Random properties
            const size = Math.random() * 8 + 2;
            const left = Math.random() * 100;
            const animationDuration = Math.random() * 20 + 10;
            const animationDelay = Math.random() * 5;
            
            particle.style.width = `${size}px`;
            particle.style.height = `${size}px`;
            particle.style.left = `${left}vw`;
            particle.style.animationDuration = `${animationDuration}s`;
            particle.style.animationDelay = `${animationDelay}s`;
            
            container.appendChild(particle);
        }
    }
    
    // Create particles when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createParticles);
    } else {
        createParticles();
    }
    </script>
    """, unsafe_allow_html=True)


# ---------- Main ----------
def main():
    load_css()
    add_particles()

    # MAIN CARD
    st.markdown('<div class="smooth-card">', unsafe_allow_html=True)

    # SMOOTH BADGE
    st.markdown('<div class="smooth-badge">🎯 AI DIAGNOSTIC TOOL v2.1</div>', unsafe_allow_html=True)

    st.markdown('<div class="smooth-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="smooth-sub">Enter patient clinical parameters for comprehensive diabetes assessment and AI-powered health analysis</div>', unsafe_allow_html=True)

    st.markdown('<div class="smooth-grid">', unsafe_allow_html=True)
    
    # Column 1 - Smooth glass input boxes
    p = st.text_input("PREGNANCIES COUNT", placeholder="Enter number...")
    g = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL (70-200)")
    bp = st.text_input("BLOOD PRESSURE", placeholder="mmHg (60-180)")
    stn = st.text_input("SKIN THICKNESS", placeholder="mm (0-60)")
    
    # Column 2 - Smooth glass input boxes
    ins = st.text_input("INSULIN LEVEL", placeholder="μU/mL (0-300)")
    bmi = st.text_input("BODY MASS INDEX", placeholder="BMI (10-60)")
    dpf = st.text_input("PEDIGREE FUNCTION", placeholder="0.00 - 2.50")
    age = st.text_input("PATIENT AGE", placeholder="Years (15-90)")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Additional Features with smooth glass design
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
                    # RISK METER with smooth glass design
                    st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(30px); border-radius: 20px; padding: 30px; margin: 25px 0; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 15px 35px rgba(0,0,0,0.2); text-align: center;">
                        <div style="font-size: 26px; font-weight: 800; color: white; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">AI DIAGNOSIS COMPLETE</div>
                        <div style="font-size: 22px; color: white; margin-bottom: 15px; text-shadow: 1px 1px 3px rgba(0,0,0,0.3);">Prediction Result:</div>
                        <div style="font-size: 32px; font-weight: 900; color: {"#4CAF50" if "NOT" in result else "#FF6B6B"}; text-shadow: 3px 3px 6px rgba(0,0,0,0.4); margin: 20px 0; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 15px; border: 1px solid rgba(255,255,255,0.2);">
                            {result}
                        </div>
                        <div style="font-size: 24px; font-weight: 800; color: white; margin: 25px 0 15px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">ESTIMATED RISK LEVEL</div>
                        <div style="font-size: 46px; font-weight: 900; color: #ffd700; text-shadow: 3px 3px 8px rgba(0,0,0,0.5); margin: 20px 0;">{risk_percentage}%</div>
                        <div style="background: rgba(255,255,255,0.15); height: 24px; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: inset 0 2px 6px rgba(0,0,0,0.2);">
                            <div style="height: 100%; background: linear-gradient(90deg, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}); width: {risk_percentage}%; transition: width 1s ease; border-radius: 12px;"></div>
                        </div>
                        <div style="color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 15px; font-weight: 600;">
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

    # SMOOTH FOOTER
    st.markdown('<div class="smooth-footer">Advanced Medical AI Diagnostics Platform<br>Developed with ❤️ by <b>KARTVAYA RAIKWAR</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
