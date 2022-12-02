import mysql.connector


def mariadb_connect():
    yhteys = mysql.connector.connect(
        host='make-s.duckdns.org',
        port=19915,
        database='lentopeli',
        user='lentopeli',
        password='fl1ght_g4m3',
        autocommit=True
    )

    return yhteys
