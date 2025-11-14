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


# ---------- VIBRANT FILM-STYLE UI CSS --------------
def load_css():
    st.markdown("""
    <style>

    /* VIBRANT GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%) !important;
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }

    /* GLASS MORPHISM HEADER */
    .vibrant-header {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(25px);
        padding: 20px 40px;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 800;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-size: 22px;
    }

    /* FLOATING SIDEBAR */
    .vibrant-sidebar {
        position: fixed;
        top: 90px;
        left: 20px;
        width: 70px;
        height: calc(100% - 120px);
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.2);
        padding-top: 40px;
        text-align: center;
        z-index: 90;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }

    .vibrant-sidebar div { 
        margin: 30px 0; 
        font-size: 24px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .vibrant-sidebar div:hover { 
        transform: scale(1.2);
        color: #ffeb3b;
    }

    /* MULTI-COLORED BLOBS */
    .color-blob-1 {
        position: absolute;
        top: -100px;
        left: -80px;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, #ff0080 0%, transparent 70%);
        filter: blur(50px);
        border-radius: 50%;
        animation: float1 12s infinite ease-in-out;
        z-index: 1;
    }
    
    .color-blob-2 {
        position: absolute;
        bottom: -120px;
        right: -100px;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, #4facfe 0%, transparent 70%);
        filter: blur(60px);
        border-radius: 50%;
        animation: float2 10s infinite ease-in-out;
        z-index: 1;
    }
    
    .color-blob-3 {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, #ffeb3b 0%, transparent 70%);
        filter: blur(40px);
        border-radius: 50%;
        animation: pulse 8s infinite ease-in-out;
        z-index: 1;
    }
    
    @keyframes float1 {
        0% { transform: translate(0,0) scale(1); }
        33% { transform: translate(30px,40px) scale(1.1); }
        66% { transform: translate(-20px,20px) scale(0.9); }
        100% { transform: translate(0,0) scale(1); }
    }
    
    @keyframes float2 {
        0% { transform: translate(0,0) scale(1); }
        33% { transform: translate(-40px,30px) scale(0.9); }
        66% { transform: translate(20px,-20px) scale(1.1); }
        100% { transform: translate(0,0) scale(1); }
    }
    
    @keyframes pulse {
        0% { opacity: 0.3; transform: translate(-50%, -50%) scale(0.8); }
        50% { opacity: 0.7; transform: translate(-50%, -50%) scale(1.2); }
        100% { opacity: 0.3; transform: translate(-50%, -50%) scale(0.8); }
    }

    /* GLASS MORPHISM CARD */
    .vibrant-card {
        margin: 130px auto;
        margin-left: 120px;
        width: 68%;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(30px);
        border-radius: 25px;
        padding: 45px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }

    /* VIBRANT BADGE */
    .vibrant-badge {
        position: relative;
        z-index: 2;
        padding: 10px 20px;
        background: linear-gradient(135deg, #ff0080, #ff8a00);
        color: white;
        border-radius: 15px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 25px;
        font-size: 16px;
        box-shadow: 0 8px 25px rgba(255,0,128,0.4);
        border: 1px solid rgba(255,255,255,0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .vibrant-title {
        font-size: 42px;
        font-weight: 900;
        z-index: 2; 
        position: relative;
        color: white;
        margin-bottom: 15px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        background: linear-gradient(135deg, #ffffff, #ffeb3b, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }

    .vibrant-sub {
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
    .vibrant-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 22px 28px;
        z-index: 2;
        position: relative;
        margin-bottom: 30px;
    }

    /* VIBRANT INPUT STYLING */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.12);
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 15px;
        padding: 14px 18px;
        font-size: 15px;
        transition: all 0.3s ease;
        color: white;
        font-weight: 500;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.7);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ffeb3b;
        box-shadow: 0 0 0 3px rgba(255,235,59,0.3);
        background: rgba(255,255,255,0.2);
    }

    /* VIBRANT BUTTON */
    .stButton > button {
        background: linear-gradient(135deg, #ff0080, #ff8a00, #ffeb3b);
        background-size: 200% 200%;
        animation: gradientShift 3s ease infinite;
        padding: 16px 32px;
        width: 100%;
        border-radius: 15px;
        color: #000;
        font-weight: 700;
        border: none;
        font-size: 18px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(255,0,128,0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(255,0,128,0.6);
    }

    /* SUCCESS MESSAGE STYLING */
    .stSuccess {
        background: linear-gradient(135deg, #00ff88, #00ccff);
        color: #000;
        border-radius: 15px;
        padding: 20px;
        border: none;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,255,136,0.4);
    }

    /* VIBRANT FOOTER */
    .vibrant-footer {
        text-align: center;
        margin-top: 40px;
        color: rgba(255,255,255,0.8);
        font-size: 16px;
        position: relative;
        z-index: 2;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: 600;
    }

    .vibrant-footer b {
        background: linear-gradient(135deg, #ffeb3b, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 900px) {
        .vibrant-card { 
            width: 85%; 
            margin-left: 100px; 
        }
        .vibrant-grid { 
            grid-template-columns: 1fr; 
        }
    }
    
    @media (max-width: 768px) {
        .vibrant-card { 
            width: 90%; 
            margin-left: 20px;
            margin-right: 20px;
        }
        .vibrant-sidebar {
            display: none;
        }
        .vibrant-title {
            font-size: 32px;
        }
    }

    </style>

    <div class="vibrant-header">
        <div>🎬 DIABETES AI SCANNER</div>
        <div>NEURAL DIAGNOSTICS</div>
    </div>

    <div class="vibrant-sidebar">
        <div>⚡</div>
        <div>🔍</div>
        <div>📊</div>
        <div>🎯</div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Main ----------
def main():
    load_css()

    # MAIN CARD
    st.markdown('<div class="vibrant-card">', unsafe_allow_html=True)

    # Multiple colored blobs
    st.markdown('<div class="color-blob-1"></div>', unsafe_allow_html=True)
    st.markdown('<div class="color-blob-2"></div>', unsafe_allow_html=True)
    st.markdown('<div class="color-blob-3"></div>', unsafe_allow_html=True)

    # Vibrant badge
    st.markdown('<div class="vibrant-badge">AI DIAGNOSTIC TOOL</div>', unsafe_allow_html=True)

    st.markdown('<div class="vibrant-title">DIABETES RISK ASSESSMENT</div>', unsafe_allow_html=True)
    st.markdown('<div class="vibrant-sub">Enter patient clinical parameters for AI-powered diabetes prediction analysis and neural network diagnostics</div>', unsafe_allow_html=True)

    st.markdown('<div class="vibrant-grid">', unsafe_allow_html=True)
    
    # Column 1
    p = st.text_input("PREGNANCIES", placeholder="Enter value...")
    g = st.text_input("GLUCOSE LEVEL", placeholder="mg/dL")
    bp = st.text_input("BLOOD PRESSURE", placeholder="mmHg")
    stn = st.text_input("SKIN THICKNESS", placeholder="mm")
    
    # Column 2  
    ins = st.text_input("INSULIN LEVEL", placeholder="μU/mL")
    bmi = st.text_input("BMI VALUE", placeholder="Body Mass Index")
    dpf = st.text_input("PEDIGREE FUNCTION", placeholder="0.00 - 2.00")
    age = st.text_input("PATIENT AGE", placeholder="Years")
    
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🚀 LAUNCH AI ANALYSIS"):
        if all([p, g, bp, stn, ins, bmi, dpf, age]):
            result = diabetes_prediction([p, g, bp, stn, ins, bmi, dpf, age])
            if result:
                st.success(f"**DIAGNOSTIC RESULT:** PATIENT {result}")
        else:
            st.warning("⚠️ Please complete all clinical parameters for analysis")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="vibrant-footer">CREATED BY <b>KARTVAYA RAIKWAR</b></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
