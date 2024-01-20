from app.game_config import KNIGHTS
from app.game_logic.knight import Knight
from app.game_logic.battle_preparation import BattlePreparation
from app.game_logic.battle import Battle


knights = {}
for knight in KNIGHTS:
    knights.update(
        {
            knight: Knight(KNIGHTS[knight]["name"],
                           KNIGHTS[knight]["power"],
                           KNIGHTS[knight]["hp"],
                           KNIGHTS[knight]["armour"],
                           KNIGHTS[knight]["weapon"],
                           KNIGHTS[knight]["potion"]
                           )
        }
    )


# BATTLE PREPARATIONS:
def battle(knights: dict[Knight]) -> dict:
    for value in knights.values():
        BattlePreparation.apply_armour(value)
        BattlePreparation.apply_weapon(value)
        BattlePreparation.apply_potion(value)

    # BATTLE:

    lancelot_vs_mordred = Battle(knights["lancelot"], knights["mordred"])
    lancelot_vs_mordred.play_round()
    arthur_vs_red_knight = Battle(knights["arthur"], knights["red_knight"])
    arthur_vs_red_knight.play_round()

    # Return battle results:
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(knights))
