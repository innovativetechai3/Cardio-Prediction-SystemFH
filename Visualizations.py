# *******************Import required libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import joblib
# Import common UI components
from Utilities import (
    show_header,
    show_disclaimer,
    show_footer
)
def visualizations_page():

    st.write("")
    show_header("Visualization")

    # Paths
    BASE_DIR = Path(__file__).resolve().parent
    IMAGE_DIR = BASE_DIR
    DATA_PATH = BASE_DIR / "Data" / "heartdiseaseFH.csv"
    HISTOGRAM = IMAGE_DIR / "HistplotFH.png"
    BOXPLOT = IMAGE_DIR / "BoxplotFH.png"
    HEATMAP = IMAGE_DIR / "HeatmapFH.png"
    CONFUSION = IMAGE_DIR / "conf_mtxFH.png"
    FEATURE = IMAGE_DIR / "featuresFH.png"
    TREE = IMAGE_DIR / "dt_clfFH.png"
    METRICS = BASE_DIR / "cardio_metrics.pkl"

    # Load Dataset
    @st.cache_data
    def load_dataset(path):
        return pd.read_csv(path)

    @st.cache_resource
    def load_metrics(path):
        return joblib.load(path)

    df = load_dataset(DATA_PATH)
    metrics = load_metrics(METRICS)

    # Page Title
    st.header("📈 Data Visualization Dashboard")

    st.markdown("""
    <div style="font-size:21px; line-height:1.8; text-align:justify;">
    
    This dashboard presents exploratory data analysis and machine learning
    visualizations generated from the heart disease dataset.
    
    The charts help patients, healthcare professionals, and researchers
    better understand the dataset, important clinical variables, and the
    performance of the trained Decision Tree model.
    
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Dataset Overview
    st.header("📊 Dataset Overview")

    total_records = len(df)
    total_features = df.shape[1] - 1

    patients_with_disease = int(df["HeartDisease"].sum())
    patients_without_disease = total_records - patients_with_disease

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Records",
            total_records
        )

    with col2:
        st.metric(
            "Total Features",
            total_features
        )

    with col3:
        st.metric(
            "Heart Disease",
            patients_with_disease
        )

    with col4:
        st.metric(
            "No Heart Disease",
            patients_without_disease
        )

    st.markdown("""
    <div style="font-size:20px; line-height:1.8; text-align:justify;">
    
    The dataset contains demographic and clinical information used to train
    the Decision Tree classifier for early heart disease risk assessment.
    
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Distribution Analysis
    st.header("📈 Distribution Analysis")

    st.markdown("""
    <div style="font-size:20px; line-height:1.8; text-align:justify;">
    
    Distribution plots illustrate how numerical clinical variables are
    spread across the patient population. These visualizations help identify
    common value ranges, skewness, and potential abnormalities.
    
    </div>
    """, unsafe_allow_html=True)

    # ---------------- Histogram ----------------

    with st.expander("📊 Histogram of Numerical Features", expanded=True):

        if HISTOGRAM.exists():

            st.image(
                HISTOGRAM,
                use_container_width=True
            )

        else:

            st.warning("Histogram image not found.")

    # ---------------- Boxplot ----------------

    with st.expander("📦 Boxplots for Outlier Detection", expanded=True):

        if BOXPLOT.exists():

            st.image(
                BOXPLOT,
                use_container_width=True
            )

        else:

            st.warning("Boxplot image not found.")

    st.divider()

    # Correlation Analysis
    st.header("🔥 Correlation Analysis")

    st.markdown("""
    <div style="font-size:20px; line-height:1.8; text-align:justify;">
    
    The correlation heatmap illustrates the strength and direction of
    relationships between numerical variables.
    
    Positive values indicate a direct relationship, whereas negative values
    indicate an inverse relationship.
    
    Variables with stronger correlations may contribute more significantly
    to heart disease prediction.
    
    </div>
    """, unsafe_allow_html=True)

    if HEATMAP.exists():

        st.image(
            HEATMAP,
            use_container_width=True
        )

    else:

        st.warning("Correlation heatmap image not found.")

    st.divider()

    # Model Performance
    st.header("🎯 Model Performance")

    st.markdown("""
    <div style="font-size:20px; line-height:1.8; text-align:justify;">
    
    The confusion matrix evaluates the predictive performance of the trained
    Decision Tree Classifier by comparing the actual class labels with the
    predicted outcomes.
    
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Accuracy",
            f"{metrics['accuracy']*100:.2f}%"
        )

    with col2:
        st.metric(
            "Precision",
            f"{metrics['precision']*100:.2f}%"
        )

    with col3:
        st.metric(
            "Recall",
            f"{metrics['recall']*100:.2f}%"
        )

    with col4:
        st.metric(
            "F1 Score",
            f"{metrics['f1_score']*100:.2f}%"
        )

    # Feature Importance
    st.header("⭐ Feature Importance")

    st.markdown("""
    <div style="font-size:20px; line-height:1.8; text-align:justify;">
    
    Feature importance identifies which clinical variables contributed most
    to the Decision Tree model during prediction.
    
    Higher importance values indicate greater influence on the final
    prediction.
    
    </div>
    """, unsafe_allow_html=True)

    if FEATURE.exists():

        st.image(
            FEATURE,
            use_container_width=True
        )

    else:

        st.warning("Feature importance image not found.")

    st.markdown("""
    <div style="
    background:#EEF7FF;
    border-left:8px solid #0D6EFD;
    padding:20px;
    border-radius:10px;
    ">

    <p style="
    font-size:24px;
    font-weight:bold;
    margin-top:0;
    ">

    Key observations:

    </p>

    <p style="
    font-size:22px;
    line-height:2.0;
    ">

    • <b>ST_Slope_Flat</b> is the most influential predictor.

    • <b>Oldpeak</b> is the second most important feature.

    • <b>MaxHR</b>, <b>Gender</b>, and <b>Chest Pain Type</b> also contribute to prediction.

    • Features with near-zero importance have minimal influence on the Decision Tree model.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Decision Tree Visualization
    st.header("🌳 Decision Tree Visualization")

    st.markdown("""
    <div style="font-size:20px; line-height:1.8; text-align:justify;">
    
    The Decision Tree Classifier is the Machine Learning model used to
    estimate the likelihood of heart disease.
    
    Each internal node represents a clinical decision based on a patient's
    health attributes, while each leaf node represents the predicted
    classification.
    
    The visualization below illustrates how the model reaches its decisions.
    
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🌳 View Complete Decision Tree", expanded=False):

        if TREE.exists():

            st.image(
                TREE,
                use_container_width=True
            )

        else:

            st.warning("Decision Tree image not found.")

    st.divider()

    # Dashboard Summary
    st.header("📋 Dashboard Summary")

    st.markdown("""
    <div style="
    background-color:#E8F4FD;
    border-left:8px solid #0D6EFD;
    padding:20px;
    border-radius:10px;
    font-size:20px;
    line-height:1.9;
    ">
    
    <b>This dashboard provides a comprehensive overview of the Heart Disease
    dataset and the trained Machine Learning model.</b>
    
    ✔ Dataset Overview summarizes patient records and dataset characteristics.
    
    ✔ Distribution Analysis illustrates the spread of important clinical
    features.
    
    ✔ Correlation Analysis identifies relationships among numerical
    variables.
    
    ✔ Model Performance demonstrates the predictive capability of the
    Decision Tree classifier.
    
    ✔ Feature Importance highlights the clinical variables that contribute
    most significantly to heart disease prediction.
    
    ✔ Decision Tree Visualization explains how the Machine Learning model
    arrives at its prediction.
    
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Clinical Interpretation
    st.header("🩺 Clinical Interpretation")

    st.markdown("""
    <div style="
    background-color:#F8F9FA;
    border-left:8px solid #198754;
    padding:20px;
    border-radius:10px;
    font-size:20px;
    line-height:1.9;
    ">
    
    The presented visualizations are intended to improve understanding of the
    dataset and the Decision Tree model.
    
    The prediction generated by this application should be considered an
    early risk assessment tool rather than a medical diagnosis.
    
    Healthcare professionals should interpret the results in conjunction
    with clinical history, physical examination, laboratory findings, and
    other diagnostic investigations.
    
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Medical Disclaimer
    show_disclaimer()

    # Footer
    show_footer()