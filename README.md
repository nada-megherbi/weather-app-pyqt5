# 🌤️ Weather App

A desktop weather application built in Python using PyQt5 and the OpenWeatherMap API. It allows users to check real-time weather conditions for any city with a clean graphical user interface.

## 🚀 Features
- Real-time weather data fetching via OpenWeatherMap API
- Modern and responsive GUI built with PyQt5
- Secure API key management using environment variables (.env)
- Error handling for invalid city names or network issues

## 🛠️ Technologies Used
- Language: Python 3
- GUI Framework: PyQt5
- API: OpenWeatherMap API
- Environment Management: python-dotenv
- Tools: Git, GitHub, VS Code

## ⚙️ Installation & Setup

1. Clone the repository:
git clone https://github.com/nada-megherbi/weather-app-pyqt5.git
cd weather-app

2. Install the required packages:
pip install pyqt5 requests python-dotenv

3. Configuration:
- Get a free API key from OpenWeatherMap.
- Create a .env file in the root directory of the project.
- Add your API key inside the .env file:
OPENWEATHER_API_KEY=your_actual_api_key_here

## ▶️ Running the Application
Launch the application using Python:
python main.py
