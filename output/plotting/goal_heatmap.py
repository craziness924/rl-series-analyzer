from series_analyzer.series import Series
from stats.events.events.goal import Goal

from carball.analysis.simulator.map_constants import GOAL_X, GOAL_Z

import matplotlib.pyplot as plt
import PIL.Image

import os

class GoalHeatmap():
    @staticmethod
    def output_plot(series: Series) -> None:
        series_points = []

        for i, game in enumerate(series.games, 1):
            game_points = []
            for event in game.events:
                if isinstance(event, Goal):
                    if event.team == 1:
                        point = (-event.position.x, event.position.z)
                    else:
                        point = (event.position.x, event.position.z)

                    game_points.append(point)
                    series_points.append(point)

            plt = GoalHeatmap._create_plot(game_points, series, i)
            plt.savefig(f"{game.path}\\goal_heatmap.png")

        plt = GoalHeatmap._create_plot(series_points, series, None)
        plt.savefig(f"{series.series_path}\\goal_heatmap.png")
        pass
        

    @staticmethod
    def _create_plot(data: 'list[(int, int)]', series: Series, game_num: int):
        goal_image = open(f"{os.getcwd()}\\output\\plotting\\assets\\croppedgoal.png", mode="rb")

        if game_num is None:
            title = f"Goal locations for series {series.name}"
        else:
            title = f"Goal locations for Game {game_num} of series {series.name}"

        img = PIL.Image.open(goal_image)
        fig, ax = plt.subplots() 
        plt.imshow(img, extent=[GOAL_X / 2, -(GOAL_X / 2), 0, GOAL_Z])  
        
        ax.set_title(title)

        plt.tick_params(
            axis='both',          
            which='both',
            bottom=False,    
            top=False,
            left=False,         
            labelbottom=False,
            labelleft=False)

        for point in data:
            plt.plot(point[0], point[1], color="pink", marker="*")

        fig.tight_layout()

        return plt      