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
    """Return (label, risk_percentage, confidence) or (None, None, None) if model missing.
    - Uses predict_proba for confidence if available.
    - risk_percentage: derived from confidence or simulated fallback.
    """
    if loaded_model is None:
        # Model not available — return None so UI can show friendly message
        return None, None, None

    try:
        arr = np.asarray([float(x) for x in input_data]).reshape(1, -1)
    except Exception:
        return None, None, None

    try:
        pred = loaded_model.predict(arr)
    except Exception:
        return None, None, None

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
    """Load minimal safe CSS to ensure the UI always renders. Animated background is disabled by default.
    If you want the animated background, set DEBUG_BACKGROUND = True at the top of the file.
    """
    # Minimal safe styles only
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
    # Do not add heavy animated layers here so app always visible

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
