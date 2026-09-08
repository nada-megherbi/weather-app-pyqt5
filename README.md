# 🌤️ Modern Weather App

A sleek, responsive desktop weather application built with **Python**, **PyQt5**, and **OpenWeatherMap API**, styled with a custom modern **Glassmorphism** QSS interface.

---

## ✨ Features

* **Real-time Weather Data:** Displays current temperature, weather conditions, and matching emojis.
* **Modern UI:** Built with a custom Glassmorphism aesthetic (gradients, transparency, rounded corners).
* **Metric Units:** Temperature displayed automatically in Celsius (`°C`).
* **Secure API Key Management:** Environment variables managed via `.env` file to prevent credential leaks.
* **Error Handling:** Clear status feedback for invalid city names or network issues.

---

## 🛠️ Tech Stack

* **Language:** Python 3.13
* **GUI Framework:** PyQt5
* **Styling:** Custom Qt Style Sheets (QSS)
* **API:** [OpenWeatherMap API](https://openweathermap.org/api)
* **Libraries:** `requests`, `python-dotenv`

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python 3 installed on your system.

### 2. Installation

Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/nada-megherbi/weather-app-pyqt5.git)
cd YOUR_REPOSITORY

#Install the required packages:
pip install pyqt5 requests python-dotenv

### 3. Configuration
Get a free API key from OpenWeatherMap.

Create a .env file in the root directory of the project.

Add your API key inside the .env file:
OPENWEATHER_API_KEY=your_actual_api_key_here

### 4. Running the Application
Launch the application using Python:
python main.py