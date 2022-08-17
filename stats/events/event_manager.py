# will calculate events and prepare them for output to csv.
# ex. create an event for a goal and name the scorers, assisters, time, location, and game it occured in

from series_analyzer.series import Series
from stats.events.event_list import StatsList

class EventManager():
    @staticmethod
    def calculate_events(series: Series) -> Series:
        game_events = StatsList.get_player_stats()

        for event in game_events:
            series = event.calculate_stat(series)
        return series