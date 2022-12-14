import cursor


def user_creation(new_user, new_password):
    sql__user_test_if_exists = f"select screen_name from game where screen_name = '{new_user}';"
    user_test_result = cursor.cursor_fecth(sql__user_test_if_exists)

    if user_test_result:
        response = {
            "value": "player_name_taken",
            "message": "Username already exists. Please try again!"
        }

        return response


    else:
        sql__new_user = f"insert into game(co2_consumed, screen_name, password, location) " \
                        f"values ('0','{new_user}', '{new_password}', 'EFHK');"
        cursor.cursor_execute(sql__new_user)

        response = {
            "value": "user_created",
            "message": "New user created."
        }

        return response
