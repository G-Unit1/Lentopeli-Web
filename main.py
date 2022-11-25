import sys
from Python_Tiedostot import matka
from Python_Tiedostot import guide
from Python_Tiedostot import kursori
from Python_Tiedostot import pelivalikko
from Python_Tiedostot import game_selector
from Python_Tiedostot import mariadb_connector
from EasterEgg import tornihajoo

if __name__ == '__main__':
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
