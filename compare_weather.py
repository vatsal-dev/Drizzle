import matplotlib.pyplot as plt
import requests
import json
import os
import datetime
from cache import load_cache
from temperature_trend import plot_temperature_twoInOne
import time
from weather import get_weather

API_KEY = '6b03a86116c4bfcfeb0a1c66bd5f92bc'
def get_weather_data(city):
    cache_data = load_cache()
    if city in cache_data:
        weather_data_variable = cache_data[city]
    return weather_data_variable
        
def compare_weather(city1, weather_data_city1, city2, weather_data_city2):
    # Call the function from the other file that plots the temperature graph
    plot_temperature_twoInOne(weather_data_city1, city1, weather_data_city2, city2 )
    return