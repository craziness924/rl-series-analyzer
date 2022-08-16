# will take numbers from the dataframe and protobuf and prepare them for output to csv. 
# ex. calculate a player's average ping in a certain series and put it into a dict for output.py to use

from carball import Game

from stats.stats.stats_list import StatsList

def StatsManager():
    def __init__(self, series):
        self.game_stats = []
        self.player_stats = []

    def calculate_stats(self, game: Game):
        StatsList.get_player_stats()
        StatsList.get_game_stats()
