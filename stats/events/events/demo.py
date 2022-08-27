from series_analyzer.crazy_game import CrazyGame
from util.vector import Vector3

class Demo():
    def __init__(self):
        self.time = None
        self.attacker = None
        self.attacker_vel = None
        self.victim = None
        self.victim_vel = None

        self.position: Vector3

class EventDemo(): # insert class into event_list.py in the correct category
    @staticmethod
    def calculate_events(game: CrazyGame, protobuf_json) -> list:
        """
        Use to calculate the game event of the specific type. 
        Is called once per game in the list of replays. 

        param: game - The CrazyGame to look through for events
        param: protobuf_json - The game's protobuf as a json to be used for analysis \

        Returns: 
            list of events to append to the game object
        """
        events = []
        

        return events
