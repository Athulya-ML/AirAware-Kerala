📌 About the Project
Air pollution is one of the leading threats to environmental and human health. The Air Quality Index (AQI) simplifies air pollution data into a single number to easily communicate risks to the public.

This project:

Uses regression models (e.g., Random Forest) to predict AQI
Is trained on data from Kerala's CAAQMS (Dec 2023 – Feb 2024)
Takes pollutant levels as input and classifies air quality (e.g., Good, Moderate, Hazardous)
Is deployed as an interactive web app with Streamlit
🚀 Features
📊 Input fields for pollutants: CO, O₃, NO, NO₂, NOx, NH₃, SO₂, PM2.5, PM10
🤖 Real-time AQI prediction using trained model
🟢 AQI classification and color-coded health categories
📈 Optional bar chart to visualize input pollutant levels
📷 AQI scale image and attractive UI styling
🧪 Tech Stack
Tool	Purpose
Python	Core programming language
Pandas	Data manipulation
Scikit-learn	Machine Learning models
Streamlit	Web interface
Matplotlib	Plotting charts
Pickle	Model serialization
🧠 How It Works
User enters pollutant concentrations.
The trained model predicts AQI based on inputs.
AQI is interpreted using CPCB standards (Good, Moderate, etc.).
User receives color-coded health guidance and can visualize inputs.
📁 Project Structure
├── project.py # Streamlit app ├── li.pkl # Trained ML model (Random Forest) ├── README.md # This file ├── requirements.txt # Required Python packages └── images/ # AQI scale, UI screenshots

🙌 Contributing Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

📬 Contact If you have any questions or want to connect, feel free to reach out:

📧 Email: sathulya235@gmail.com

📎 GitHub: Athulya-ML

🌱 Final Note This project is a small step toward raising awareness about air quality and its impact on public health. Built with care using machine learning and visual tools to make pollution data more understandable and actionable.

Breathe clean. Think green. 💚
