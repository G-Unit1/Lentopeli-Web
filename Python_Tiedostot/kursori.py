from Python_Tiedostot import mariadb_connector


def kursori_func(sql_komento):
    yhteys = mariadb_connector.mariadb_connect()

    kursori = yhteys.cursor()

    kursori.execute(sql_komento)

    tulos = kursori.fetchall()

    return tulos
