# IMPORTANT: pip install requests
# A basic implementation of a weather
# Author: Jorn Blaedel Garbosa

# Import the json and requests modules
import json
import requests

# Define the API endpoint and API key
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "f2456eef8d597178590c1840458a6659"

# Function to get the current weather for a given location


def get_weather(location):
    # Construct the API request URL
    url = f"{ENDPOINT}?q={location}&appid={API_KEY}"

    # Use the requests module to make an HTTP GET request to the API
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code != 200:
        # If the response is not successful, print an error message
        print("Error: Could not get weather data")
        return

    # Use the json module to parse the JSON response
    data = json.loads(response.text)

    # Get the current temperature and weather conditions from the API response
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']

    # Print the current temperature and weather conditions
    print(f"The current temperature in {location} is {temperature}°F")
    print(f"The current weather conditions are: {weather}")

# Main program


# Ask the user for a location
location = input("Enter a city or zip code: ")

# Get the current weather for the given location
get_weather(location)
