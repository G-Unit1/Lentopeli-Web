import time
import sys


def scroll_txt(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def end_credits():
    # black = "\033[0;30m"
    # purple = "\033[0;35m"
    # blue = "\033[0;34m"
    # green = "\033[0;32m"
    # red = "\033[0;31m"
    yellow = "\033[0;33m"
    white = "\033[0;37m"

    print(yellow)
    scroll_txt(
        "          You won!\n\n\n       Game Developers:\n\n\n           Markus\n           Salin"
        "\n\n\n          "
        "Valtteri\n           Latvio\n\n\n            Kim\n          Löfgren\n\n\n           Eemil\n         "
        "Kärkkäinen\n\n\n    Thank you for playing!\n")

    print(white)
    input("\n\nPress anything to quit game: ")
