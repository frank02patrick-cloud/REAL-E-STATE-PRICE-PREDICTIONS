import pandas as pd
import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="PREDICTION OF REAL ESTATE PRICES",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Modern Custom CSS
st.markdown(
    """
<style>
/* App dark theme background */
.stApp {
    background-color: #0E1117;
    color: #FAFAFA;
}

/* Title Container */
.main-title {
    background: #161B22;
    padding: 28px 20px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 30px;
    border: 1px solid #30363D;
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.25);
}

.main-title h1 {
    color: #FF6B6B;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 8px;
}

.main-title p {
    color: #2E8B57;
    font-size: 16px;
    font-weight: 500;
}

/* Input Cards */
div[data-testid="stColumn"] > div {
    background-color: #161B22;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #21262D;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.15);
}

/* Form Input Field Customization */
div[data-baseweb="input"] > div, 
div[data-baseweb="select"] > div {
    background-color: #0D1117 !important;
    border-color: #30363D !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    color: #FFFFFF !important;
}

/* Centered & Styled Predict Button */
div.stButton {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 15px;
}

div.stButton > button {
    width: 280px !important;
    background: linear-gradient(135deg, #FF6B6B 0%, #FF4757 100%) !important;
    color: #FFFFFF !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 12px 24px !important;
    border-radius: 10px !important;
    border: none !important;
    box-shadow: 0px 4px 15px rgba(255, 107, 107, 0.3) !important;
    transition: all 0.25s ease-in-out !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%) !important;
    box-shadow: 0px 6px 20px rgba(30, 136, 229, 0.4) !important;
    transform: translateY(-2px);
}

div.stButton > button:active {
    transform: translateY(1px);
}

/* Prediction Output Card */
.result-card {
    background: rgba(46, 139, 87, 0.1);
    border: 1.5px solid #2E8B57;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin-top: 25px;
}

.result-card h3 {
    color: #2E8B57;
    font-size: 18px;
    margin-bottom: 8px;
}

.result-card p {
    color: #FFFFFF;
    font-size: 26px;
    font-weight: 700;
    margin: 0;
}
</style>
""",
    unsafe_allow_html=True,
)

# Header Section
st.markdown(
    """
<div class="main-title">
    <h1>🏠 PREDICTION OF REAL ESTATE PRICES</h1>
    <p>Enter the real estate characteristics to predict the price in million RWF.</p>
</div>
""",
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model():
    return joblib.load("house_price_model.sav")


model = load_model()

# Input Grid Layout
col1, col2, col3 = st.columns(3)
with col1:
    neighborhood = st.selectbox(
        "Neighborhood",
        ["Kigali City", "Nyarugenge", "Gasabo", "Kicukiro", "Huye", "Musanze"],
    )
with col2:
    distance = st.number_input(
        "Distance to City Centre (km)", 0.07, 27.40, 3.27
    )
with col3:
    area = st.number_input("Area (m²)", 26.0, 426.4, 105.7)

col4, col5 = st.columns(2)
with col4:
    bedrooms = st.number_input("Bedrooms", 1, 6, 3, step=1)
with col5:
    bathrooms = st.number_input("Bathrooms", 1, 5, 3, step=1)

col6, col7 = st.columns(2)
with col6:
    age = st.number_input("House Age (years)", 0.4, 49.5, 6.8)
with col7:
    parking = st.number_input("Parking Spaces", 0, 3, 1, step=1)

# Centered Predict Button Block
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    predict = st.button("Predict Price ✨")

if predict:
    row = pd.DataFrame(
        [
            {
                "Area_m2": area,
                "Bedrooms": bedrooms,
                "Bathrooms": bathrooms,
                "House_Age_Years": age,
                "Distance_to_City_km": distance,
                "Parking_Spaces": parking,
                "Neighborhood": neighborhood,
            }
        ]
    )

    price = model.predict(row)[0]

    st.markdown(
        f"""
        <div class="result-card">
            <h3>Estimated House Price</h3>
            <p>{price:.2f} Million RWF</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
