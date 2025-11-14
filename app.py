import numpy as np
import pickle
import streamlit as st
import os

model_path = os.path.join(os.path.dirname(__file__), "trained_model.sav")
with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

def diabetes_prediction(input_data):
    input_data = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return "The person is NOT diabetic" if prediction[0] == 0 else "The person IS diabetic"


# ---------------- CSS LIQUID GAS BACKGROUND ----------------
liquid_css = """
<style>
.stApp {
    background: radial-gradient(circle at 30% 20%, rgba(255,120,10,0.35), transparent 60%),
                radial-gradient(circle at 70% 80%, rgba(255,175,10,0.30), transparent 60%),
                linear-gradient(135deg, #111, #1b1b1b);
}

.bubble {
    position: fixed;
    width: 220px;
    height: 220px;
    background: radial-gradient(circle, rgba(255,140,40,0.35), rgba(255,140,40,0.05));
    border-radius: 50%;
    filter: blur(40px);
    animation: float 8s ease-in-out infinite;
    z-index: -1;
}

#b1 { top: 10%; left: 20%; animation-delay: 0s; }
#b2 { top: 50%; left: 60%; animation-delay: 2s; }
#b3 { top: 70%; left: 30%; animation-delay: 4s; }

@keyframes float {
    0%   { transform: translateY(0px) scale(1); }
    50%  { transform: translateY(-40px) scale(1.15); }
    100% { transform: translateY(0px) scale(1); }
}

/* glass card */
.glassbox {
    backdrop-filter: blur(20px);
    background: rgba(255,255,255,0.12);
    border-radius: 22px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.18);
}
</style>

<div class="bubble" id="b1"></div>
<div class="bubble" id="b2"></div>
<div class="bubble" id="b3"></div>
"""

def main():
    st.markdown(liquid_css, unsafe_allow_html=True)

    st.markdown("<h1 style='color:white;text-align:center;'>Diabetes Prediction</h1>", unsafe_allow_html=True)

    st.markdown("<div class='glassbox'>", unsafe_allow_html=True)

    labels = [
        "Number of Pregnancies","Glucose Level","Blood Pressure",
        "Skin Thickness","Insulin Level","BMI",
        "Diabetes Pedigree Function","Age"
    ]

    inputs = [st.text_input(label) for label in labels]

    if st.button("Predict"):
        st.success(diabetes_prediction(inputs))

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
