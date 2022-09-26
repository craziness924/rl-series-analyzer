from series_analyzer.series import Series

from stats.events.events.kickoff import Kickoff
import matplotlib.pyplot as plt

from util.point import PiePoint


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
    def output_plot(series: Series, save_points: bool) -> None:
        series_winners = []
        for i, game in enumerate(series.games, 1):
            game_winners = []
            for event in game.events:
                if isinstance(event, Kickoff):
                    first_touch = event.first_touch_team

                    color = "magenta"
                    explode = 0.0

                    if first_touch == 0:
                        color = "orange"
                    elif first_touch == 1:
                        color = "blue"
                        
                    point = PiePoint(event.first_touch_team, color=color)

                    game_winners.append(point)
                    series_winners.append(point)

            plt = KickoffPlot._create_plot(game_winners, series, i)
            plt.savefig(f"{game.path}\\first_touches.png")

            if (save_points):
                with open(f"{series.series_path}\\game{i}\\{KickoffPlot.get_debug_filename()}", mode="w") as f:
                    for point in game_winners:
                        f.write(f"{str(point)}\n")

        plt = KickoffPlot._create_plot(series_winners, series)
        plt.savefig(f"{series.series_path}\\first_touches.png")

        if (save_points):
            with open(f"{series.series_path}\\{KickoffPlot.get_debug_filename()}", mode="w") as f:
                for point in series_winners:
                    f.write(f"{str(point)}\n")


    @staticmethod
    def _create_plot(data: 'list[PiePoint]', series: Series = None, game_num: int = None):
        if series is not None:  
            if game_num is None:
                title = f"First touches for series {series.name}"
            else:
                title = f"First touches for Game {game_num} of series {series.name}"
        else:
            title = f"First touches for test plot!"


        fig, ax = plt.subplots()

        blue_wins = 0
        orange_wins = 0

        colors = []
        labels = []
        explode = []

        for point in data:
            if point.x == 0:
                orange_wins += 1
            elif point.x == 1:
                blue_wins += 1

        if orange_wins > blue_wins:
            explode = [.1, 0]
        else:
            explode = [0, .1]

        ax.pie([blue_wins, orange_wins], explode=explode, labels=["blue", "orange"], colors=["blue", "orange"])
        
        plt.title(title)

        return plt      