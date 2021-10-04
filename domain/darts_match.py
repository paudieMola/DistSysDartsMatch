class DartsMatch:
    """ This was the original hardcoded script
    def __init__(self, type, player1, player2):
        self.type = type
        self.player1 = player1
        self.player2 = player2
    """

    def __init__(self):
        self.active = True
        self.players = []
        self.last_player_index = -1
        self.visits = []
        self.winning_num_darts = -1
        self.winning_player_index = -1

    def register_player(self, username):
        if username not in self.players:
            index = len(self.players)
            self.players.append(username)
            self.visits.append([]) #necessary for stats
            return index
        else:
            return -1