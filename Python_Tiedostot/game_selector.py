import sys
import matka
import guide
import kursori
import EasterEgg


def new_game():
    difficulty = ""
    pelaajan_sijainti = ""

    username = input("Syötä nimesi: ")

    sql_user_test_if_exists = "select screen_name from game where screen_name = '" + username + "';"

    user_test_result = kursori.kursori_func(sql_user_test_if_exists)

    if username != "":

        if user_test_result:
            print("Käyttäjänimi on jo tietokannassa.")
            print("1. Yritä toista nimeä\n2. Jatkaaksesi peliä")

            valinta = input("Valinta (1/2): ")

            if valinta == "1":
                new_game()

            elif valinta == "2":
                pelaaja = continue_game(username)

                for i in pelaaja:
                    pelaajan_sijainti = i[0]

                matka.peli(pelaajan_sijainti, username)

            else:
                print("Väärä valinta!")
                new_game()

        else:
            vaikeus = input("Valitse lentokone!\n1: Airbus A320\n2: Boeing 737\n3. Airbus A380\nValinta: ")
            if vaikeus in ("1", "2", "3"):
                if vaikeus == "1":
                    difficulty = "50"

                elif vaikeus == "2":
                    difficulty = "100"

                elif vaikeus == "3":
                    difficulty = "150"

                sql_new_user = "insert into game(difficulty, co2_consumed, screen_name, location) values ('" + difficulty + "' , '50','" + username + "', 'EFHK');"

                kursori.kursori_func(sql_new_user)

                pelaajan_sijainti = continue_game(username)

                matka.peli(pelaajan_sijainti, username)

            else:
                print("Et syöttänyt kunnollista vaikeusastetta!")
                new_game()
    else:
        print("Et syöttänyt nimeä!")
        new_game()


def continue_game(username):

    sql_select_player_profile = "select location from game where screen_name = '" + username + "';"
    pelaaja_profiili = kursori.kursori_func(sql_select_player_profile)[0][0]

    if not pelaaja_profiili:
        print("Käyttäjää ei ole tietokannassa.")
        print("Luo uusi pelaaja (1) tai kokeile uutta nimeä (2).")

        valinta = int(input("Valinta (1/2): "))

        if valinta == 1:
            new_game()
            return pelaaja_profiili

        elif valinta == 2:
            username = input("Syötä nimesi: ")
            pelaaja_profiili = continue_game(username)
            return pelaaja_profiili

    else:
        print("Käyttäjän tideot ladattu!")

        return pelaaja_profiili


def delete_game():
    pelaajan_sijainti = ""

    sql_print_all_users = "select screen_name from game;"
    print_all_users = kursori.kursori_func(sql_print_all_users)
    if not print_all_users:
        print("Pelejä ei löytynyt.")

    else:
        print("Olemassa olevat pelit:")
        x = 1
        for i in print_all_users:
            print(f"{x}: {i[0]}")
            x = x + 1

        username = input("Syötä käyttäjä jonka pelin haluat poistaa: ")

        sql_user_test_if_exists = "select screen_name from game where screen_name = '" + username + "';"

        user_test_result = kursori.kursori_func(sql_user_test_if_exists)
        if user_test_result:
            print(f"Käyttäjä {username} poistetaan\nY jos haluat poistaa\nN jos et halua poistaa")
            valinta = input("Valinta (Y/N): ").upper()

            if valinta == "Y":
                sql_remove_goals = "delete goal_reached from goal_reached inner join game where goal_reached.game_id = game.id and game.screen_name = '" + username + "';"
                kursori.kursori_func(sql_remove_goals)

                sql_remove_game = "delete from game where screen_name = '" + username + "';"
                kursori.kursori_func(sql_remove_game)
                print("Käyttäjä poistettu!")

            elif valinta == "N":
                return

    valinta = input("1/ New game \n2/ Continue game\n3/ Delete saved game\n4/ Guide\n5/ Exit\nValinta: ")
    if valinta in ("1", "2", "3", "4", "5", "666"):
        valinta = int(valinta)

        if valinta == 1:
            new_game()

        elif valinta == 2:
            sql_print_all_users = "select screen_name from game;"
            print_all_users = kursori.kursori_func(sql_print_all_users)

            if not print_all_users:
                print("Pelejä ei löytynyt.")

            else:
                print("Olemassa olevat pelit:")
                x = 1
                for i in print_all_users:
                    print(f"{x}: {i[0]}")
                    x = x + 1

            username = input("Valitse peli: ")
            pelaaja = continue_game(username)

            for i in pelaaja:
                pelaajan_sijainti = i[0]

            matka.peli(pelaajan_sijainti, username)

        elif valinta == 3:
            delete_game()

        elif valinta == 4:
            guide.game_guide()

        elif valinta == 5:
            print("Exiting game.")
            sys.exit()

        elif valinta == 666:
            EasterEgg.tornihajoo.torni()

    else:
        print("Väärä syöte.")
        print("Ohjelma sulkeutuu")
