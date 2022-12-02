import time
from Flask import kursori
import end_credits


def check_goal(continent, username, player_location):
    # Valitaan pelaajan id
    sql_find_player_id = "select id from game where screen_name = '" + username + "';"
    player_id = kursori.kursori_func(sql_find_player_id)[0][0]

    # Valitaan goal_id
    sql_find_goal_id = "select id from goal where target = '" + continent + "';"
    goal_id = kursori.kursori_func(sql_find_goal_id)[0][0]

    # Valitaan mantereen nimi
    sql_find_continent_name = f"select name from goal where target = '{continent}'"
    continent_name = kursori.kursori_func(sql_find_continent_name)[0][0]

    # Tarkistetaanko onko pelaaja jo saavuttanut kyseisen goalin
    sql_check_goal_status = f"select goal_id from goal_reached where game_id = {player_id} and goal_id = {goal_id};"
    goal_id_check = kursori.kursori_func(sql_check_goal_status)

    if not goal_id_check:
        print(f"New goal reached: {goal_id} - {continent_name}")
        time.sleep(1)

        sql_update_goal = f"insert into goal_reached (goal_id, game_id) values ('{goal_id}', '{player_id}');"
        kursori.kursori_func(sql_update_goal)

        sql_check_if_goals_done = f"select goal_id from goal_reached where game_id = {player_id}"
        game_complete_check = kursori.kursori_func(sql_check_if_goals_done)

        if game_complete_check == [(1,), (2,), (3,), (4,), (5,), (6,)] and player_location != "EFHK":
            print("All goals completed.")
            print("Return to Helsinki-Vantaa Airport to win the game")

    elif goal_id_check:
        sql_check_if_goals_done = f"select goal_id from goal_reached where game_id = {player_id}"
        game_complete_check = kursori.kursori_func(sql_check_if_goals_done)

        if game_complete_check == [(1,), (2,), (3,), (4,), (5,), (6,)] and player_location != "EFHK":
            print("All goals completed.")
            print("Return to Helsinki-Vantaa Airport to win the game")

        if game_complete_check == [(1,), (2,), (3,), (4,), (5,), (6,)] and player_location == "EFHK":
            sql_check_total_co2 = f"select co2_consumed from game where screen_name = '{username}'"
            total_co2 = kursori.kursori_func(sql_check_total_co2)[0][0]

            print(f"CO2 päästösi olivat: {total_co2}g")
            time.sleep(1)

            sql_remove_goals = "delete goal_reached from goal_reached inner join game where goal_reached.game_id = game.id and game.screen_name = '" + username + "';"
            kursori.kursori_func(sql_remove_goals)

            sql_remove_game = "delete from game where screen_name = '" + username + "';"
            kursori.kursori_func(sql_remove_game)

            end_credits.end_credits()
            exit()
