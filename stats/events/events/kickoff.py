from series_analyzer.crazy_game import CrazyGame
from util.vector import Vector3

class KickoffPlayer():
    def __init__(self):
        self.id: str = None
        self.kickoff_position: str = None
        self.touch_position: str = None

        self.player_position: Vector3 = None
        self.starting_position: Vector3 = None

        self.first_touch: bool = None


class Kickoff():
    def __init__(self):
        self.time: int = None # beginning of kickoff
        self.time_of_touch: int = None # frame that touch occured on
        self.time_to_touch: float = None # time in seconds taken for first touch to be made
        self.type: str = None # type of kickoff

        self.kickoffGoal: float = None # time in seconds until the next goal. is None if there's no goal after the kickoff
        self.players: 'list[KickoffPlayer]' = []

class EventKickoff():
    @staticmethod
    def calculate_events(game: CrazyGame, protobuf_json) -> list:
        """
        Use to calculate the game event of the specific type. 
        Is called once per game in the list of replays. 

        param: game - The CrazyGame to look through for kickoff events
        param: protobuf_json - The game's protobuf as a json to be used for analysis

        Returns: 
            list of kickoff events to append to the game object
        """
        events = []
        

        for kickoff in protobuf_json["gameStats"]["kickoffStats"]:
            kickoff_touch = kickoff["touch"] 
            kickoffInfo = Kickoff()

            kickoffInfo.time = kickoff["startFrame"]
            kickoffInfo.time_of_touch = kickoff["touchFrame"]
            kickoffInfo.time_to_touch = kickoff["touchTime"]

            kickoffInfo.type = kickoff["type"]

            if "kickoffGoal" in kickoff_touch:
                kickoffInfo.kickoffGoal = kickoff_touch["kickoffGoal"]

            for player in kickoff_touch["players"]:
                kickoffPlayer = KickoffPlayer()
                kickoffPlayer.id = player["player"]["id"]
                kickoffPlayer.kickoff_position = player["kickoffPosition"]
                kickoffPlayer.touch_position = player["touchPosition"]

                player_position = player["playerPosition"]
                kickoffPlayer.player_position = Vector3(player_position["posX"], player_position["posY"], player_position["posZ"])
                
                starting_position = player["startPosition"]
                kickoffPlayer.starting_position = Vector3(starting_position["posX"], player_position["posY"], player_position["posZ"])
                
                kickoffPlayer.first_touch = (kickoffPlayer.id == kickoff_touch["firstTouchPlayer"]["id"])

                kickoffInfo.players.append(kickoffPlayer)
            events.append(kickoffInfo)
        return events
