# Drizzle

## Command-Line Weather Forecast Tool

This command-line tool allows you to fetch the current weather forecast for a specific city using the OpenWeatherMap API. It also incorporates data visualization capabilities to present weather data in a visually appealing manner.


## Features

- Fetches the current weather forecast for a specified city.
- Utilizes the OpenWeatherMap API to retrieve accurate weather data.
- Parses the API response to extract relevant weather information.
- Implements robust error handling for API requests and responses. Handles misspelled city names and displays appropriate error messages.
- Incorporates data visualization using Matplotlib.
- Presents weather patterns and trends through visually appealing charts. Allows users to download and share the generated graphs.
- Provides an interactive and personalized experience. Greets the user by name and prompts further actions through commands.
- Offers the choice to use a default location or input a new one.
- Displays the weather forecast for the next six days at various intervals.
- Supports setting the previously entered location as the default for subsequent runs.

| Feature | Description | Implementation with **GitHub Copilot** and **Microsoft Technologies** | User Benefits | Tech Stack Used |
| --- | --- | --- | --- | --- |
| **Graphs** | Visualize weather data trends with interactive charts | Utilized GitHub Copilot to assist in generating code for chart rendering and data visualization. Enhanced the visualization of the graph using suggestions made by GitHub Copilot. | Easily track and analyze historical weather patterns and forecast trends. Make informed decisions based on visual insights. | GitHub Copilot, Data Analytics,  Matplotlib library |
| **Autocomplete** | Start typing a city name and get suggestions to complete it. | Integrated GitHub Copilot to optimize the autocomplete feature and used GeoNames API to fetch city names for the suggestions. | Save time and avoid typos by quickly selecting the correct city name from the suggested options. The suggestions are retrieved from the GeoNames API, ensuring that valid and up-to-date city names are provided.| GitHub Copilot, GeoNames API, prompt_toolkit, prompt, prompt_toolkit.completion, Completer, and Completion libraries. |
| **Caching Update more details** | The cache mechanism implemented in the code allows for quicker retrieval of weather data for previously searched cities, reducing response times and minimizing dependence on external APIs | Integrated GitHub Copilot to optimize the autocomplete feature and used GeoNames API to fetch city names for the suggestions. | Save time and avoid typos by quickly selecting the correct city name from the suggested options. The suggestions are retrieved from the GeoNames API, ensuring that valid and up-to-date city names are provided.| GitHub Copilot, GeoNames API, prompt_toolkit, prompt, prompt_toolkit.completion, Completer, and Completion libraries. |
| **Interactive Mode** | Engage with real-time weather information through command-line controls | Leveraged GitHub Copilot's code generation capabilities to build interactive controls. Utilized the capabilities of GitHub Copilot to generate test cases and identify errors automatically. | Explore current weather conditions, forecasts, and additional details interactively. Interactive mode simplifies the input process for users by presenting them with clear choices and prompts. This reduces the chances of input errors and ensures that users provide the required information in a structured and consistent manner. | GitHub Copilot, JSON library (for configuration file handling), PIL (Python Imaging Library, for working with images) |                 
| **Compare Weather** | Compare weather conditions between multiple locations side by side | Employed GitHub Copilot to assist in developing the comparison feature, enabling simultaneous display of weather data for different locations. <br> Used Data Analytics to compare weather between two cities and display the comparison through a graph, each city with a different color, making it easy for the user to conclude decisions. | Plan trips, events, or outdoor activities by comparing weather forecasts for different locations. Make well-informed decisions based on comprehensive weather comparisons. | GitHub Copilot, <br> OpenWeather API, <br> Data Analytics, <br> REQUESTS library (for making API requests), <br> MATPLOTLIB library |
| **System Tray Icon** | Access weather information directly from the system tray | Integrated GitHub Copilot to implement system tray functionality, allowing users to access weather information with a single click. Utilized Microsoft's cloud-based notification services to deliver real-time weather updates and notifications to the system tray, ensuring timely information delivery without disrupting user workflow. | Check current weather conditions, temperature, or receive notifications without the need to open the app. Conveniently stay informed with just a glance. | GitHub Copilot, Azure                 |
| **Auto Update in Background** | Automatically fetch updated weather data at regular intervals | Utilized GitHub Copilot's code suggestions to develop the background auto-update functionality. Integrated Microsoft Azure's cloud-based scheduling and data retrieval services to automatically fetch and update weather data at predetermined intervals. This ensures users always have access to the latest and most accurate weather information without manual intervention. | Stay up-to-date with the latest weather information without manual intervention. Ensure accurate and timely forecasts without the need to constantly refresh or manually update. | GitHub Copilot, Azure                 |
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
