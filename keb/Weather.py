"""
keb

Description:
"""
import requests  # Import the requests library to make HTTP requests

# Format used in this script:
# - Input/output interaction through console (using input() and print())
# - API request with parameters passed in a Python dictionary
# - Response data parsed from JSON format and accessed as nested Python dictionaries
# - Menu-based interaction using numbered choices

# API configuration
API_KEY = 'c3647a82a2b304d3331fb5f595fb8f40'  # Your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Base URL for current weather data

# Ask for city name with basic input check
city = ""
while city == "":
    city = input("Enter the city name to get weather information: ")  # Prompt user for a city
    if city == "":
        print("City name cannot be empty. Please try again.")  # Reject empty input

# Set parameters for the API request
params = {
    'q': city,          # City name
    'appid': API_KEY,   # API key
    'units': 'metric'   # Temperature in Celsius
}

# Make the API request
response = requests.get(BASE_URL, params=params)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response

    # Display city and country info if available
    if 'name' in data and 'sys' in data and 'country' in data['sys']:
        print("\nWeather Information:")
        print("City:", data['name'])
        print("Country:", data['sys']['country'])
    else:
        print("Some location information is missing.")

    # Display a menu of available weather data
    print("\nAvailable Information:")
    print("1. Weather description")
    print("2. Temperature")
    print("3. Humidity")
    print("4. Wind Speed")
    print("5. All details")

    # Ask user to choose which information they want
    valid_choices = ['1', '2', '3', '4', '5']
    choice = input("Enter the number for the information you want: ")
    while choice not in valid_choices:
        print("Invalid choice. Please enter a number from 1 to 5.")
        choice = input("Enter the number for the information you want: ")

    # Extract relevant data from the response, safely
    weather = data['weather'][0] if 'weather' in data and len(data['weather']) > 0 else {}
    main = data['main'] if 'main' in data else {}
    wind = data['wind'] if 'wind' in data else {}
    visibility = data['visibility'] if 'visibility' in data else "Not available"

    # Display specific info based on user's choice
    if choice == '1':
        print("Weather:", weather['description'] if 'description' in weather else "Not available")
    elif choice == '2':
        if 'temp' in main:
            print("Temperature:", main['temp'], "°C")
        else:
            print("Temperature data not available.")
    elif choice == '3':
        if 'humidity' in main:
            print("Humidity:", main['humidity'], "%")
        else:
            print("Humidity data not available.")
    elif choice == '4':
        if 'speed' in wind:
            print("Wind Speed:", wind['speed'], "m/s")
        else:
            print("Wind speed data not available.")
    elif choice == '5':
        # Display all available weather details
        print("Weather:", weather['description'] if 'description' in weather else "Not available")
        print("Temperature:", main['temp'], "°C" if 'temp' in main else "Temperature data not available")
        print("Humidity:", main['humidity'], "%" if 'humidity' in main else "Humidity data not available")
        print("Wind Speed:", wind['speed'], "m/s" if 'speed' in wind else "Wind speed data not available")
        print("Pressure:", main['pressure'], "hPa" if 'pressure' in main else "Pressure data not available")
        print("Visibility:", visibility, "meters")
else:
    # Handle failed request with basic error message
    print("Failed to retrieve data. Please check your network connection or city name.")

