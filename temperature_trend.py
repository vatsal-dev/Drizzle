import matplotlib.pyplot as plt

def plot_temperature_trend(weather_data):
    dates_list = [forecast["date"] for forecast in weather_data]
    temperature_list = [forecast["temperature"] - 273.15 for forecast in weather_data]  # Convert from Kelvin to Celsius

    plt.plot(dates_list, temperature_list)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")  # Update the y-axis label
    plt.title("Temperature Trend")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def plot_temperature_twoInOne(data, city, color):
    dates = []
    temperatures = []

    for item in data:
        dt_txt = item['dt_txt']
        temperature = item['main']['temp']
        dates.append(dt_txt)
        temperatures.append(temperature)

    plt.plot(dates, temperatures, label=city, color=color)
    plt.show()