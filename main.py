"""
from Python_Tiedostot import matka
from Python_Tiedostot import guide
from Python_Tiedostot import kursori
from Python_Tiedostot import pelivalikko
from Python_Tiedostot import game_selector
from Python_Tiedostot import mariadb_connector
from EasterEgg import tornihajoo
"""
import json

import flask

from Python_Tiedostot import kursori

app = flask.Flask(__name__)


@app.route('/get_player_data/<string:player_name>')
def get_player_data(player_name):
    sql_get_player_data = f"select screen_name, co2_consumed, location, difficulty from game where screen_name = '{player_name}'"

    player_data = kursori.kursori_func(sql_get_player_data)

    json_format = {
        "screen_name": player_data[0][0],
        "co2_consumed": player_data[0][1],
        "location": player_data[0][2],
        "difficulty": player_data[0][3]
    }

    json_data = json.dumps(json_format, default=lambda o: o.__dict__, indent=4)

    return json_data


@app.route('/update_player_data/<string:player_name>,<string:new_location>')
def update_player_data(player_name, new_location):
    sql_update_player_data = f"update game set location = '{new_location}' where screen_name = '{player_name}'"

    kursori.kursori_func(sql_update_player_data)

    return "true"


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

    """
    print("Establishing SQL-connection")
    mariadb_connector.mariadb_connect()
    print("Connected!")

    valinta = pelivalikko.pelivalikko()
    pelaajan_sijainti = ""

    if valinta == "new_game":
        game_selector.new_game()

    elif valinta == "continue_game":

        sql_print_all_users = "select screen_name from game;"
        print_all_users = kursori.kursori_func(sql_print_all_users)

        if not print_all_users:
            print("Pelejä ei löytynyt.")
            print("1. Luo uusi peli\n2. Sulje peli")

            valinta = input("Valinta (1/2): ")

            if valinta == "1":
                game_selector.new_game()

            if valinta == "2":
                sys.exit()

        else:
            print("Olemassa olevat pelit:")
            x = 1
            for i in print_all_users:
                print(f"{x}: {i[0]}")
                x = x + 1

            username = input("Valitse peli: ")

            pelaajan_sijainti = game_selector.continue_game(username)

            matka.peli(pelaajan_sijainti, username)

    elif valinta == "delete_game":
        game_selector.delete_game()

    elif valinta == "tutorial":
        guide.game_guide()

    elif valinta == "exit":
        print("Exiting game!")
        sys.exit()

    elif valinta == "torni":
        tornihajoo.torni()
"""
