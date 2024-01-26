import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        main_info = weather_data['main']
        weather_info = weather_data['weather'][0]

        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {main_info['temp']}°C")
        print(f"Description: {weather_info['description']}")
        print(f"Humidity: {main_info['humidity']}%")
        print(f"Pressure: {main_info['pressure']} hPa")
    else:
        print("Weather information not available.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your API key
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)
