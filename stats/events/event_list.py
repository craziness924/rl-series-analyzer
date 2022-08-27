from stats.events.events.demo import EventDemo
from stats.events.events.shot import EventShot
from stats.events.events.kickoff import EventKickoff
from stats.events.events.goal import EventGoal

class StatsList():
    @staticmethod
    def get_player_stats():
        return []
        
    @staticmethod
    def get_game_events():
        return [
            EventDemo(),
            EventShot(),
            EventKickoff(),
            EventGoal()
        ]