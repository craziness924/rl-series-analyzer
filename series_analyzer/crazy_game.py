from carball.analysis.analysis_manager import AnalysisManager
from carball.json_parser.player import Player

class CrazyGame():
    def __init__(self):
        self.path = None
        self.analysis: AnalysisManager = None
        self.replay_info: ReplayInfo = None
        self.players: 'list[Player]' = None
        self.events = []
        self.stats = GameStats()

class ReplayInfo():
    def __init__(self, data, game, start_time):
        self.data = data
        self.game = game
        self.start_time = start_time

class GameStats():
    def __init__(self):
        pass