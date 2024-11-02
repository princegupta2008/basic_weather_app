import requests


def get_weather(city_name, api_key):
    """
    Fetches weather data for a given city from the OpenWeatherMap API.

    Parameters:
    - city_name: str, the name of the city
    - api_key: str, the API key for OpenWeatherMap

    Returns:
    - dict containing weather information if successful, None otherwise.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def display_weather_info(weather_data):
    """
    Displays temperature, humidity, and general weather conditions.

    Parameters:
    - weather_data: dict containing weather data.
    """
    if weather_data:
        main_data = weather_data.get("main", {})
        weather_description = weather_data.get("weather", [{}])[0].get("description", "No description")

        temperature = main_data.get("temp", "N/A")
        humidity = main_data.get("humidity", "N/A")

        print(f"\nWeather in {weather_data.get('name', 'Unknown location')}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("No weather data to display.")


def main():
    api_key = "YOUR_API_KEY"  # Replace this with your actual OpenWeatherMap API key
    city_name = input("Enter the name of the city: ")

    weather_data = get_weather(city_name, api_key)
    display_weather_info(weather_data)

# Uncomment the line below to run the main function
# main()
