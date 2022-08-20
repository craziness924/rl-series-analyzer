from carball.json_parser.game import Game

from series_analyzer.crazy_game import CrazyGame
from util.goal_regions import goal_areas
from util.vector import Vector3

from pandas import DataFrame

class Goal():
    def __init__(self):
        self.time = None
        self.scorer = None
        self.team = None
        self.area = None
        self.position = None
        self.velocity = None
        
    @staticmethod
    def get_time_string():
        pass

class EventGoal():
    @staticmethod
    def _distance_sort(x):
        return x["dist"]

    @staticmethod
    def calculate_events(game: CrazyGame) -> list:
        events = []
        # TODO: make events specific for each game
        for goal in game.analysis.game.goals:
            goalInfo = Goal()

            ball_df = game.analysis.data_frame.ball

            ball_x = ball_df.pos_x
            ball_y = ball_df.pos_y
            ball_z = ball_df.pos_z

            ball_v_x = ball_df.vel_x[goal.frame_number]
            ball_v_y = ball_df.vel_y[goal.frame_number]
            ball_v_z = ball_df.vel_y[goal.frame_number]

            ball_pos = Vector3(ball_x[goal.frame_number], ball_y[goal.frame_number], ball_z[goal.frame_number])
            ball_vel = Vector3(ball_v_x, ball_v_y, ball_v_z)

            goalInfo.scorer = goal.player
            goalInfo.time = goal.frame_number
            goalInfo.team = goal.player_team
            goalInfo.area = EventGoal._get_goal_area(goal, ball_pos)
            goalInfo.position = ball_pos
            goalInfo.velocity = ball_vel

            events.append(goalInfo)
        return events

    @staticmethod
    def _get_goal_area(goal, ball_pos):
        if goal.player_team == 0:
            team = "orange"
        else:
            team = "blue"

        distances = []
        for area in goal_areas[team]:
            distance = {}
            area_pos = Vector3(goal_areas[team][area][0], goal_areas[team][area][1], goal_areas[team][area][2])

            distance["dist"] = area_pos.dist(ball_pos)
            distance["area"] = area
            
            distances.append(distance)

        distances.sort(key=EventGoal._distance_sort)
        return distances[0]["area"]