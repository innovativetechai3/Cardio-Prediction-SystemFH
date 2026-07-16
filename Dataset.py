# *******************Import required libraries
import streamlit as st
import pandas as pd
from pathlib import Path
# Import common UI components
from Utilities import (
    show_header,
    show_disclaimer,
    show_footer
)

# Paths
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "Data" / "heartdiseaseFH.csv")


def dataset_page():
    show_header("Dataset")
    st.markdown("""
    <style>
    .block-container{
        padding-top:1rem;
        padding-bottom:1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Dataset Summary
    st.header("📋 Dataset Summary")

    missing = df.isnull().sum().sum()

    st.markdown(f"""
    <div style="
    background:#eef7ff;
    padding:20px;
    border-left:6px solid #0d6efd;
    border-radius:8px;
    ">

    <p style="font-size:19px; line-height:1.8;">

    <b>Dataset Name:</b> Heart Disease Prediction Dataset<br>

    <b>Total Patients:</b> {df.shape[0]}<br>

    <b>Total Clinical Features:</b> {df.shape[1] - 1}<br>

    <b>Target Variable:</b> HeartDisease<br>

    <b>Missing Values:</b> {missing}<br>

    <b>Machine Learning Algorithm:</b> Decision Tree Classifier

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Dataset Metrics
    m1, m2, m3, m4, m5, m6 = st.columns(6)

    m1.metric("👨 Patients", df.shape[0])

    m2.metric("🩺 Features", df.shape[1] - 1)

    m3.metric("🎯 Target", "1")

    m4.metric("❌ Missing", missing)

    m5.metric("📂 Format", "CSV")

    m6.metric("🤖 Model", "Decision Tree")

    st.divider()

    # Patient Data Preview
    st.header("🩺 Patient Data Preview")

    st.markdown("""
    <p style="font-size:20px;">
    The table below displays the first five patient records from the
    heart disease dataset used during model development.
    </p>
    """, unsafe_allow_html=True)

    st.dataframe(
        df.head(),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Feature Information
    st.header("📑 Feature Information")

    feature_info = pd.DataFrame({

        "Feature Name": df.columns,

        "Data Type": df.dtypes.astype(str).values

    })

    st.dataframe(
        feature_info,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Dataset Integrity Check
    st.header("✔ Dataset Integrity")

    missing_values = df.isnull().sum()

    if missing_values.sum() == 0:

        st.markdown("""
        <div style="
        background:#E8F5E9;
        border-left:6px solid #198754;
        padding:18px;
        border-radius:8px;
        ">

        <h2 style="
        color:#198754;
        margin-top:0;
        font-size:22px;
        ">
        ✅ Dataset Validation Successful
        </h2>

        <p style="font-size:20px; line-height:1.8;">

        No missing values were detected.

        <br><br>

        The dataset is complete, clean, and ready for
        machine learning model training and evaluation.

        </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.warning("Missing values were detected in the dataset.")

        missing_df = pd.DataFrame({

            "Feature": missing_values.index,

            "Missing Values": missing_values.values

        })

        missing_df = missing_df[missing_df["Missing Values"] > 0]

        st.dataframe(
            missing_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # Clinical Statistics
    st.header("📈 Clinical Statistics")

    st.markdown("""
    <p style="font-size:20px;">
    The statistical summary below provides descriptive measures for
    all numerical clinical variables including count, mean, standard
    deviation, minimum, maximum and quartile values.
    </p>
    """, unsafe_allow_html=True)

    st.dataframe(
        df.describe().T,
        use_container_width=True
    )

    st.divider()

    # Clinical Features
    st.header("🧬 Clinical Features Included")

    left, right = st.columns(2)

    with left:

        st.markdown("""
    ### Patient Demographics

    - 👤 Age
    - 🚻 Gender

    ### Vital Signs

    - ❤️ Resting Blood Pressure
    - 💓 Maximum Heart Rate

    ### Laboratory Measurements

    - 🧪 Cholesterol
    - 🍬 Fasting Blood Sugar
    """)

    with right:

        st.markdown("""
    ### Clinical Examination

    - 🩺 Chest Pain Type
    - 📈 Resting ECG
    - 🏃 Exercise-Induced Angina
    - 📉 ST Slope
    - 📊 Old Peak

    ### Target Variable

    - 🎯 Heart Disease
    """)

    st.divider()

    # Target Variable
    st.header("🎯 Target Variable")

    st.markdown("""
    <div style="
    background:#eef7ff;
    border-left:6px solid #0d6efd;
    padding:18px;
    border-radius:8px;
    ">

    <p style="font-size:20px; line-height:1.8;">

    <b>HeartDisease</b> is the target variable used for prediction.

    <ul style="font-size:19px;">

    <li><b>0</b> → No Heart Disease</li>

    <li><b>1</b> → Heart Disease</li>

    </ul>

    The Decision Tree classifier learns relationships between
    the clinical features and this target variable to estimate
    a patient's likelihood of heart disease.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Dataset Source
    st.header("📚 Dataset Source")

    st.markdown("""
    <div style="
    background:#EEF7FF;
    border-left:6px solid #0D6EFD;
    padding:18px;
    border-radius:8px;
    ">

    <p style="font-size:20px; line-height:1.8;">

    This project uses the Heart Disease Prediction Dataset containing
    918 anonymized patient records collected from multiple clinical
    examinations.

    The dataset includes demographic information,
    laboratory measurements, ECG findings, exercise test results,
    and other cardiovascular indicators commonly used in heart
    disease risk assessment.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Medical Disclaimer
    show_disclaimer()

    # Footer
    show_footer()