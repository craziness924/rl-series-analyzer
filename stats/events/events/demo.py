from series_analyzer.crazy_game import CrazyGame
from util.vector import Vector3

from carball.json_parser.player import Player

class Demo():
    def __init__(self):
        self.time: int = None

        self.attacker: Player = None
        self.attacker_vel: Vector3 = None
        self.victim: Player = None
        self.victim_vel: Vector3 = None

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
        
        for demo in game.analysis.game.demos:
            demoInfo = Demo()

            demoInfo.time = demo["frame_number"]
            demoInfo.attacker = demo["attacker"]
            demoInfo.victim = demo["victim"]

            attacker_vel = demo["attacker_vel"]
            demoInfo.attacker_vel = Vector3(attacker_vel[0], attacker_vel[1], attacker_vel[2])

            victim_vel = demo["victim_vel"]
            demoInfo.victim_vel = Vector3(victim_vel[0], victim_vel[1], victim_vel[2])

            attacker_df = demoInfo.attacker.data.loc[demoInfo.time]

            attacker_pos_x = attacker_df.pos_x
            attacker_pos_y = attacker_df.pos_y
            attacker_pos_z = attacker_df.pos_z
            
            demoInfo.position = Vector3(attacker_pos_x, attacker_pos_y, attacker_pos_z)
            
            events.append(demoInfo)
        return events
