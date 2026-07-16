# *******************Import required libraries
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
# Import common UI components
from Utilities import (
    show_header,
    show_disclaimer,
    show_footer
)

# Project Path
BASE_DIR = Path(__file__).resolve().parent

# Load Trained Machine Learning Model
model = joblib.load(BASE_DIR / "cardio_predict.pkl")
expected_columns = joblib.load(BASE_DIR / "cardio_columns.pkl")

# Prediction Page

def prediction_page():

    show_header("Prediction")

    st.markdown("""
    <style>

    /* ==========================================================
       Labels
       Age, Gender, Resting Blood Pressure, Chest Pain Type...
       ========================================================== */

    label[data-testid="stWidgetLabel"] p{
        font-size:24px !important;
        font-weight:700 !important;
    }

    /* ==========================================================
       Number input values
       40, 120, 200, 150, 1.00
       ========================================================== */

    div[data-testid="stNumberInput"] input{
        font-size:24px !important;
        font-weight:600 !important;
    }

    /* ==========================================================
       + and - buttons
       ========================================================== */

    div[data-testid="stNumberInput"] button{
        font-size:22px !important;
    }

    /* ==========================================================
       Selected dropdown value
       Male, ATA, No, Normal, Up
       ========================================================== */

    div[data-testid="stSelectbox"] input{
    font-size:24px !important;
    font-weight:600 !important;
    }

    /* ==========================================================
       Dropdown options
       Male, Female, ATA, NAP, TA...
       ========================================================== */

    div[role="option"]{
    font-size:24px !important;
    font-weight:600 !important;
    }

    /* ==========================================================
       Predict Button
       ========================================================== */

    div[data-testid="stButton"] button{
        height:65px !important;
        padding:0 25px !important;
    }

    div[data-testid="stButton"] button p{
        font-size:24px !important;
        font-weight:700 !important;
    }

    </style>
    """, unsafe_allow_html=True)


    # Patient Information

    st.header("🩺 Patient Information")

    left, right = st.columns(2)

    with left:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=40
        )

        resting_bp = st.number_input(
            "Resting Blood Pressure",
            min_value=50,
            max_value=250,
            value=120
        )

        cholesterol = st.number_input(
            "Cholesterol",
            min_value=50,
            max_value=700,
            value=200
        )

        max_hr = st.number_input(
            "Maximum Heart Rate",
            min_value=50,
            max_value=250,
            value=150
        )

        oldpeak = st.number_input(
            "Old Peak",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=0.1
        )

        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"]
        )

    with right:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "TA", "ASY"]
        )

        fasting_bs = st.selectbox(
            "Fasting Blood Sugar",
            ["No", "Yes"]
        )

        exercise_angina = st.selectbox(
            "Exercise Angina",
            ["No", "Yes"]
        )

        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

    st.divider()

    predict = st.button(
        "❤️ Predict Heart Disease Risk"
    )

    # Generate Prediction

    if predict:

        # Label Encoding

        gender = 1 if gender == "Male" else 0
        exercise_angina = 1 if exercise_angina == "Yes" else 0
        fasting_bs = 1 if fasting_bs == "Yes" else 0

        # Create Model Input Features

        input_data = {

            "Age": age,
            "Gender": gender,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_bs,
            "MaxHR": max_hr,
            "ExerciseAngina": exercise_angina,
            "Oldpeak": oldpeak,

            "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
            "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,

            "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
            "RestingECG_ST": 1 if resting_ecg == "ST" else 0,

            "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
            "ST_Slope_Up": 1 if st_slope == "Up" else 0
        }

        # Convert Input Data to DataFrame

        input_df = pd.DataFrame([input_data])

        # Match the feature order used during model training
        input_df = input_df.reindex(
            columns=expected_columns,
            fill_value=0
        )

        # Prediction
        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0]

        risk = probability[1] * 100

        st.divider()

        # Assessment Result

        st.header("🩺 Assessment Result")

        if prediction == 1:

            st.markdown("""
            <div style="
            background-color:#F8D7DA;
            border-left:8px solid #DC3545;
            padding:18px;
            border-radius:10px;
            font-size:30px;
            font-weight:bold;
            color:#721C24;
            ">
            ⚠ High Risk of Heart Disease
            </div>
            """, unsafe_allow_html=True)

            st.metric(
                "Estimated Risk",
                f"{risk:.1f}%"
            )

            st.markdown("""
            <div style="
            background-color:#F8D7DA;
            border-left:8px solid #DC3545;
            padding:18px;
            border-radius:10px;
            font-size:22px;
            line-height:1.6;
            color:#721C24;
            ">

            The assessment indicates an increased likelihood of heart disease.

            This result represents an early risk assessment and should not be considered a medical diagnosis.

            Please consult a qualified healthcare professional for further evaluation.

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div style="
            background-color:#D1E7DD;
            border-left:8px solid #198754;
            padding:18px;
            border-radius:10px;
            font-size:30px;
            font-weight:bold;
            color:#0F5132;
            ">
            ✅ Low Risk of Heart Disease
            </div>
            """, unsafe_allow_html=True)

            st.metric(
                "Estimated Risk",
                f"{risk:.1f}%"
            )

            st.markdown("""
            <div style="
            background-color:#D1E7DD;
            border-left:8px solid #198754;
            padding:18px;
            border-radius:10px;
            font-size:22px;
            line-height:1.6;
            color:#0F5132;
            ">

            The assessment indicates a lower likelihood of heart disease based on the provided information.

            Maintaining a healthy lifestyle and regular medical check-ups is recommended.

            </div>
            """, unsafe_allow_html=True)

        # Patient Summary

        st.divider()

        st.header("📋 Patient Summary")
        summary = pd.DataFrame({

            "Clinical Parameter": [

                "Age",
                "Gender",
                "Resting Blood Pressure",
                "Cholesterol",
                "Maximum Heart Rate",
                "Fasting Blood Sugar",
                "Chest Pain Type",
                "Exercise Angina",
                "Resting ECG",
                "ST Slope",
                "Old Peak"

            ],

            "Value": [

                age,
                "Male" if gender == 1 else "Female",
                resting_bp,
                cholesterol,
                max_hr,
                "Yes" if fasting_bs else "No",
                chest_pain,
                "Yes" if exercise_angina else "No",
                resting_ecg,
                st_slope,
                oldpeak

            ]

        })

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

    # Medical Disclaimer

    show_disclaimer()

    # Footer

    show_footer()