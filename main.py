import argparse
import json
import os
from weather import get_weather
from weather import extract_weather_data
from compare_weather import compare_weather
from compare_weather import get_weather_data

CONFIG_FILE = "config.json"
flag=0
def get_user_info():
    if os.path.isfile(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                config_data = json.load(file)
                name = config_data.get("name")
                default_location = config_data.get("location")
        except json.JSONDecodeError:
            print("Invalid or empty JSON file. Starting from scratch.")
            name = input("Enter your name: ")
            default_location = input("Enter your default location: ")
    else:
        name = input("Enter your name: ")
        default_location = input("Enter your default location: ")

    print(f"Hey {name}. Welcome back! Choose an option: \n")
    print("1. Use default location")
    print("2. Use new location")
    print("3. Compare Weather of two locations")
    choice = input("Enter your choice (1 or 2 or 3): ")

    if choice == "2":
        location = input("Enter new location: ")
        get_weather(location)
        
    elif choice == "3":
        flag=1
        city1 = input("Enter the first city name: ")
        city2 = input("Enter the second city name: ")

        weather_data_city1 = get_weather_data(city1)
        weather_data_city2 = get_weather_data(city2)
        compare_weather(city1, weather_data_city1, city2, weather_data_city2)
        
    elif choice == "1":
        location = default_location
        get_weather(location)

    with open(CONFIG_FILE, "w") as file:
        config_data = {"name": name, "location": location}
        json.dump(config_data, file)

    return

def main():
    get_user_info()
    
if __name__ == "__main__":
    main()