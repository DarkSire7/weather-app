import dotenv
import requests
import os
from pprint import pprint

dotenv.load_dotenv()


def get_weather_data(city):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("OPEN_API")}&q={city}&units=metric"

    # print(request_url)

    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    city = input("Enter city")
    weather_data = get_weather_data(city)
    print("Current weather data is: ")
    pprint(weather_data)
