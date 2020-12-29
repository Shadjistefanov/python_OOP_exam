class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        player_name = player.username
        names = [p.username for p in self.players]

        if player_name in names:
            raise ValueError(f"Player {player_name} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player_to_remove = self.find(player)
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username):
        player = [p for p in self.players if p.username == username][0]
        return player

