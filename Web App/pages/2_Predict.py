import streamlit as st
import pickle
import pandas as pd
import time
import os

st.markdown("""
<style>

.main {
    background-color: #0F172A;
}

.stApp {
    background: linear-gradient(180deg, #0F172A 0%, #10141c 100%);
}

/* ===========================
   HEADER
=========================== */

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

/* ===========================
   TITLE
=========================== */

.title-container {
    text-align: center;
    padding: 1.2rem 0 .3rem;
}

.title-container h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0;
}

.subtitle {
    text-align:center;
    color:#b7c0cc;
    font-size:1.05rem;
    margin-top:-.3rem;
    margin-bottom:1.5rem;
}

/* ===========================
   CARDS
=========================== */

.section-card {

    background:#161b22;

    border:1px solid #262c36;

    border-radius:16px;

    padding:1.5rem;

    margin-bottom:1rem;

}

.section-title{

    color:#00c6ff;

    font-weight:700;

    font-size:1.2rem;

}

/* ===========================
   TEXT
=========================== */

p,
label,
.stMarkdown{

    color:#e6e9ef;

}

/* ===========================
   SIDEBAR
=========================== */

[data-testid="stSidebar"]{

    background:#10141c;

    border-right:1px solid #262c36;

}

[data-testid="stSidebar"] *{

    color:#d3d9e2 !important;

}

/* ===========================
   CAPTION
=========================== */

[data-testid="stCaptionContainer"]{

    color:#8a94a3 !important;

}

/* ===========================
   INPUTS
=========================== */

.stSelectbox label,
.stNumberInput label{

    color:#cdd4de !important;

    font-weight:600;

}

div[data-baseweb="select"]>div{

    background:#0e1117;

    border:1px solid #2c333f;

    color:#e6e9ef;

}

div[data-testid="stNumberInput"] input{

    background:#0e1117;

    color:#e6e9ef;

    border:1px solid #2c333f;

    border-radius:8px;

}

div[data-testid="stNumberInput"] input:focus{

    border:1px solid #00c6ff;

    box-shadow:0 0 0 1px #00c6ff55;

}

div[data-testid="stNumberInput"] button{

    background:#161b22;

    border:1px solid #2c333f;

    color:#e6e9ef;

}

div[data-testid="stNumberInput"] button:hover{

    background:#1e2530;

    color:#00c6ff;

}

/* ===========================
   BUTTON
=========================== */

div.stButton>button{

    width:100%;

    background:linear-gradient(90deg,#00c6ff,#0072ff);

    color:white;

    font-size:1.05rem;

    font-weight:700;

    padding:.75rem;

    border:none;

    border-radius:12px;

    transition:.25s;

}

div.stButton>button:hover{

    transform:scale(1.02);

    box-shadow:0 6px 20px rgba(0,114,255,.35);

}

/* ===========================
   RESULT CARD
=========================== */

.result-card{

    background:#161b22;

    border:1px solid #2c333f;

    border-radius:18px;

    padding:2rem;

    text-align:center;

    margin-top:1rem;

}

.result-card h2{

    color:#9ca3af;

    font-size:1rem;

    margin-bottom:.5rem;

}

.result-card h1{

    font-size:3rem;

    font-weight:800;

    margin:0;

}

/* ===========================
   METRICS
=========================== */

[data-testid="metric-container"]{

    background:#161b22;

    border:1px solid #262c36;

    border-radius:15px;

    padding:18px;

}

/* ===========================
   PROGRESS BAR
=========================== */

.stProgress > div > div > div{

    background:linear-gradient(90deg,#00c6ff,#0072ff);

}

/* ===========================
   DATAFRAME
=========================== */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}

/* ===========================
   ALERTS
=========================== */

/* سيب Streamlit يتحكم في ألوانهم */
div[data-baseweb="notification"]{

    border-radius:12px;

}

</style>
""", unsafe_allow_html=True)

# ===========================
# Load Model
# ===========================


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Fraud_Detection.pkl")
model = pickle.load(
    open(model_path, "rb")
)

# ===========================
# Dictionaries
# ===========================

category = [8, 4, 0, 2, 9, 3, 11, 12, 1, 10, 5, 13, 6, 7]

category_2 = [
    'misc_net',
    'gas_transport',
    'kids_pets',
    'home',
    'shopping_net',
    'food_dining',
    'personal_care',
    'grocery_pos',
    'entertainment',
    'shopping_pos',
    'misc_pos',
    'travel',
    'health_fitness',
    'grocery_net'
]

gender_2 = ["Female", "Male"]
gender = [0, 1]

finally_category = dict(zip(category_2, category))
finally_gender = dict(zip(gender_2, gender))

# ===========================
# Layout
# ===========================
st.markdown('<div class="title-container"><h1>Transaction Prediction</h1></div>', unsafe_allow_html=True)
st.markdown("---")
col1, col2 = st.columns(2, gap="large")

