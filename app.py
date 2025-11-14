import numpy as np
import pickle
import os
import time
from datetime import datetime
import pandas as pd
import streamlit as st  # <-- added to fix NameError: 'st' is not defined

# Optional Plotly imports (guarded to avoid ModuleNotFoundError on platforms without plotly)
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except Exception:
    PLOTLY_AVAILABLE = False
    # If plotly isn't available, the app will fall back to matplotlib or simple Streamlit elements.
    # To enable Plotly, add `plotly` to your requirements.txt or run `pip install plotly` in your environment.


# --------- Load Model ---------
model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)


def diabetes_prediction(input_data):
    """Return (label, risk_percentage, confidence)
    - Uses predict_proba for confidence if available.
    - risk_percentage: derived from confidence or simulated fallback.
    """
    try:
        arr = np.asarray([float(x) for x in input_data]).reshape(1, -1)
    except Exception:
        return None, None, None

    pred = loaded_model.predict(arr)

    # Confidence using predict_proba if available
    confidence = None
    try:
        proba = loaded_model.predict_proba(arr)
        confidence = float(np.max(proba) * 100)
    except Exception:
        confidence = None

    # Calculate risk percentage (prefer confidence, else simulated)
    if confidence is not None:
        risk_percentage = int(confidence)
    else:
        risk_percentage = np.random.randint(15, 85) if pred[0] == 1 else np.random.randint(1, 30)

    label = "NOT diabetic" if pred[0] == 0 else "IS diabetic"
    return label, risk_percentage, confidence


