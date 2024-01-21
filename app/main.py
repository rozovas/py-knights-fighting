from app.game_config import KNIGHTS
from app.game_logic.knight import Knight
from app.game_logic.battle import Battle

# creating knight instances and placing into a dict
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


# battle
def battle(knights: dict[Knight]) -> dict:
    # preparing knights for a battle: applying armour, weapon, potion
    for value in knights.values():
        value.prepare_knight_for_battle()

    # battles
    lancelot_vs_mordred = Battle(knights["lancelot"], knights["mordred"])
    lancelot_vs_mordred.play_round()

    arthur_vs_red_knight = Battle(knights["arthur"], knights["red_knight"])
    arthur_vs_red_knight.play_round()

    # returning battle results:
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(knights))
