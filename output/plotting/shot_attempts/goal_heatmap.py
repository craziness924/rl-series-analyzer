from series_analyzer.series import Series
from stats.events.events.goal import Goal
from series_analyzer.crazy_game import CrazyGame
from util.point import Point

from carball.analysis.simulator.map_constants import GOAL_X, GOAL_Z

import matplotlib.pyplot as plt
import PIL.Image

import os

class GoalHeatmap():
    @staticmethod
    def get_debug_filename():
        return "goal_heatmap_points.txt"

    @staticmethod
    def generate_points_for_game(game: CrazyGame) -> 'list[Point]':
        points: list[Point] = []
        for event in game.events:
            if isinstance(event, Goal):
                if event.team == 1:
                    point = Point(-event.position.x, event.position.z, color="orange", marker="o")
                else:
                    point = Point(-event.position.x, event.position.z, color="#4deaff", marker="o")

                points.append(point)
        return points

    @staticmethod
    def output_plot(series: Series, save_points: bool) -> None:
        series_points = []

        for i, game in enumerate(series.games, 1):
            game_points = GoalHeatmap.generate_points_for_game(game)

            for point in game_points:
                series_points.append(point)

            if (save_points):
                with open(f"{game.path}\\{GoalHeatmap.get_debug_filename()}", mode="w") as f:
                    for point in series_points:
                        f.write(f"{str(point)}\n")
                        
            plt = GoalHeatmap._create_plot(game_points, series, i)
            plt.savefig(f"{game.path}\\goal_heatmap.png")

        plt = GoalHeatmap._create_plot(series_points, series, None)
        plt.savefig(f"{series.series_path}\\goal_heatmap.png")

        if (save_points):
            with open(f"{series.series_path}\\{GoalHeatmap.get_debug_filename()}", mode="w") as f:
                for point in series_points:
                    f.write(f"{str(point)}\n")
        pass
        

    @staticmethod
    def _create_plot(data: 'list[Point]', series: Series = None, game_num: int = None):
        goal_image = open(f"{os.getcwd()}\\output\\plotting\\assets\\croppedgoal.png", mode="rb")

        if series is not None:  
            if game_num is None:
                title = f"Goal locations for series {series.name}"
            else:
                title = f"Goal locations for Game {game_num} of series {series.name}"
        else:
            title = f"Goal locations for test plot!"

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
            plt.plot(point.x, point.y, color=point.color, marker=point.marker)
        #   plt.plot(500, 600, color="orange", marker="+")

        plt.legend()
        fig.tight_layout()

        return plt      