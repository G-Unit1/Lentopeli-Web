import kursori


def login():
    i = int(5)
    while i > 0:
        username = (input("Enter your username: ")).lower()
        sql__check_for_username = f"select screen_name from game where screen_name = '{username}';"
        user_test_result = kursori.kursori_func(sql__check_for_username)[0][0]
        if user_test_result != "":
            password = (input("Enter your password: "))
            check_for_password = f"select password from game where screen_name = '{username}' "
            password_result = kursori.kursori_func(check_for_password)[0][0]

            if username == user_test_result and password == password_result:
                print("Welcome to flight world!")
                break
            else:
                print("Username or password incorrect!")
        i -= 1
