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

def plot_temperature_twoInOne(data1, city1, data2, city2):
    dates1 = []
    temperatures1 = []

    for item in data1:
        date = item['date']
        temperature = item['temperature']
        dates1.append(date)
        temperatures1.append(float(temperature))

    dates2 = []
    temperatures2 = []

    for item in data2:
        date = item['date']
        temperature = item['temperature']
        dates2.append(date)
        temperatures2.append(float(temperature))

    plt.plot(dates1, temperatures1, label=city1, color='red')
    plt.plot(dates2, temperatures2, label=city2, color='blue')
    plt.show()