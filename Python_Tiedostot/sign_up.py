import kursori

new_user = input("Enter your name: ").lower()
sql__user_test_if_exists = f"select screen_name from game where screen_name = '{new_user}';"

user_test_result = kursori.kursori_func(sql__user_test_if_exists)

if new_user != "":

    if user_test_result:
        print("Username already in use")
    else:
        new_password = input("Enter a password: ")
        difficulty = input("Pick difficulty (1 easy, 2 medium, 3 hard): ")
        sql__new_user = f"insert into game(difficulty, co2_consumed, screen_name, password , location) values ('{difficulty}','50','{new_user}', '{new_password}', 'EFHK');"
        kursori.kursori_func(sql__new_user)
else:
    print("No username entered")