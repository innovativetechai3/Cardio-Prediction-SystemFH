# *******************Import required libraries
import streamlit as st
# Import common UI components
from Utilities import (
    show_header,
    show_disclaimer,
    show_footer
)

# Feature Box
def feature_box(text):
    st.markdown(f"""
    <div style="
        background:#d4edda;
        color:#155724;
        padding:14px;
        border-radius:10px;
        font-size:20px;
        font-weight:600;
        margin-bottom:12px;
        border-left:6px solid #28a745;
        box-shadow:0 2px 6px rgba(0,0,0,0.08);
    ">
        ✔ {text}
    </div>
    """, unsafe_allow_html=True)

# Home Page
def home_page():

    show_header("App")

    # Welcome
    st.header("Welcome")

    st.markdown("""
    <div style="font-size:22px; line-height:1.8; text-align:justify;">

    Welcome to the <b>Cardio Prediction System</b>.

    This application helps estimate the likelihood of heart disease using
    important health information. The prediction is generated within seconds
    to support early awareness and risk assessment.

    The system utilizes a trained <b>Machine Learning Model</b>
    to analyze patient information and classify the possibility of heart disease.

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Why Choose This Application
    st.header("Why Choose This Application?")

    left, right = st.columns(2)

    with left:
        feature_box("Quick Risk Assessment")
        feature_box("Easy to Use")
        feature_box("Instant Prediction")

    with right:
        feature_box("Supports Early Detection")
        feature_box("Secure & Private")
        feature_box("Accessible Anywhere")

    st.divider()

    # How It Works
    st.header("🩺 How It Works")

    st.markdown("""
    <div style="font-size:22px; line-height:1.8;">
    The prediction is based on several health-related factors,
    including age, blood pressure, cholesterol level, heart rate,
    chest pain type, and other clinical information.

    <br>

    Simply enter the required information on the <b>Prediction</b>
    page, and the system will estimate the likelihood of heart
    disease.

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Getting Starteds
    st.header("Getting Started")

    st.markdown("""
    <div style="
    background:#E8F4FD;
    border-left:6px solid #2196F3;
    padding:20px;
    border-radius:10px;
    font-size:22px;
    line-height:1.8;
    ">

    <b>Follow these simple steps:</b>

    <ol>
    <li>Open the <b>Prediction</b> page from the navigation menu.</li>
    <li>Enter all required patient information.</li>
    <li>Click the <b>Predict</b> button.</li>
    <li>Review the generated prediction.</li>
    <li>If the prediction indicates possible heart disease, consult a qualified healthcare professional.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    show_disclaimer()

    show_footer()