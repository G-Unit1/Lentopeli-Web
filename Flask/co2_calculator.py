import math
import kursori
import weather_search
from geopy import distance


def co2_calculator(player_name, airport):
    sql__find_player_coordinates = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport INNER JOIN game " \
                                   f"WHERE airport.ident = game.location AND game.screen_name = '{player_name}'"
    player_coordinates = kursori.kursori_hae(sql__find_player_coordinates)

    sql__find_target_coordinates = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident = '{airport}'"
    target_coordinates = kursori.kursori_hae(sql__find_target_coordinates)

    weather = weather_search.fetch_weather(airport)

    flight_distance = math.floor(distance.distance(player_coordinates, target_coordinates).miles)

    co2_emissions = math.floor((flight_distance * 0.095) * weather['wind'])

    sql__update_player_co2 = f"update game set co2_consumed = co2_consumed + {co2_emissions} where screen_name = '{player_name}';"
    kursori.kursori_aja(sql__update_player_co2)

    return co2_emissions
