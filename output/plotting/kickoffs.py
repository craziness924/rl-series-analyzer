from series_analyzer.series import Series
from series_analyzer.crazy_game import CrazyGame
from util.point import Point

from stats.events.events.kickoff import Kickoff
import matplotlib.pyplot as plt

#TODO: maybe separate all kickoff plots into their own classes
class KickoffPlot():
    @staticmethod
    def get_debug_filename():
        return "kickoff_data.txt"

    @staticmethod
    def determine_winners():
        """
        At some point, we want to make an intelligent detection for a kickoff "win". It's not just about sending ball somewhere.
        
        """
        raise NotImplementedError()

    @staticmethod
    def generate_points_for_game(game: CrazyGame) -> 'list[Points]':
        points = []
        for event in game.events:
            if isinstance(event, Kickoff):
                if event.first_touch_team == 0:
                    label = "blue"
                    color = "blue"
                else:
                    label = "orange"
                    color = "orange"
                
                #TODO: determine_winners()

                point = Point(x=event.first_touch_team, color=color, marker=None, label=label, explode=0.0)
                points.append(point)
        return points

    @staticmethod
    def output_plot(series: Series, save_points: bool) -> None:
        series_points = []
        for i, game in enumerate(series.games, 1):
            game_points = KickoffPlot.generate_points_for_game(game=game)

            for point in game_points:
                series_points.append(point)
            plot = KickoffPlot._create_plot(data=game_points, series=series, game_num=i)
            plot.show()

        plot = KickoffPlot._create_plot(data=series_points, series=series, game_num=None)
        plot.show()
    
    @staticmethod
    def _create_plot(data: 'list[Point]', series: Series = None, game_num: int = None):
        if game_num is None:
            title = f"Kickoff percents for series {series.name}"
        else:
            title = f"Kickoff percents for game {game_num} of series {series.name}"
        
        fig, ax = plt.subplots()

        x = []
        labels = []
        colors = []
        explode = []
        for point in data:
            x.append(point.x)
            labels.append(point.label)
            colors.append(point.color)
            explode.append(point.explode)

        ax.title = title
        ax.pie(x=x, labels=labels, colors=colors, explode=explode)

        return plt      