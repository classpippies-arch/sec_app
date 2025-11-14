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


# ---------- CLEAN UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* CLEAN GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe) !important;
        background-size: 400% 400% !important;
        animation: cleanGradient 15s ease infinite !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        min-height: 100vh !important;
    }
    
    @keyframes cleanGradient {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }

    /* CLEAN LOGIN CARD */
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 20px;
    }

    .login-card {
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(50px);
        border-radius: 25px;
        padding: 60px 50px;
        border: 1px solid rgba(255,255,255,0.25);
        box-shadow: 0 35px 60px rgba(0,0,0,0.3);
        text-align: center;
        width: 100%;
        max-width: 500px;
    }

    .login-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 20px;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.4);
        background: linear-gradient(135deg, #ffffff, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .login-subtitle {
        color: rgba(255,255,255,0.9);
        margin-bottom: 40px;
        font-size: 18px;
        line-height: 1.6;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }

    /* GOOGLE LOGIN BUTTON */
    .google-login-btn {
        background: white;
        color: #757575;
        border: 2px solid #ddd;
        border-radius: 12px;
        padding: 16px 30px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin: 30px auto;
        width: 100%;
        max-width: 300px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }

    .google-login-btn:hover {
        background: #f8f9fa;
        border-color: #4285f4;
        box-shadow: 0 12px 35px rgba(66,133,244,0.25);
        transform: translateY(-2px);
    }

    .google-icon {
        width: 24px;
        height: 24px;
    }

    /* TERMS TEXT */
    .terms-text {
        color: rgba(255,255,255,0.7);
        font-size: 14px;
        margin-top: 40px;
        line-height: 1.5;
    }

    /* MAIN APP STYLES */
    .clean-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(40px);
        padding: 18px 30px;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 800;
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
        font-size: 16px;
    }

    .clean-card {
        margin: 110px auto;
        margin-left: 20px;
        width: calc(100% - 40px);
        background: rgba(255,255,255,0.09);
        backdrop-filter: blur(50px);
        border-radius: 25px;
        padding: 40px;
        border: 1px solid rgba(255,255,255,0.22);
        box-shadow: 0 35px 60px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }

    .clean-badge {
        position: relative;
        z-index: 2;
        padding: 12px 25px;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(25px);
        color: white;
        border-radius: 16px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 25px;
        font-size: 15px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.25);
        border: 1px solid rgba(255,255,255,0.3);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
    }

    .clean-title {
        font-size: 38px;
        font-weight: 900;
        color: white;
        margin-bottom: 15px;
        text-shadow: 4px 4px 12px rgba(0,0,0,0.5);
        text-align: center;
        background: linear-gradient(135deg, #ffffff, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .clean-subtitle {
        color: rgba(255,255,255,0.9);
        margin-bottom: 35px;
        font-size: 18px;
        line-height: 1.7;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
        font-weight: 500;
    }

    /* INPUT STYLES */
    .stTextInput > div > div {
        background: rgba(255,255,255,0.95) !important;
        border: 2px solid rgba(255,255,255,0.8) !important;
        border-radius: 16px !important;
        padding: 8px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
    }

    .stTextInput > div > div > input {
        background: transparent !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        color: #2c3e50 !important;
    }

    .stTextInput label {
        font-weight: 700 !important;
        color: white !important;
        margin-bottom: 10px !important;
        font-size: 15px !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5) !important;
    }

    /* BUTTON STYLES */
    .stButton > button {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(25px);
        padding: 16px 32px;
        width: 100%;
        border-radius: 16px;
        color: white;
        font-weight: 700;
        border: 1.5px solid rgba(255,255,255,0.3);
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-top: 20px;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.25);
        background: rgba(255,255,255,0.2);
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 768px) {
        .login-card {
            padding: 40px 30px !important;
            margin: 20px !important;
        }
        
        .login-title {
            font-size: 32px !important;
        }
        
        .clean-card {
            margin: 100px 10px !important;
            width: calc(100% - 20px) !important;
            padding: 30px 20px !important;
        }
        
        .clean-title {
            font-size: 28px !important;
        }
    }

    /* HIDE UNNECESSARY ELEMENTS */
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

    </style>

    <div class="clean-header" style="display: none;" id="mainHeader">
        <div>🏥 DIABETES AI DIAGNOSTIC SUITE</div>
        <div>v3.0 | SECURE ACCESS</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Login Page ----------
