import flask
import log_in
import sign_up
import get_player
import delete_player
import fly_to_airport
from flask_cors import CORS

app = flask.Flask(__name__)


# This flask app is used to create a new user
@app.route('/new_game/<string:new_user>,<string:new_password>')
def new_game(new_user, new_password):
    response = sign_up.user_creation(new_user, new_password)

    return response


# This flask app is used to log into an existing user
@app.route('/continue_game/<string:player_name>,<string:password>')
def continue_game(player_name, password):
    response = log_in.login(player_name, password)

    return response


# This flask app is used to delete an existing user
@app.route('/delete_player/<string:player_name>,<string:password>')
def delete_user(player_name, password):
    response = delete_player.delete(player_name, password)

    return response


# This flask app is used to find all player data
# (screen_name, co2_consumed, location (ICAO + Coords) and available flights (ICAO + Coords)
@app.route('/get_player/<string:player_name>')
def get_player_data(player_name):
    response = get_player.get_player(player_name)

    return response


# This flask app is used to update the players location
@app.route('/fly_to/<string:player_name>,<string:airport>')
def fly_to(player_name, airport):
    response = fly_to_airport.fly(player_name, airport)

    return response


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(use_reloader=True, host='0.0.0.0', port=15486, ssl_context=('/home/make/Certificates/certificate.crt','/home/make/Certificates/private.key'))
