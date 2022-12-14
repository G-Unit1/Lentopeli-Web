import cursor
import json


def get_player(player_name):
    sql__get_player = f"select screen_name, co2_consumed from game where screen_name = '{player_name}'"
    player_data = cursor.cursor_fecth(sql__get_player)

    sql__get_player_location = f"SELECT game.location, airport.latitude_deg, airport.longitude_deg, " \
                               f"airport.municipality, country.name, airport.continent FROM game INNER JOIN " \
                               f"airport INNER JOIN country WHERE airport.ident = game.location AND " \
                               f"airport.iso_country = country.iso_country AND game.screen_name = '{player_name}'"
    player_location = cursor.cursor_fecth(sql__get_player_location)[0]

    sql__get_flights = f"SELECT flights.destination, airport.latitude_deg, airport.longitude_deg, airport.name, " \
                       f"airport.municipality, country.name, airport.continent FROM airport INNER JOIN flights " \
                       f"INNER JOIN game INNER JOIN country WHERE airport.ident = flights.destination AND " \
                       f"airport.iso_country = country.iso_country and flights.origin = game.location AND " \
                       f"game.screen_name = '{player_name}'"
    flights = cursor.cursor_fecth(sql__get_flights)

    sql__check_goals_reached = f"SELECT goal.id FROM goal INNER JOIN game inner join goal_reached WHERE " \
                               f"goal_reached.game_id = game.id AND goal_reached.goal_id = goal.id " \
                               f"AND game.screen_name = '{player_name}';"
    goals_reached_result = cursor.cursor_fecth(sql__check_goals_reached)

    goals_reached = []
    for i in goals_reached_result:
        if i == (1,):
            goals_reached.append(1)
        if i == (2,):
            goals_reached.append(2)
        if i == (3,):
            goals_reached.append(3)
        if i == (4,):
            goals_reached.append(4)
        if i == (5,):
            goals_reached.append(5)
        if i == (6,):
            goals_reached.append(6)

    json_format = {
        "player_data": {
            "screen_name": player_data[0][0],
            "co2_consumed": player_data[0][1],
            "location": player_location,
            "goals_reached": goals_reached
        },
        "flights": flights
    }

    return json_format
