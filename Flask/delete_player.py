import cursor

def delete(player_name, password):
    sql__check_for_player_name = f"select screen_name from game where screen_name = '{player_name}';"
    user_test_result = cursor.cursor_fecth(sql__check_for_player_name)[0][0]

    if user_test_result != "":

        sql__check_for_password = f"select password from game where screen_name = '{player_name}' "
        password_result = cursor.cursor_fecth(sql__check_for_password)[0][0]

        if player_name == user_test_result and password == password_result:
            response = {
                "value": "true",
                "message": "User deleted!"
            }

            sql__delete_user = f"delete from game where screen_name = '{player_name}'"
            cursor.cursor_execute(sql__delete_user)

            return response

        else:
            response = {
                "value": "false",
                "message": "player_name or password were incorrect!"
            }

            return response
