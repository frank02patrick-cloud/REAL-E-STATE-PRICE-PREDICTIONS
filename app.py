import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_title="PREDICTION OF REAL E-STATE PRICES", page_icon="🏠",  initial_sidebar_state="expanded")
st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #0E1117;
}

/* Title */
.main-title {
    background-color: #0E1117;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-family: "Trebuchet MS", sans-serif;
    margin-bottom: 20px;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.08);
}

.main-title h1 {
    color: #FF6B6B;
    font-size: 38px;
    margin-bottom: 5px;
}

.main-title p {
    color: #2E8B57;
    font-size: 17px;
}

/* Input boxes */
div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"] {
    background-color: grey;
    padding: 10px;
    border-radius: 10px;
}

/* Predict button */
.stButton > button {
    width: 100%;
    background-color: #FF6B6B;
    color: blue;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 10px;
    border: none;
}

/* Button hover */
.stButton > button:hover {
    background-color: #1E88E5;
    color: green;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="main-title">
    <h1>🏠 PREDICTION OF REAL E-STATE PRICES</h1>
    <p>Enter the real e-state characteristics to predict the price in million RWF.
    </p>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.sav")
model = load_model()

col1, col2, col3 = st.columns(3)
with col1:
    neighborhood=st.selectbox("Neighborhood", [ 'Kigali City', 'Nyarugenge' , 'Gasabo', 'Kicukiro' , 'Huye' , 'Musanze' ])
with col2:
    distance=st.number_input("Distance to City Centre (km)", 0.07, 27.40, 3.27)
with col3:
    area=st.number_input("Area (m²)", 26.0, 426.4, 105.7)
    
col4, col5 = st.columns(2)
with col4:
    bedrooms=st.number_input("Bedrooms", 1, 6, 3, step=1)
with col5:
    bathrooms=st.number_input("Bathrooms", 1, 5, 3, step=1)
col6, col7 = st.columns(2)
with col6:
    age=st.number_input("House Age (years)", 0.4, 49.5, 6.8)
with col7:
    parking=st.number_input("Parking Spaces", 0, 3, 1, step=1)

if st.button("Predict"):
    row=pd.DataFrame([{"Area_m2":area,
                       "Bedrooms":bedrooms,
                       "Bathrooms":bathrooms,
                       "House_Age_Years":age,
                       "Distance_to_City_km":distance,
                       "Parking_Spaces":parking,
                       "Neighborhood":neighborhood}])
    price=model.predict(row)[0]
    st.success(f"Predicted house price: {price:.2f} million RWF")
