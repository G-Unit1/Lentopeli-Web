import sys
import matka
import kursori
import game_selector


def game_guide():
    pelaajan_sijainti = ""

    print(f"Goal of the game is to visit every continent with the least amount of CO2 emissions.\n"
          f"Navigate through the game with a keyboard.\nNow take to the skies!")

    enter = input("Press Enter to exit guide")

    if enter == "":
        valinta = input("1/ New game \n2/ Continue game\n3/ Delete saved game\n4/ Guide\n5/ Exit\nValinta: ")
        if valinta in ("1", "2", "3", "4", "5"):
            valinta = int(valinta)

            if valinta == 1:
                game_selector.new_game()

            elif valinta == 2:
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

            elif valinta == 3:
                game_selector.delete_game()

            elif valinta == 4:
                game_guide()

            elif valinta == 5:
                print("Exiting game.")
                sys.exit()

        else:
            print("Väärä syöte.")
            print("Ohjelma sulkeutuu")
