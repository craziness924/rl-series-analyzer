from series_analyzer.crazy_game import CrazyGame

class Kickoff():
    def __init__(self):
        self.time = None

class EventKickoff():
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
        

        for kickoff in protobuf_json["gameStats"]["kickoffStats"]:
            pass
        return events
