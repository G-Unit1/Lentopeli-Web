import kursori
import log_in


def user_creation():
    new_user = input("Enter your name: ").lower()
    sql__user_test_if_exists = f"select screen_name from game where screen_name = '{new_user}';"

    user_test_result = kursori.kursori_func(sql__user_test_if_exists)

    if new_user != "":

        if user_test_result:
            already = "Username already in use"
            print(already)
            prompt = input("would you like to login or pick a new user name (Y login, n new user) ")
            if prompt == "y":
                log_in.login()
            elif prompt == "n":
                user_creation()



        else:
            new_password = input("Enter a password: ")
            difficulty = input("Pick difficulty (1 easy, 2 medium, 3 hard): ")
            sql__new_user = f"insert into game(difficulty, co2_consumed, screen_name, password , location) values ('{difficulty}','50','{new_user}', '{new_password}', 'EFHK');"
            kursori.kursori_func(sql__new_user)
            log_in.login()
    else:
        answer = f"No username entered"
        print(answer)
        return answer


user_creation()
