
from output.plotting.goal_heatmap import GoalHeatmap

class OutputList():
    @staticmethod
    def get_csv_outputs():
        return []
    @staticmethod
    def get_plotting_outputs():
        return [
            GoalHeatmap()
        ]