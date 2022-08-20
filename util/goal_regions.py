from carball.analysis.simulator.map_constants import GOAL_X, GOAL_Y, GOAL_Z

goal_areas = {}
def calculate_goal_areas():
    goal_areas["orange"] = {}
    goal_areas["blue"] = {}

    goal_areas["orange"]["bottom_left"] = (GOAL_X / 2, 5120, 0)
    goal_areas["orange"]["bottom_middle"] = (0, 5120, 0)
    goal_areas["orange"]["bottom_right"] = (-(GOAL_X / 2), 5120, 0)
    goal_areas["orange"]["top_left"] = (GOAL_X / 2, 5120, GOAL_Z)
    goal_areas["orange"]["top_middle"] = (0, 5120, GOAL_Z)
    goal_areas["orange"]["top_right"] = (-(GOAL_X / 2), 5120, GOAL_Z)
    
    goal_areas["blue"] = {}

    for area in goal_areas["orange"]:
        orange_vector = goal_areas["orange"][area]
        blue_vector = (-orange_vector[0], -orange_vector[1], orange_vector[2])
        
        goal_areas["blue"][area] = blue_vector

