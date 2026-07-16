# ❤️ Cardio Prediction System

A Machine Learning web application developed using **Python**, **Scikit-learn**, and **Streamlit** to predict the likelihood of heart disease based on patient clinical information.

The application provides an intuitive interface for entering patient data and instantly predicts whether a patient is at risk of heart disease.

---

# Project Overview
The Cardio Prediction System is a Machine Learning-based web application developed to estimate the likelihood of heart disease using patient clinical information.

The application utilizes a trained Decision Tree Classifier to analyze important cardiovascular risk factors and provide an early prediction within seconds.

It is intended for educational purposes, preliminary risk assessment, and demonstration of Machine Learning in healthcare.

## Features

- Heart disease risk prediction
- User-friendly Streamlit interface
- Decision Tree Classification model
- Patient summary after prediction
- Dataset explorer
- Interactive data visualizations
- Model performance metrics
- Responsive and clean UI

---

## Machine Learning Workflow

- Data Collection
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Feature Selection
- Model Training
- Model Evaluation
- Model Deployment using Streamlit

---

## Algorithm Used

- Decision Tree Classifier

---

## Dataset Features

The model uses the following patient attributes:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

# Model Performance

| Metric | Value |
|--------|------:|
| Algorithm | Decision Tree Classifier |
| Prediction Type | Binary Classification |
| Accuracy | **78.80%** |
| Precision (Weighted Avg.) | **79.02%** |
| Recall (Weighted Avg.) | **78.80%** |
| F1-Score (Weighted Avg.) | **78.85%** |

---

## Confusion Matrix

| Actual \ Predicted | No Heart Disease | Heart Disease |
|-------------------|-----------------:|--------------:|
| No Heart Disease | 65 | 17 |
| Heart Disease | 22 | 80 |

---

## Key Findings

- Decision Tree Classifier achieved **78.80%** prediction accuracy.
- **ST_Slope_Flat** was the most influential feature for prediction.
- **Oldpeak**, **Maximum Heart Rate (MaxHR)** and **Gender** were among the most important predictive features.
- The application provides real-time heart disease risk prediction through an interactive Streamlit interface.

---

# Web Application

The project includes a professional web application developed using **Streamlit** with custom **HTML** and **CSS** for an enhanced and responsive user interface.

## Web Application Features

- Professional Streamlit web application
- Custom HTML & CSS styling
- User-friendly interface
- Real-time heart disease prediction
- Interactive dashboard
- Patient clinical data input
- Instant risk assessment
- Dataset explorer
- Interactive visualizations
- Responsive layout

---

# How to Run

## Clone the Repository

```bash
git clone https://github.com/<your-username>/Cardio-Prediction-System.git
```

## Navigate to the Project Directory

```bash
cd Cardio-Prediction-System
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit pandas numpy scikit-learn matplotlib joblib
```

## Launch the Application

```bash
streamlit run App.py
```

## Open in Your Browser

If the browser does not open automatically, visit:

```
http://localhost:8501
```

---

# Future Enhancements

- Random Forest Classifier
- XGBoost Classifier
- Hyperparameter Tuning
- Cross Validation
- Probability-Based Risk Score
- PDF Report Generation
- User Authentication
- Cloud Deployment
- Docker Containerization

---

# Author

**Farhana Hameed**

© 2026 Innovative Tech. All Rights Reserved.