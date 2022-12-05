import flask
import log_in
import sign_up
import kursori

app = flask.Flask(__name__)


# This flask app is used to create a new user
@app.route('/new_game/<string:new_user>,<string:new_password>')
def new_game(new_user, new_password):
    response = sign_up.user_creation(new_user, new_password)

    return response


# This flask app is used to log into an existing user
@app.route('/continue_game/<string:username>,<string:password>')
def continue_game(username, password):
    response = log_in.login(username, password)

    return response


# This flask app is used to find all player data (screen_name, co2_consumed, location (ICAO + Coords) and available flights (ICAO + Coords)
@app.route('/get_player/<string:player_name>')
def get_player_data(player_name):
    sql__get_player = f"select screen_name, co2_consumed from game where screen_name = '{player_name}'"
    player_data = kursori.kursori_func(sql__get_player)

    sql__get_player_location = f"select location, latitude_deg, longitude_deg from game " \
                               f"inner join airport where airport.ident = game.location and game.screen_name = '{player_name}'"
    player_location = kursori.kursori_func(sql__get_player_location)[0]

    sql__get_flights = f"SELECT destination, latitude_deg, longitude_deg FROM airport INNER JOIN flights " \
                       f"INNER JOIN game WHERE airport.ident = flights.destination AND " \
                       f"flights.origin = game.location AND game.screen_name = '{player_name}'"
    flights = kursori.kursori_func(sql__get_flights)

    json_format = {
        "player_data": {
            "screen_name": player_data[0][0],
            "co2_consumed": player_data[0][1],
            "location": player_location
        },
        "flights": flights
    }

    return json_format


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(use_reloader=True, host='127.0.0.1', port=15486)
