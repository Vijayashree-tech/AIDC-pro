import streamlit as st
import requests

# App title
st.set_page_config(page_title="💧 Water Predictor for Farmers", layout="centered")
st.title("🚜 Water Requirement Predictor")
st.subheader("Using ML to Help Farmers with Smart Irrigation 💦")

# Input fields
st.markdown("### 📥 Enter Input Details:")
rainfall = st.slider("Rainfall (in mm)", 0, 300, 120)
temperature = st.slider("Temperature (°C)", 0, 50, 30)
humidity = st.slider("Humidity (%)", 0, 100, 70)

soil_type = st.selectbox("Soil Type", ["loam", "clay", "sand"])
crop_type = st.selectbox("Crop Type", ["rice", "wheat", "maize"])
acres = st.number_input("Acres of Land", min_value=0.1, value=1.0, step=0.1)

# Predict button
if st.button("🔍 Predict Water Requirement"):
    url = "http://127.0.0.1:5000/predict"  # Change this to your hosted backend URL if deployed
    data = {
        "rainfall": rainfall,
        "temperature": temperature,
        "humidity": humidity,
        "soil_type": soil_type,
        "crop_type": crop_type,
        "acres": acres
    }

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"💧 Estimated Water Required: *{result['prediction']} liters*")
        else:
            st.error("⚠ Failed to get prediction from server. Try again.")
    except Exception as e:
        st.error(f"🚫 Error connecting to server: {e}")

# Feedback
st.markdown("---")
st.markdown("### 📝 Feedback")
feedback = st.text_area("Leave your feedback here...")
if st.button("📩 Submit Feedback"):
    st.success("Thank you for your valuable feedback! 🙌")