# ======================================================
# LEFT SIDE
# ======================================================

with col1:

    st.markdown(
        """
        <div class="section-card">
        <div class="section-title">
        <h2 style="text-align:center;">Transaction Information</h2>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Transaction & Temporal")

    amt = st.number_input("Transaction Amount", min_value=0.0)

    category_box = st.selectbox("Merchant Category", category_2)
    ca = finally_category[category_box]

    trans_hour = st.number_input(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        step=1,
    )

    trans_weekday = st.number_input(
        "Transaction Weekday",
        min_value=0,
        max_value=31,
        step=1,
    )

    st.markdown("---")

    st.markdown("### Customer")

    customer_age = st.number_input(
        "Customer Age",
        min_value=16,
        max_value=120,
        step=1,
    )

    gender_box = st.selectbox("Gender", gender_2)
    gender_encoded = finally_gender[gender_box]

    city_pop = st.number_input(
        "City Population",
        min_value=0,
        step=1,
    )

    st.markdown("---")

    st.markdown("### Location")

    distance_customer_merchant = st.number_input(
        "Distance Between Customer & Merchant",
        min_value=0.0,
    )

    max_distance_last_txn = st.number_input(
        "Max Distance Last Transaction",
        min_value=0.0,
    )

    st.markdown("---")

    st.markdown("### Customer Behaviour")

    customer_avg_amt_so_far = st.number_input(
        "Average Spending",
        min_value=0.0,
    )

    amt_deviation_from_avg = st.number_input(
        "Amount Deviation",
    )

    customer_txn_count_1h = st.number_input(
        "Transactions Last Hour",
        min_value=0,
        step=1,
    )

    st.markdown("---")

    predict = st.button(
        "Analyze Transaction",
        use_container_width=True,
    )

# ======================================================
# RIGHT SIDE
# ======================================================

with col2:

    st.markdown(
        """
        <div class="section-card">
        <div class="section-title">
        <h2 style="text-align:center;">Prediction Result</h2>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if predict:

        input_df = pd.DataFrame({
            "amt": [amt],
            "category": [ca],
            "trans_hour": [trans_hour],
            "trans_weekday": [trans_weekday],
            "customer_age": [customer_age],
            "distance_customer_merchant": [distance_customer_merchant],
            "customer_avg_amt_so_far": [customer_avg_amt_so_far],
            "amt_deviation_from_avg": [amt_deviation_from_avg],
            "customer_txn_count_1h": [customer_txn_count_1h],
            "max_distance_last_txn": [max_distance_last_txn],
            "city_pop": [city_pop],
            "gender": [gender_encoded],
        })

        with st.spinner("Analyzing transaction..."):
            time.sleep(1)

            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0]

        legit_prob = probability[0] * 100
        fraud_prob = probability[1] * 100

        # -----------------------------
        # Prediction Card
        # -----------------------------

        if prediction == 1:

            st.markdown(
                """
                <div class="result-card">
                    <h2>Prediction</h2>
                    <h1>🚨 FRAUD</h1>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                """
                <div class="result-card">
                    <h2>Prediction</h2>
                    <h1>✅ LEGITIMATE</h1>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")

        # -----------------------------
        # Probabilities
        # -----------------------------

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "Fraud Probability",
                f"{fraud_prob:.2f}%"
            )

        with c2:
            st.metric(
                "Legitimate Probability",
                f"{legit_prob:.2f}%"
            )

        st.write("### Fraud Risk")

        #st.progress(fraud_prob / 100)

        # -----------------------------
        # Risk Level
        # -----------------------------

        if fraud_prob >= 70:

            st.error("🔴 High Risk")

        elif fraud_prob >= 40:

            st.warning("🟡 Medium Risk")

        else:

            st.success("🟢 Low Risk")

        st.markdown("---")

        # -----------------------------
        # Summary
        # -----------------------------

        st.subheader("Summary")

        if prediction == 1:

            st.error(
                """
This transaction exhibits multiple characteristics commonly associated with fraudulent activity.

**Recommendation:** Review this transaction before approval.
"""
            )

        else:

            st.success(
                """
The transaction appears consistent with the customer's historical behavior.

No significant fraud indicators were detected.
"""
            )

        st.markdown("---")

        # -----------------------------
        # Prediction Details
        # -----------------------------

        st.subheader("Prediction Details")

        d1, d2, d3 = st.columns(3)

        d1.metric(
            "Fraud",
            f"{fraud_prob:.2f}%"
        )

        d2.metric(
            "Legitimate",
            f"{legit_prob:.2f}%"
        )

        d3.metric(
            "Threshold",
            "50%"
        )

    else:

        st.info(
            """
👈 Fill in the transaction details and click **Analyze Transaction** to evaluate the fraud risk.
"""
        )