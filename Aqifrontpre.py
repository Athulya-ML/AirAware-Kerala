import streamlit as st
import pickle

# ------------------ Page Style ------------------
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.title("Air Quality Index Predictor")

# ------------------ About Section ------------------
st.markdown("""
<h3 style='text-decoration: underline; color: #2e8b57;'>📘 About the project</h3>
<div style='background-color: #e6f7ff; border: 2px solid #3399ff; padding: 20px; 
            border-radius: 10px; font-size: 16px; line-height: 1.6; color: #003366;'>
Air pollution is one of the most critical environmental issues impacting human health and ecosystems globally. 
To monitor and manage air quality, governments use the Air Quality Index (AQI) — a standardized value that indicates 
how polluted the air currently is or how polluted it is forecast to become.<br><br>

This project focuses on building a Machine Learning-based model to predict AQI values using historical air quality 
data obtained from Continuous Ambient Air Quality Monitoring Stations (CAAQMS) in Kerala, India.<br><br>

The data includes pollutant concentrations such as:<br>
- PM2.5, PM10<br>
- CO, NO, NO₂, NOx, SO₂, NH₃, Ozone (O₃)<br><br>

Using regression algorithms like Random Forest, we aim to estimate AQI based on these pollutant levels and help 
visualize trends for better environmental management and public awareness.
</div>
""", unsafe_allow_html=True)

# ------------------ Image ------------------
st.image(r"C:\Users\akhil\OneDrive\Pictures\Saved Pictures\26840.jpg", use_container_width=True)

# ------------------ Inputs ------------------
st.subheader("🧪 Enter Pollutant Concentrations:")
CO = st.number_input("Carbon Monoxide (CO)")
Ozone = st.number_input("Ozone (O₃)")
NO = st.number_input("Nitric Oxide (NO)")
NO2 = st.number_input("Nitrogen Dioxide (NO₂)")
NOX = st.number_input("Nitrogen Oxides (NOx)")
NH3 = st.number_input("Ammonia (NH₃)")
SO2 = st.number_input("Sulphur Dioxide (SO₂)")
PM25 = st.number_input("Particulate Matter ≤ 2.5 μm (PM2.5)")
PM10 = st.number_input("Particulate Matter ≤ 10 μm (PM10)")

# ------------------ Prediction ------------------
if st.button("🚀 Predict AQI"):
    with open(r'C:\Users\akhil\Downloads\li.pkl', 'rb') as file:
        classifier = pickle.load(file)
        prediction = classifier.predict([[CO, Ozone, NO, NO2, NOX, NH3, SO2, PM25, PM10]])
        predicted_aqi = prediction[0]

        st.markdown(f"### 🧾 Predicted AQI: `{round(predicted_aqi, 2)}`")

        if predicted_aqi <= 50:
            st.success("🟢 Good")
        elif predicted_aqi <= 100:
            st.info("🟡 Moderate 🌤️")
        elif predicted_aqi <= 150:
            st.warning("🟠 Unhealthy for Sensitive Groups ⚠️")
        elif predicted_aqi <= 200:
            st.error("🔴 Unhealthy 🛑")
        elif predicted_aqi <= 300:
            st.error("🟣 Very Unhealthy ☣️")
        elif predicted_aqi <= 500:
            st.error("☠️ Hazardous")
        else:
            st.warning("📉 AQI value out of range")

# ------------------ AQI Chart ------------------
st.image(r"C:\Users\akhil\Downloads\WhatsApp Image 2025-06-03 at 6.22.58 PM.jpeg",
         caption="AQI Classification Scale",
         use_container_width=True)

# ------------------ Footer ------------------
st.markdown("🧠 Built with Machine Learning · 🌏 For cleaner air in Kerala!")
