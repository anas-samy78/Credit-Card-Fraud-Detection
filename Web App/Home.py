import streamlit  as st
import pandas as pd 
import pickle
import os

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)
st.markdown('<div class="title-container"><h1>💳 Credit Card Fraud Detection System</h1></div>', unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "card.png")
st.image(image_path)
st.markdown("""
### Machine Learning Powered Fraud Detection

This dashboard demonstrates a fraud detection system built using **XGBoost** and advanced feature engineering.

Use the navigation menu on the left to:

- Predict a transaction
- View model performance
- Explore feature importance
- Learn more about the project
""")

st.markdown("""
    <style>
        .main {
            background-color: #0F172A;
        }
        .stApp {
            background: linear-gradient(180deg, #0F172A 0%, #10141c 100%);
        }

        header[data-testid="stHeader"] {
            background-color: #0e1117;
            border-bottom: 1px solid #262c36;
        }
        [data-testid="stToolbar"] {
            background-color: transparent;
        }
        [data-testid="stDecoration"] {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
        }

        .title-container {
            text-align: center;
            padding: 1.2rem 0 0.3rem 0;
        }
        .title-container h1 {
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .subtitle {
            text-align: center;
            color: #b7c0cc;
            font-size: 1.05rem;
            margin-top: -0.3rem;
            margin-bottom: 1.5rem;
        }
        .section-card {
            background-color: #161b22;
            padding: 1.5rem 1.5rem 1rem 1.5rem;
            border-radius: 16px;
            border: 1px solid #262c36;
            margin-bottom: 1.2rem;
        }
        .section-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #00c6ff;
            margin-bottom: 0.8rem;
        }

        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, span {
            color: #e6e9ef;
        }
        [data-testid="stSidebar"] {
            background-color: #10141c;
            border-right: 1px solid #262c36;
        }
        [data-testid="stSidebar"] * {
            color: #d3d9e2 !important;
        }
        [data-testid="stCaptionContainer"] {
            color: #8a94a3 !important;
        }
        .stSelectbox label, .stNumberInput label {
            color: #cdd4de !important;
            font-weight: 600;
        }

        div[data-baseweb="select"] > div {
            background-color: #0e1117;
            border: 1px solid #2c333f;
            color: #e6e9ef;
        }

        div[data-testid="stNumberInput"] input {
            background-color: #0e1117;
            color: #e6e9ef;
            border: 1px solid #2c333f;
            border-radius: 8px;
        }
        div[data-testid="stNumberInput"] input:focus {
            border: 1px solid #00c6ff;
            box-shadow: 0 0 0 1px #00c6ff55;
        }
        div[data-testid="stNumberInput"] button {
            background-color: #161b22;
            border: 1px solid #2c333f;
            color: #e6e9ef;
        }
        div[data-testid="stNumberInput"] button:hover {
            background-color: #1e2530;
            color: #00c6ff;
        }

        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 0.7rem 0;
            border-radius: 12px;
            border: none;
            transition: 0.25s ease;
        }
        div.stButton > button:hover {
            transform: scale(1.015);
            box-shadow: 0 6px 20px rgba(0, 114, 255, 0.35);
        }
        .result-card {
            background: linear-gradient(135deg, #0072ff33, #00c6ff1a);
            border: 1px solid #0072ff55;
            padding: 2rem;
            border-radius: 18px;
            text-align: center;
            margin-top: 1.5rem;
        }
        .result-card h2 {
            color: #b7c0cc;
            font-size: 1.1rem;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }
        .result-card h1 {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00c6ff, #00ffb2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Precision", "95%")
col2.metric("Recall", "80%")
col3.metric("PR-AUC", "92.7%")
col4.metric("ROC-AUC", "99.8%")