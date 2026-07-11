import streamlit as st
import os

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

st.markdown('<div class="title-container"><h1>Model Performance</h1></div>', unsafe_allow_html=True)
st.write(
    "Comprehensive evaluation of the XGBoost fraud detection model. "
)
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Precision",
    "95%",
    help="Percentage of predicted frauds that were actually fraudulent."
)

col2.metric(
    "Recall",
    "80%",
    help="Percentage of actual frauds successfully detected."
)

col3.metric(
    "F1 Score",
    "87%"
)

col4.metric(
    "PR-AUC",
    "92.68%"
)

st.divider()

st.subheader("Classification Report")

import pandas as pd

report = pd.DataFrame({

    "Class":[
        "Legitimate (0)",
        "Fraud (1)"
    ],

    "Precision":[
        1.00,
        0.95
    ],

    "Recall":[
        1.00,
        0.80
    ],

    "F1-Score":[
        1.00,
        0.87
    ],

    "Support":[
        257797,
        1538
    ]

})

st.dataframe(
    report,
    use_container_width=True,
    hide_index=True
)

st.info(
"""
Since the dataset is highly imbalanced,
the Fraud class (Class 1) metrics
are the primary indicators of model quality.
"""
)

st.divider()

st.subheader("Confusion Matrix")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "output7.png")
st.image(
    image_path,
    use_container_width=True
)
st.divider()

c1,c2,c3,c4=st.columns(4)

c1.metric("True Negative","257,732")
c2.metric("False Positive","65")
c3.metric("False Negative","311")
c4.metric("True Positive","1,227")

st.divider()
st.subheader("Business Interpretation")
st.success("""
The model successfully detects **80%** of fraudulent transactions while maintaining a **95% Precision**, resulting in only **65 false positives** out of more than **257,000** legitimate transactions.

This balance makes the model suitable for real-world fraud detection systems, where minimizing unnecessary transaction blocks is just as important as detecting fraudulent activity.
""")

st.caption(
"""
The evaluation focuses on Precision, Recall, F1-Score and PR-AUC because the dataset is highly imbalanced. Accuracy is intentionally excluded as a primary metric.
"""
)

st.markdown("---")
st.markdown("You can download the report file from here :")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(BASE_DIR, "Fraud_Detection.pdf")

with open(pdf_path, "rb") as pdf:
    st.download_button(
        label="Download Full Project Report",
        data=pdf,
        file_name="Credit_Card_Fraud_Detection_Report.pdf",
        mime="application/pdf"
    )

"""import base64

with open(pdf_path, "rb") as f:
    pdf = base64.b64encode(f.read()).decode("utf-8")

pdf_display = f"""
<iframe
    src="data:application/pdf;base64,{pdf}"
    width="100%"
    height="900px"
    type="application/pdf">
</iframe>
"""

st.markdown(pdf_display, unsafe_allow_html=True)"""
