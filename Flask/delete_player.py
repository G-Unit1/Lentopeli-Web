import kursori

def delete(username, password):
    sql__check_for_username = f"select screen_name from game where screen_name = '{username}';"
    user_test_result = kursori.cursor_fetch(sql__check_for_username)[0][0]

    if user_test_result != "":

        sql__check_for_password = f"select password from game where screen_name = '{username}' "
        password_result = kursori.cursor_fetch(sql__check_for_password)[0][0]

        if username == user_test_result and password == password_result:
            response = {
                "value": "true",
                "message": "User deleted!"
            }

            sql__delete_user = f"delete from game where screen_name = '{username}'"
            kursori.cursor_execute(sql__delete_user)

            return response

        else:
            response = {
                "value": "false",
                "message": "Username or password were incorrect!"
            }

            return response