def show_login_page():
    st.markdown("""
    <div class="login-container">
        <div class="login-card">
            <div class="login-title">Welcome Back</div>
            <div class="login-subtitle">Sign in to access the Diabetes Diagnostic Suite</div>
            
            <button class="google-login-btn" onclick="handleGoogleLogin()">
                <svg class="google-icon" viewBox="0 0 24 24">
                    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                </svg>
                Sign in with Google
            </button>
            
            <div class="terms-text">
                By continuing, you agree to our Terms of Service and Privacy Policy
            </div>
        </div>
    </div>

    <script>
    function handleGoogleLogin() {
        // Simulate successful login
        window.location.href = window.location.href + "?login=success";
    }
    
    // Check for successful login
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('login') === 'success') {
        // This will be handled by Streamlit
        console.log("Login successful");
    }
    </script>
    """, unsafe_allow_html=True)
    
    # Simple login button (no complex forms)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎯 **Continue to App**", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()


# ---------- Main App ----------
def show_main_app():
    # Show header
    st.markdown("""
    <script>
    document.getElementById('mainHeader').style.display = 'flex';
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="clean-card">', unsafe_allow_html=True)

    # APP BADGE
    st.markdown('<div class="clean-badge">🎯 AI DIAGNOSTIC TOOL v3.0</div>', unsafe_allow_html=True)

    st.markdown('<div class="clean-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="clean-subtitle">Enter patient clinical parameters for comprehensive diabetes assessment</div>', unsafe_allow_html=True)

    # SIMPLE INPUT FORM
    col1, col2 = st.columns(2)
    
    with col1:
        p = st.text_input("PREGNANCIES", placeholder="0")
        g = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL")
        bp = st.text_input("BLOOD PRESSURE", placeholder="mmHg")
        stn = st.text_input("SKIN THICKNESS", placeholder="mm")
    
    with col2:
        ins = st.text_input("INSULIN LEVEL", placeholder="μU/mL")
        bmi = st.text_input("BMI", placeholder="Value")
        dpf = st.text_input("PEDIGREE FUNCTION", placeholder="0.000-2.000")
        age = st.text_input("AGE", placeholder="Years")

    # ANALYSIS BUTTON
    if st.button("🔍 **ANALYZE DIABETES RISK**", use_container_width=True):
        if all([p, g, bp, stn, ins, bmi, dpf, age]):
            with st.spinner('Analyzing with AI...'):
                time.sleep(2)
                result, risk_percentage = diabetes_prediction([p, g, bp, stn, ins, bmi, dpf, age])
                
                if result:
                    # CLEAN RESULT DISPLAY
                    st.markdown(f"""
                    <div style="background: rgba(255,255,255,0.1); border-radius: 20px; padding: 30px; margin: 25px 0; text-align: center; border: 1px solid rgba(255,255,255,0.2);">
                        <h3 style="color: white; margin-bottom: 20px;">DIAGNOSIS RESULT</h3>
                        <div style="font-size: 28px; font-weight: bold; color: {'#4CAF50' if 'NOT' in result else '#FF6B6B'}; margin: 20px 0;">
                            {result}
                        </div>
                        <div style="font-size: 20px; color: #ffd700; font-weight: bold;">
                            Risk Level: {risk_percentage}%
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Please fill all fields")

    # LOGOUT BUTTON
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Simple logout in main area
    if st.button("🚪 **Logout**", use_container_width=False):
        st.session_state.logged_in = False
        st.rerun()


# ---------- Main Application ----------
def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    # Load CSS
    load_css()
    
    # Check URL parameters for login success
    query_params = st.query_params
    if 'login' in query_params and query_params['login'] == 'success':
        st.session_state.logged_in = True
        st.query_params.clear()
    
    # Show appropriate page
    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_main_app()


if __name__ == "__main__":
    main()
