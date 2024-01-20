from app.game_logic.knight import Knight


class Battle:

    def __init__(self, player1: Knight, player2: Knight) -> None:
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]

    def play_round(self) -> None:
        self.player1.hp -= self.player2.power - self.player1.protection
        self.player2.hp -= self.player1.power - self.player2.protection

        # check if someone fell in battle
        for player in self.players:
            if player.hp <= 0:
                player.hp = 0
