import requests
import os
# from whatsapp_client import Whatsapp_Client
# from dotenv import load_dotenv
#
# load_dotenv()
class Weather_Client:
    def __init__(self):
        self.API_KEY = os.getenv("API_WEATHER_TOKEN")
        self.rain_threshold = 40
        self.weather_data = None

        if not self.API_KEY:
            raise ValueError("API key is missing. Please set the environment variable 'API_WEATHER_TOKEN'.")

        self.weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat=32.0730&lon=34.7742&units=imperial&APPID={self.API_KEY}"
        )

        if self.weather_data.status_code != 200:
            raise Exception(f"Failed to fetch weather data: {self.weather_data.status_code}")

    def retry_function(self, retires=3, exception=Exception):
        def decorator(func):
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < retires:
                    try:
                        return func(*args, **kwargs)
                    except exception as e:
                        attempts = +1
                        print(f'Failed: ({attempts}/{retires})')
                raise exception

            return wrapper

        return decorator

    def temp_cel(self):
        temp_F = self.weather_data.json()["main"]["temp"]
        temp_C = round(
            (temp_F - 32) * 5 / 9)

        return temp_C

    def chance_for_rain(self, temp_c):
        rain = self.weather_data.json().get("rain", {})
        chance_for_rain = rain.get("5h", 0)

        # Using the sentences as a list, so I can edit or add in the future other custom-made.
        sentence = f"""It looks like rain is in the forecast! 🌧️\nThe chance of rain in Tel Aviv is {chance_for_rain}%.\nThe current temperature is {temp_c}°C. Don't forget your umbrella when you're heading out!"""

        if chance_for_rain >= self.rain_threshold:
            weather_forecast = sentence[0]
            return weather_forecast
        else:
            return f"🌞 Low chance of rain in Tel Aviv today ({chance_for_rain}%)—perfect day to enjoy the sunshine!🌞"

    @retry_function(retires=5, exception=requests.exceptions.HTTPError)
    def get_weather(self):
        # edge case for not finding the city
        if self.weather_data.json()["cod"] == "404":
            no_city = " No city found"
            print(no_city)

            return no_city
        weather = self.weather_data.json()["weather"][0]["main"]
        temp_C = self.temp_cel()
        check_rain = self.chance_for_rain(self.temp_cel())

        return check_rain
