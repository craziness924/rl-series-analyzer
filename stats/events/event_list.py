from stats.events.events.demo import EventDemo
from stats.events.events.goal import EventGoal

class StatsList():
    @staticmethod
    def get_player_stats():
        return [
            EventGoal(), 
            EventDemo(),
        ]