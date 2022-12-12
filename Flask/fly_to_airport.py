import kursori
import goal_manager
import co2_calculator


def fly(player_name, airport):
    co2_emissions = co2_calculator.co2_calculator(player_name, airport)

    sql__update_player_location = f"update game set location = '{airport}' where screen_name = '{player_name}';"
    kursori.kursori_aja(sql__update_player_location)

    goal_manager.goal_manager(player_name)

    response = {
        "value": "true",
        "message": f"You just flew to {airport}",
        "flight_co2_emissions": co2_emissions,
    }

    return response
