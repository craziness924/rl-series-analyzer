class CrazyGame():
    def __init__(self):
        self.path = None
        self.analysis = None
        self.replay_info = None
        self.events = []

class ReplayInfo():
    def __init__(self, data, game, start_time):
        self.data = data
        self.game = game
        self.start_time = start_time