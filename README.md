# 🌤️ Weather Info App

## Purpose/Problem Statement
The Weather Info App provides real-time weather information for any city using the OpenWeatherMap API. It solves the problem of accessing accurate weather data without needing to visit multiple websites or open complex apps. The app offers a simple and efficient way for users to check current weather details directly in the terminal.

---

## Target Audience
- **Students**: Who need quick and easy access to weather information for planning their day.
- **Travelers**: Looking for up-to-date weather before traveling or during their trips.
- **Casual Users**: Anyone who wants reliable weather information without the hassle of navigating complex apps.

---

## Solution + Limitations
The app allows users to input a city name and choose from a variety of weather details, such as weather description, temperature, humidity, wind speed, or all available details. The app is interactive and provides clear output in the terminal.

### Limitations:
- The app only supports fetching weather data for one city at a time.
- There is currently no error handling for invalid API keys or network issues.
- The app does not include an extended forecast (e.g., 5-day or 7-day forecast).
- The app only supports temperature in Celsius.

---

## Key Features / Key Components
- **City Input**: The user enters the name of a city to retrieve weather data.
- **Weather Information**: Users can select from options like weather description, temperature (°C), humidity, wind speed, or view all details.
- **Clean Terminal Output**: Weather information is displayed in a simple, readable format.

---

## Technical Challenges + Future Plans
### Challenges:
- Ensuring the user input is validated without using `.strip()` or `try/except`, which made it necessary to approach input handling creatively.
- Parsing the JSON data from the API response to ensure the information is accessed and displayed correctly.

### Future Plans:
- Add support for Fahrenheit temperature units.
- Implement error handling to catch invalid user input or failed API requests.
- Build a graphical user interface (GUI) to make the app more visually appealing.
- Add extended forecast options for 5-day or 7-day weather data.

---

## Project Timeline
- **Day 1-2**: Setting up the OpenWeatherMap API and learning how to make requests and process JSON data.
- **Day 3**: Developing the core functionality for fetching weather information based on city input.
- **Day 4**: Implementing options for selecting specific weather details and displaying them.
- **Day 5**: Testing the app with various cities to ensure it works correctly.
- **Day 6**: Refining the code and optimizing the structure, adding simple messages for the user.

---

## Tools and Resources Used
- **OpenWeatherMap API**: For fetching real-time weather data.
- **Python Documentation**: To understand the syntax and functionality of Python features used.
- **Tutorials on Python `requests` Library**: Helped with making API calls and handling the JSON response.
- **Stack Overflow**: Used for troubleshooting issues related to JSON parsing and user input validation.

---
