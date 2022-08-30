from series_analyzer.series import Series

from stats.events.events.kickoff import Kickoff
import matplotlib.pyplot as plt


class GoalHeatmap():
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
                    pass
                     #game_winners.append(event.first_touch_team)


    @staticmethod
    def _create_plot(data: 'list[int]', series: Series = None, game_num: int = None):
        fig, ax = plt.subplots()

        ax.pie()

        return plt      