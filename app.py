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
# Toggle to quickly disable animated background for debugging or slow hosts
DEBUG_BACKGROUND = False

def load_css():
    """Load CSS. If DEBUG_BACKGROUND is False, insert a lightweight monochrome theme without heavy animated layers.
    If DEBUG_BACKGROUND is True, enable the full liquid-glass animated background.
    """
    if not DEBUG_BACKGROUND:
        # Lightweight safe CSS (no huge blurred layers) for reliable rendering
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600;800;900&display=swap');
        .stApp{ font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; background:#0b0b0b; color:#fff; }
        .professional-card{ margin:120px auto; width:88%; max-width:1100px; padding:28px; border-radius:18px; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.03); backdrop-filter: blur(8px);} 
        .professional-title{ font-size:48px; font-weight:900; color:#fff; margin-bottom:6px }
        .professional-badge{ display:inline-block; padding:8px 14px; border-radius:12px; font-weight:800; color:white; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.04)}
        .stTextInput label{ color:rgba(255,255,255,0.95)!important; font-weight:800!important }
        .stButton > button{ font-weight:800 }
        </style>
        """, unsafe_allow_html=True)
        # do not insert animated background layers
        return

    # Full animated background (only used when DEBUG_BACKGROUND == True)
    st.markdown("""
    <style>
    /* Base app - full black/white glassy theme */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600;800;900&display=swap');

    .stApp{ font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; background:#0b0b0b; color:#fff; min-height:100vh; overflow-x:hidden; }
    .liquid-bg{ position:fixed; inset:0; z-index:0; pointer-events:none; background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.01) 50%, rgba(255,255,255,0.03) 100%); backdrop-filter: blur(8px); mix-blend-mode: screen; will-change: transform, opacity; }
    .liquid-bg::before, .liquid-bg::after{ content:""; position:absolute; width:130vmax; height:130vmax; left:50%; top:50%; transform:translate(-50%,-50%); background: radial-gradient(circle at 25% 30%, rgba(255,255,255,0.08), rgba(255,255,255,0.00) 35%), radial-gradient(circle at 70% 70%, rgba(255,255,255,0.06), rgba(255,255,255,0.00) 30%); filter: blur(80px) saturate(130%); animation: floatyFast 8s ease-in-out infinite; opacity:0.95; mix-blend-mode: screen; }
    .liquid-bg::after{ background: radial-gradient(circle at 40% 60%, rgba(255,255,255,0.06), rgba(255,255,255,0.00) 30%), radial-gradient(circle at 60% 30%, rgba(255,255,255,0.07), rgba(255,255,255,0.00) 30%); animation-duration: 10s; transform: translate(-52%,-48%) scale(1.02); opacity:0.92; filter: blur(90px) saturate(140%); }
    @keyframes floatyFast{ 0% { transform: translate(-50%,-50%) scale(1) rotate(0deg); opacity:0.95 } 25% { transform: translate(-46%,-54%) scale(1.08) rotate(3deg); opacity:1 } 50% { transform: translate(-50%,-50%) scale(1.12) rotate(6deg); opacity:0.96 } 75% { transform: translate(-54%,-46%) scale(1.06) rotate(-3deg); opacity:1 } 100% { transform: translate(-50%,-50%) scale(1) rotate(0deg); opacity:0.95 } }
    .glass-sheen{ position:fixed; inset:0; z-index:1; pointer-events:none; mix-blend-mode:overlay; background: linear-gradient(120deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.08) 50%, rgba(255,255,255,0.01) 100%); animation: sheen 6s linear infinite, sheenPulse 5.8s ease-in-out infinite; opacity:0.98; }
    @keyframes sheen { from {background-position:0% 50%;} to {background-position:100% 50%;} } @keyframes sheenPulse { 0% { opacity:0.92 } 50% { opacity:1 } 100% { opacity:0.92 } }

    /* rest of CSS (cards, inputs) unchanged for brevity */
    .professional-card{ margin:120px auto; width:88%; max-width:1200px; z-index:100; position:relative; padding:44px; border-radius:22px; background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border: 1px solid rgba(255,255,255,0.04); backdrop-filter: blur(18px); box-shadow: 0 40px 90px rgba(0,0,0,0.7); }
    .professional-badge{display:inline-block; padding:10px 18px; border-radius:14px; font-weight:800; color:white; background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.04)}
    .professional-title{font-size:56px; font-weight:900; color:#ffffff; text-align:left; margin:8px 0 6px 0; letter-spacing:1px}
    </style>

    <!-- Background layers inserted into DOM for animated liquid glass feel -->
    <div class="liquid-bg"></div>
    <div class="glass-sheen"></div>
    """, unsafe_allow_html=True)



# ---------- Main Application ----------

def main():
    # initialize session history
    if 'history' not in st.session_state:
        st.session_state.history = []
    # Load professional CSS (futuristic liquid glass)
    load_css()

    # DEBUG BANNER (temporary) - visible marker to ensure app renders despite heavy CSS
    st.markdown('<div style="position:relative; z-index:9999; color:#fff; font-weight:900; padding:10px 18px; background:rgba(0,0,0,0.35); border-radius:8px; margin-bottom:12px">🔧 App loaded — if you see a blank page, disable the liquid background in load_css()</div>', unsafe_allow_html=True)

    # MAIN CONTENT CARD
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    # PROFESSIONAL BADGE + HELP BUTTON
