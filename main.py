import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY") 






import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class weatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")  
        self.setGeometry(700, 300, 400, 500)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Alignements
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Object Names
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Stylesheet
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }

            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }

            QLineEdit#city_input {
                font-size: 30px;
            }

            QPushButton#get_weather_button {
                font-size: 25px;
                font-weight: bold;
            }

            QLabel#temperature_label {
                font-size: 60px;
            }

            QLabel#emoji_label {
                font-size: 100px;
                font-family: "Segoe UI Emoji";
            }

            QLabel#description_label {
                font-size: 35px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        city = self.city_input.text().strip()
        
        if not city:
            self.display_error("Enter the city")
            return



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
                    self.display_error("Requête invalide")
                case 401:
                    self.display_error("Clé API non activée/invalide")
                case 404:
                    self.display_error("Ville introuvable")
                case _:
                    self.display_error("Erreur HTTP")
        except requests.exceptions.RequestException:
            self.display_error("Erreur de connexion")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.emoji_label.setText("")
        self.description_label.setText("")

    def display_weather(self, data):
        # Température directement en °C grâce à &units=metric
        temp_c = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"]

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