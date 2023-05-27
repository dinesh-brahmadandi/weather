import requests

api_key = "2b8aefcd7dc3bbe081e8fe045860bb4f"

def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity']
            }
            return weather_info
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

city_name = input("Enter a city name: ")
weather_data = get_weather(city_name)

if weather_data:
    print(f"Weather in {weather_data['city']}:")
    print(f"Temperature: {weather_data['temperature']} K")
    print(f"Humidity: {weather_data['humidity']}%")
