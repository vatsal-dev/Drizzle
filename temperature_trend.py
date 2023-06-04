import matplotlib.pyplot as plt
import numpy as np

def plot_temperature_trend(weather_data):
    dates_list = [forecast["date"] for forecast in weather_data]
    temperature_list = [forecast["temperature"] - 273.15 for forecast in weather_data]  # Convert from Kelvin to Celsius

    # Create a higher density x-axis for the smooth curve
    x = np.linspace(0, len(dates_list) - 1, 2000)

    plt.figure(figsize=(10, 6))
    plt.plot(x, np.interp(x, range(len(dates_list)), temperature_list), color='blue', linestyle='-', linewidth=2)
    plt.scatter(range(len(dates_list)), temperature_list, color='blue', marker='o')
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trend")

    tick_positions = range(0, len(dates_list), 2)
    tick_labels = dates_list[::2]
    plt.xticks(tick_positions, tick_labels, rotation=45, fontsize=8)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
