from Flask import kursori


def co2_calc(matka, username):
    co2_perkm = 0

    sql = "select difficulty from game where screen_name = '" + username + "';"
    co2 = kursori.kursori_func(sql)

    for i in co2:
        co2_perkm = i[0]

    emissions = (co2_perkm * matka) / 1000

    return emissions
