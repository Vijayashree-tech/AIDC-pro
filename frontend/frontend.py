import streamlit as st
import requests
import time

# Page Configuration
st.set_page_config(
    page_title="💧 AquaPredict Pro", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced Styling with Modern UI/UX
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Styles */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main Container */
        .main-container {
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 40px;
            margin: 20px auto;
            max-width: 1200px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(148, 163, 184, 0.2);
        }
        
        /* Header Section */
        .hero-section {
            text-align: center;
            margin-bottom: 50px;
            padding: 30px 0;
        }
        
        .main-title {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            letter-spacing: -0.02em;
        }
        
        .subtitle {
            font-size: 1.3rem;
            color: #cbd5e1;
            font-weight: 400;
            margin-bottom: 10px;
        }
        
        .description {
            font-size: 1rem;
            color: #94a3b8;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        /* Card Styles */
        .input-card {
            background: rgba(30, 41, 59, 0.6);
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(71, 85, 105, 0.5);
            position: relative;
            overflow: hidden;
        }
        
        .input-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #10b981 0%, #3b82f6 50%, #06b6d4 100%);
        }
        
        .card-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #f1f5f9;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        /* Form Styling */
        .stSelectbox > div > div {
            background-color: rgba(51, 65, 85, 0.8);
            border: 2px solid rgba(71, 85, 105, 0.6);
            border-radius: 12px;
            transition: all 0.3s ease;
            color: #f1f5f9;
        }
        
        .stSelectbox > div > div:focus-within {
            border-color: #10b981;
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
        }
        
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #10b981 0%, #06b6d4 100%);
        }
        
        .stNumberInput > div > div {
            background-color: rgba(51, 65, 85, 0.8);
            border: 2px solid rgba(71, 85, 105, 0.6);
            border-radius: 12px;
            transition: all 0.3s ease;
            color: #f1f5f9;
        }
        
        .stNumberInput > div > div:focus-within {
            border-color: #10b981;
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
        }
        
        /* Button Styling */
        .predict-button {
            display: flex;
            justify-content: center;
            margin: 40px 0;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #06b6d4 100%);
            color: white;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 15px 40px;
            border: none;
            border-radius: 15px;
            box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.4);
            transition: all 0.3s ease;
            min-width: 250px;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 35px -5px rgba(16, 185, 129, 0.6);
        }
        
        /* Result Card */
        .result-card {
            background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #06b6d4 100%);
            color: white;
            padding: 35px;
            border-radius: 20px;
            text-align: center;
            margin: 30px 0;
            box-shadow: 0 15px 35px -5px rgba(16, 185, 129, 0.4);
            position: relative;
            overflow: hidden;
        }
        
        .result-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: shimmer 3s ease-in-out infinite;
        }
        
        @keyframes shimmer {
            0%, 100% { transform: rotate(0deg); }
            50% { transform: rotate(180deg); }
        }
        
        .result-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 15px 0;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
        
        .result-label {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 10px;
        }
        
        .result-subtitle {
            font-size: 1rem;
            opacity: 0.8;
        }
        
        /* Loading Animation */
        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px;
        }
        
        .spinner {
            width: 50px;
            height: 50px;
            border: 5px solid rgba(71, 85, 105, 0.3);
            border-top: 5px solid #10b981;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Error Styling */
        .error-card {
            background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin: 20px 0;
            box-shadow: 0 10px 25px -5px rgba(239, 68, 68, 0.4);
        }
        
        /* Info Cards */
        .info-grid {
            display: none;
        }
        
        .info-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px -3px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0;
            transition: transform 0.3s ease;
        }
        
        .info-card:hover {
            transform: translateY(-5px);
        }
        
        .info-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
        }
        
        .info-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 8px;
        }
        
        .info-text {
            font-size: 0.9rem;
            color: #64748b;
            line-height: 1.5;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            
            .main-container {
                margin: 10px;
                padding: 25px;
            }
            
            .input-card {
                padding: 25px;
            }
        }
    </style>
""", unsafe_allow_html=True)


# Hero Section
st.markdown("""
    <div class="hero-section">
        <div class="main-title">🌾 AquaPredict Pro</div>
        <div class="subtitle">AI-Powered Water Management for Smart Agriculture</div>
        <div class="description">
            Optimize your irrigation with precision agriculture technology. 
            Get accurate water requirement predictions based on real-time environmental data.
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown('<div class="card-title">📊 Field Parameters</div>', unsafe_allow_html=True)

# Create three columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🌤️ Weather Conditions")
    st.markdown('<div style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 15px;">Environmental factors affecting water needs</div>', unsafe_allow_html=True)
    rainfall = st.slider("🌧️ Rainfall (mm)", 0, 300, 120, help="Average rainfall in your area")
    temperature = st.slider("🌡️ Temperature (°C)", 0, 50, 30, help="Average temperature")
    humidity = st.slider("💧 Humidity (%)", 0, 100, 70, help="Relative humidity percentage")

with col2:
    st.markdown("#### 🌱 Crop Information")
    st.markdown('<div style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 15px;">Specify your agricultural setup</div>', unsafe_allow_html=True)
    crop_type = st.selectbox(
        "🌾 Crop Type", 
        ["rice", "wheat", "maize", "sugarcane", "cotton"],
        help="Select your primary crop"
    )
    soil_type = st.selectbox(
        "🏔️ Soil Type", 
        ["loam", "clay", "sandy", "silt"],
        help="Your soil composition"
    )

