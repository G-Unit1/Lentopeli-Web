import sys

from EasterEgg import rikki
import time


def torni():
    while True:
        flight_number = str(input("Anna lennon numero: ")).upper()

        if flight_number == "AA11":
            rikki.torni_kaatuu()
            print("Rip pohjoistorni")
            time.sleep(2)

        elif flight_number == "UA175":
            rikki.torni_kaatuu()
            print("Rip etelätorni")
            time.sleep(2)

        else:
            print("Program Exit")
            sys.exit()
