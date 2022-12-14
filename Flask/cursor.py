import mariadb_connector


def cursor_fecth(sql_command):
    connection = mariadb_connector.mariadb_connect()

    cursor = connection.cursor()

    cursor.execute(sql_command)

    result = cursor.fetchall()

    return result


def cursor_execute(sql_command):
    connection = mariadb_connector.mariadb_connect()

    cursor = connection.cursor()

    cursor.execute(sql_command)
