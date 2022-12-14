import cursor


def login(player_name, password):
    sql__check_for_player_name = f"select screen_name from game where screen_name = '{player_name}';"
    user_test_result = cursor.cursor_fecth(sql__check_for_player_name)

    if user_test_result:

        sql__check_for_password = f"select password from game where screen_name = '{player_name}' "
        password_result = cursor.cursor_fecth(sql__check_for_password)

        if player_name == user_test_result[0][0] and password == password_result[0][0]:
            response = {
                "value": "true",
                "message": "Welcome to Flight World!"
            }

            return response

        else:
            response = {
                "value": "false",
                "message": "Username or password were incorrect or taken!"
            }

            return response

    else:
        response = {
            "value": "false",
            "message": "Username or password were incorrect or taken!"
        }

        return response
