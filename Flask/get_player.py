import kursori


def get_player(player_name):
    sql__get_player = f"select screen_name, co2_consumed from game where screen_name = '{player_name}'"
    player_data = kursori.kursori_hae(sql__get_player)

    sql__get_player_location = f"SELECT game.location, airport.latitude_deg, airport.longitude_deg, " \
                               f"airport.municipality, country.name, airport.continent FROM game INNER JOIN " \
                               f"airport INNER JOIN country WHERE airport.ident = game.location AND " \
                               f"airport.iso_country = country.iso_country AND game.screen_name = '{player_name}'"
    player_location = kursori.kursori_hae(sql__get_player_location)[0]

    sql__get_flights = f"SELECT destination, latitude_deg, longitude_deg FROM airport INNER JOIN flights " \
                       f"INNER JOIN game WHERE airport.ident = flights.destination AND " \
                       f"flights.origin = game.location AND game.screen_name = '{player_name}'"
    flights = kursori.kursori_hae(sql__get_flights)

    json_format = {
        "player_data": {
            "screen_name": player_data[0][0],
            "co2_consumed": player_data[0][1],
            "location": player_location
        },
        "flights": flights
    }

    return json_format
