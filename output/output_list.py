
from output.plotting.goal_heatmap import GoalHeatmap
from output.plotting.kickoffs import KickoffPlot

class OutputList():
    @staticmethod
    def get_csv_outputs():
        return []
    @staticmethod
    def get_plotting_outputs():
        return [
            GoalHeatmap(),
            KickoffPlot()
        ]