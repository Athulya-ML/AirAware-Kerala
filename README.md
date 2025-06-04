# 🌍 ClearAirML – Air Quality Index Predictor

## 📌 About the Project

Air pollution is one of the leading threats to environmental and human health. The **Air Quality Index (AQI)** simplifies complex air pollution data into a single number to easily communicate risks to the public.

This project:

- Uses regression models (e.g., **Random Forest**) to predict AQI
- Is trained on real-time data from **Kerala's CAAQMS (Dec 2023 – Feb 2024)**
- Accepts pollutant levels as input and classifies air quality (e.g., Good, Moderate, Hazardous)
- Is deployed as an interactive web app using **Streamlit**

---

## 🚀 Features

- 📊 Input fields for pollutants: **CO, O₃, NO, NO₂, NOx, NH₃, SO₂, PM2.5, PM10**
- 🤖 Real-time AQI prediction using a trained ML model
- 🟢 AQI classification with color-coded health categories
- 📈 (Optional) bar chart to visualize input pollutant levels
- 📷 AQI scale image and clean, user-friendly UI design

---

## 🧪 Tech Stack

| Tool         | Purpose                  |
|--------------|---------------------------|
| **Python**   | Core programming language |
| **Pandas**   | Data manipulation         |
| **Scikit-learn** | Machine Learning models |
| **Streamlit**| Web interface             |
| **Matplotlib** | Plotting charts (optional) |
| **Pickle**   | Model serialization       |

---

## 🧠 How It Works

1. User enters pollutant concentrations through the UI.
2. The trained model predicts AQI based on input values.
3. AQI is interpreted using **CPCB standards** (e.g., Good, Moderate, Unhealthy).
4. User receives a visual and color-coded health warning.

---

## 📁 Project Structure

AQI-Predictor/
├── app.py # Streamlit app
├── li.pkl # Trained ML model (Random Forest or Linear Regression)
├── requirements.txt # Required Python packages
├── README.md # Project documentation (this file)
└── images/
├── aqi-scale.jpeg # AQI classification chart
└── pollution.jpg # UI image (optional)


---

## 🙌 Contributing

Contributions are welcome! 🎉  
If you have suggestions, improvements, or bug fixes, feel free to **open an issue** or **submit a pull request**.

---

## 📬 Contact

- 📧 Email: [sathulya235@gmail.com](mailto:sathulya235@gmail.com)
- 🐙 GitHub: [Athulya-ML](https://github.com/Athulya-ML)

---

## 🌱 Final Note

This project is a small step toward raising awareness about **air quality** and its direct impact on public health.  
Built with care using machine learning and visualization tools to make pollution data more **understandable** and **actionable**.

> **Breathe clean. Think green. 💚**

---
