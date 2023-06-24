# Drizzle
## Command-Line Weather Forecast Tool

This command-line tool lets you fetch a specific city's current weather forecast using the OpenWeatherMap API. It also incorporates data visualization capabilities to present weather data visually appealingly.

- [Features](#features)
- [Use of Github Copilot and Microsoft Technologies](#use-of-github-copilot-and-microsoft-technologies)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Real-time Weather Forecast** :partly_sunny: : Fetches the current weather forecast for a specified city, keeping you up-to-date with the latest conditions.

- **Powered by OpenWeatherMap API** :earth_americas: : Utilizes the reliable and accurate OpenWeatherMap API to retrieve precise weather data.

- **Data Extraction and Parsing** :mag_right: : Automatically extracts and parses the API response to extract relevant weather information, providing you with concise and meaningful data.

- **Robust Error Handling** :warning: : Implements robust error handling for API requests and responses. Seamlessly handles misspelled city names and displays informative error messages.

- **Stunning Data Visualization** :bar_chart: : Experience weather patterns and trends come to life through visually appealing charts powered by Matplotlib. Explore the data with interactive and downloadable graphs.

- **Personalized Interaction** :bust_in_silhouette: : Enjoy an interactive and personalized experience. The tool greets you by name and prompts further actions through intuitive commands.

- **Flexible Location Options** :round_pushpin: : Choose between using a default location or inputting a new one, giving you the flexibility to explore weather forecasts for any desired location.

- **Detailed Forecast Display** :calendar: : Get a comprehensive view of the weather forecast for the next six days at various intervals, ensuring you have all the information you need to plan ahead.

- **Convenient Default Location** :house_with_garden: : Set your previously entered location as the default for subsequent runs, saving you time and effort.

- **Caching Weather Data** :floppy_disk: : Implements caching of weather data to improve performance and reduce API calls. The tool checks the cache for previously fetched weather data for a specific city and retrieves it if available, saving time and resources.

Enhance your weather exploration with this feature-rich tool. Read about the features in detail. 😎🌦️

## Use of GitHub Copilot and Microsoft Technologies 

| Feature | Description | Implementation with **GitHub Copilot** and **Microsoft Technologies** | User Benefits | Tech Stack Used |
| --- | --- | --- | --- | --- |
| **Graphs** | Visualize weather data trends with interactive charts | Utilized GitHub Copilot to assist in generating code for chart rendering and data visualization. Enhanced the visualization of the graph using suggestions made by GitHub Copilot. | Easily track and analyze historical weather patterns and forecast trends. <br> Make informed decisions based on visual insights. | GitHub Copilot, <br> Data Analytics, <br> MATPLOTLIB library |
| **Autocomplete** | Start typing a city name and get suggestions to complete it. | Integrated GitHub Copilot to optimize the autocomplete feature and used GeoNames API to fetch city names for the suggestions. | Save time and avoid typos by quickly selecting the correct city name from the suggested options. The suggestions are retrieved from the GeoNames API, ensuring that valid and up-to-date city names are provided.| GitHub Copilot, GeoNames API, prompt_toolkit, prompt, prompt_toolkit.completion, Completer, and Completion libraries. |
| **Caching Update more details** | The cache mechanism implemented in the code allows for quicker retrieval of weather data for previously searched cities, reducing response times and minimizing dependence on external APIs | Integrated GitHub Copilot to optimize the autocomplete feature and used GeoNames API to fetch city names for the suggestions. | Save time and avoid typos by quickly selecting the correct city name from the suggested options. The suggestions are retrieved from the GeoNames API, ensuring that valid and up-to-date city names are provided.| GitHub Copilot, GeoNames API, prompt_toolkit, prompt, prompt_toolkit.completion, Completer, and Completion libraries. |
| **Interactive Mode** | Engage with real-time weather information through command-line controls | Leveraged GitHub Copilot's code generation capabilities to build interactive controls. Utilized the capabilities of GitHub Copilot to generate test cases and identify errors automatically. | Explore current weather conditions, forecasts, and additional details interactively. Interactive mode simplifies the input process for users by presenting them with clear choices and prompts. This reduces the chances of input errors and ensures that users provide the required information in a structured and consistent manner. | GitHub Copilot, JSON library (for configuration file handling), PIL (Python Imaging Library, for working with images) |                 
| **Compare Weather** | Compare weather conditions between multiple locations side by side | Employed GitHub Copilot to assist in developing the comparison feature, enabling simultaneous display of weather data for different locations. <br> Used Data Analytics to compare weather between two cities and display the comparison through a graph, each city with a different color, making it easy for the user to conclude decisions. | Plan trips, events, or outdoor activities by comparing weather forecasts for different locations. Make well-informed decisions based on comprehensive weather comparisons. | GitHub Copilot, <br> OpenWeather API, <br> Data Analytics, <br> REQUESTS library (for making API requests), <br> MATPLOTLIB library |
| **System Tray Icon** | Access weather information directly from the system tray | Utilized GitHub Copilot's code generation capabilities to implement system tray functionality, enabling users to access weather information with a single click easily. | Check current weather conditions, temperature, or receive notifications without the need to open the app. Conveniently stay informed with just a glance. | GitHub Copilot, Azure                 |
| **Auto Update in Background** | Automatically fetch updated weather data at regular intervals | Utilized GitHub Copilot's code suggestions to develop the background auto-update functionality. Integrated Microsoft Azure's cloud-based scheduling and data retrieval services to automatically fetch and update weather data at predetermined intervals. This ensures users always have access to the latest and most accurate weather information without manual intervention. | Stay up-to-date with the latest weather information without manual intervention. Ensure accurate and timely forecasts without the need to constantly refresh or manually update. | GitHub Copilot, Azure                 |
| **Notifications** | Automatically fetch updated weather data at regular intervals | Utilized GitHub Copilot's code suggestions to develop the background auto-update functionality. Integrated Microsoft Azure's cloud-based scheduling and data retrieval services to automatically fetch and update weather data at predetermined intervals. This ensures users always have access to the latest and most accurate weather information without manual intervention. | Stay up-to-date with the latest weather information without manual intervention. Ensure accurate and timely forecasts without the need to constantly refresh or manually update. | GitHub Copilot, Azure                 |
| **Personalization** | Customize app settings, preferences and default location. | Employed GitHub Copilot to streamline the development of personalization features, allowing users to customize various app settings . Integrated Microsoft Azure's cloud-based storage and configuration services to securely store and retrieve user preferences, ensuring a personalized experience across devices and sessions. | Tailor the app to suit individual preferences with various options such as using default location to fetch weather, auto update the same in background or even enter a new city and compare weather . Enhance the user experience and create a personalized weather app environment. | GitHub Copilot, Azure |


### Prerequisites

Before running the tool, make sure you have the following prerequisites installed:

*   Python (version 3.10 or higher)
*   pip (to install Python packages)

### Installation

1.  Clone the repository or download the project files.
    
2.  Open a terminal or command prompt and navigate to the project directory.
    
3.  Install the required Python packages by running the following command:
    
    `pip install -r requirements.txt`
    
    This will automatically install the necessary packages, including Matplotlib for data visualization.
    

### Usage

To fetch the weather forecast for a specific city, follow these steps:

1.  Open a terminal or command prompt and navigate to the project directory.
    
2.  Run the following command:
    
    ```cli
    python main.py
    ```
    
    This will execute the tool and prompt you for the desired city.


The tool will prompt you to enter your name and city:

                Enter your name: [Your Name]
                Enter your city: [Your City]

Enter your name and city, and then press Enter.

3. The tool will greet you and present the following options:

                Hello [Your Name], what do you want to choose?

                1.Use default location
                2.Use new location
                Enter your choice (1 or 2):


4. Enter your choice by typing `1` or `2` and press Enter.

                - If you choose option `1`, the tool will use the previously entered city as the default location and fetch the weather forecast for that location without prompting for input again.

                - If you choose option `2`, the tool will prompt you to enter a new location:

                    ```
                    Enter new location:
                    ```

            Enter the desired city name and press Enter.

5. The tool will fetch the weather forecast for the specified location for the next 6 days at different time intervals. It will display the results, including data visualizations- will show the graph for the weather changes in next few days. User is free to zoom in, zoom out, save and share the graph. 

6. The entered city will be set as the default location for the next time you run the tool.
