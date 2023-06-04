import argparse
import json
import os
from weather import get_weather
from compare_weather import compare_weather

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
        compare_weather = input("Do you want to compare weather for two cities? (y/n): ")

        if compare_weather.lower() == 'n':
            print("Okay! Here's the weather of your location")
        elif compare_weather.lower() == 'y':
            flag=1
            city1 = input("Enter the first city name: ")
            city2 = input("Enter the second city name: ")

            weather_data_city1 = get_weather(city1)
            weather_data_city2 = get_weather(city2)
            compare_weather(city1, weather_data_city1, city2, weather_data_city2)
        


    print(f"Hey {name}. Welcome back! Choose an option: \n")
    compare_weather = input("Do you want to compare weather for two cities? (y/n): ")

    if compare_weather.lower() == 'n':
        print("Okay! Make your choice then")
        print("1. Use default location")
        print("2. Use new location")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "2":
             location = input("Enter new location: ")
        else:
            location = default_location

        with open(CONFIG_FILE, "w") as file:
                config_data = {"name": name, "location": location}
                json.dump(config_data, file)

        return name, location

    elif compare_weather.lower() == 'y':
        flag=1
        city1 = input("Enter the first city name: ")
        city2 = input("Enter the second city name: ")

        weather_data_city1 = get_weather(city1)
        weather_data_city2 = get_weather(city2)
        compare_weather(city1, weather_data_city1, city2, weather_data_city2)
    

def main():
    name, location = get_user_info()
    if(flag!=1):
        get_weather(location)

if __name__ == "__main__":
    main()
