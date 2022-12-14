import mariadb_connector


def kursori_fecth(sql_command):
    connection = mariadb_connector.mariadb_connect()

    kursori = connection.cursor()

    kursori.execute(sql_command)

    result = kursori.fetchall()

    return result


def kursori_execute(sql_command):
    connection = mariadb_connector.mariadb_connect()

    kursori = connection.cursor()

    kursori.execute(sql_command)