with col3:
    st.markdown("#### 📏 Field Specifications")
    st.markdown('<div style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 15px;">Area and irrigation details</div>', unsafe_allow_html=True)
    acres = st.number_input(
        "🌾 Field Area (acres)", 
        min_value=0.1, 
        value=1.0, 
        step=0.1,
        help="Total cultivated area"
    )
    
    # Additional field for irrigation efficiency
    irrigation_efficiency = st.slider(
        "💦 Irrigation Efficiency (%)", 
        60, 95, 80,
        help="Efficiency of your irrigation system"
    )

st.markdown('</div>', unsafe_allow_html=True)

# Info Cards Section
st.markdown("""
    <div class="info-grid">
        <div class="info-card">
            <div class="info-icon">🎯</div>
            <div class="info-title">Precise Predictions</div>
            <div class="info-text">AI algorithms analyze multiple factors for accurate water requirements</div>
        </div>
        <div class="info-card">
            <div class="info-icon">💰</div>
            <div class="info-title">Cost Savings</div>
            <div class="info-text">Optimize water usage and reduce irrigation costs by up to 30%</div>
        </div>
        <div class="info-card">
            <div class="info-icon">🌱</div>
            <div class="info-title">Better Yields</div>
            <div class="info-text">Proper water management leads to healthier crops and higher productivity</div>
        </div>
        <div class="info-card">
            <div class="info-icon">🌍</div>
            <div class="info-title">Eco-Friendly</div>
            <div class="info-text">Sustainable farming practices for environmental conservation</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# Center the button using Streamlit columns
# This ensures the button is always centered on all screen sizes
button_col1, button_col2, button_col3 = st.columns([12,10,10])
with button_col2:
    predict_clicked = st.button("🔮 Calculate Water Requirement", key="predict_btn")

if predict_clicked:
    url = "http://127.0.0.1:5000/predict"
    data = {
        "rainfall": rainfall,
        "temperature": temperature,
        "humidity": humidity,
        "soil_type": soil_type,
        "crop_type": crop_type,
        "acres": acres
    }
    try:
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            prediction = round(result["prediction_lr"], 2)
            # Adjust prediction based on irrigation efficiency
            adjusted_prediction = round(prediction * (100 / irrigation_efficiency), 2)
            water_saved = round(adjusted_prediction - prediction, 2)
            # Display results
            st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">💧 Recommended Water Requirement</div>
                    <div class="result-value">{adjusted_prediction:,} L</div>
                    <div class="result-subtitle">For {acres} acres of {crop_type.title()}</div>
                </div>
            """, unsafe_allow_html=True)
            # Additional insights
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(
                    label="📈 Base Requirement",
                    value=f"{prediction:,} L",
                    help="Raw AI prediction"
                )
            with col2:
                st.metric(
                    label="⚡ Efficiency Adjusted",
                    value=f"{adjusted_prediction:,} L",
                    delta=f"+{water_saved} L",
                    help="Adjusted for irrigation efficiency"
                )
            with col3:
                daily_req = round(adjusted_prediction / 7, 2)  # Assuming weekly requirement
                st.metric(
                    label="📅 Daily Average",
                    value=f"{daily_req:,} L",
                    help="Estimated daily water need"
                )
            # Recommendations
            st.markdown("### 💡 Smart Recommendations")
            recommendations = []
            if humidity < 50:
                recommendations.append("🌡️ Low humidity detected - consider mulching to reduce water evaporation")
            if temperature > 35:
                recommendations.append("🔥 High temperature - increase irrigation frequency during cooler hours")
            if rainfall > 200:
                recommendations.append("🌧️ High rainfall expected - reduce irrigation schedule accordingly")
            if soil_type == "sandy":
                recommendations.append("🏖️ Sandy soil drains quickly - consider more frequent, smaller irrigations")
            if irrigation_efficiency < 75:
                recommendations.append("💦 Consider upgrading to drip irrigation for better water efficiency")
            if recommendations:
                for rec in recommendations:
                    st.info(rec)
            else:
                st.success("✅ Your current parameters look optimal for efficient water usage!")
        else:
            st.markdown("""
                <div class="error-card">
                    ⚠️ <strong>Service Unavailable</strong><br>
                    Unable to connect to prediction service. Please check if the backend server is running.
                </div>
            """, unsafe_allow_html=True)
    except requests.exceptions.Timeout:
        st.markdown("""
            <div class="error-card">
                ⏰ <strong>Request Timeout</strong><br>
                The prediction service is taking too long to respond. Please try again.
            </div>
        """, unsafe_allow_html=True)
    except requests.exceptions.ConnectionError:
        st.markdown("""
            <div class="error-card">
                🔌 <strong>Connection Error</strong><br>
                Cannot connect to the prediction service. Please ensure the backend server is running on localhost:5000.
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"""
            <div class="error-card">
                🚫 <strong>Unexpected Error</strong><br>
                {str(e)}
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; color: #94a3b8; border-top: 1px solid rgba(71, 85, 105, 0.3);">
        <p>🌱 Built with ❤️ for sustainable agriculture • Powered by AI & Machine Learning</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main container