import kursori


def login(username, password):
    sql__check_for_username = f"select screen_name from game where screen_name = '{username}';"
    user_test_result = kursori.kursori_hae(sql__check_for_username)

    if user_test_result:

        sql__check_for_password = f"select password from game where screen_name = '{username}' "
        password_result = kursori.kursori_hae(sql__check_for_password)

        if username == user_test_result[0][0] and password == password_result[0][0]:
            response = {
                "value": "true",
                "message": "Welcome to Flight World!"
            }

            return response

        else:
            response = {
                "value": "false",
                "message": "Username or password were incorrect!"
            }

            return response

    else:
        response = {
            "value": "false",
            "message": "Username or password were incorrect!"
        }

        return response
