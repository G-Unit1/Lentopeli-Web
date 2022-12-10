import kursori


def fly(username, airport):
    sql__update_player_location = f"update game set location = '{airport}' where screen_name = '{username}';"
    kursori.kursori_aja(sql__update_player_location)

    response = {
        "value": "true",
        "message": f"You just flew to {airport}"
    }

    return response
