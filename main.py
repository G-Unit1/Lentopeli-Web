import flask
from Python_Tiedostot import kursori

app = flask.Flask(__name__)


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
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
