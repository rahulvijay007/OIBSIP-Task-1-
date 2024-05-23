import requests
def fetch_weather(key, loc):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={loc}&appid={key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None
def display_weather(weather):
    if weather:
        print(f"Weather in {weather['name']}:")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Humidity: {weather['main']['humidity']}%")
        print(f"Weather Conditions: {weather['weather'][0]['description']}")
    else:
        print("No weather data to display.")
if __name__ == "__main__":
    api_key = "dfabeb00d8686b59777b2d2e3a2d4144" 
    location = input("Enter city name: ")
    weather_data = fetch_weather(api_key, location)
    display_weather(weather_data)