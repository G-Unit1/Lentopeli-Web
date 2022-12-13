import kursori
import requests


def fetch_weather(airport):
    sql__find_target_coordinates = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident = '{airport}'"
    target_coordinates = kursori.kursori_hae(sql__find_target_coordinates)[0]

    api_key = "2f216a569415f45775cd6b7fe63dcecc"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={target_coordinates[0]}&lon={target_coordinates[1]}&appid={api_key}&units=metric&lang=en"
    response = requests.get(url)

    json_response = response.json()

    wind = json_response['wind']['speed']
    temp = json_response['main']['temp']
    weather = json_response['weather'][0]['main']

    response = {
        "weather": weather,
        "wind": wind,
        "temp": temp
    }

    return response
