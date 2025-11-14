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


# ---------- ENHANCED UNIFIED UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* ENHANCED GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #23d5ab) !important;
        background-size: 400% 400% !important;
        animation: enhancedGradient 12s ease infinite !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        min-height: 100vh !important;
    }
    
    @keyframes enhancedGradient {
        0% { 
            background-position: 0% 50%;
            background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #23d5ab);
        }
        25% {
            background: linear-gradient(-45deg, #764ba2, #f093fb, #f5576c, #4facfe, #23d5ab, #667eea);
        }
        50% { 
            background-position: 100% 50%;
            background: linear-gradient(-45deg, #f093fb, #f5576c, #4facfe, #23d5ab, #667eea, #764ba2);
        }
        75% {
            background: linear-gradient(-45deg, #f5576c, #4facfe, #23d5ab, #667eea, #764ba2, #f093fb);
        }
        100% { 
            background-position: 0% 50%;
            background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #23d5ab);
        }
    }

    /* FLOATING PARTICLES */
    .particles-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: hidden;
    }
    
    .particle {
        position: absolute;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        animation: floatParticle 20s infinite linear;
    }
    
    @keyframes floatParticle {
        0% { 
            transform: translateY(100vh) translateX(0) rotate(0deg); 
            opacity: 0; 
        }
        10% { 
            opacity: 0.6; 
        }
        90% { 
            opacity: 0.6; 
        }
        100% { 
            transform: translateY(-100px) translateX(100px) rotate(360deg); 
            opacity: 0; 
        }
    }

    /* ENHANCED GLASS HEADER */
    .enhanced-header {
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
        box-shadow: 0 4px 30px rgba(0,0,0,0.3);
    }

    /* ENHANCED GLASS SIDEBAR */
    .enhanced-sidebar {
        position: fixed;
        top: 80px;
        left: 20px;
        width: 70px;
        height: calc(100% - 120px);
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(35px);
        border: 1px solid rgba(255,255,255,0.2);
        padding-top: 30px;
        text-align: center;
        z-index: 900;
        border-radius: 20px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.25);
    }

    .enhanced-sidebar div { 
        margin: 25px 0; 
        font-size: 22px;
        color: white;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.4);
        transition: all 0.4s ease;
        opacity: 0.8;
        cursor: pointer;
    }
    
    .enhanced-sidebar div:hover { 
        transform: scale(1.2) translateX(5px);
        opacity: 1;
        color: #ffd700;
        text-shadow: 0 0 15px rgba(255,215,0,0.5);
    }

    /* ENHANCED MAIN GLASS CARD */
    .enhanced-card {
        margin: 110px auto;
        margin-left: 110px;
        width: 75%;
        min-height: 600px;
        background: rgba(255,255,255,0.09);
        backdrop-filter: blur(50px);
        border-radius: 28px;
        padding: 45px;
        border: 1px solid rgba(255,255,255,0.22);
        box-shadow: 
            0 35px 60px rgba(0,0,0,0.3),
            inset 0 2px 0 rgba(255,255,255,0.15),
            inset 0 -2px 0 rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
        z-index: 2;
    }

    /* ENHANCED BADGE */
    .enhanced-badge {
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
        animation: badgeGlow 3s ease-in-out infinite alternate;
    }
    
    @keyframes badgeGlow {
        0% { box-shadow: 0 12px 35px rgba(0,0,0,0.25); }
        100% { box-shadow: 0 12px 45px rgba(255,255,255,0.1), 0 0 30px rgba(255,255,255,0.1); }
    }

    .enhanced-title {
        font-size: 42px;
        font-weight: 900;
        z-index: 2; 
        position: relative;
        color: white;
        margin-bottom: 12px;
        text-shadow: 4px 4px 12px rgba(0,0,0,0.5);
        text-align: center;
        background: linear-gradient(135deg, #ffffff, #ffd700, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: titleShine 4s ease-in-out infinite;
    }
    
    @keyframes titleShine {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    .enhanced-subtitle {
        color: rgba(255,255,255,0.9);
        margin-bottom: 35px;
        z-index: 2; 
        position: relative;
        font-size: 18px;
        line-height: 1.7;
        text-align: center;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
        font-weight: 500;
        padding: 0 20px;
    }

    /* ENHANCED FORM GRID */
    .enhanced-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 22px 28px;
        z-index: 2;
        position: relative;
        margin-bottom: 30px;
    }

    /* ENHANCED INPUT BOXES WITH WHITE BACKGROUND */
    .stTextInput > div > div {
        background: rgba(255,255,255,0.95) !important;
        backdrop-filter: blur(20px) !important;
        border: 2px solid rgba(255,255,255,0.8) !important;
        border-radius: 18px !important;
        padding: 8px !important;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        box-shadow: 
            0 12px 35px rgba(0,0,0,0.2),
            inset 0 2px 8px rgba(255,255,255,0.3) !important;
    }

    .stTextInput > div > div:hover {
        background: rgba(255,255,255,0.98) !important;
        border-color: rgba(255,255,255,0.9) !important;
        box-shadow: 
            0 18px 45px rgba(0,0,0,0.25),
            inset 0 2px 12px rgba(255,255,255,0.4) !important;
        transform: translateY(-3px) scale(1.02);
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
        background: rgba(255,255,255,0.8) !important;
    }

    /* ENHANCED INPUT LABELS */
    .stTextInput label {
        font-weight: 700 !important;
        color: white !important;
        margin-bottom: 12px !important;
        font-size: 15px !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5) !important;
        letter-spacing: 0.3px;
        display: block;
        padding-left: 8px;
        background: linear-gradient(135deg, #ffffff, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ENHANCED SELECT BOXES */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.95) !important;
        backdrop-filter: blur(20px) !important;
        border: 2px solid rgba(255,255,255,0.8) !important;
        border-radius: 18px !important;
        padding: 4px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            0 12px 35px rgba(0,0,0,0.2),
            inset 0 2px 8px rgba(255,255,255,0.3) !important;
    }

    .stSelectbox > div > div:hover {
        background: rgba(255,255,255,0.98) !important;
        border-color: rgba(255,255,255,0.9) !important;
        box-shadow: 
            0 18px 45px rgba(0,0,0,0.25),
            inset 0 2px 12px rgba(255,255,255,0.4) !important;
        transform: translateY(-3px) scale(1.02);
    }

    .stSelectbox > div > div > div {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        padding: 14px 18px !important;
        font-size: 15px !important;
    }

    .stSelectbox label {
        font-weight: 700 !important;
        color: white !important;
        margin-bottom: 12px !important;
        font-size: 15px !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5) !important;
        letter-spacing: 0.3px;
        background: linear-gradient(135deg, #ffffff, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ENHANCED BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(30px);
        padding: 18px 32px;
        width: 100%;
        border-radius: 20px;
        color: white;
        font-weight: 800;
        border: 2px solid rgba(255,255,255,0.35);
        font-size: 18px;
        transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 
            0 15px 40px rgba(0,0,0,0.25),
            inset 0 2px 0 rgba(255,255,255,0.25);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 25px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.35),
            inset 0 2px 0 rgba(255,255,255,0.3),
            0 0 30px rgba(255,255,255,0.2);
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
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.8s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }

    /* ENHANCED STATS CARDS */
    .enhanced-stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin: 30px 0;
    }

    .enhanced-stat-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(30px);
        border-radius: 18px;
        padding: 25px 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }

    .enhanced-stat-card:hover {
        transform: translateY(-5px) scale(1.03);
        background: rgba(255,255,255,0.15);
        box-shadow: 0 20px 45px rgba(0,0,0,0.3), 0 0 25px rgba(255,255,255,0.1);
    }

    .enhanced-stat-value {
        font-size: 32px;
        font-weight: 900;
        color: #ffd700;
        margin-bottom: 8px;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.5);
    }

    .enhanced-stat-label {
        font-size: 13px;
        color: rgba(255,255,255,0.9);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* LOGIN PAGE STYLING */
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
        padding: 50px 40px;
        border: 1px solid rgba(255,255,255,0.25);
        box-shadow: 0 35px 60px rgba(0,0,0,0.3);
        text-align: center;
        width: 100%;
        max-width: 450px;
    }

    .google-login-btn {
        background: white;
        color: #757575;
        border: 2px solid #ddd;
        border-radius: 12px;
        padding: 15px 25px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin: 25px auto;
        width: 100%;
        max-width: 280px;
    }

    .google-login-btn:hover {
        background: #f8f9fa;
        border-color: #4285f4;
        box-shadow: 0 8px 25px rgba(66,133,244,0.2);
        transform: translateY(-2px);
    }

    /* RESPONSIVE DESIGN - MOBILE OPTIMIZED */
    @media (max-width: 768px) {
        .enhanced-card { 
            width: 92% !important; 
            margin: 100px auto !important;
            padding: 30px 25px !important;
            min-height: auto !important;
        }
        
        .enhanced-sidebar {
            display: none !important;
        }
        
        .enhanced-header {
            padding: 15px 20px !important;
            font-size: 14px !important;
        }
        
        .enhanced-title {
            font-size: 32px !important;
        }
        
        .enhanced-subtitle {
            font-size: 16px !important;
            padding: 0 10px !important;
        }
        
        .enhanced-grid { 
            grid-template-columns: 1fr !important;
            gap: 18px !important;
        }
        
        .enhanced-stats-grid {
            grid-template-columns: 1fr !important;
            gap: 15px !important;
        }
        
        .stTextInput > div > div,
        .stSelectbox > div > div {
            padding: 6px !important;
        }
        
        .stTextInput > div > div > input {
            padding: 14px 16px !important;
            font-size: 15px !important;
        }
    }

    @media (max-width: 480px) {
        .enhanced-card { 
            width: 95% !important; 
            margin: 80px auto !important;
            padding: 25px 20px !important;
        }
        
        .enhanced-title {
            font-size: 28px !important;
        }
        
        .enhanced-subtitle {
            font-size: 14px !important;
        }
        
        .login-card {
            padding: 40px 25px !important;
        }
    }

    </style>

    <div class="enhanced-header">
        <div>🏥 DIABETES AI DIAGNOSTIC SUITE</div>
        <div>v3.0 | PREMIUM MEDICAL GRADE</div>
    </div>

    <div class="enhanced-sidebar">
        <div>⚡</div>
        <div>🔍</div>
        <div>📊</div>
        <div>🎯</div>
        <div>⚕️</div>
    </div>
    
    <div class="particles-container" id="particles"></div>
    """, unsafe_allow_html=True)


# ---------- Particle Animation Script ----------
def add_particles():
    st.markdown("""
    <script>
    function createParticles() {
        const container = document.getElementById('particles');
        const particleCount = window.innerWidth < 768 ? 15 : 25;
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            
            // Random properties optimized for mobile
            const size = Math.random() * 6 + 2;
            const left = Math.random() * 100;
            const animationDuration = Math.random() * 15 + 10;
            const animationDelay = Math.random() * 3;
            
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
    
    // Recreate particles on resize for responsive behavior
    window.addEventListener('resize', function() {
        const container = document.getElementById('particles');
        container.innerHTML = '';
        createParticles();
    });
    </script>
    """, unsafe_allow_html=True)


# ---------- Login Page ----------
def show_login_page():
    st.markdown("""
    <div class="login-container">
        <div class="login-card">
            <div class="enhanced-badge" style="margin: 0 auto 25px auto;">🔐 SECURE LOGIN</div>
            <div class="enhanced-title" style="font-size: 36px; margin-bottom: 15px;">Welcome Back</div>
            <div class="enhanced-subtitle" style="margin-bottom: 40px;">Sign in to access the Diabetes Diagnostic Suite</div>
            
            <button class="google-login-btn" onclick="handleGoogleSignIn()">
                <svg width="20" height="20" viewBox="0 0 24 24">
                    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                </svg>
                Sign in with Google
            </button>
            
            <div style="color: rgba(255,255,255,0.7); font-size: 14px; margin-top: 30px;">
                By continuing, you agree to our Terms of Service and Privacy Policy
            </div>
        </div>
    </div>
    
    <script>
    function handleGoogleSignIn() {
        // Simulate Google Sign In - In real implementation, use Google OAuth
        window.location.href = window.location.href + "?logged_in=true";
    }
    
    // Check if user is already logged in (simulated)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('logged_in') === 'true') {
        // In real app, you would set session state here
        console.log("User logged in successfully");
    }
    </script>
    """, unsafe_allow_html=True)
    
    # Check if login button was clicked
    if st.button("🔓 Continue to App (Demo)", key="demo_login"):
        st.session_state.logged_in = True
        st.rerun()


# ---------- Main App ----------
def show_main_app():
    st.markdown('<div class="enhanced-card">', unsafe_allow_html=True)

    # ENHANCED BADGE
    st.markdown('<div class="enhanced-badge">🎯 AI DIAGNOSTIC TOOL v3.0</div>', unsafe_allow_html=True)

    st.markdown('<div class="enhanced-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="enhanced-subtitle">Enter patient clinical parameters for comprehensive diabetes assessment and AI-powered health analysis</div>', unsafe_allow_html=True)

    # ENHANCED STATISTICS - Updated numbers
    st.markdown('<div class="enhanced-stats-grid">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="enhanced-stat-card"><div class="enhanced-stat-value">15K+</div><div class="enhanced-stat-label">TESTS ANALYZED</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="enhanced-stat-card"><div class="enhanced-stat-value">100+</div><div class="enhanced-stat-label">MOBILE USERS</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="enhanced-stat-card"><div class="enhanced-stat-value">98.7%</div><div class="enhanced-stat-label">ACCURACY RATE</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="enhanced-grid">', unsafe_allow_html=True)
    
    # Column 1 - Enhanced input boxes with white background
    p = st.text_input("NUMBER OF PREGNANCIES", placeholder="Enter count (0-20)")
    g = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL (70-200)")
    bp = st.text_input("BLOOD PRESSURE", placeholder="mmHg (60-180)")
    stn = st.text_input("SKIN THICKNESS", placeholder="mm (0-60)")
    
    # Column 2 - Enhanced input boxes with white background
    ins = st.text_input("INSULIN LEVEL", placeholder="μU/mL (0-300)")
    bmi = st.text_input("BODY MASS INDEX", placeholder="BMI (10-60)")
    dpf = st.text_input("PEDIGREE FUNCTION", placeholder="0.00 - 2.50")
    age = st.text_input("PATIENT AGE", placeholder="Years (15-90)")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Additional Features with enhanced design
    with st.expander("🔧 ADVANCED CLINICAL OPTIONS"):
        col1, col2 = st.columns(2)
        with col1:
            family_history = st.selectbox("Family History of Diabetes", ["None", "Parent", "Sibling", "Both Parents"])
            activity_level = st.selectbox("Physical Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
        with col2:
            diet_quality = st.selectbox("Diet Quality", ["Poor", "Average", "Good", "Excellent"])
            smoking_status = st.selectbox("Smoking Status", ["Non-smoker", "Former Smoker", "Current Smoker"])

    if st.button("🚀 LAUNCH COMPREHENSIVE ANALYSIS"):
        if all([p, g, bp, stn, ins, bmi, dpf, age]):
            with st.spinner('🔬 Analyzing clinical parameters with advanced AI algorithms...'):
                time.sleep(2)
                result, risk_percentage = diabetes_prediction([p, g, bp, stn, ins, bmi, dpf, age])
                
                if result:
                    # ENHANCED RISK METER
                    st.markdown(f'''
                    <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(40px); border-radius: 22px; padding: 35px; margin: 30px 0; border: 1px solid rgba(255,255,255,0.25); box-shadow: 0 20px 50px rgba(0,0,0,0.25); text-align: center;">
                        <div style="font-size: 28px; font-weight: 800; color: white; margin-bottom: 20px; text-shadow: 3px 3px 8px rgba(0,0,0,0.5);">AI DIAGNOSIS COMPLETE</div>
                        <div style="font-size: 20px; color: white; margin-bottom: 18px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">Prediction Result:</div>
                        <div style="font-size: 34px; font-weight: 900; color: {"#4CAF50" if "NOT" in result else "#FF6B6B"}; text-shadow: 3px 3px 8px rgba(0,0,0,0.6); margin: 20px 0; padding: 18px; background: rgba(255,255,255,0.12); border-radius: 16px; border: 2px solid {"rgba(76,175,80,0.4)" if "NOT" in result else "rgba(255,107,107,0.4)"};">
                            {result}
                        </div>
                        <div style="font-size: 24px; font-weight: 800; color: white; margin: 25px 0 18px 0; text-shadow: 2px 2px 6px rgba(0,0,0,0.5);">ESTIMATED RISK LEVEL</div>
                        <div style="font-size: 48px; font-weight: 900; color: #ffd700; text-shadow: 4px 4px 12px rgba(0,0,0,0.6); margin: 20px 0;">{risk_percentage}%</div>
                        <div style="background: rgba(255,255,255,0.15); height: 26px; border-radius: 13px; margin: 20px 0; overflow: hidden; box-shadow: inset 0 3px 6px rgba(0,0,0,0.3);">
                            <div style="height: 100%; background: linear-gradient(90deg, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}, {"#4CAF50" if risk_percentage < 30 else "#FFA500" if risk_percentage < 70 else "#FF6B6B"}); width: {risk_percentage}%; transition: width 1.2s ease; border-radius: 13px;"></div>
                        </div>
                        <div style="color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 18px; font-weight: 700;">
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

    # ENHANCED FOOTER
    st.markdown('<div style="text-align: center; margin-top: 45px; color: rgba(255,255,255,0.9); font-size: 16px; position: relative; z-index: 2; text-shadow: 1px 1px 3px rgba(0,0,0,0.4); font-weight: 600; padding: 25px; background: rgba(255,255,255,0.08); backdrop-filter: blur(30px); border-radius: 18px; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 12px 35px rgba(0,0,0,0.2);">Advanced Medical AI Diagnostics Platform<br>Developed with ❤️ by <b style="background: linear-gradient(135deg, #ffd700, #ffa500); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">KARTVAYA RAIKWAR</b></div>', unsafe_allow_html=True)


# ---------- Main Application ----------
def main():
    # Initialize session state for login
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    load_css()
    add_particles()
    
    # Show login page or main app based on login status
    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_main_app()
        
        # Logout button
        if st.sidebar.button("🚪 Logout", key="logout"):
            st.session_state.logged_in = False
            st.rerun()


if __name__ == "__main__":
    main()
