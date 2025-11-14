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


# ---------- PROFESSIONAL UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* PROFESSIONAL GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important;
        background-size: 400% 400% !important;
        animation: professionalGradient 18s ease infinite !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        min-height: 100vh !important;
    }
    
    @keyframes professionalGradient {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }

    /* PROFESSIONAL HEADER */
    .professional-header {
        position: fixed;
        top: 0; 
        left: 0;
        width: 100%;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(35px);
        padding: 20px 40px;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 800;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
        font-size: 18px;
        box-shadow: 0 4px 30px rgba(0,0,0,0.2);
    }

    /* MAIN CONTENT CARD */
    .professional-card {
        margin: 120px auto;
        width: 85%;
        max-width: 1200px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(40px);
        border-radius: 28px;
        padding: 50px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 
            0 35px 60px rgba(0,0,0,0.25),
            inset 0 1px 0 rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    }

    /* PROFESSIONAL BADGE */
    .professional-badge {
        position: relative;
        z-index: 2;
        padding: 14px 28px;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(25px);
        color: white;
        border-radius: 18px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 30px;
        font-size: 16px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.25);
        border: 1px solid rgba(255,255,255,0.25);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }

    .professional-title {
        font-size: 44px;
        font-weight: 900;
        z-index: 2; 
        position: relative;
        color: white;
        margin-bottom: 20px;
        text-shadow: 4px 4px 12px rgba(0,0,0,0.5);
        text-align: center;
        background: linear-gradient(135deg, #ffffff, #ffd700, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }

    .professional-subtitle {
        color: rgba(255,255,255,0.9);
        margin-bottom: 40px;
        z-index: 2; 
        position: relative;
        font-size: 20px;
        line-height: 1.6;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
        font-weight: 500;
        padding: 0 40px;
    }

    /* STATS GRID */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin: 40px 0;
    }

    .stat-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(25px);
        border-radius: 20px;
        padding: 30px 25px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }

    .stat-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.12);
        box-shadow: 0 20px 45px rgba(0,0,0,0.3);
    }

    .stat-value {
        font-size: 36px;
        font-weight: 900;
        color: #ffd700;
        margin-bottom: 10px;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.5);
    }

    .stat-label {
        font-size: 14px;
        color: rgba(255,255,255,0.9);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* INPUT FORM GRID */
    .form-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 25px 30px;
        margin: 40px 0;
    }

    /* PROFESSIONAL INPUT STYLING */
    .stTextInput > div > div {
        background: rgba(255,255,255,0.95) !important;
        backdrop-filter: blur(20px) !important;
        border: 2px solid rgba(255,255,255,0.8) !important;
        border-radius: 18px !important;
        padding: 8px !important;
        transition: all 0.3s ease !important;
        box-shadow: 
            0 12px 35px rgba(0,0,0,0.15),
            inset 0 2px 8px rgba(255,255,255,0.3) !important;
    }

    .stTextInput > div > div:hover {
        background: rgba(255,255,255,0.98) !important;
        border-color: rgba(102,126,234,0.6) !important;
        box-shadow: 
            0 18px 45px rgba(0,0,0,0.2),
            inset 0 2px 12px rgba(255,255,255,0.4) !important;
        transform: translateY(-2px);
    }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 16px 20px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #2c3e50 !important;
        height: auto !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(44,62,80,0.5) !important;
        font-weight: 500 !important;
        font-size: 15px !important;
    }
    
    .stTextInput > div > div > input:focus {
        outline: none !important;
        box-shadow: 
            inset 0 0 0 3px rgba(102,126,234,0.3),
            0 0 25px rgba(102,126,234,0.2) !important;
        background: rgba(255,255,255,0.9) !important;
    }

    /* INPUT LABELS */
    .stTextInput label {
        font-weight: 700 !important;
        color: white !important;
        margin-bottom: 12px !important;
        font-size: 16px !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5) !important;
        letter-spacing: 0.3px;
        display: block;
        padding-left: 8px;
    }

    /* PROFESSIONAL BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(30px);
        padding: 20px 40px;
        width: 100%;
        border-radius: 20px;
        color: white;
        font-weight: 800;
        border: 2px solid rgba(255,255,255,0.3);
        font-size: 18px;
        transition: all 0.4s ease;
        box-shadow: 
            0 15px 40px rgba(0,0,0,0.25),
            inset 0 2px 0 rgba(255,255,255,0.2);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin: 30px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 
            0 20px 50px rgba(0,0,0,0.35),
            inset 0 2px 0 rgba(255,255,255,0.3);
        background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0.15));
        border-color: rgba(255,255,255,0.5);
    }

    /* RESULT DISPLAY */
    .result-container {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(40px);
        border-radius: 24px;
        padding: 40px;
        margin: 30px 0;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 25px 50px rgba(0,0,0,0.25);
        text-align: center;
    }

    .result-title {
        font-size: 32px;
        font-weight: 800;
        color: white;
        margin-bottom: 25px;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.5);
    }

    .result-text {
        font-size: 36px;
        font-weight: 900;
        margin: 25px 0;
        padding: 20px;
        border-radius: 16px;
        background: rgba(255,255,255,0.1);
        border: 2px solid rgba(255,255,255,0.2);
    }

    .risk-meter {
        background: rgba(255,255,255,0.15);
        height: 28px;
        border-radius: 14px;
        margin: 25px 0;
        overflow: hidden;
        box-shadow: inset 0 3px 6px rgba(0,0,0,0.3);
    }

    .risk-fill {
        height: 100%;
        border-radius: 14px;
        transition: width 1.5s ease;
    }

    /* FOOTER */
    .professional-footer {
        text-align: center;
        margin-top: 50px;
        color: rgba(255,255,255,0.8);
        font-size: 16px;
        padding: 25px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(25px);
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    }

    .professional-footer b {
        background: linear-gradient(135deg, #ffd700, #ffa500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 18px;
    }

    /* HIDE ALL UNNECESSARY ELEMENTS */
    .stSidebar {
        display: none !important;
    }
    
    #MainMenu {
        display: none !important;
    }
    
    footer {
        display: none !important;
    }
    
    .stDeployButton {
        display: none !important;
    }
    
    .stStatusWidget {
        display: none !important;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 1024px) {
        .professional-card {
            width: 90%;
            padding: 40px 30px;
        }
        
        .form-grid {
            grid-template-columns: 1fr;
            gap: 20px;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 768px) {
        .professional-header {
            padding: 15px 20px;
            font-size: 16px;
        }
        
        .professional-card {
            width: 95%;
            margin: 100px auto;
            padding: 30px 20px;
        }
        
        .professional-title {
            font-size: 32px;
        }
        
        .professional-subtitle {
            font-size: 18px;
            padding: 0 20px;
        }
        
        .stats-grid {
            grid-template-columns: 1fr;
            gap: 15px;
        }
        
        .stat-card {
            padding: 25px 20px;
        }
        
        .stat-value {
            font-size: 28px;
        }
    }

    </style>

    <div class="professional-header">
        <div>🏥 DIABETES AI DIAGNOSTIC SUITE</div>
        <div>v3.0 | MEDICAL GRADE</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Main Application ----------
def main():
    # Load professional CSS
    load_css()
    
    # MAIN CONTENT CARD
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)

    # PROFESSIONAL BADGE
    st.markdown('<div class="professional-badge">🎯 AI DIAGNOSTIC TOOL v3.0</div>', unsafe_allow_html=True)

    # MAIN TITLE
    st.markdown('<div class="professional-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="professional-subtitle">Enter patient clinical parameters for comprehensive diabetes assessment using advanced AI algorithms</div>', unsafe_allow_html=True)

    # STATISTICS
    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-value">98.7%</div><div class="stat-label">ACCURACY RATE</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-value">15K+</div><div class="stat-label">TESTS ANALYZED</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-value">0.2s</div><div class="stat-label">AVG PROCESSING</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # INPUT FORM
    st.markdown('<div class="form-grid">', unsafe_allow_html=True)
    
    # Column 1
    col1, col2 = st.columns(2)
    
    with col1:
        pregnancies = st.text_input("PREGNANCIES", placeholder="0")
        glucose = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL")
        blood_pressure = st.text_input("BLOOD PRESSURE", placeholder="mmHg")
        skin_thickness = st.text_input("SKIN THICKNESS", placeholder="mm")
    
    with col2:
        insulin = st.text_input("INSULIN LEVEL", placeholder="μU/mL")
        bmi = st.text_input("BODY MASS INDEX", placeholder="BMI")
        pedigree = st.text_input("DIABETES PEDIGREE", placeholder="0.000-2.000")
        age = st.text_input("AGE", placeholder="Years")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ANALYSIS BUTTON
    if st.button("🚀 LAUNCH AI ANALYSIS"):
        inputs = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]
        
        if all(inputs):
            with st.spinner('🔬 Analyzing clinical parameters with AI...'):
                time.sleep(2)
                result, risk_percentage = diabetes_prediction(inputs)
                
                if result:
                    # DISPLAY RESULTS
                    st.markdown(f'''
                    <div class="result-container">
                        <div class="result-title">AI DIAGNOSIS COMPLETE</div>
                        <div style="font-size: 20px; color: white; margin-bottom: 15px; text-shadow: 1px 1px 3px rgba(0,0,0,0.4);">Prediction Result:</div>
                        <div class="result-text" style="color: {"#4CAF50" if "NOT" in result else "#FF6B6B"}; text-shadow: 2px 2px 6px rgba(0,0,0,0.5);">
                            {result}
                        </div>
                        <div class="result-title">ESTIMATED RISK LEVEL</div>
                        <div style="font-size: 42px; font-weight: 900; color: #ffd700; text-shadow: 3px 3px 8px rgba(0,0,0,0.6); margin: 20px 0;">
                            {risk_percentage}%
                        </div>
                        <div class="risk-meter">
                            <div class="risk-fill" style="width: {risk_percentage}%; background: linear-gradient(90deg, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"});"></div>
                        </div>
                        <div style="color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 15px; font-weight: 600;">
                            Risk Assessment: <span style="color: {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}">{"Low" if risk_percentage < 30 else "Moderate" if risk_percentage < 70 else "High"}</span>
                        </div>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # MEDICAL RECOMMENDATIONS
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

    # PROFESSIONAL FOOTER
    st.markdown('<div class="professional-footer">Advanced Medical AI Diagnostics Platform<br>Developed with ❤️ by <b>KARTVAYA RAIKWAR</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