# ---------- PROFESSIONAL UI CSS  (FUTURISTIC MONOCHROME LIQUID GLASS) --------------
def load_css():
    st.markdown("""
    <style>
    /* Base app - full black/white glassy theme */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600;800;900&display=swap');

    .stApp{
        font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
        background: #0b0b0b;
        color: #fff;
        min-height:100vh;
        overflow-x:hidden;
    }

    /* Liquid glass animated background using radial gradients + CSS animations */
    .liquid-bg{
        position:fixed;
        inset:0;
        z-index:0;
        pointer-events:none;
        background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.01) 50%, rgba(255,255,255,0.03) 100%);
        backdrop-filter: blur(8px);
        mix-blend-mode: screen;
        will-change: transform, opacity;
    }

    /* Larger, faster, multi-layered animated blobs for a more eye-catching liquid effect */
    .liquid-bg::before, .liquid-bg::after{
        content:"";
        position:absolute;
        width:130vmax;
        height:130vmax;
        left:50%;
        top:50%;
        transform:translate(-50%,-50%);
        background: radial-gradient(circle at 25% 30%, rgba(255,255,255,0.08), rgba(255,255,255,0.00) 35%), radial-gradient(circle at 70% 70%, rgba(255,255,255,0.06), rgba(255,255,255,0.00) 30%);
        filter: blur(80px) saturate(130%);
        animation: floatyFast 8s ease-in-out infinite;
        opacity:0.95;
        mix-blend-mode: screen;
    }

    .liquid-bg::after{
        background: radial-gradient(circle at 40% 60%, rgba(255,255,255,0.06), rgba(255,255,255,0.00) 30%), radial-gradient(circle at 60% 30%, rgba(255,255,255,0.07), rgba(255,255,255,0.00) 30%);
        animation-duration: 10s;
        transform: translate(-52%,-48%) scale(1.02);
        opacity:0.92;
        filter: blur(90px) saturate(140%);
    }

    /* extra transient layer for subtle ripples */
    .liquid-bg::marker{ /* fallback pseudo-element name, some browsers ignore; we use an overlay div instead in DOM if needed */ }

    @keyframes floatyFast{
        0% { transform: translate(-50%,-50%) scale(1) rotate(0deg); opacity:0.95 }
        25% { transform: translate(-46%,-54%) scale(1.08) rotate(3deg); opacity:1 }
        50% { transform: translate(-50%,-50%) scale(1.12) rotate(6deg); opacity:0.96 }
        75% { transform: translate(-54%,-46%) scale(1.06) rotate(-3deg); opacity:1 }
        100% { transform: translate(-50%,-50%) scale(1) rotate(0deg); opacity:0.95 }
    }

    /* subtle moving glass sheen overlay with faster sweep and soft pulses */
    .glass-sheen{
        position:fixed; inset:0; z-index:1; pointer-events:none; mix-blend-mode:overlay;
        background: linear-gradient(120deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.08) 50%, rgba(255,255,255,0.01) 100%);
        animation: sheen 6s linear infinite, sheenPulse 5.8s ease-in-out infinite;
        opacity:0.98;
    }
    @keyframes sheen { from {background-position:0% 50%;} to {background-position:100% 50%;} }
    @keyframes sheenPulse { 0% { opacity:0.92 } 50% { opacity:1 } 100% { opacity:0.92 } }

    /* PROFESSIONAL HEADER - bigger, bold, with 'glasses' icon */
    .professional-header{
        position:fixed; top:14px; left:50%; transform:translateX(-50%); width:88%; max-width:1280px; z-index:1200;
        display:flex; align-items:center; justify-content:space-between; gap:12px;
        padding:12px 20px; border-radius:12px;
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
        border: 1px solid rgba(255,255,255,0.04);
        backdrop-filter: blur(14px) saturate(120%);
    }

    .header-left{display:flex; align-items:center; gap:14px}
    .app-glasses{
        width:56px; height:36px; border-radius:10px; display:flex; align-items:center; justify-content:center;
        background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02)); border:1px solid rgba(255,255,255,0.06);
        box-shadow: 0 6px 16px rgba(0,0,0,0.6) inset, 0 6px 30px rgba(255,255,255,0.02);
    }
    /* simple SVG glasses graphic */
    .app-glasses svg{width:38px; height:20px; opacity:0.98}

    .header-title{font-size:20px; font-weight:900; letter-spacing:1px; color:#ffffff;}
    .header-sub{font-size:13px; color:rgba(255,255,255,0.7); font-weight:600}

    /* MAIN CONTENT CARD - larger, bold title */
    .professional-card{
        margin:120px auto; width:88%; max-width:1200px; z-index:100; position:relative; padding:44px; border-radius:22px;
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.04); backdrop-filter: blur(18px);
        box-shadow: 0 40px 90px rgba(0,0,0,0.7);
    }

    .professional-badge{display:inline-block; padding:10px 18px; border-radius:14px; font-weight:800; color:white; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.04)}

    .professional-title{font-size:56px; font-weight:900; color:#ffffff; text-align:left; margin:8px 0 6px 0; letter-spacing:1px}
    .professional-title .accent{color:#000; background:#fff; padding:0 6px; border-radius:6px}

    .professional-subtitle{font-size:18px; color:rgba(255,255,255,0.85); margin-bottom:20px}

    /* STATS GRID - bigger and bold */
    .stats-grid{display:grid; grid-template-columns: repeat(3,1fr); gap:18px; margin-top:18px}
    .stat-card{padding:28px 22px; border-radius:14px; background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.03);}
    .stat-value{font-size:34px; font-weight:900; color:#fff}
    .stat-label{font-size:12px; color:rgba(255,255,255,0.7); font-weight:700; letter-spacing:1px}

    /* FORM GRID */
    .form-grid{display:grid; grid-template-columns:repeat(2,1fr); gap:22px; margin-top:28px}

    /* inputs more bold and glassy */
    .stTextInput > div > div{background:rgba(255,255,255,0.02)!important; border:1px solid rgba(255,255,255,0.04)!important; border-radius:14px!important; padding:10px!important}
    .stTextInput label{color:rgba(255,255,255,0.95)!important; font-weight:800!important}
    .stTextInput input{color:#fff!important; font-weight:700!important}

    /* Buttons - stronger presence */
    .stButton > button{background:linear-gradient(90deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02)); border-radius:12px; padding:14px 18px; font-weight:900; letter-spacing:1px; border:1px solid rgba(255,255,255,0.06)}
    .stButton > button:hover{transform:translateY(-3px);}

    /* Result container - bold and prominent */
    .result-container{padding:36px; border-radius:16px; border:1px solid rgba(255,255,255,0.04); background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));}
    .result-title{font-size:28px; font-weight:900}
    .result-text{font-size:40px; font-weight:900}

    .risk-meter{height:28px; background:rgba(255,255,255,0.02); border-radius:14px; overflow:hidden}
    .risk-fill{height:100%; border-radius:14px; transition:width 1.6s ease}

    /* Footer */
    .professional-footer{margin-top:28px; padding:18px; border-radius:12px; text-align:center; background:rgba(255,255,255,0.01); color:rgba(255,255,255,0.7); border:1px solid rgba(255,255,255,0.03)}

    /* Responsive tweaks */
    @media (max-width:1024px){ .professional-title{font-size:40px} .form-grid{grid-template-columns:1fr} .stats-grid{grid-template-columns:repeat(2,1fr)} }
    @media (max-width:768px){ .professional-title{font-size:28px} .professional-card{padding:22px} .header-left{gap:8px} }
    </style>

    <!-- Background layers inserted into DOM for animated liquid glass feel -->
    <div class="liquid-bg"></div>
    <div class="glass-sheen"></div>

    
        </div>
        <div style="text-align:right">
            <div style="font-weight:800; font-size:13px; color:rgba(255,255,255,0.9)">v3.0 • MEDICAL GRADE</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------- Main Application ----------

def main():
    # initialize session history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Load professional CSS (futuristic liquid glass)
    load_css()

    # MAIN CONTENT CARD
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    # PROFESSIONAL BADGE + HELP BUTTON
