import os
import sys
import requests
from dotenv import load_dotenv
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout, QFrame)
from PyQt5.QtCore import Qt

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY") 


class weatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")  
        
        # Fixed window size to prevent stretching
        self.setFixedSize(400, 620)

        # ----------------------------------------------------
        # 1. MODERN GLASSMORPHISM STYLESHEET
        # ----------------------------------------------------
        self.setStyleSheet("""
            /* Main background gradient */
            QWidget#main_window {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0f172a, stop:0.5 #1e1b4b, stop:1 #311042);
                font-family: 'Segoe UI', Roboto, sans-serif;
                color: #ffffff;
            }

            /* Input Field */
            QLineEdit#city_input {
                background-color: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 20px;
                padding: 12px 20px;
                font-size: 30px;
                color: #ffffff;
            }
            QLineEdit#city_input:focus {
                border: 1.5px solid #a855f7;
                background-color: rgba(255, 255, 255, 0.12);
            }

            /* Modern Glowing Button */
            QPushButton#get_weather_button {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6366f1, stop:1 #a855f7);
                border: none;
                border-radius: 20px;
                padding: 12px;
                font-size: 28px;
                font-weight: bold;
                color: #ffffff;
            }
            QPushButton#get_weather_button:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4f46e5, stop:1 #9333ea);
            }
            QPushButton#get_weather_button:pressed {
                background-color: #4338ca;
            }

            /* Glassmorphism Card */
            QFrame#weather_card {
                background-color: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 24px;
            }

            /* Result Labels */
            QLabel#city_label {
                font-size: 32px;
                font-weight: 600;
                color: #f3e8ff;
            }
            QLabel#temperature_label {
                font-size: 64px;
                font-weight: 800;
                color: #ffffff;
            }
            QLabel#emoji_label {
                font-size: 95px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label {
                font-size: 22px;
                font-weight: 500;
                color: #c084fc;
            }
        """)

        # Set Object Name for main window styling
        self.setObjectName("main_window")

        # ----------------------------------------------------
        # 2. WIDGET LAYOUTS
        # ----------------------------------------------------
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 40, 30, 40)
        main_layout.setSpacing(15)

        # Input fields
        self.city_input = QLineEdit(self)
        self.city_input.setObjectName("city_input")
        self.city_input.setPlaceholderText("Enter a city name...")
        self.city_input.setAlignment(Qt.AlignCenter)

        self.get_weather_button = QPushButton("Get Weather", self)
        self.get_weather_button.setObjectName("get_weather_button")

        main_layout.addWidget(self.city_input)
        main_layout.addWidget(self.get_weather_button)

        # Create the "Glassmorphism Card" frame to hold the results
        self.card = QFrame(self)
        self.card.setObjectName("weather_card")

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 25, 20, 25)

        self.city_label = QLabel(self)
        self.city_label.setObjectName("city_label")

        self.temperature_label = QLabel(self)
        self.temperature_label.setObjectName("temperature_label")

        self.emoji_label = QLabel(self)
        self.emoji_label.setObjectName("emoji_label")

        self.description_label = QLabel(self)
        self.description_label.setObjectName("description_label")

        # Center-align all result labels inside the card
        for label in [self.city_label, self.temperature_label, self.emoji_label, self.description_label]:
            label.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(label)

        self.card.setLayout(card_layout)
        main_layout.addWidget(self.card)

        # Apply main layout
        self.setLayout(main_layout)

        # Connect button click signal to event handler
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text().strip()
        
        if not city:
            self.display_error("Please enter a city")
            return

        # Request weather data with metric units and English language output
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request")
                case 401:
                    self.display_error("Invalid API key")
                case 404:
                    self.display_error("City not found")
                case _:
                    self.display_error("HTTP error occurred")
        except requests.exceptions.RequestException:
            self.display_error("Connection error")

    def display_error(self, message):
        self.city_label.setText("")
        self.temperature_label.setText("")
        self.emoji_label.setText("⚠️")
        self.description_label.setText(message)

    def display_weather(self, data):
        city_name = data["name"]
        temp_c = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"]

        self.city_label.setText(city_name)
        self.temperature_label.setText(f"{temp_c:.1f}°C")
        self.description_label.setText(description.capitalize())
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌧️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 700 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        return "🌡️"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = weatherApp()   
    weather_app.show()
    sys.exit(app.exec_())