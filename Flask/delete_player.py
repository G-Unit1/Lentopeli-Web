import cursor


def delete(player_name):
    sql__delete_goals = f"delete goal_reached from goal_reached inner join game where goal_reached.game_id = game.id and game.screen_name = '{player_name}';"
    cursor.cursor_execute(sql__delete_goals)

    sql__delete_user = f"delete from game where screen_name = '{player_name}'"
    cursor.cursor_execute(sql__delete_user)

    response = {
        "value": "user_deleted",
        "message": "User deleted"
    }

    return response
