import kursori


def fly(username, airport):
    try:
        sql__update_player_location = f"update game set location = '{airport}' where screen_name = '{username}';"
        kursori.kursori_func(sql__update_player_location)

        response = {
            "value": "true",
            "message": f"You just flew to {airport}"
        }

        return response

    except:
        response = {
            "value": "false"
        }
