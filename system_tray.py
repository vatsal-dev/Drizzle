import pystray
import json
import os
from PIL import Image
from weather import get_weather, extract_weather_data
from compare_weather import compare_weather, get_weather_data
from datetime import datetime, timedelta



class UpdateInfoMenuItem(pystray.MenuItem):
    def __init__(self, default_location):
        self.default_location = default_location
        self.weather_data = get_weather_data(default_location)
        self.last_updated_time = None  # Initialize last_updated_time to None
        super().__init__('Update Info', self.action)

    def action(self):
        self.weather_data = get_weather_data(self.default_location)
        self.last_updated_time = datetime.now()  # Update last_updated_time with the current time

    @property
    def text(self):
        ## Only show weather of next four intervals
        count = 0
        interval_weather = []
        
        # relative dates
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        tomorrow = today + timedelta(days=1)
        for entry in self.weather_data:
            dt_str = entry["date"]
            temperature = entry["temperature"]

            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            if dt.date() == today.date():
                dt_formatted = f"Today, {dt.strftime('%I:%M %p')}"
            elif dt.date() == tomorrow.date():
                dt_formatted = f"Tomorrow, {dt.strftime('%I:%M %p')}"
            else:
                if dt.hour == 0:
                    dt_formatted = "12 AM"
                elif dt.hour == 12:
                    dt_formatted = "12 PM"
                elif dt.hour > 12:
                    dt_formatted = f"{dt.hour - 12} PM"
                else:
                    dt_formatted = f"{dt.hour} AM"

            temperature_celsius = round(temperature - 273, 1)

            interval_weather.append(f"{dt_formatted}: {temperature_celsius}°C")

            count += 1
            if count == 4:
                break

        return "Click to update: " + " | ".join(interval_weather)

def exit_action(icon, item):
    icon.stop()

def create_icon(default_location):
    image = Image.open("V:\WeatherCast\WeatherCast\weather.png")
    
    menu = (
        UpdateInfoMenuItem(default_location),
        pystray.MenuItem('Last Updated: N/A', None, enabled=False),
        pystray.MenuItem('Exit', exit_action), 
    )

    icon = pystray.Icon("name_of_your_app", image, "MeteoMate", menu)
    icon.menu = menu

    return icon

def system_tray(default_location):
    icon = create_icon(default_location)

    # Run the main loop
    try:
        icon.run()
    except AttributeError as e:
        print(f"Error: {e} - Please check if the required methods exist in the pystray library.")

##? Weather Icon From: <a href="https://www.flaticon.com/free-icons/weather" title="weather icons">Weather icons created by iconixar - Flaticon</a>
