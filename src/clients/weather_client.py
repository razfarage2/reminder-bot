import requests
import os


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
