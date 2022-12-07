import flask
import log_in
import sign_up
import get_player
import delete_player
import fly_to_airport

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


# This flask app is used to delete an existing user
@app.route('/delete_player/<string:username>,<string:password>')
def delete_user(username, password):
    response = delete_player.delete(username, password)

    return response


# This flask app is used to find all player data
# (screen_name, co2_consumed, location (ICAO + Coords) and available flights (ICAO + Coords)
@app.route('/get_player/<string:username>')
def get_player_data(username):
    response = get_player.get_player(username)

    return response


# This flask app is used to update the players location
@app.route('/fly_to/<string:username>,<string:airport>')
def fly_to(username, airport):
    response = fly_to_airport.fly(username, airport)

    return response


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(use_reloader=True, host='127.0.0.1', port=15486)
