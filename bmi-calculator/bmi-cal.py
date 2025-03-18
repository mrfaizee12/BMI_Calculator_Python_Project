import streamlit as st

# Updated CSS (removed .main container styles)
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background: linear-gradient(90deg, #4CAF50, #45a049);
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #45a049, #4CAF50);
        }
        .bmi-result {
            font-size: 24px;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            background: #f9f9f9;
            margin-top: 20px;
        }
        div[data-baseweb="input"] {
            background: none !important;
        }
        input {
            background: none !important;
            border: none !important;
            border-bottom: 2px solid #4CAF50 !important;
            padding: 8px !important;
            font-size: 16px !important;
            text-align: center !important;
        }
        input:focus {
            outline: none !important;
            border-bottom: 2px solid #45a049 !important;
        }
        .height-label {
            font-size: 16px;
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Web App Title
st.markdown("<h1 style='text-align:center; color:#333;'>🏋️‍♂️ BMI Calculator</h1>", unsafe_allow_html=True)

# Short Description
st.markdown("""
    <p style='text-align:center; color:#666; font-size:16px;'>
    Calculate your Body Mass Index (BMI) to know if you are underweight, normal, overweight, or obese.
    </p>
""", unsafe_allow_html=True)

# User Inputs (inside a styled div)
st.markdown('<div class="main">', unsafe_allow_html=True)

# Session State for Dynamic Updates
if "height_ft" not in st.session_state:
    st.session_state.height_ft = 5
if "height_in" not in st.session_state:
    st.session_state.height_in = 5
if "height_m" not in st.session_state:
    st.session_state.height_m = round(((5 * 12) + 5) * 0.0254, 2)

# Function to Update Meters when Feet/Inches Change
def update_meters():
    total_inches = (st.session_state.height_ft * 12) + st.session_state.height_in
    st.session_state.height_m = round(total_inches * 0.0254, 2)

# Function to Update Feet/Inches when Meters Change
def update_feet_inches():
    total_inches = round(st.session_state.height_m / 0.0254)
    st.session_state.height_ft = total_inches // 12
    st.session_state.height_in = total_inches % 12

# Height Input Fields with Labels
st.markdown("<p class='height-label'>Enter your height:</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    feet = st.number_input("Feet", min_value=1, max_value=8, step=1, key="height_ft", on_change=update_meters)
with col2:
    inches = st.number_input("Inches", min_value=0, max_value=11, step=1, key="height_in", on_change=update_meters)
with col3:
    meters = st.number_input("Meters", min_value=0.5, max_value=2.5, step=0.01, format="%.2f", key="height_m", on_change=update_feet_inches)

# Weight Input
st.markdown("<p class='height-label'>Enter your weight (kg):</p>", unsafe_allow_html=True)
weight = st.number_input("", min_value=10.0, max_value=300.0, step=0.5, format="%.1f")

# BMI Calculation
if st.button("Calculate BMI"):
    if st.session_state.height_m > 0 and weight > 0:
        bmi = round(weight / (st.session_state.height_m ** 2), 2)
        
        # BMI Category & Styling
        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
        
        # Display Result with Styling
        st.markdown(f"<div class='bmi-result' style='color:{color};'>Your BMI: {bmi} ({category})</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter valid height and weight!")

st.markdown('</div>', unsafe_allow_html=True)  # Close div
