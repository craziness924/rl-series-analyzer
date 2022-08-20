# will calculate events and prepare them for output to csv.
# ex. create an event for a goal and name the scorers, assisters, time, location, and game it occured in

from series_analyzer.series import Series
from stats.events.event_list import StatsList


class EventManager():
    @staticmethod
    def _event_sort(x):
        return x.time
    @staticmethod
    def calculate_events(series: Series) -> Series:
        game_events = StatsList.get_game_events()
        for game in series.games:
            for event in game_events:
                events = event.calculate_events(game)
                for event in events:
                    game.events.append(event)
                    pass
            if len(game.events) > 0:
                game.events.sort(key=EventManager._event_sort)
        return series