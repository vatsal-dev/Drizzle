import matplotlib.pyplot as plt
import requests
import json
import os
import datetime
from temperature_trend import plot_temperature_twoInOne
import time
from weather import get_weather

def compare_weather(city1, weather_data_city1, city2, weather_data_city2):
    # Call the function from the other file that plots the temperature graph
    plot_temperature_twoInOne(weather_data_city1, city1, 'blue')
    plot_temperature_twoInOne(weather_data_city2, city2, 'red')
    return