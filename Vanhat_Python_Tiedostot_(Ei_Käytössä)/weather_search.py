import requests

# import json

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "e76965d853e439fea2c006d1e2545908"
city = input("Syötä kaupunki: ") # change to clicked circle/pin

url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric&lang=fi"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response['main']['temp']
        description = json_response['weather'][0]['description']
        country = json_response['sys']['country']
        wind_Speed = json_response['wind']['speed']
        print(f"{country}\n"
              f"{city}\n"
              f"Lämpötila: {temp}°C\n"
              f"Tuulen nopeus: {wind_Speed}m/s\n"
              f"Sää: {description}\n")
    elif response.status_code == 404:
        print(f"Kaupunkia: {city}, ei löydy :(")

except requests.exceptions.RequestException as e:
    print("hakua ei voitu suorittaa" + str(e))
    # change prints to valid responses
