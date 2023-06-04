# MeteoMateCLI
# MeteorologicalMateCLI

# Command-Line Weather Forecast Tool

This command-line tool allows you to fetch the current weather forecast for a specific city using the OpenWeatherMap API. It also incorporates data visualization capabilities to present weather data in a visually appealing manner.


## Features

- Fetches the current weather forecast for a specified city.
- Utilizes the OpenWeatherMap API to retrieve accurate weather data.
- Parses the API response to extract relevant weather information.
- Implements robust error handling for API requests and responses. Handles misspelled city names and displays appropriate error messages.
- Incorporates data visualization using Matplotlib.
- Presents weather patterns and trends through visually appealing charts, graphs, or maps. Allows users to download and share the generated graphs.
- Provides an interactive and personalized experience. Greets the user by name and prompts further actions through commands.
- Offers the choice to either use a default location or input a new location.
- Displays the weather forecast for the next 6 days at various time intervals.
- Supports setting the previously entered location as the default for subsequent runs.

## Prerequisites

Before running the tool, ensure that you have the following installed:

- Python (version X.X.X or higher)
- pip (to install Python packages)

## Installation

1. Clone the repository or download the project files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required Python packages by running the following command:

                ||   pip install -r requirements.txt  || 

This will install the necessary packages, including Matplotlib for data visualization.

## Usage

To fetch the weather forecast for a specific city, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command:

                ||  python main.py    ||



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
