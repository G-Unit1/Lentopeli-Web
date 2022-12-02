def pelivalikko():

    valinta = input("1/ New game \n2/ Continue game\n3/ Delete saved game\n4/ Guide\n5/ Exit\nValinta: ")

    if valinta in ("1", "2", "3", "4", "5", "911"):
        valinta = int(valinta)

        if valinta == 1:
            return "new_game"

        elif valinta == 2:
            return "continue_game"

        elif valinta == 3:
            return "delete_game"

        elif valinta == 4:
            return "tutorial"

        elif valinta == 5:
            return "exit"

        elif valinta == 911:
            return "torni"
    else:
        print("Väärä syöte.")
        pelivalikko()
