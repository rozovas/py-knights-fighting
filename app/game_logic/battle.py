from app.game_logic.knight import Knight


class Battle:

    def __init__(self, player1: Knight, player2: Knight) -> None:
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]

    def play_round(self) -> None:
        for player in self.players:
            another_player = self.player2 if player == self.player1 \
                else self.player2
            player.hp -= another_player.power - player.protection
            # check if someone fell in battle
            if player.hp <= 0:
                player.hp = 0
