# *******************Import required libraries
import streamlit as st
# Import common UI components
from Utilities import (
    show_header,
    show_disclaimer,
    show_footer
)

# About Page
def about_page():

    show_header("About")

    st.markdown("""
        <style>

        /* Success Box Text */
        div[data-testid="stAlert"] p{
            font-size:22px !important;
            font-weight:600;
        }

        /* Metric Labels */
        div[data-testid="stMetricLabel"] p{
            font-size:22px !important;
            font-weight:700;
        }

        /* Metric Values */
        div[data-testid="stMetricValue"] p{
            font-size:28px !important;
            font-weight:700;
        }
        
        </style>
        """, unsafe_allow_html=True)

    # Project Overview
    st.header("❤️ Project Overview")

    st.markdown("""
    <div style="font-size:21px; line-height:1.8; text-align:justify;">

    The Cardio Prediction System is a Machine Learning-based web
    application developed to estimate the likelihood of heart disease
    using patient clinical information.

    The application utilizes a trained <b>Decision Tree Classifier</b>
    to analyze important cardiovascular risk factors and provide an
    early prediction within seconds.

    It is intended for educational purposes, preliminary risk
    assessment, and demonstration of Machine Learning in healthcare.

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Project Objectives
    st.header("🎯 Project Objectives")

    left, right = st.columns(2)

    with left:
        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:8px solid #28A745;
        padding:18px;
        border-radius:10px;
        font-size:20px;
        font-weight:700;
        color:#198754;
        margin-bottom:15px;
        ">
        Provide instant heart disease risk prediction
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:8px solid #28A745;
        padding:18px;
        border-radius:10px;
        font-size:20px;
        font-weight:700;
        color:#198754;
        margin-bottom:15px;
        ">
        Support preliminary patient screening
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:8px solid #28A745;
        padding:18px;
        border-radius:10px;
        font-size:20px;
        font-weight:700;
        color:#198754;
        ">
        Promote cardiovascular health awareness
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:8px solid #28A745;
        padding:18px;
        border-radius:10px;
        font-size:20px;
        font-weight:700;
        color:#198754;
        margin-bottom:15px;
        ">
        Assist healthcare professionals
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:8px solid #28A745;
        padding:18px;
        border-radius:10px;
        font-size:20px;
        font-weight:700;
        color:#198754;
        margin-bottom:15px;
        ">
        Demonstrate Machine Learning applications
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:8px solid #28A745;
        padding:18px;
        border-radius:10px;
        font-size:20px;
        font-weight:700;
        color:#198754;
        ">
        Encourage timely medical consultation
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # Key Features
    st.header("✨ Key Features")

    left, right = st.columns(2)

    with left:
        for item in [
            "Decision Tree Classification",
            "Instant Risk Assessment",
            "Simple & User-Friendly Interface",
            "Professional Clinical Dashboard"
        ]:
            st.markdown(f"""
            <div style="
            background:#E8F5E9;
            border-left:8px solid #28A745;
            padding:18px;
            border-radius:10px;
            font-size:20px;
            font-weight:700;
            color:#198754;
            margin-bottom:15px;
            ">
            {item}
            </div>
            """, unsafe_allow_html=True)

    with right:

        for item in [
            "Interactive Data Visualization",
            "Dataset Exploration",
            "Local Machine Learning Prediction",
            "Educational Healthcare Tool"
        ]:
            st.markdown(f"""
            <div style="
            background:#E8F5E9;
            border-left:8px solid #28A745;
            padding:18px;
            border-radius:10px;
            font-size:20px;
            font-weight:700;
            color:#198754;
            margin-bottom:15px;
            ">
            {item}
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # Intended Users
    st.header("👥 Intended Users")

    doctor, student, patient = st.columns(3)

    with doctor:

        st.info("""
### 👨‍⚕️ Healthcare Professionals

Use the system as a supporting tool for
preliminary cardiovascular risk assessment.
""")

    with student:

        st.info("""
### 👩‍🎓 Students & Researchers

Learn how Machine Learning can be applied
to disease prediction using clinical data.
""")

    with patient:

        st.info("""
### ❤️ Patients

Obtain an early assessment of heart disease
risk and improve health awareness.
""")

    st.divider()

    # Dataset Information
    st.header("📊 Dataset Information")

    left, right = st.columns(2)

    with left:

        st.metric("Dataset", "Heart Disease")

        st.metric("Prediction Type", "Binary Classification")

        st.metric("Target Variable", "HeartDisease")

    with right:

        st.metric("Clinical Features", "11")

        st.metric("Machine Learning", "Decision Tree")

        st.metric("Platform", "Streamlit")

    st.divider()

    # System Summary
    st.header("📋 System Summary")

    st.markdown("""
<div style="
background:#E8F4FD;
border-left:8px solid #0D6EFD;
padding:20px;
border-radius:10px;
font-size:20px;
line-height:1.9;
">

<b>The Cardio Prediction System combines Machine Learning and
clinical information to provide an efficient heart disease
risk assessment tool.</b>

✔ Decision Tree Classifier

✔ Binary Heart Disease Prediction

✔ Interactive Patient Dashboard

✔ Clinical Data Visualization

✔ Dataset Exploration

✔ Educational Machine Learning Demonstration

✔ Professional Streamlit Interface

</div>
""", unsafe_allow_html=True)

    st.divider()

    # Medical Disclaimer
    show_disclaimer()

    # Footer
    show_footer()