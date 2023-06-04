import argparse
import json
import os
from weather import get_weather

CONFIG_FILE = "config.json"

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
    choice = input("Enter your choice (1 or 2): ")

    if choice == "2":
        location = input("Enter new location: ")
    else:
        location = default_location

    with open(CONFIG_FILE, "w") as file:
        config_data = {"name": name, "location": location}
        json.dump(config_data, file)

    return name, location

def main():
    name, location = get_user_info()
    get_weather(location)

if __name__ == "__main__":
    main()
