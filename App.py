# *******************Import required libraries
import streamlit as st
from pathlib import Path
from Utilities import load_css
from Home import home_page
from Prediction import prediction_page
from Dataset import dataset_page
from Visualizations import visualizations_page
from About import about_page

# Project Paths
BASE_DIR = Path(__file__).resolve().parent
logo_path = BASE_DIR / "images" / "cardio_logo.png"

# Page Configuration
st.set_page_config(
    page_title="Cardio Prediction System",
    page_icon=logo_path,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
load_css()

# Sidebar Navigation Style
st.markdown("""
<style>

/* Sidebar title */
[data-testid="stSidebar"] h3{
    font-size:24px;
    font-weight:700;
    color:#0d6efd;
}

/* Remove extra spacing */
[data-testid="stSidebar"]{
    padding-top:10px;
}

/* Radio button labels */
div[role="radiogroup"] label{
    background:white;
    border-radius:10px;
    padding:12px 16px;
    margin-bottom:8px;
    border:1px solid #E5E7EB;
    transition:all .25s ease;
}

/* Hover effect */
div[role="radiogroup"] label:hover{
    background:#EAF3FF;
    border-color:#0d6efd;
    cursor:pointer;
}

/* Selected option */
div[role="radiogroup"] label:has(input:checked){
    background:#0d6efd;
    color:white;
    border-color:#0d6efd;
    font-weight:600;
}

/* Hide default radio circles */
div[role="radiogroup"] input[type="radio"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:

    page = st.radio(
        "",
        [
            "🏠 Home",
            "❤️ Prediction",
            "📋 Dataset",
            "📈 Visualizations",
            "📝 About"
        ],
        label_visibility="collapsed"
    )

# Routing

if page == "🏠 Home":
    home_page()

elif page == "❤️ Prediction":
    prediction_page()

elif page == "📋 Dataset":
    dataset_page()

elif page == "📈 Visualizations":
    visualizations_page()

elif page == "📝 About":
    about_page()