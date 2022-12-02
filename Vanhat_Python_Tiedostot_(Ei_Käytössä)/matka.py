import time
from Flask import kursori
import goal_checker
import co2_calculator
from geopy import distance


# funktio joka mittaa välimatkan lentokenttien välillä

def quit_game():
    print("Saving game", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(" Game saved!")
    time.sleep(0.5)
    print("Quitting game")


def hae_lentoasema_koord(lentoasema):
    sql = "select latitude_deg, longitude_deg from airport where ident = '" + lentoasema + "';"

    tulos = kursori.kursori_func(sql)

    return tulos


# pelin pääfunktio, joka sisältää pelin toiminnan

def peli(pelaajan_sijainti, username):
    pelaajan_kohde = str
    kohteet = [pelaajan_sijainti]

    while pelaajan_kohde != "":
        time.sleep(1)
        pelaajan_sijainti_koord = hae_lentoasema_koord(pelaajan_sijainti)

        sql_get_airport_name = "select name from airport where ident = '" + pelaajan_sijainti + "';"
        airport_name = kursori.kursori_func(sql_get_airport_name)[0][0]

        sql_get_airport_country = "select country.name from country inner join airport where country.iso_country = airport.iso_country and airport.ident = '" + pelaajan_sijainti + "';"
        airport_country = kursori.kursori_func(sql_get_airport_country)[0][0]

        sql_get_airport_continent = "select country.continent from country inner join airport where country.iso_country = airport.iso_country and airport.ident = '" + pelaajan_sijainti + "';"
        airport_continent = kursori.kursori_func(sql_get_airport_continent)[0][0]

        goal_checker.check_goal(airport_continent, username, pelaajan_sijainti)

        print(f"Nykyinen sijaintisi: {pelaajan_sijainti} - {airport_name}, {airport_country}, {airport_continent}")

        print("Saatavilla olevat kohteet:")

        sql_targets_available = "select destination from flights where origin = '" + pelaajan_sijainti + "';"
        targets = kursori.kursori_func(sql_targets_available)

        x = 1

        for i in targets:

            if x % 10 != 0:
                print(f"{x}: {i[0]},", end=' ')

            elif x % 10 == 0:
                print(f"{x}: {i[0]},", end=' ')
                print("")

            x = x + 1

        print("")

        print("Syötä lentokentän icao-koodi jolle matkustat, tai syötä 'quit' tallentaaksesi ja lopettaaksesi pelin.")
        pelaajan_kohde = input("Valinta: ").upper()

        if pelaajan_kohde == "QUIT":
            quit_game()
            break

        pelaajan_kohde_koord = hae_lentoasema_koord(pelaajan_kohde)

        matka = int(distance.distance(pelaajan_sijainti_koord, pelaajan_kohde_koord).km)

        if pelaajan_kohde != "" or pelaajan_kohde == "EFHK":
            print(f"Lentokenttien etäisyys: {matka}km")

            co2 = co2_calculator.co2_calc(matka, username)
            print(f"Lennon CO2 päästöt: {co2}g")

            sql_add_co2 = f"update game set co2_consumed = co2_consumed + {co2} where screen_name = '{username}';"
            kursori.kursori_func(sql_add_co2)

            sql_check_total_co2 = f"select co2_consumed from game where screen_name = '{username}'"
            total_co2 = kursori.kursori_func(sql_check_total_co2)[0][0]

            print(f"CO2 päästösi tähän mennessä: {total_co2}g")

            sql_targets_available = " select destination from flights where origin = '" + pelaajan_kohde + "';"
            targets = kursori.kursori_func(sql_targets_available)

            if not targets:
                while not targets:
                    print("Päädyit umpikujaan.")
                    print("Valitse lentokenttä jolle palata: ")
                    for i in kohteet:
                        print(i)

                    pelaajan_kohde = input("Mihin kohteista haluat: ").upper()

                    sql_targets_available = " select destination from flights where origin = '" + pelaajan_kohde + "';"
                    targets = kursori.kursori_func(sql_targets_available)
                    pelaajan_sijainti = pelaajan_kohde

            else:
                sql_update_player_location = "update game set location = '" + pelaajan_kohde + "' where screen_name = '" + username + "';"
                kursori.kursori_func(sql_update_player_location)

                pelaajan_sijainti = pelaajan_kohde

                kohteet.append(pelaajan_kohde)
