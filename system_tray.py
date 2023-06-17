import pystray
import json
import os
from PIL import Image
from weather import get_weather, extract_weather_data
from compare_weather import compare_weather, get_weather_data



class UpdateInfoMenuItem(pystray.MenuItem):
    def __init__(self, default_location):
        self.default_location = default_location
        self.weather_data = get_weather_data(default_location)
        super().__init__('Update Info', self.action)

    def action(self):
        self.weather_data = get_weather_data(self.default_location)

    @property
    def text(self):
        return f"Weather: {self.weather_data}"

def exit_action(icon, item):
    icon.stop()

def create_icon(default_location):
    image = Image.open("V:\WeatherCast\WeatherCast\weather.png")

    menu = (UpdateInfoMenuItem(default_location),
            pystray.MenuItem('Exit', exit_action))

    icon = pystray.Icon("name_of_your_app", image, "MeteoMate", menu)
    icon.menu = menu

    return icon

def system_tray(default_location):
    icon = create_icon(default_location)

    ##? Weather Icon From: <a href="https://www.flaticon.com/free-icons/weather" title="weather icons">Weather icons created by iconixar - Flaticon</a>
    # Run the main loop
    icon.run()

