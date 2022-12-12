import kursori

def goal_manager(player_name):
    sql__find_player_id = f"SELECT game.id FROM game WHERE game.screen_name = '{player_name}';"
    player_id = kursori.kursori_hae(sql__find_player_id)[0][0]


    sql__check_continent_id = f"SELECT goal.id FROM goal INNER JOIN airport INNER JOIN game WHERE " \
                         f"airport.ident = game.location AND goal.target = airport.continent AND" \
                         f" game.screen_name = '{player_name}';"
    continent_id = kursori.kursori_hae(sql__check_continent_id)[0]


    sql__check_goals_reached = f"SELECT goal_reached.goal_id FROM goal_reached INNER JOIN game WHERE " \
                               f"goal_reached.game_id = game.id AND game.screen_name = '{player_name}';"
    goals_reached = kursori.kursori_hae(sql__check_goals_reached)

    if continent_id not in goals_reached:
        sql__update_goals = f"INSERT INTO goal_reached (goal_id, game_id) VALUES ('{continent_id[0]}', '{player_id}')"
        kursori.kursori_aja(sql__update_goals)




goal_manager('make')
