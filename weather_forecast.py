import requests
import json
api_key = "2b8aefcd7dc3bbe081e8fe045860bb4f"
base_url = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error occurred while fetching weather data.")
        return None
if __name__ == "__main__":
    city = input("Enter a city name: ")
    weather = get_weather(city)

    if weather:
        print("Weather forecast for", city)
        print("Temperature:", weather["main"]["temp"], "°C")
        print("Weather condition:", weather["weather"][0]["description"])
    else:
        print("Failed to fetch weather data.")

