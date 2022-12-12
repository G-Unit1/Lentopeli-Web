import kursori
from geopy import distance


def co2_calculator(player_name, airport):
    sql__find_player_coordinates = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport INNER JOIN game " \
                                   f"WHERE airport.ident = game.location AND game.screen_name = '{player_name}'"
    player_coordinates = kursori.kursori_hae(sql__find_player_coordinates)

    print(player_coordinates)

    sql__find_target_coordinates = f"SELECT airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident = '{airport}'"
    target_coordinates = kursori.kursori_hae(sql__find_target_coordinates)

    print(target_coordinates)

    flight_distance = distance.distance(player_coordinates, target_coordinates).miles.__floor__()

    print(flight_distance)
    # TODO: Finish the CO2 calculator





co2_calculator('make', 'KJFK')
