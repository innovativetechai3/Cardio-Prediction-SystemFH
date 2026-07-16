# *******************Import required libraries
import streamlit as st
import base64
from pathlib import Path

# Project Paths
BASE_DIR = Path(__file__).resolve().parent
LOGO = BASE_DIR / "images" / "cardio_logo.png"
BLOGO = BASE_DIR / "images" / "ITLogo.png"

# Load Logos
with open(LOGO, "rb") as img_file:
    logo_base64 = base64.b64encode(img_file.read()).decode()

with open(BLOGO, "rb") as bimg_file:
    blogo_base64 = base64.b64encode(bimg_file.read()).decode()

# Common CSS
def load_css():

    st.markdown("""
    <style>

    /* Reduce top/bottom page padding */
    .block-container{
        padding-top:1rem;
        padding-bottom:1rem;
    }

    /* Fixed sidebar width */
    section[data-testid="stSidebar"]{
        min-width:320px;
        max-width:320px;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] *{
        font-size:20px !important;
        font-weight:600 !important;
        transition:none !important;
    }

    /* Navigation links */
    section[data-testid="stSidebar"] a{
        padding-top:10px !important;
        padding-bottom:10px !important;
    }

    </style>
    """, unsafe_allow_html=True)

# Header
def show_header(page):

    col1, col2 = st.columns([0.5, 6])

    with col1:
        st.write("")
        st.write("")
        st.image(LOGO, width=250)

    with col2:
        st.write("")
        st.title("Cardio Prediction System")
        st.subheader("Early Heart Disease Risk Assessment")

    descriptions = {

        "App": """
         <p style="font-size:22px;">
         <b>Cardio Prediction System</b>
         is an application uses Machine Learning techniques to estimate
         the likelihood of heart disease and support early risk assessment.
         </p>
         """,

        "Prediction": """
        <p style="font-size:22px;">
         Enter the patient's clinical information below to estimate the
         likelihood of heart disease. Complete all required fields and
         click <b>Assess Heart Disease Risk</b> to generate an early risk
         assessment.</p>
         """,

        "Dataset": """
        <p style="font-size:22px;">
         Explore the heart disease dataset used to train the Machine Learning
         model. Review patient records, attributes, and data structure.</p>
         """,

        "Visualization": """
        <p style="font-size:22px;">
         Analyze the dataset through charts and visualizations to better
         understand feature distributions and relationships.</p>
         """,

        "About": """
        <p style="font-size:22px;">
         The <b>Cardio Prediction System</b> is a Machine Learning–based web application
         that estimates an individual's risk of heart disease using commonly available clinical information.
         <br>
         <b>Our Vision: Predict. Prevent. Protect Your Heart. ❤️</b></p>
         """
    }

    if page in descriptions:
        st.markdown(f"""
         <p style="font-size:22px;">
         {descriptions[page]}
         </p>
         """, unsafe_allow_html=True)

    st.divider()

# Medical Disclaimer

def show_disclaimer():

    st.markdown("""
    <div style="
        background-color:#fff3cd;
        border-left:6px solid #f0ad4e;
        padding:18px;
        border-radius:8px;
    ">

    <h3 style="margin-top:0;">⚠️ Medical Disclaimer</h3>

    <p style="font-size:20px; line-height:1.8;">
    This application provides an early risk assessment for educational and informational purposes only.
    </p>

    <p style="font-size:20px; line-height:1.8;">
    <b>It is not intended to replace professional medical evaluation, diagnosis, or treatment.</b>
    </p>

    <p style="font-size:20px; line-height:1.8;">
    Always consult a qualified healthcare professional regarding any medical concerns.
    </p>

    </div>
    """, unsafe_allow_html=True)

# Footer

def show_footer():

    st.divider()

    st.markdown(f"""
    <div style="
        background:#f8f9fa;
        padding:25px;
        border-radius:10px;
        text-align:center;
        border:1px solid #d9d9d9;
    ">

    <img src="data:image/png;base64,{logo_base64}" width="150">

    <h2 style="margin:10px 0 5px 0;color:#d63384;">
    Cardio Prediction System
    </h2>

    <p style="font-size:18px;margin:5px;">
     <b>Our Vision: Predict. Prevent. Protect Your Heart. ❤️</b>
    </p>

    <p style="font-size:18px;margin:5px;">
    <b>Version:</b> 1.0
    </p>

    <p style="font-size:18px;margin:5px;">
    <b>Developed By:</b> Farhana Hameed
    </p>

    <p style="font-size:18px;margin:5px;">
    <b>Project Type:</b> Machine Learning Classification System
    </p>

    <hr>

    <p style="font-size:18px;color:#163d8c;">
    <b>© 2026 Cardio Prediction System:</b> Developed for Educational Purposes
    </p>

    <table style="width:100%;margin-top:10px;">
        <tr>
            <td style="text-align:center;font-size:18px;color:#163d8c;">
                <b>Machine Learning Project:</b> By Innovative Tech
                <img src="data:image/png;base64,{blogo_base64}"
                     width="42"
                     style="vertical-align:middle;border-radius:50%;margin-left:8px;">
            </td>
        </tr>
    </table>

    </div>
    """, unsafe_allow_html=True)