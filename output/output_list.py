from output.csv.basic_stats import BasicStats
from output.plotting.shot_attempts.goal_heatmap import GoalHeatmap

class OutputList():
    @staticmethod
    def get_csv_outputs():
        return [
            BasicStats()
        ]
    @staticmethod
    def get_plotting_outputs():
        return [
            GoalHeatmap()
        ]