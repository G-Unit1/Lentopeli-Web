import mariadb_connector


def kursori_hae(sql_command):
    yhteys = mariadb_connector.mariadb_connect()

    kursori = yhteys.cursor()

    kursori.execute(sql_command)

    tulos = kursori.fetchall()

    return tulos


def kursori_aja(sql_command):
    yhteys = mariadb_connector.mariadb_connect()

    kursori = yhteys.cursor()

    kursori.execute(sql_command)
