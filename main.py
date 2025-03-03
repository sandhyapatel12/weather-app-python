import requests  # Used to send HTTP requests to the weather API
import pyttsx3  # Used for text-to-speech conversion (works on Windows)
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv(dotenv_path=".env")


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to get weather information for a given city
def get_weather(city):
    # Define the API key (Replace this with a valid API key if needed)
    API_KEY = os.getenv("API_KEY")

    # Construct the API request URL
    url = f"https://api.weatherstack.com/current?access_key={API_KEY}&query={city}"

    try:
        # Send a request to the weather API and get the response
        response = requests.get(url)

        # Convert the response data to JSON format
        data = response.json()

        # Check if the API response contains weather data
        if "current" in data:
            # Extract the current temperature from the API response
            curr_temp = data["current"]["temperature"]

            # Print the temperature on the console
            print(f"The current temperature in {city} is {curr_temp}°C")

            # Convert the weather message to speech (works on Windows)
            engine.say(f"The current weather in {city} is {curr_temp} degrees")
            engine.runAndWait()  # Speak the message

        else:
            # If no weather data is found, show an error message
            print("Error: Unable to retrieve weather data. Check the city name or API key.")

    # Handle any errors that may occur while making the API request
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user to enter a city name
city = input("Enter the name of the city: ")

# Call the function to get weather information for the entered city
get_weather(city)
