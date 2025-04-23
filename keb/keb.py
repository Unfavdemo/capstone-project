"""
keb

Description:
"""

import requests

# API configuration
API_KEY = 'c3647a82a2b304d3331fb5f595fb8f40'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Ask for city name with basic input check
city = ""
while city == "":
    city = input("Enter the city name to get weather information: ")
    if city == "":
        print("City name cannot be empty. Please try again.")

# Make the API request
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}
response = requests.get(BASE_URL, params=params)

# Check if the response was successful
if response.status_code == 200:
    data = response.json()

    # Display city and country info
    if 'name' in data and 'sys' in data and 'country' in data['sys']:
        print("\nWeather Information:")
        print("City:", data['name'])
        print("Country:", data['sys']['country'])
    else:
        print("Some location information is missing.")

    # Display menu
    print("\nAvailable Information:")
    print("1. Weather description")
    print("2. Temperature")
    print("3. Humidity")
    print("4. Wind Speed")
    print("5. All details")

    # Ask for choice
    valid_choices = ['1', '2', '3', '4', '5']
    choice = input("Enter the number for the information you want: ")
    while choice not in valid_choices:
        print("Invalid choice. Please enter a number from 1 to 5.")
        choice = input("Enter the number for the information you want: ")

    weather = data['weather'][0] if 'weather' in data and len(data['weather']) > 0 else {}
    main = data['main'] if 'main' in data else {}
    wind = data['wind'] if 'wind' in data else {}
    visibility = data['visibility'] if 'visibility' in data else "Not available"

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
        print("Weather:", weather['description'] if 'description' in weather else "Not available")
        print("Temperature:", main['temp'], "°C" if 'temp' in main else "Temperature data not available")
        print("Humidity:", main['humidity'], "%" if 'humidity' in main else "Humidity data not available")
        print("Wind Speed:", wind['speed'], "m/s" if 'speed' in wind else "Wind speed data not available")
        print("Pressure:", main['pressure'], "hPa" if 'pressure' in main else "Pressure data not available")
        print("Visibility:", visibility, "meters")
else:
    print("Failed to retrieve data. Please check your network connection or city name.")
