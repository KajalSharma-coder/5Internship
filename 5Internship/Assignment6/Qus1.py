import requests
from datetime import datetime

city = input("Enter city name: ")

api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=246c5972d37205572b347da61dfc82fa&units=metric"

response = requests.get(url)

data = response.json()

if data["cod"] != 200:
    print("City not found!")
else:
    # Basic info
    city_name = data["name"]
    country = data["sys"]["country"]

    # Coordinates
    lon = data["coord"]["lon"]
    lat = data["coord"]["lat"]

    # Temperature details
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    # Atmospheric data
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    # Weather description
    weather = data["weather"][0]["description"]

    # Wind
    wind_speed = data["wind"]["speed"]

    # Visibility
    visibility = data["visibility"]

    # Sunrise & Sunset
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])

    print("\n------ Weather Report ------")
    print(f"City: {city_name}, {country}")

    print(f"Coordinates: Latitude {lat}, Longitude {lon}")

    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Minimum Temp: {temp_min}°C")
    print(f"Maximum Temp: {temp_max}°C")

    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")

    print(f"Weather Condition: {weather}")

    print(f"Wind Speed: {wind_speed} m/s")

    print(f"Visibility: {visibility} meters")

    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")