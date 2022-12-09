import mariadb_connector


def cursor_fetch(sql_command):
    yhteys = mariadb_connector.mariadb_connect()

    kursori = yhteys.cursor()

    kursori.execute(sql_command)

    tulos = kursori.fetchall()

    return tulos


def cursor_execute(sql_command):
    yhteys = mariadb_connector.mariadb_connect()

    kursori = yhteys.cursor()

    kursori.execute(sql_command)
